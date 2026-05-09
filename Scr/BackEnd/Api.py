from fastapi import FastAPI, status, Depends, APIRouter, Query
from database import Base, engine, sessionlocal, get_db
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List
from fastapi.exceptions import HTTPException
from models import Student, Department, Instructor, Course, CourseOffering, Enrollment, Prerequisite, CourseDepartment
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func, and_, case
import jwt
from datetime import datetime, timedelta, timezone
from fastapi.security import APIKeyHeader
import joblib
import numpy as np
import re, os
import pandas as pd

ai_model = None
std_dev_data = None
svd_data = None
model1 = None
model2 = None
model3 = None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "grade_model.pkl")
STD_DEV_PATH = os.path.join(BASE_DIR, "std_dev_residuals.pkl")
SVD_MODEL_PATH = os.path.join(BASE_DIR, "svd_model.pkl")

paths = {
    "model1": os.path.join(BASE_DIR, "model1.pkl"),
    "model2": os.path.join(BASE_DIR, "model2.pkl"),
    "model3": os.path.join(BASE_DIR, "model3.pkl"),
    "gpa_main": os.path.join(BASE_DIR, "gpa_model (2).pkl")
}

def load_all_ai_assets():
    global ai_model, std_dev_data, svd_data, gpa_model, model1, model2, model3
    print("--- Start Loading Models ---")
    try:
        if os.path.exists(MODEL_PATH):     ai_model     = joblib.load(MODEL_PATH)
        if os.path.exists(STD_DEV_PATH):   std_dev_data = joblib.load(STD_DEV_PATH)
        if os.path.exists(SVD_MODEL_PATH): svd_data     = joblib.load(SVD_MODEL_PATH)
    except Exception as e:
        print(f"Error in first set: {e}")
    try:
        if os.path.exists(paths["model1"]):   model1    = joblib.load(paths["model1"])
        if os.path.exists(paths["model2"]):   model2    = joblib.load(paths["model2"])
        if os.path.exists(paths["model3"]):   model3    = joblib.load(paths["model3"])
        if os.path.exists(paths["gpa_main"]): gpa_model = joblib.load(paths["gpa_main"])
    except Exception as e:
        print(f"Critical Error loading new models: {e}")

load_all_ai_assets()

app = FastAPI()
Base.metadata.create_all(bind=engine)

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
oauth2_scheme = APIKeyHeader(name="Authorization", auto_error=False)

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=3000)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    actual_token = token.replace("Bearer ", "") if token and "Bearer " in token else token
    try:
        payload = jwt.decode(actual_token, SECRET_KEY, algorithms=[ALGORITHM])
        student_id: str = payload.get("sub")
        if not student_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        return student_id
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

class StudentSchema(BaseModel):
    Student_ID: str
    Name: str
    Password: str
    Email: Optional[str] = None
    Level: Optional[int] = None
    Department_ID: str
    model_config = ConfigDict(from_attributes=True)


@app.post("/login")
def login(id: str, passw: str, db: Session = Depends(get_db)):
    user = db.query(Student).filter(Student.Student_ID == id).first()
    if not user or user.Password != passw:
        raise HTTPException(status_code=401, detail="The username is not found or the password is wrong")
    token = create_token(data={"sub": user.Student_ID})
    return {"access_token": token, "token_type": "bearer"}


