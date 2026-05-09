import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit.components.v1 as components

st.set_page_config(page_title="Student Performance Dashboard", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    * {
        margin: 0;
        padding: 0;
    }
    
    body {
        background-color: #f5f5f5;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    }
    
    .stApp {
        background-color: #f5f5f5;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #000000 !important;
        font-weight: 700 !important;
    }
    
    p, span, div, label {
        color: #000000 !important;
    }
    
    .stSelectbox label {
        color: #000000 !important;
        font-weight: 700 !important;
    }
    
    .stSelectbox [data-baseweb="select"] {
        background-color: white;
    }
    
    .metric-card {
        background-color: white;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 20px;
        text-align: center;
    }
    
    .metric-label {
        font-size: 12px;
        color: #000000;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 10px;
        font-weight: 700;
    }
    
    .metric-value {
        font-size: 32px;
        font-weight: 900;
        margin-bottom: 5px;
        color: #000000;
    }
    
    .chart-box {
        background-color: white;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 20px;
    }
    
    .chart-title {
        font-size: 16px;
        font-weight: 900;
        margin-bottom: 15px;
        color: #000000;
    }
    
    .breakdown-item {
        display: flex;
        justify-content: space-between;
        padding: 10px 0;
        border-bottom: 1px solid #f0f0f0;
        font-size: 14px;
        color: #000000;
        font-weight: 600;
    }
    
    .breakdown-label {
        color: #000000;
        font-weight: 700;
    }
    
    .breakdown-value {
        font-weight: 900;
        color: #000000;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.main .block-container,
div[data-testid="stAppViewContainer"] .block-container,
section[data-testid="stAppViewContainer"] > .main > .block-container {
    padding-top: 25px !important;
    padding-block-start: 25px !important;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    file_name = "Data - Analysis, Database.xlsx"
    
    student_df = pd.read_excel(file_name, sheet_name='Student')
    instructor_df = pd.read_excel(file_name, sheet_name='Instructor')
    course_df = pd.read_excel(file_name, sheet_name='Course')
    course_offering_df = pd.read_excel(file_name, sheet_name='Course_Offering')
    enrollment_df = pd.read_excel(file_name, sheet_name='Enrollment')
    department_df = pd.read_excel(file_name, sheet_name='Department')
    
    return {
        'student': student_df,
        'instructor': instructor_df,
        'course': course_df,
        'course_offering': course_offering_df,
        'enrollment': enrollment_df,
        'department': department_df
    }

data = load_data()

query_params = st.query_params
student_id = query_params.get("student_id", None)

if student_id is None:
    st.error("No student ID provided in URL. Please access via the desktop application.")
    st.stop()

if isinstance(student_id, list):
    student_id = student_id[0]

student_mask = data['student']['Student_ID'].astype(str) == str(student_id)
if not student_mask.any():
    st.error(f"Student with ID '{student_id}' not found.")
    st.stop()

selected_student = data['student'][student_mask].iloc[0]
student_id = selected_student['Student_ID']
student_dept = selected_student['Department_ID']
student_enrollments = data['enrollment'][data['enrollment']['Student_ID'].astype(str) == str(student_id)]

enrollment_with_details = student_enrollments.merge(
    data['course_offering'][['Offering_ID', 'Course_ID', 'Semester', 'Year']],
    on='Offering_ID',
    how='left'
).merge(
    data['course'][['Course_ID', 'Course_Code', 'Course_Title', 'Credit_Hours']],
    on='Course_ID',
    how='left'
)

enrollment_with_details = enrollment_with_details.dropna(subset=['Attendance', 'Final_Grade'])
enrollment_with_details[['Attendance', 'Final_Grade']] = enrollment_with_details[['Attendance', 'Final_Grade']].replace([np.inf, -np.inf], np.nan)
enrollment_with_details = enrollment_with_details.dropna(subset=['Attendance', 'Final_Grade'])

dept_mapping = dict(zip(data['department']['Department_ID'], data['department']['Department_Name']))

components.html("""
<style>
    body {
        margin: 0;
        background: transparent;
        font-family: Calibri, sans-serif;
    }
    .header-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 0 20px 0;
        margin: 0 0 0 0; 
    }
    .title {
        font-size: 28px;
        font-weight: 700;
        color: black;
        margin: 0;
    }
    .print-btn {
        background-color: #0f0736;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 10px;
        font-weight: bold;
        cursor: pointer;
        font-size: 14px;
    }
    .print-btn:hover {
        background-color: #190C5A;
    }
</style>
<div class="header-row">
    <div class="title">Student Performance Dashboard</div>
    <button class="print-btn" onclick="window.parent.print()">Print Report</button>
</div>
""", height=40)
st.markdown("<hr style='margin: 5px 0; border: none; border-top: 2px solid #white;'>", unsafe_allow_html=True)

st.markdown(f"""
<div style='display: flex; gap: 20px; padding: 20px; background-color: white; border-radius: 8px; border: 1px solid #e0e0e0; margin-bottom: 30px;'>
    <div style='width: 80px; height: 80px; background-color: #e0e0e0; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 40px; flex-shrink: 0;'>👤</div>
    <div>
        <h2 style='margin: 0 0 8px 0; font-size: 24px; font-weight: 900; color: #000000;'>{selected_student['Name']}</h2>
        <p style='margin: 4px 0; color: #000000; font-size: 14px; font-weight: 700;'>ID: {selected_student['Student_ID']}</p>
        <p style='margin: 4px 0; color: #000000; font-size: 14px; font-weight: 700;'>Department: {dept_mapping.get(student_dept, student_dept)}</p>
    </div>
</div>
""", unsafe_allow_html=True)

if len(enrollment_with_details) > 0:
    MAX_POINTS_PER_HOUR = 50

    def final_grade_to_gpa_point(score, credit_hours):
        """Map Final_Grade to GPA point using the official percentage scale."""
        if pd.isna(score) or credit_hours == 0:
            return 0.0
        pct = (score / (MAX_POINTS_PER_HOUR * credit_hours)) * 100
        if pct < 60:
            return 0.0      # F
        elif 60 <= pct < 65:
            return 2.0      # D
        elif 65 <= pct < 70:
            return 2.33     # C
        elif 70 <= pct < 75:
            return 2.67     # C+
        elif 75 <= pct < 80:
            return 3.0      # B
        elif 80 <= pct < 85:
            return 3.33     # B+
        elif 85 <= pct < 90:
            return 4.0      # A
        else:  # pct >= 90
            return 4.0      # A+

    def compute_weighted_gpa(enroll_df):
        """
        GPA = Σ(grade_point * credit_hours for PASSED courses) /
              Σ(credit_hours for ALL graded courses).
        Course is PASSED if Final_Grade >= 60% of (50 * Credit_Hours).
        """
        if enroll_df.empty or 'Credit_Hours' not in enroll_df.columns:
            return 0.0

        hours = pd.to_numeric(enroll_df['Credit_Hours'], errors='coerce').fillna(0)
        total_attempted = hours.sum()
        if total_attempted == 0:
            return 0.0

        passed_mask = enroll_df['Final_Grade'] >= 0.6 * (MAX_POINTS_PER_HOUR * hours)
        passed = enroll_df[passed_mask]
        if passed.empty:
            return 0.0

        grade_points = passed.apply(
            lambda row: final_grade_to_gpa_point(row['Final_Grade'],
                                                 row['Credit_Hours']),
            axis=1
        )
        numerator = (grade_points * hours[passed_mask]).sum()
        return numerator / total_attempted

    student_gpa = compute_weighted_gpa(enrollment_with_details)

    student_level = selected_student['Level']

    all_enrollment_global = data['enrollment'].merge(
        data['course_offering'][['Offering_ID', 'Course_ID']],
        on='Offering_ID', how='left'
    ).merge(
        data['course'][['Course_ID', 'Credit_Hours']],
        on='Course_ID', how='left'
    )
    all_enrollment_global = all_enrollment_global.dropna(subset=['Final_Grade'])
    all_enrollment_global[['Final_Grade']] = all_enrollment_global[['Final_Grade']].replace(
        [np.inf, -np.inf], np.nan
    )
    all_enrollment_global = all_enrollment_global.dropna(subset=['Final_Grade'])

    all_enrollment_with_level = all_enrollment_global.merge(
        data['student'][['Student_ID', 'Level']],
        on='Student_ID', how='left'
    )

    same_level_enrollments = all_enrollment_with_level[all_enrollment_with_level['Level'] == student_level]

    all_students_gpa = same_level_enrollments.groupby('Student_ID').apply(
        compute_weighted_gpa
    ).reset_index(name='GPA')
    all_students_gpa_series = all_students_gpa['GPA']

    student_avg_score = enrollment_with_details['Final_Grade'].mean()
    student_attendance = enrollment_with_details['Attendance'].mean() / 15 * 100
    student_rank = (all_students_gpa_series > student_gpa).sum() + 1
    
    if student_gpa >= 3.0:
        gpa_color = "#27ae60"
    elif student_gpa >= 2.0:
        gpa_color = "#3498db"
    else:
        gpa_color = "#e74c3c"
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown(f"""
        <div style='background-color: white; border: 2px solid #e0e0e0; border-radius: 8px; padding: 20px; text-align: center;'>
            <div style='font-size: 12px; color: #000000; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 10px; font-weight: 900;'>GPA</div>
            <div style='font-size: 36px; font-weight: 900; margin-bottom: 5px; color: {gpa_color};'>{student_gpa:.2f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style='background-color: white; border: 2px solid #e0e0e0; border-radius: 8px; padding: 20px; text-align: center;'>
            <div style='font-size: 12px; color: #000000; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 10px; font-weight: 900;'>Avg Score</div>
            <div style='font-size: 36px; font-weight: 900; margin-bottom: 5px; color: #000000;'>{student_avg_score:.0f}%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style='background-color: white; border: 2px solid #e0e0e0; border-radius: 8px; padding: 20px; text-align: center;'>
            <div style='font-size: 12px; color: #000000; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 10px; font-weight: 900;'>Attendance</div>
            <div style='font-size: 36px; font-weight: 900; margin-bottom: 5px; color: #000000;'>{student_attendance:.0f}%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div style='background-color: white; border: 2px solid #e0e0e0; border-radius: 8px; padding: 20px; text-align: center;'>
            <div style='font-size: 12px; color: #000000; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 10px; font-weight: 900;'>Class Rank</div>
            <div style='font-size: 36px; font-weight: 900; margin-bottom: 5px; color: #000000;'>#{student_rank}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown(f"""
        <div style='background-color: white; border: 2px solid #e0e0e0; border-radius: 8px; padding: 20px; text-align: center;'>
            <div style='font-size: 12px; color: #000000; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 10px; font-weight: 900;'>Courses</div>
            <div style='font-size: 36px; font-weight: 900; margin-bottom: 5px; color: #000000;'>{len(enrollment_with_details)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr style='margin: 30px 0; border: none; border-top: 1px solid #e0e0e0;'>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div style='font-size: 16px; font-weight: 900; margin-bottom: 15px; color: #000000;'>GPA Trend Over Semesters</div>", unsafe_allow_html=True)
        
        gpa_by_semester = enrollment_with_details.groupby(['Year', 'Semester']).apply(compute_weighted_gpa).reset_index(name='GPA')
        gpa_by_semester['Period'] = gpa_by_semester['Year'].astype(str) + ' S' + gpa_by_semester['Semester'].astype(str)
        
        fig = go.Figure(data=[
            go.Scatter(
                x=gpa_by_semester['Period'],
                y=gpa_by_semester['GPA'],
                mode='lines+markers',
                line=dict(color='#3498db', width=3),
                marker=dict(size=8, color='#3498db'),
                fill='tozeroy',
                fillcolor='rgba(52, 152, 219, 0.1)',
                hovertemplate='%{x}<br>GPA: %{y:.2f}<extra></extra>',
                text=gpa_by_semester['GPA'].round(2),
                textposition='top center',
                textfont=dict(color='#000000', size=10, family='Arial Black')
            )
        ])
        
        fig.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            margin=dict(l=50, r=20, t=20, b=20),
            height=300,
            yaxis_range=[0,4], 
            xaxis=dict(showgrid=False, tickfont=dict(color='#000000', size=10, family='Arial Black')),
            yaxis=dict(showgrid=True, gridwidth=1, gridcolor='#f0f0f0', tickfont=dict(color='#000000', size=10, family='Arial Black')),
            font=dict(family='Arial Black', size=10, color='#000000'),
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    with col2:
        st.markdown("<div style='font-size: 16px; font-weight: 900; margin-bottom: 15px; color: #000000;'>Attendance vs Score</div>", unsafe_allow_html=True)
        
        fig = go.Figure(data=[
            go.Scatter(
                x=enrollment_with_details['Attendance'],
                y=enrollment_with_details['Final_Grade'],
                mode='markers',
                marker=dict(
                    size=8,
                    color=enrollment_with_details['Final_Grade'],
                    colorscale=[[0, '#e74c3c'], [0.5, '#3498db'], [1, '#27ae60']],
                    showscale=False,
                    line=dict(width=1, color='#000000')
                ),
                text=enrollment_with_details['Course_Title'].astype(str) + ' ' + enrollment_with_details['Course_Code'].astype(str),
                hovertemplate='%{text}<br>Attendance: %{x:.0f}<br>Score: %{y:.0f}<extra></extra>',
                textfont=dict(color='#000000', size=10, family='Arial Black')
            )
        ])

        att_vals = enrollment_with_details['Attendance'].to_numpy(dtype=float)
        grade_vals = enrollment_with_details['Final_Grade'].to_numpy(dtype=float)
        finite_mask = np.isfinite(att_vals) & np.isfinite(grade_vals)
        if finite_mask.sum() >= 2:
            att_slice = att_vals[finite_mask]
            if np.ptp(att_slice) > 0:
                z = np.polyfit(att_slice, grade_vals[finite_mask], 1)
                p = np.poly1d(z)
                x_trend = np.linspace(att_slice.min(), att_slice.max(), 100)
                fig.add_trace(go.Scatter(
                    x=x_trend,
                    y=p(x_trend),
                    mode='lines',
                    line=dict(color='#000000', width=2, dash='dash'),
                    hoverinfo='skip'
                ))
        
        fig.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            margin=dict(l=50, r=20, t=20, b=20),
            height=300,
            xaxis=dict(title='Attendance', showgrid=True, gridwidth=1, gridcolor='#f0f0f0', tickfont=dict(color='#000000', size=10, family='Arial Black'), title_font=dict(color='#000000', size=10, family='Arial Black')),
            yaxis=dict(title='Score', showgrid=True, gridwidth=1, gridcolor='#f0f0f0', tickfont=dict(color='#000000', size=10, family='Arial Black'), title_font=dict(color='#000000', size=10, family='Arial Black')),
            font=dict(family='Arial Black', size=10, color='#000000'),
            hovermode='closest'
        )
        
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div style='font-size: 16px; font-weight: 900; margin-bottom: 15px; color: #000000;'>Student vs Department Avg</div>", unsafe_allow_html=True)
        
        all_enrollment = data['enrollment'].merge(
            data['student'][['Student_ID', 'Department_ID']],
            on='Student_ID'
        )
        
        dept_avg = all_enrollment.groupby('Department_ID')['Final_Grade'].mean().reset_index()
        dept_avg['Department'] = dept_avg['Department_ID'].map(dept_mapping)
        dept_avg['Final_Grade'] = dept_avg['Final_Grade'].replace([np.inf, -np.inf], np.nan).fillna(0)
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=dept_avg['Department'],
            y=dept_avg['Final_Grade'],
            name='Department Average',
            marker=dict(color='#3498db'),
            text=dept_avg['Final_Grade'].round(0),
            textposition='auto',
            textfont=dict(color='#000000', size=11, family='Arial Black'),
            hovertemplate='%{x}<br>Avg: %{y:.0f}<extra></extra>'
        ))
        
        fig.add_trace(go.Bar(
            x=[dept_mapping.get(student_dept, student_dept)],
            y=[student_avg_score],
            name='Your Score',
            marker=dict(color='#27ae60'),
            text=[student_avg_score.round(0)],
            textposition='auto',
            textfont=dict(color='#000000', size=11, family='Arial Black'),
            hovertemplate='Your Score<br>%{y:.0f}<extra></extra>'
        ))
        
        fig.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            margin=dict(l=50, r=20, t=20, b=20),
            height=300,
            xaxis=dict(showgrid=False, tickfont=dict(color='#000000', size=10, family='Arial Black'), title_font=dict(color='#000000', size=10, family='Arial Black')),
            yaxis=dict(showgrid=True, gridwidth=1, gridcolor='#f0f0f0', tickfont=dict(color='#000000', size=10, family='Arial Black'), title_font=dict(color='#000000', size=10, family='Arial Black')),
            font=dict(family='Arial Black', size=10, color='#000000'),
            hovermode='x unified',
            barmode='group',
            legend=dict(font=dict(color='#000000', size=10, family='Arial Black'))
        )
        
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
with col2:
        st.markdown("<div style='font-size: 16px; font-weight: 900; margin-bottom: 15px; color: #000000;'>Top vs Weakest Courses</div>", unsafe_allow_html=True)
        
        top_courses = enrollment_with_details.nlargest(5, 'Final_Grade')[['Course_Code', 'Course_Title', 'Final_Grade']].copy()
        weakest_courses = enrollment_with_details.nsmallest(5, 'Final_Grade')[['Course_Code', 'Course_Title', 'Final_Grade']].copy()
        
        top_courses['Label'] = top_courses['Course_Title'].astype(str) + ' ' + top_courses['Course_Code'].fillna('').astype(str)
        weakest_courses['Label'] = weakest_courses['Course_Title'].astype(str) + ' ' + weakest_courses['Course_Code'].fillna('').astype(str)
        
        combined = pd.concat([
            top_courses[['Label', 'Final_Grade']].assign(Type='Top'),
            weakest_courses[['Label', 'Final_Grade']].assign(Type='Weakest')
        ])
        combined['Final_Grade'] = combined['Final_Grade'].replace([np.inf, -np.inf], np.nan).fillna(0)

        colors = ['#27ae60' if t == 'Top' else '#e74c3c' for t in combined['Type']]
        
        fig = go.Figure(data=[go.Pie(
            labels=combined['Label'],
            values=combined['Final_Grade'],
            marker=dict(colors=colors, line=dict(color='white', width=2)),
            textfont=dict(color='#000000', size=8, family='Arial Black'),
            textposition='inside',
            hovertemplate='%{label}<br>Grade: %{value:.0f}<extra></extra>'
        )])
        
        fig.update_layout(
            paper_bgcolor='white',
            margin=dict(l=20, r=20, t=20, b=20),
            height=300,
            font=dict(family='Arial Black', size=8, color='#000000'),
            legend=dict(font=dict(color='#000000', size=7, family='Arial Black'), orientation='v', yanchor='middle', y=0.5, xanchor='left', x=1.02)
        )
        
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
st.markdown("""
<style>
    table tr:hover {
        background-color: #e8f4f8 !important;
    }
</style>
""", unsafe_allow_html=True)
st.markdown("<hr style='margin: 30px 0; border: none; border-top: 1px solid #e0e0e0;'>", unsafe_allow_html=True)
    
st.markdown("<div style='font-size: 16px; font-weight: 900; margin-bottom: 15px; color: #000000;'>Courses Enrolled</div>", unsafe_allow_html=True)

courses_table = enrollment_with_details[['Course_Title', 'Course_Code', 'Attendance', 'CourseWork_Grade', 'Final_Grade', 'Semester', 'Year']].copy()
courses_table.columns = ['Title', 'Code', 'Attendance', 'Coursework', 'Final Grade', 'Semester', 'Year']

for col in ['Attendance', 'Coursework', 'Final Grade']:
    courses_table[col] = pd.to_numeric(courses_table[col], errors='coerce').fillna(0).astype(int)

courses_table = courses_table.reset_index(drop=True)

html_table = "<table style='width: 100%; border-collapse: collapse; background-color: white;'>"
html_table += "<tr style='background-color: #f0f0f0;'>"
for col in courses_table.columns:
    html_table += f"<th style='border: 1px solid #e0e0e0; padding: 12px; text-align: center; color: #000000; font-weight: 900;'>{col}</th>"
html_table += "</tr>"

for idx, row in courses_table.iterrows():
    html_table += "<tr>"
    for val in row:
        html_table += f"<td style='border: 1px solid #e0e0e0; padding: 12px; text-align: center; color: #000000;'>{val}</td>"
    html_table += "</tr>"

html_table += "</table>"

st.markdown(html_table, unsafe_allow_html=True)