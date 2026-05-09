from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Department(Base):
    __tablename__ = "department"
    Department_ID = Column(String(10), primary_key=True)
    Department_Name = Column(String(100), nullable=False)
    
    students = relationship("Student", back_populates="department")
    instructors = relationship("Instructor", back_populates="department")
    courses = relationship("CourseDepartment", back_populates="department")

class Student(Base):
    __tablename__ = "student"
    Student_ID = Column(String(10), primary_key=True)
    Name = Column(String(100), nullable=False)
    Password = Column(String(100), nullable=False)
    Email = Column(String(100))
    Level = Column(Integer)
    Department_ID = Column(String(10), ForeignKey("department.Department_ID"))

    department = relationship("Department", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")

class Course(Base):
    __tablename__ = "course"
    Course_ID = Column(String(10), primary_key=True)
    Course_Title = Column(String(100))
    Course_Code = Column(String(20))
    Credit_Hours = Column(Integer) 

    offerings = relationship("CourseOffering", back_populates="course")
    departments = relationship("CourseDepartment", back_populates="course")

class Instructor(Base):
    __tablename__ = "instructor"
    Instructor_ID = Column(String(10), primary_key=True)
    Name = Column(String(100))
    Email = Column(String(100))
    Department_ID = Column(String(10), ForeignKey("department.Department_ID"))
    
    department = relationship("Department", back_populates="instructors")

class CourseOffering(Base):
    __tablename__ = "course_offering"
    Offering_ID = Column(String(10), primary_key=True)
    Course_ID = Column(String(10), ForeignKey("course.Course_ID"))
    Instructor_ID = Column(String(10), ForeignKey("instructor.Instructor_ID"))
    Semester = Column(Integer) 
    Year = Column(Integer)

    instructor = relationship("Instructor")
    course = relationship("Course", back_populates="offerings")
    enrollments = relationship("Enrollment", back_populates="offering")

class Enrollment(Base):
    __tablename__ = "enrollment"
    Enrollment_ID = Column(String(10), primary_key=True)
    Student_ID = Column(String(10), ForeignKey("student.Student_ID"))
    Offering_ID = Column(String(10), ForeignKey("course_offering.Offering_ID"))
    Attendance = Column(Integer)
    CourseWork_Grade = Column(Integer)
    Final_Grade = Column(Integer)      

    student = relationship("Student", back_populates="enrollments")
    offering = relationship("CourseOffering", back_populates="enrollments")

class Prerequisite(Base):
    __tablename__ = "prerequisite"
    Course_ID = Column(String(10), ForeignKey("course.Course_ID"), primary_key=True)
    Prerequisite_Course_ID = Column(String(10), ForeignKey("course.Course_ID"), primary_key=True)

class CourseDepartment(Base):
    __tablename__ = "course_department"
    Course_ID = Column(String(10), ForeignKey("course.Course_ID"), primary_key=True)
    Department_ID = Column(String(10), ForeignKey("department.Department_ID"), primary_key=True)
    Permission_Type = Column(String(20))

    course = relationship("Course", back_populates="departments")
    department = relationship("Department", back_populates="courses")