@app.get("/get_data")
def get_profile(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    student_id = decode_token(token)

    student = db.query(Student).filter(Student.Student_ID == student_id).first()
    if not student:
        raise HTTPException(status_code=401, detail="Student not found")

    dept = db.query(Department).filter(Department.Department_ID == student.Department_ID).first()
    dept_name = dept.Department_Name if dept else "N/A"

    return {
        "user_data": {
            "student_id": student.Student_ID,
            "name": student.Name,
            "level": student.Level,
            "email": student.Email,
            "department_name": dept_name
        }
    }


@app.get("/calculations")
def Mathematical_calculations(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    student_id = decode_token(token)

    student = db.query(Student).filter(Student.Student_ID == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    records = (
        db.query(Course.Course_Title, Course.Course_ID, Course.Credit_Hours, Enrollment.CourseWork_Grade, Enrollment.Final_Grade)
        .join(CourseOffering, Course.Course_ID == CourseOffering.Course_ID)
        .join(Enrollment, CourseOffering.Offering_ID == Enrollment.Offering_ID)
        .filter(Enrollment.Student_ID == student_id, Enrollment.Final_Grade != None)
        .all()
    )

    attempted_ids = {}
    passed_ids = {}
    sections = {"math": {}, "stat": {}, "cs": {}, "chem": {}, "phys": {}, "others": {}}

    for title, course_id, hours, course_grade, final_grade in records:
        attempted_ids[course_id] = hours

        is_passed = final_grade >= (hours * 30)
        if is_passed:
            passed_ids[course_id] = hours

        title_upper = title.upper()
        if "COMP" in title_upper:
            target_sections = "cs"
        elif "MATH" in title_upper:
            target_sections = "math"
        elif "STAT" in title_upper:
            target_sections = "stat"
        elif "CHEM" in title_upper:
            target_sections = "chem"
        elif "PHYS" in title_upper:
            target_sections = "phys"
        else:
            target_sections = "others"

        if course_id not in sections[target_sections]:
            sections[target_sections][course_id] = is_passed
        elif is_passed:
            sections[target_sections][course_id] = True

    total_hours = sum(attempted_ids.values()) or 0
    total_passed_hours = sum(passed_ids.values()) or 0
    total_faild_hours = total_hours - total_passed_hours

    if student.Department_ID == "D1":
        required_hours = 134
    elif student.Department_ID == "D2":
        required_hours = 140

    total_Remaining_hours = required_hours - total_passed_hours

    final_rates = {}
    for sec, courses in sections.items():
        total_unique_courses = len(courses)
        if total_unique_courses == 0:
            final_rates[f"{sec}_rate"] = 100.0
        else:
            passed_count = sum(1 for status in courses.values() if status == True)
            rate = (passed_count / total_unique_courses) * 100
            final_rates[f"{sec}_rate"] = round(rate, 2)

    return {
        "Remaining hours": total_Remaining_hours,
        "Credit Attempted": total_hours,
        "Credit Passed": total_passed_hours,
        "Credit Failed": total_faild_hours,
        "success rates": final_rates
    }


@app.get("/get_courses")
def get_courses(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    student_id = decode_token(token)

    student = db.query(Student).filter(Student.Student_ID == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    enroll_rows = (
        db.query(
            Enrollment.Offering_ID,
            Enrollment.CourseWork_Grade,
            Enrollment.Final_Grade,
            Enrollment.Attendance,
            Course.Course_ID,
            Course.Course_Title,
            Course.Course_Code,
            Course.Credit_Hours,
            Instructor.Name.label("instructor_name"),
        )
        .join(CourseOffering, Enrollment.Offering_ID == CourseOffering.Offering_ID)
        .join(Course, CourseOffering.Course_ID == Course.Course_ID)
        .outerjoin(Instructor, CourseOffering.Instructor_ID == Instructor.Instructor_ID)
        .filter(Enrollment.Student_ID == student_id)
        .all()
    )

    perm_rows = (
        db.query(CourseDepartment.Course_ID, CourseDepartment.Permission_Type)
        .filter(CourseDepartment.Department_ID == student.Department_ID)
        .all()
    )
    perm_map = {r.Course_ID: r.Permission_Type for r in perm_rows}

    offering_ids = list({r.Offering_ID for r in enroll_rows if r.Final_Grade is not None})
    offering_stats = {}
    if offering_ids:
        raw_stats = (
            db.query(
                Enrollment.Offering_ID,
                func.count(Enrollment.Enrollment_ID).label("total"),
                func.sum(
                    case((Enrollment.Final_Grade >= (
                        db.query(Course.Credit_Hours)
                        .join(CourseOffering, CourseOffering.Course_ID == Course.Course_ID)
                        .filter(CourseOffering.Offering_ID == Enrollment.Offering_ID)
                        .scalar_subquery() * 30
                    ), 1), else_=0)
                ).label("passed")
            )
            .filter(Enrollment.Offering_ID.in_(offering_ids), Enrollment.Final_Grade != None)
            .group_by(Enrollment.Offering_ID)
            .all()
        )
        for row in raw_stats:
            t_count = row.total
            s_count = row.passed or 0
            offering_stats[row.Offering_ID] = {
                "success_rate": f"{round((s_count / t_count) * 100, 1)}%" if t_count else "N/A",
                "num_failed": t_count - s_count
            }

    current_courses = []
    passed = []
    failed = []
    taken_codes = set()

    for person in enroll_rows:
        hours = person.Credit_Hours
        full_mark = hours * 50
        passing_grade = full_mark * 0.6
        student_total = person.Final_Grade or 0
        permission_val = perm_map.get(person.Course_ID, "General")
        instructor_name = person.instructor_name or "TBD"

        if person.Final_Grade is None:
            current_courses.append({
                "course_name": person.Course_Title,
                "course_code": person.Course_Code,
                "course_hours": hours,
                "permission": permission_val,
                "course_instructor": instructor_name,
            })
            continue

        if student_total >= (0.9 * full_mark): grade = "A"
        elif student_total >= (0.85 * full_mark): grade = "A-"
        elif student_total >= (0.80 * full_mark): grade = "B+"
        elif student_total >= (0.75 * full_mark): grade = "B"
        elif student_total >= (0.70 * full_mark): grade = "C+"
        elif student_total >= (0.65 * full_mark): grade = "C"
        elif student_total >= (0.60 * full_mark): grade = "D"
        else: grade = "F"

        stats = offering_stats.get(person.Offering_ID, {})

        course_data = {
            "course_name": person.Course_Title,
            "course_code": person.Course_Code,
            "credit_hours": hours,
            "grade": grade,
            "coursework_grade": person.CourseWork_Grade,
            "student_grade": student_total,
            "attendance": person.Attendance,
            "permission": permission_val,
            "instructor": instructor_name,
            "success_rate_this_semester": stats.get("success_rate", "N/A"),
            "Number_of_students_who_failed": stats.get("num_failed", 0),
        }

        if student_total >= passing_grade:
            del course_data["Number_of_students_who_failed"]
            del course_data["success_rate_this_semester"]
            passed.append(course_data)
            taken_codes.add((person.Course_Title, person.Course_Code))
        else:
            del course_data["grade"]
            failed.append(course_data)

    all_dept_courses = (
        db.query(Course)
        .join(CourseDepartment, Course.Course_ID == CourseDepartment.Course_ID)
        .filter(CourseDepartment.Department_ID == student.Department_ID)
        .all()
    )

    remaining_course_ids = [
        c.Course_ID for c in all_dept_courses
        if (c.Course_Title, c.Course_Code) not in taken_codes
    ]

    hist_stats = {}
    if remaining_course_ids:
        hist_rows = (
            db.query(
                CourseOffering.Course_ID,
                func.count(Enrollment.Enrollment_ID).label("total"),
                func.sum(
                    case((Enrollment.Final_Grade >= (Course.Credit_Hours * 30), 1), else_=0)
                ).label("passed")
            )
            .join(Enrollment, CourseOffering.Offering_ID == Enrollment.Offering_ID)
            .join(Course, CourseOffering.Course_ID == Course.Course_ID)
            .filter(CourseOffering.Course_ID.in_(remaining_course_ids), Enrollment.Final_Grade != None)
            .group_by(CourseOffering.Course_ID)
            .all()
        )
        for row in hist_rows:
            total_h = row.total
            passed_h = row.passed or 0
            hist_stats[row.Course_ID] = {
                "overall_rate": f"{round((passed_h / total_h) * 100, 1)}%" if total_h else "No history",
                "overall_number_failed": total_h - passed_h
            }

    last_instructor_rows = (
        db.query(CourseOffering.Course_ID, Instructor.Name)
        .outerjoin(Instructor, CourseOffering.Instructor_ID == Instructor.Instructor_ID)
        .filter(CourseOffering.Course_ID.in_(remaining_course_ids))
        .order_by(CourseOffering.Course_ID, CourseOffering.Offering_ID.desc())
        .distinct(CourseOffering.Course_ID)
        .all()
    )
    last_instructor_map = {r.Course_ID: (r.Name or "TBD") for r in last_instructor_rows}

    remaining = []
    for c in all_dept_courses:
        if (c.Course_Title, c.Course_Code) in taken_codes:
            continue

        type_info_rem = db.query(CourseDepartment).filter(
            CourseDepartment.Course_ID == c.Course_ID,
            CourseDepartment.Department_ID == student.Department_ID
        ).first()
        permission_rem = type_info_rem.Permission_Type if type_info_rem else "General"

        hs = hist_stats.get(c.Course_ID, {})
        remaining.append({
            "course_name": c.Course_Title,
            "course_code": c.Course_Code,
            "credit_hours": c.Credit_Hours,
            "permission": permission_rem,
            "instructor": last_instructor_map.get(c.Course_ID, "TBD"),
            "overall_success_rate": hs.get("overall_rate", "No history"),
            "overall_number_failed": hs.get("overall_number_failed", 0),
        })

    return {
        "current_courses": current_courses,
        "passed": passed,
        "failed": failed,
        "remaining": remaining,
    }


class PredictionInput(BaseModel):
    full_course_code: str
    expected_coursework: float = Field(..., ge=0)
    expected_attendance: float = Field(..., ge=0, le=15)


@app.post("/ai/predict/secure")
def predict_grade_secure(data: PredictionInput, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    student_id = decode_token(token)

    match = re.search(r'([a-zA-Z]+)\s*(\d+)', data.full_course_code)
    if not match:
        raise HTTPException(status_code=400, detail="Format error. Example: COMP310")

    dept_prefix = match.group(1).upper()
    code_number = int(match.group(2))

    course = db.query(Course).filter(
        and_(Course.Course_Title == dept_prefix, Course.Course_Code == code_number)
    ).first()
    if not course:
        raise HTTPException(status_code=404, detail=f"Course {dept_prefix}{code_number} not found.")

    max_coursework = course.Credit_Hours * 15
    if data.expected_coursework > max_coursework:
        raise HTTPException(status_code=400, detail=f"Max coursework for this course is {max_coursework}")

    if ai_model is None:
        raise HTTPException(status_code=500, detail="AI Model missing on server")

    try:
        input_data = np.array([[data.expected_coursework, data.expected_attendance]])
        raw_prediction = ai_model.predict(input_data)[0]

        max_total_marks = course.Credit_Hours * 50
        max_final_allowed = max_total_marks - max_coursework
        predicted_final = max(0, min(raw_prediction, max_final_allowed))

        margin_of_error = 1.96 * float(std_dev_data) if std_dev_data is not None else 0
        lower_final = max(0, predicted_final - margin_of_error) + data.expected_coursework
        upper_final = min(max_final_allowed, predicted_final + margin_of_error) + data.expected_coursework
        expected_total = data.expected_coursework + predicted_final

        return {
            "status": "Success",
            "course_info": {"name": f"{dept_prefix} {code_number}", "credit_hours": course.Credit_Hours},
            "prediction": {
                "expected_final_score": round(float(predicted_final), 2),
                "expected_total_grade": round(float(expected_total), 2),
                "confidence_interval": {
                    "min_final": round(float(lower_final), 2),
                    "max_final": round(float(upper_final), 2),
                    "error_margin": round(float(margin_of_error), 2),
                }
            },
            "verdict": "Pass" if lower_final >= (course.Credit_Hours * 30) else "Fail"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Error: {str(e)}")


@app.get("/ai/recommend")
def get_recommendations(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    global svd_data
    student_id = decode_token(token)

    if svd_data is None:
        raise HTTPException(status_code=500, detail="SVD Model not loaded on server")

    try:
        if isinstance(svd_data, dict):
            df = svd_data.get("svd_preds_df")
        else:
            df = svd_data

        if df is None:
            raise HTTPException(status_code=500, detail="Invalid SVD data structure")
        if student_id not in df.index:
            raise HTTPException(status_code=404, detail=f"No recommendations for student {student_id}")

        enroll_rows = (
            db.query(CourseOffering.Course_ID, Enrollment.Final_Grade, Course.Credit_Hours)
            .join(Enrollment, CourseOffering.Offering_ID == Enrollment.Offering_ID)
            .join(Course, CourseOffering.Course_ID == Course.Course_ID)
            .filter(Enrollment.Student_ID == student_id)
            .all()
        )
        taken_course_ids = {r.Course_ID for r in enroll_rows}
        passed_course_ids = {
            r.Course_ID for r in enroll_rows
            if r.Final_Grade is not None and r.Final_Grade >= (r.Credit_Hours * 30)
        }

        all_prereqs = db.query(Prerequisite.Course_ID, Prerequisite.Prerequisite_Course_ID).all()
        prereq_map = {}
        for p in all_prereqs:
            prereq_map.setdefault(p.Course_ID, []).append(p.Prerequisite_Course_ID)

        candidate_ids = [c_id for c_id in df.loc[student_id].index if c_id not in taken_course_ids]
        course_info_map = {
            c.Course_ID: c
            for c in db.query(Course).filter(Course.Course_ID.in_(candidate_ids)).all()
        }

        sorted_candidates = df.loc[student_id].sort_values(ascending=False)
        final_recommendations = []

        for c_id, score in sorted_candidates.items():
            if c_id in taken_course_ids:
                continue
            prereq_ids = prereq_map.get(c_id, [])
            if not all(req_id in passed_course_ids for req_id in prereq_ids):
                continue
            course_info = course_info_map.get(c_id)
            if course_info:
                final_recommendations.append({
                    "course_name": f"{course_info.Course_Title} {course_info.Course_Code}",
                    "credit_hours": course_info.Credit_Hours,
                    "match_score": round(float(score), 2),
                })
            if len(final_recommendations) == 50:
                break

        return {"status": "success", "recommendations": final_recommendations}

    except Exception as e:
        print(f"Recommendation Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal AI Logic Error")


@app.get("/ai/predict-graduation-gpa")
def predict_gpa(
    level: int = Query(..., ge=1, le=3, description="Level must be between 1 and 3"),
    gpa_year1: float = Query(0.0, ge=0.0, le=4.0),
    gpa_year2: float = Query(0.0, ge=0.0, le=4.0),
    gpa_year3: float = Query(0.0, ge=0.0, le=4.0),
):
    try:
        if level == 1:
            if model1 is None: raise ValueError("Model 1 not loaded")
            features = np.array([[gpa_year1]])
            prediction = model1.predict(features)[0]
        elif level == 2:
            if model2 is None: raise ValueError("Model 2 not loaded")
            features = np.array([[gpa_year1, gpa_year2]])
            prediction = model2.predict(features)[0]
        elif level == 3:
            if model3 is None: raise ValueError("Model 3 not loaded")
            features = np.array([[gpa_year1, gpa_year2, gpa_year3]])
            prediction = model3.predict(features)[0]

        final_result = max(0.0, min(4.0, float(prediction)))
        return {"status": "success", "predicted_gpa": round(final_result, 2)}

    except Exception as e:
        print(f"Prediction Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal AI Error")