from PySide6.QtCore import QUrl, QTimer, Signal, QObject, QEvent, QEventLoop, Qt
from PySide6.QtWidgets import QWidget, QFileDialog, QProgressBar, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QSpacerItem, QSizePolicy
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QFont

from MainWindow_UI import Ui_MainWindow
from StreamlitServer import StreamlitServer, STREAMLIT_URL
from AuthenticationService import get_auth_service
from API_URL import API_URL
from Network import NetworkClient

import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import ssl
import re

class HorizontalWheel(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Wheel:
            delta = event.angleDelta().y()
            obj.horizontalScrollBar().setValue(obj.horizontalScrollBar().value() - delta)
            return True
        return super().eventFilter(obj, event)

class ProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRange(0, 100)
        self.setTextVisible(False)

class MainWindow(QWidget):
    logout_requested = Signal()
    _GRADE_POINTS = {
        'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'C+': 2.67, 'C': 2.33, 'D': 2.0, 'F': 0.0
    }
    _GRADE_NAMES = {
        'A': 'Excellent', 'A-': 'Excellent', 'B+': 'Very Good', 'B': 'Very Good',
        'C+': 'Good', 'C': 'Good', 'D': 'Acceptable', 'F': 'Failed'
    }
    GPAStyling = '<html><head/><body><p align="center"><span style=" font-size:36pt;">{}</span></p></body></html>'
    GPABadSign = (
        "border-radius: 10px;"
        "background-color: qlineargradient(x1:0, x2:1, y1:0, y2:1, stop:0 rgb(128,15,28), stop:1 black);"
        "color: white;"
    )
    GPAMediocreSign = (
        "border-radius: 10px;"
        "background-color: qlineargradient(x1:0, x2:1, y1:0, y2:1, stop:0 rgb(27,49,96), stop:1 black);"
        "color: white;"
    )
    GPAGreatSign = (
        "border-radius: 10px;"
        "background-color: qlineargradient(x1:0, x2:1, y1:0, y2:1, stop:0 rgb(7,74,45), stop:1 black);"
        "color: white;"
    )

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.SearchForCourseButton.setCheckable(False)
        self.ui.UndoButton.setCheckable(False)

        self.HorizontalWheel = HorizontalWheel()
        self.ui.CurrentCoursesScrollArea.installEventFilter(self.HorizontalWheel)

        self.student_id = None
        self.streamlit = StreamlitServer()
        self.current_gpa = 0.0

        self.ui.ProfileButton.clicked.connect(self.switch_to_profile)
        self.ui.CoursesButton.clicked.connect(self.switch_to_courses)
        self.ui.AiButton.clicked.connect(self.switch_to_ai)
        self.ui.AnalysisButton.clicked.connect(self.switch_to_analysis)
        self.ui.LogOutButton.clicked.connect(self._on_logout_clicked)
        self.ui.SearchForCourseButton.clicked.connect(self._search_course)
        self.ui.UndoButton.clicked.connect(self._undo_search)

        self.ui.FinalGradeCalculatorButton.clicked.connect(lambda: self._switch_ai_subpage(0))
        self.ui.WhatToRegesterButton.clicked.connect(lambda: self._switch_ai_subpage(1))
        self.ui.FinalGPAPredictorButton.clicked.connect(lambda: self._switch_ai_subpage(2))

        self.ai_network = NetworkClient()
        self.predict_output_index = 0
        self.ui.FinalGradeCalculateButton.clicked.connect(self._on_predict_grade_clicked)

        self.ui.FinalGPAPredictorPredictButton.clicked.connect(self._on_predict_gpa_clicked)

        self.registration_progress_bars = {}
        self._setup_registration_progress_bars()

        self._setup_progress_bars()
        self._setup_analysis_page()
        self.switch_to_profile()

        self.streamlit.start()
        QTimer.singleShot(2000, self._check_streamlit_alive)

        self.passed_courses_layout = self.ui.PassedCoursesActualScrollAreaWidget_Layout
        self.failed_courses_layout = self.ui.FailedCoursesActualScrollAreaWidget_Layout
        self.remaining_courses_layout = self.ui.RemainingCoursesActualScrollAreaWidget_Layout

        self.ui.PassedCourse_1.hide()
        self.ui.FailedCourse_1.hide()
        self.ui.RemainingCourse_1.hide()

        self._clear_layout(self.passed_courses_layout)
        self._clear_layout(self.failed_courses_layout)
        self._clear_remaining_layout()

        self.auth_service = get_auth_service()
        self.auth_service.courses_loaded.connect(self._populate_courses)
        self.auth_service.login_success.connect(self._on_login_success)

        self.all_course_cards = []
        self.default_line_edit_style = self.ui.SearchForCourseLineEdit.styleSheet()
        self.error_line_edit_style = """border-radius: 10px;
            background-color: qlineargradient(
                x1:0, x2:1
                stop:0 rgb(27, 49, 96),
                stop:1 rgb(7, 74, 45)
            );
            color: "red";
            padding-left: 10px;"""

        self.search_active = False

    def reset_ui(self):
        self.ui.ProfileButton.setChecked(True)
        self.ui.AnalysisButton.setChecked(False)
        self.ui.CoursesButton.setChecked(False)
        self.ui.AiButton.setChecked(False)
        self.ui.LogOutButton.setChecked(False)
        self.ui.SearchForCourseButton.setChecked(False)
        self.ui.UndoButton.setChecked(False)

        self.ui.StackedWidget.setCurrentIndex(0)

        self.ui.SearchForCourseLineEdit.clear()
        self.ui.SearchForCourseLineEdit.setStyleSheet(self.default_line_edit_style)

        self._clear_layout(self.passed_courses_layout)
        self._clear_layout(self.failed_courses_layout)
        self._clear_remaining_layout()
        for i in range(5):
            card = getattr(self.ui, f"CurrentCourse_{i+1}", None)
            if card:
                card.hide()

        self.all_course_cards = []
        self.search_active = False
        self._set_scroll_enabled(True)

        self.current_course_cards = []
        self.passed_course_cards = []
        self.failed_course_cards = []
        self.remaining_course_cards = []
        self.current_courses_data = []
        self.passed_courses_data = []
        self.failed_courses_data = []

        self._clear_ai_sub_buttons()
        self._recommendations_loaded = False 

    def _rebuild_all_course_cards(self):
        cards = []
        if hasattr(self, 'current_course_cards'):
            cards.extend(self.current_course_cards)
        if hasattr(self, 'passed_course_cards'):
            cards.extend(self.passed_course_cards)
        if hasattr(self, 'failed_course_cards'):
            cards.extend(self.failed_course_cards)
        if hasattr(self, 'remaining_course_cards'):
            cards.extend(self.remaining_course_cards)
        self.all_course_cards = cards

    def _clear_layout(self, layout):
        while layout.count() > 1:
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def _clear_remaining_layout(self):
        layout = self.remaining_courses_layout
        while layout.count() > 1:
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def _setup_progress_bars(self):
        self.progress_bars = {}
        mapping = [
            (self.ui.COMPProgressBar_Layout, self.ui.COMPValueLabel, self.ui.COMPLabel),
            (self.ui.STATProgressBar_Layout, self.ui.STATValueLabel, self.ui.STATLabel),
            (self.ui.MATHProgressBar_Layout, self.ui.MATHValueLabel, self.ui.MATHLabel),
            (self.ui.PHYSProgressBar_Layout, self.ui.PHYSValueLabel, self.ui.PHYSLabel),
            (self.ui.CHEMProgressBar_Layout, self.ui.CHEMValueLabel, self.ui.CHEMLabel),
            (self.ui.OthersProgressBar_Layout, self.ui.OthersValueLabel, self.ui.OthersLabel)
        ]
        for layout, value_label, category_label in mapping:
            progress_bar = ProgressBar()
            layout.addWidget(progress_bar)
            self.progress_bars[value_label] = (progress_bar, category_label, value_label)

    def _setup_registration_progress_bars(self):
        """Create white VERTICAL progress bars with 10px border-radius and transparent background."""
        style = (
            "QProgressBar { background: transparent; border: none; }"
            "QProgressBar::chunk { background-color: #FFFFFF; border-radius: 10px; }"
        )
        mapping = [
            (self.ui.RegesteredCOMPProgressBar, self.ui.RegesteredCOMPValueLabel, self.ui.RegesteredCOMPLabel),
            (self.ui.RegesteredSTATProgressBar, self.ui.RegesteredSTATValueLabel, self.ui.RegesteredSTATLabel),
            (self.ui.RegesteredMATHProgressBar, self.ui.RegesteredMATHValueLabel, self.ui.RegesteredMATHLabel),
            (self.ui.RegesteredOthersProgressBar, self.ui.RegesteredOthersValueLabel, self.ui.RegesteredOthersLabel)
        ]
        for placeholder_widget, value_label, category_label in mapping:
            if placeholder_widget.layout() is not None:
                QWidget().setLayout(placeholder_widget.layout())
            new_layout = QVBoxLayout(placeholder_widget)
            new_layout.setContentsMargins(0, 0, 0, 0)
            new_layout.setSpacing(0)
            bar = ProgressBar()
            bar.setOrientation(Qt.Orientation.Vertical)
            bar.setStyleSheet(style)
            bar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
            bar.setMinimumWidth(15)
            new_layout.addWidget(bar)
            self.registration_progress_bars[value_label] = (bar, category_label, value_label)

    def set_student_id(self, student_id: str):
        self.student_id = student_id

    def preload_analysis(self):
        url = f"{STREAMLIT_URL}?student_id={self.student_id}"
        self.analysis_web_view.setUrl(QUrl(url))

    def switch_to_profile(self):
        self.ui.StackedWidget.setCurrentIndex(0)
        self._set_active_button(self.ui.ProfileButton)

    def switch_to_analysis(self):
        self.ui.StackedWidget.setCurrentIndex(1)
        self._set_active_button(self.ui.AnalysisButton)

    def switch_to_ai(self):
        self.ui.StackedWidget.setCurrentIndex(2)
        self._set_active_button(self.ui.AiButton)
        self._reset_ai_predictor()
        self._reset_gpa_predictor()
        self._auto_fill_gpa_inputs()
        if not getattr(self, '_recommendations_loaded', False):
            self._load_recommendations()

    def _load_recommendations(self):
        token = getattr(self.auth_service, 'access_token', None)
        if not token:
            return
        url = f"{API_URL}/ai/recommend"
        headers = {"Authorization": f"Bearer {token}"}
        self.ai_network.response_received.connect(self._handle_recommendations_response)
        self.ai_network.get(url, headers)

    def _handle_recommendations_response(self, data: dict):
        self.ai_network.response_received.disconnect(self._handle_recommendations_response)
        self._recommendations_loaded = True

        status = data.get("status")
        if status != "success":
            return

        recs = data.get("recommendations", [])
        if not recs:
            return

        level = int(self.user_data.get("level", 1))
        dept_name = self.user_data.get("department_name", "")
        dept_id = "D1" if dept_name == "CS" else "D2"

        if dept_id == "D1":
            available_map = {1: 17, 2: 17, 3: 16, 4: 16}
        else:
            available_map = {1: 17, 2: 18, 3: 17, 4: 18}
        target_hours = available_map.get(level, 0)

        style_html = '<html><head/><body><p><span style=" font-size:14pt; font-weight:400;">{}</span></p></body></html>'
        self.ui.WhatToRegisterCurrentLevelValueLabel.setText(style_html.format(str(level)))
        self.ui.AvailableHoursValueLabel.setText(style_html.format(str(target_hours)))

        remaining_lookup = {}
        for rem in getattr(self, 'remaining_courses_data', []):
            key = (rem.get("course_name", "") + rem.get("course_code", "")).replace(" ", "")
            remaining_lookup[key] = rem

        selected = []
        current_sum = 0
        for rec in recs:
            course_full_name = rec.get("course_name", "")
            lookup_key = course_full_name.replace(" ", "")
            rem_data = remaining_lookup.get(lookup_key, {})
            pass_rate = rem_data.get("overall_success_rate", "No history")
            if pass_rate == "No history" or pass_rate == "N/A":
                continue

            hrs = rec.get("credit_hours", 0)
            if current_sum + hrs <= target_hours:
                selected.append(rec)
                current_sum += hrs

        self.ui.CoursesToRegisterValueLabel.setText(style_html.format(str(len(selected))))

        scroll_widget = self.ui.WhatToRegisterPageScrollAreaActualWidget
        scroll_layout = scroll_widget.layout()
        if scroll_layout is None:
            scroll_layout = QVBoxLayout(scroll_widget)
            scroll_layout.setSpacing(5)
            scroll_layout.setContentsMargins(0, 0, 0, 0)
        else:
            while scroll_layout.count():
                item = scroll_layout.takeAt(0)
                w = item.widget()
                if w:
                    w.deleteLater()

        scroll_layout.setContentsMargins(0, 35, 0, 0)

        for idx, rec in enumerate(selected, 1):
            course_full_name = rec.get("course_name", "")
            course_hours = rec.get("credit_hours", "")
            lookup_key = course_full_name.replace(" ", "")
            rem_data = remaining_lookup.get(lookup_key, {})
            permission = rem_data.get("permission", "N/A")
            pass_rate = rem_data.get("overall_success_rate", "N/A")
            remaining_students = rem_data.get("overall_number_failed", "N/A")
            item_widget = self._create_suggested_course_item(
                idx, course_full_name, permission, course_hours, remaining_students, pass_rate
            )
            scroll_layout.addWidget(item_widget)

        if hasattr(self.ui, 'layoutWidget'):
            self.ui.layoutWidget.hide()

        card_height = 105
        spacing = 5
        count = len(selected)
        content_height = count * card_height + max(0, count - 1) * spacing if count else 0

        if count % 2 == 1:
            container_height = (count + 1) * card_height + (count - 1) * spacing
        else:
            container_height = content_height

        top_margin = 35
        final_content_height = content_height + top_margin
        final_container_height = container_height + top_margin

        scroll_widget.setMinimumHeight(final_content_height)
        scroll_widget.setMaximumHeight(final_content_height)
        scroll_widget.setGeometry(0, 0, 585, final_content_height)

        outer_widget = self.ui.WhatToRegisterPageScrollAreaWidget
        outer_widget.setMinimumHeight(final_container_height)
        outer_widget.setMaximumHeight(final_container_height)
        outer_widget.setGeometry(0, 0, 585, final_container_height)

        categories = {"COMP": 0, "STAT": 0, "MATH": 0, "OTHERS": 0}
        for rec in selected:
            name = rec.get("course_name", "").upper()
            if "COMP" in name:
                categories["COMP"] += 1
            elif "STAT" in name:
                categories["STAT"] += 1
            elif "MATH" in name:
                categories["MATH"] += 1
            else:
                categories["OTHERS"] += 1
        total = len(selected) or 1

        for value_label, (bar, cat_label, val_label) in self.registration_progress_bars.items():
            if value_label is self.ui.RegesteredCOMPValueLabel:
                cnt = categories["COMP"]
            elif value_label is self.ui.RegesteredSTATValueLabel:
                cnt = categories["STAT"]
            elif value_label is self.ui.RegesteredMATHValueLabel:
                cnt = categories["MATH"]
            elif value_label is self.ui.RegesteredOthersValueLabel:
                cnt = categories["OTHERS"]
            else:
                cnt = 0
            pct = round((cnt / total) * 100)
            bar.setValue(pct)
            val_label.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:11pt; font-weight:700;">{pct}%</span></p></body></html>'
            )

    def switch_to_courses(self):
        self.ui.StackedWidget.setCurrentIndex(3)
        self._set_active_button(self.ui.CoursesButton)

    def _set_active_button(self, active_btn):
        for btn in [self.ui.ProfileButton, self.ui.AnalysisButton,
                    self.ui.AiButton, self.ui.CoursesButton]:
            btn.setChecked(btn is active_btn)
        if active_btn is self.ui.AiButton:
            self._sync_ai_sub_buttons()
        else:
            self._clear_ai_sub_buttons()

    def _clear_ai_sub_buttons(self):
        for btn in [self.ui.FinalGradeCalculatorButton,
                     self.ui.WhatToRegesterButton,
                     self.ui.FinalGPAPredictorButton]:
            btn.setChecked(False)

    def _sync_ai_sub_buttons(self):
        idx = self.ui.AIPageStackedWidget.currentIndex()
        buttons = [self.ui.FinalGradeCalculatorButton,
                   self.ui.WhatToRegesterButton,
                   self.ui.FinalGPAPredictorButton]
        for i, btn in enumerate(buttons):
            btn.setChecked(i == idx)

    def _switch_ai_subpage(self, index):
        self._set_active_button(self.ui.AiButton)
        self.ui.AIPageStackedWidget.setCurrentIndex(index)
        self._sync_ai_sub_buttons()

    def _reset_ai_predictor(self):
        self.ui.CourseIDErrorLabel.hide()
        self.ui.CourseWorkErrorLabel.hide()
        self.ui.CourseWorkErrorValueLabel.hide()
        self.ui.AttendanceErrorLabel.hide()
        for i in range(1, 7):
            widget = getattr(self.ui, f"FinalGradeCalculatorOutputWidget_{i}", None)
            if widget:
                widget.hide()
        self.predict_output_index = 0
        self.ui.CourseIDBox.clear()
        self.ui.CourseWorkBox.clear()
        self.ui.AttendanceBox.clear()
        self._switch_ai_subpage(0)

    def _on_predict_grade_clicked(self):
        course_input = self.ui.CourseIDBox.text().strip()
        coursework_input = self.ui.CourseWorkBox.text().strip()
        attendance_input = self.ui.AttendanceBox.text().strip()

        self.ui.CourseIDErrorLabel.hide()
        self.ui.CourseWorkErrorLabel.hide()
        self.ui.CourseWorkErrorValueLabel.hide()
        self.ui.AttendanceErrorLabel.hide()

        if not course_input:
            self.ui.CourseIDErrorLabel.show()
            return

        errors = []

        coursework_val = None
        if coursework_input:
            try:
                coursework_val = float(coursework_input)
            except ValueError:
                errors.append(('coursework', 'invalid'))
            else:
                if coursework_val < 0:
                    errors.append(('coursework', 'negative'))
        else:
            errors.append(('coursework', 'empty'))

        attendance_val = None
        if attendance_input:
            try:
                attendance_val = float(attendance_input)
            except ValueError:
                errors.append(('attendance', 'invalid'))
            else:
                if attendance_val < 0:
                    errors.append(('attendance', 'negative'))
                elif attendance_val > 15:
                    errors.append(('attendance', 'max'))
        else:
            errors.append(('attendance', 'empty'))

        if errors:
            for field, reason in errors:
                if field == 'coursework':
                    if reason in ('invalid', 'negative'):
                        self.ui.CourseWorkErrorLabel.setText(
                            '<html><head/><body><p><span style=" font-size:14pt;">The Number Must be Positive</span></p></body></html>'
                        )
                        self.ui.CourseWorkErrorLabel.show()
                        self.ui.CourseWorkErrorValueLabel.hide()
                    elif reason == 'empty':
                        self.ui.CourseWorkErrorLabel.setText(
                            '<html><head/><body><p><span style=" font-size:14pt;">Coursework is required</span></p></body></html>'
                        )
                        self.ui.CourseWorkErrorLabel.show()
                        self.ui.CourseWorkErrorValueLabel.hide()
                elif field == 'attendance':
                    if reason in ('invalid', 'negative'):
                        self.ui.AttendanceErrorLabel.setText(
                            '<html><head/><body><p><span style=" font-size:14pt;">The Number Must be Positive</span></p></body></html>'
                        )
                        self.ui.AttendanceErrorLabel.show()
                    elif reason == 'max':
                        self.ui.AttendanceErrorLabel.setText(
                            '<html><head/><body><p><span style=" font-size:14pt;">Maximum Attendance is 15</span></p></body></html>'
                        )
                        self.ui.AttendanceErrorLabel.show()
                    elif reason == 'empty':
                        self.ui.AttendanceErrorLabel.setText(
                            '<html><head/><body><p><span style=" font-size:14pt;">Attendance is required</span></p></body></html>'
                        )
                        self.ui.AttendanceErrorLabel.show()
            return

        payload = {
            "full_course_code": course_input.upper(),
            "expected_coursework": coursework_val,
            "expected_attendance": attendance_val
        }
        token = getattr(self.auth_service, 'access_token', None)
        if not token:
            return
        url = f"{API_URL}/ai/predict/secure"
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        self.ai_network.response_received.connect(self._handle_predict_response)
        self.ai_network.post_json(url, payload, headers)

    def _handle_predict_response(self, data: dict):
        self.ai_network.response_received.disconnect(self._handle_predict_response)
        status = data.get("status", "")
        full_course_code = self.ui.CourseIDBox.text().strip().upper()
        coursework_val = self.ui.CourseWorkBox.text().strip()
        attendance_val = self.ui.AttendanceBox.text().strip()

        if status == "Success":
            idx = (self.predict_output_index % 6) + 1
            widget = getattr(self.ui, f"FinalGradeCalculatorOutputWidget_{idx}", None)
            if widget:
                style_html = '<html><head/><body><p><span style=" font-size:14pt; font-weight:400;">{}</span></p></body></html>'
                display_id = re.sub(r'([A-Za-z]+)\s*(\d+)', r'\1 \2', full_course_code).upper()

                id_val = getattr(self.ui, f"IDValueLabel_{idx}", None)
                if id_val:
                    id_val.setText(style_html.format(display_id))
                    id_val.setStyleSheet("background-color: none; font-family: Calibri;")

                cw_val = getattr(self.ui, f"CourseWorkValueLabel_{idx}", None)
                if cw_val:
                    cw_val.setText(style_html.format(coursework_val))
                    cw_val.setStyleSheet("background-color: none; font-family: Calibri;")

                att_val = getattr(self.ui, f"AttendanceValueLabel_{idx}", None)
                if att_val:
                    att_val.setText(style_html.format(attendance_val))
                    att_val.setStyleSheet("background-color: none; font-family: Calibri;")

                min_val = getattr(self.ui, f"MinExpectedFinalGradeValueLabel_{idx}", None)
                max_val = getattr(self.ui, f"MaxExpectedFinalGradeValueLabel_{idx}", None)
                if min_val and max_val:
                    confidence = data.get("prediction", {}).get("confidence_interval", {})
                    min_predicted = confidence.get("min_final", 0)
                    max_predicted = confidence.get("max_final", 0)
                    min_val = getattr(self.ui, f"MinExpectedFinalGradeValueLabel_{idx}", None)
                    max_val = getattr(self.ui, f"MaxExpectedFinalGradeValueLabel_{idx}", None)
                    if min_val and max_val:
                        confidence = data.get("prediction", {}).get("confidence_interval", {})
                        min_predicted = confidence.get("min_final", 0)
                        max_predicted = confidence.get("max_final", 0)
                        min_val.setText(style_html.format(str(int(round(min_predicted)))))
                        min_val.setStyleSheet("background-color: none; font-family: Calibri;")
                        max_val.setText(style_html.format(str(int(round(max_predicted)))))
                        max_val.setStyleSheet("background-color: none; font-family: Calibri;")

                        verdict = data.get("verdict", "Fail")
                        if verdict.lower() == "fail":
                            widget.setStyleSheet(self.GPABadSign)
                        else:
                            widget.setStyleSheet(self.GPAGreatSign)

                widget.show()
                self.predict_output_index += 1
        else:
            detail = data.get("detail", "")
            if isinstance(detail, list):
                detail = " ".join(str(d) for d in detail)
            detail = detail.lower() if isinstance(detail, str) else ""

            if "max coursework" in detail:
                match = re.search(r'is (\d+)', detail)
                max_cw = match.group(1) if match else "?"
                self.ui.CourseWorkErrorLabel.setText(
                    '<html><head/><body><p><span style=" font-size:14pt;">Maximum for this Course is:</span></p></body></html>'
                )
                self.ui.CourseWorkErrorValueLabel.setText(
                    f'<html><head/><body><p><span style=" font-size:14pt; font-weight:400;">{max_cw}</span></p></body></html>'
                )
                self.ui.CourseWorkErrorLabel.show()
                self.ui.CourseWorkErrorValueLabel.show()
            elif "attendance" in detail:
                self.ui.AttendanceErrorLabel.setText(
                    '<html><head/><body><p><span style=" font-size:14pt;">Maximum Attendance is 15</span></p></body></html>'
                )
                self.ui.AttendanceErrorLabel.show()
            else:
                self.ui.CourseIDErrorLabel.show()

    def _reset_gpa_predictor(self):
        """Hide error labels and the result card when entering the AI page."""
        self.ui.Level_1_GPAErrorLabel.hide()
        self.ui.Level_2_GPAErrorLabel.hide()
        self.ui.ExpectedGPACard.hide()
        self.ui.Level_1_GPABox.clear()
        self.ui.Level_2_GPABox.clear()

    def _auto_fill_gpa_inputs(self):
        """
        Read level and current GPA, then:
        - display level
        - show/hide the Level 2 input group
        - pre‑fill the boxes accordingly
        """
        level = int(self.user_data.get("level", 1))
        gpa = getattr(self, 'current_gpa', 0.0)
        html_val = '<html><head/><body><p><span style=" font-size:14pt; font-weight:400;">{}</span></p></body></html>'

        self.ui.FinalGPAPredictorCurrentLevelValueLabel.setText(html_val.format(str(level)))
        self.ui.CurrentGPAValueLabel.setText(html_val.format(f"{gpa:.2f}"))

        level2_widgets = [
            self.ui.Level_2_GPABoxLabel,
            self.ui.Level_2_GPABox,
            self.ui.Level_2_GPAErrorLabel
        ]

        if level == 1:
            for w in level2_widgets:
                w.hide()
            self.ui.Level_1_GPABox.setText(f"{gpa:.2f}")
        elif level == 2:
            for w in level2_widgets:
                w.hide()
            self.ui.Level_1_GPABox.clear()
        else:
            for w in level2_widgets:
                w.show()
            self.ui.Level_1_GPABox.clear()
            self.ui.Level_2_GPABox.clear()

        self.ui.Level_1_GPAErrorLabel.hide()
        self.ui.Level_2_GPAErrorLabel.hide()

    def _on_predict_gpa_clicked(self):
        self.ui.Level_1_GPAErrorLabel.hide()
        self.ui.Level_2_GPAErrorLabel.hide()
        self.ui.ExpectedGPACard.hide()

        level = int(self.user_data.get("level", 1))
        gpa = getattr(self, 'current_gpa', 0.0)

        year1_str = self.ui.Level_1_GPABox.text().strip()
        year2_str = self.ui.Level_2_GPABox.text().strip()

        if level == 1:
            if not year1_str:
                self._show_gpa_error(self.ui.Level_1_GPAErrorLabel, "Please fill the data")
                return
            try:
                v = float(year1_str)
                if v < 0 or v > 4:
                    self._show_gpa_error(self.ui.Level_1_GPAErrorLabel, "Value must be between 0 and 4")
                    return
            except ValueError:
                self._show_gpa_error(self.ui.Level_1_GPAErrorLabel, "Enter a valid number")
                return
            gpa_year1 = v
            gpa_year2 = 0.0
            gpa_year3 = 0.0

        elif level == 2:
            if not year1_str:
                self._show_gpa_error(self.ui.Level_1_GPAErrorLabel, "Please fill the data")
                return
            try:
                v = float(year1_str)
                if v < 0 or v > 4:
                    self._show_gpa_error(self.ui.Level_1_GPAErrorLabel, "Value must be between 0 and 4")
                    return
            except ValueError:
                self._show_gpa_error(self.ui.Level_1_GPAErrorLabel, "Enter a valid number")
                return
            gpa_year1 = v
            gpa_year2 = gpa
            gpa_year3 = 0.0

        else:
            if not year1_str:
                self._show_gpa_error(self.ui.Level_1_GPAErrorLabel, "Please fill the data")
                return
            if not year2_str:
                self._show_gpa_error(self.ui.Level_2_GPAErrorLabel, "Please fill the data")
                return
            try:
                v1 = float(year1_str)
                if v1 < 0 or v1 > 4:
                    self._show_gpa_error(self.ui.Level_1_GPAErrorLabel, "Value must be between 0 and 4")
                    return
                v2 = float(year2_str)
                if v2 < 0 or v2 > 4:
                    self._show_gpa_error(self.ui.Level_2_GPAErrorLabel, "Value must be between 0 and 4")
                    return
            except ValueError:
                try:
                    float(year1_str)
                except ValueError:
                    self._show_gpa_error(self.ui.Level_1_GPAErrorLabel, "Enter a valid number")
                    return
                try:
                    float(year2_str)
                except ValueError:
                    self._show_gpa_error(self.ui.Level_2_GPAErrorLabel, "Enter a valid number")
                    return
            gpa_year1 = v1
            gpa_year2 = v2
            gpa_year3 = gpa

        token = getattr(self.auth_service, 'access_token', None)
        if not token:
            return
        params = {
            "level": level,
            "gpa_year1": gpa_year1,
            "gpa_year2": gpa_year2,
            "gpa_year3": gpa_year3
        }
        query = "&".join(f"{k}={v}" for k, v in params.items())
        url = f"{API_URL}/ai/predict-graduation-gpa?{query}"
        headers = {"Authorization": f"Bearer {token}"}
        self.ai_network.response_received.connect(self._handle_gpa_prediction_response)
        self.ai_network.get(url, headers)

    def _show_gpa_error(self, label, message):
        label.setText(
            f'<html><head/><body><p><span style=" font-size:14pt;">{message}</span></p></body></html>'
        )
        label.show()

    def _handle_gpa_prediction_response(self, data: dict):
        self.ai_network.response_received.disconnect(self._handle_gpa_prediction_response)
        if data.get("status") != "success":
            return
        gpa = data.get("predicted_gpa", 0.0)
        gpa = max(0.0, min(4.0, gpa))
        self._update_gpa_prediction_card(gpa)

    def _update_gpa_prediction_card(self, gpa):
        self.ui.ExpectedGPAValueLabel.setText(
            '<html><head/><body><p align="center"><span style=" font-size:36pt;">'
            f'{gpa:.2f}'
            '</span></p></body></html>'
        )
        letter, name = self._gpa_to_letter_and_name(gpa)

        self.ui.ExpectedGPAScoreCodeValueLabel.setText(
            '<html><head/><body><p align="center"><span style=" font-size:36pt;">'
            f'{letter}'
            '</span></p></body></html>'
        )
        self.ui.ExpectedGPAScoreCodeValueLabel.setAlignment(Qt.AlignCenter)

        self.ui.ExpectedGPAScoreNameValueLabel.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:14pt;">{name}</span></p></body></html>'
        )
        self.ui.ExpectedGPAScoreNameValueLabel.setAlignment(Qt.AlignCenter)

        if gpa < 2:
            self.ui.ExpectedGPACard.setStyleSheet(self.GPABadSign)
        elif gpa <= 3:
            self.ui.ExpectedGPACard.setStyleSheet(self.GPAMediocreSign)
        else:
            self.ui.ExpectedGPACard.setStyleSheet(self.GPAGreatSign)

        self.ui.ExpectedGPACard.show()

    def _create_suggested_course_item(self, rank, course_id, permission, hours, remaining_students, pass_rate):
        outer_widget = QWidget()
        outer_layout = QHBoxLayout(outer_widget)
        outer_layout.setSpacing(5)
        outer_layout.setContentsMargins(0, 0, 0, 0)

        rank_widget = QWidget()
        rank_widget.setMinimumSize(50, 50)
        rank_widget.setMaximumSize(50, 50)
        rank_widget.setStyleSheet("""
            border-radius: 10px;
            background-color: qlineargradient(x1:0, x2:1, y1:0, y2:1, stop:0 rgb(27, 49, 96), stop:1 black);
            color: white;
        """)
        rank_layout = QVBoxLayout(rank_widget)
        rank_layout.setContentsMargins(0, 0, 0, 0)
        rank_layout.setSpacing(0)
        rank_label = QLabel(f'<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:700;">#{rank}</span></p></body></html>')
        rank_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        rank_layout.addWidget(rank_label)

        outer_layout.addWidget(rank_widget)

        course_widget = self._create_suggested_course_widget(course_id, permission, hours, remaining_students, pass_rate)
        outer_layout.addWidget(course_widget)

        spacer = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        outer_layout.addItem(spacer)

        return outer_widget

    def _create_suggested_course_widget(self, course_id, permission, hours, remaining_students, pass_rate):
        style_html = '<html><head/><body><p><span style=" font-size:14pt; font-weight:400;">{}</span></p></body></html>'
        bold_style_html = '<html><head/><body><p><span style=" font-size:14pt; font-weight:700;">{}</span></p></body></html>'
        
        widget = QWidget()
        widget.setMinimumSize(530, 105)
        widget.setMaximumSize(530, 105)
        widget.setStyleSheet("""
            border-radius: 10px;
            background-color: qlineargradient(x1:0, x2:1, y1:0, y2:1, stop:0 rgb(27, 49, 96), stop:1 black);
            color: white;
        """)
        h_layout = QHBoxLayout(widget)
        h_layout.setSpacing(5)
        h_layout.setContentsMargins(10, 10, 10, 10)

        summary_layout = QVBoxLayout()
        summary_layout.setSpacing(0)

        id_hours_layout = QHBoxLayout()
        id_hours_layout.setSpacing(5)
        id_label = QLabel(bold_style_html.format("ID:"))
        id_label.setStyleSheet("background-color: none; font-family: Calibri;")
        id_val = QLabel(style_html.format(course_id))
        id_val.setStyleSheet("background-color: none; font-family: Calibri;")
        id_hours_layout.addWidget(id_label)
        id_hours_layout.addWidget(id_val)
        id_hours_layout.addStretch()
        summary_layout.addLayout(id_hours_layout)

        perm_layout = QHBoxLayout()
        perm_layout.setSpacing(5)
        perm_label = QLabel(bold_style_html.format("Permission:"))
        perm_label.setStyleSheet("background-color: none; font-family: Calibri;")
        perm_val = QLabel(style_html.format(permission))
        perm_val.setStyleSheet("background-color: none; font-family: Calibri;")
        perm_layout.addWidget(perm_label)
        perm_layout.addWidget(perm_val)
        perm_layout.addStretch()
        summary_layout.addLayout(perm_layout)

        hours_layout = QHBoxLayout()
        hours_layout.setSpacing(5)
        hours_label = QLabel(bold_style_html.format("Hours:"))
        hours_label.setStyleSheet("background-color: none; font-family: Calibri;")
        hours_val = QLabel(style_html.format(str(hours)))
        hours_val.setStyleSheet("background-color: none; font-family: Calibri;")
        hours_layout.addWidget(hours_label)
        hours_layout.addWidget(hours_val)
        hours_layout.addStretch()
        summary_layout.addLayout(hours_layout)

        h_layout.addLayout(summary_layout)

        sep = QFrame()
        sep.setMinimumSize(1, 50)
        sep.setMaximumSize(1, 50)
        sep.setStyleSheet("background-color: white;")
        sep.setFrameShape(QFrame.Shape.VLine)
        sep.setFrameShadow(QFrame.Shadow.Sunken)
        h_layout.addWidget(sep)

        spacer = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        h_layout.addItem(spacer)

        details_layout = QVBoxLayout()
        details_layout.setSpacing(0)

        rem_stud_layout = QHBoxLayout()
        rem_stud_layout.setSpacing(5)
        rem_stud_label = QLabel(bold_style_html.format("Remaining Students:"))
        rem_stud_label.setStyleSheet("background-color: none; font-family: Calibri;")
        rem_stud_val = QLabel(style_html.format(str(remaining_students)))
        rem_stud_val.setStyleSheet("background-color: none; font-family: Calibri;")
        rem_stud_layout.addWidget(rem_stud_label)
        rem_stud_layout.addWidget(rem_stud_val)
        rem_stud_layout.addStretch()
        details_layout.addLayout(rem_stud_layout)

        pass_rate_layout = QHBoxLayout()
        pass_rate_layout.setSpacing(5)
        pass_rate_label = QLabel(bold_style_html.format("Pass Rate:"))
        pass_rate_label.setStyleSheet("background-color: none; font-family: Calibri;")
        pass_rate_val = QLabel(style_html.format(pass_rate))
        pass_rate_val.setStyleSheet("background-color: none; font-family: Calibri;")
        pass_rate_layout.addWidget(pass_rate_label)
        pass_rate_layout.addWidget(pass_rate_val)
        pass_rate_layout.addStretch()
        details_layout.addLayout(pass_rate_layout)

        details_layout.addItem(QSpacerItem(20, 35, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        h_layout.addLayout(details_layout)

        return widget

    def set_user_data(self, user_data: dict):
        LabelsStyling = '<html><head/><body><p><span style=" font-size:14pt;">{}</span></p></body></html>'
        CreditsLabelsStyling = '<html><head/><body><p align="center"><span style=" font-size:28pt;">{}</span></p></body></html>'
        RatesLabelsStyling = '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:700;">{}%</span></p></body></html>'
        GPAStyling = '<html><head/><body><p align="center"><span style=" font-size:36pt;">{}</span></p></body></html>'

        self.ui.FullNameValueLabel.setText(LabelsStyling.format(user_data.get("name", "")))
        self.ui.FullNameValueLabel.setStyleSheet("font-family: Calibri;")
        self.ui.IDValueLabel.setText(LabelsStyling.format(user_data.get("student_id", "")))
        self.ui.IDValueLabel.setStyleSheet("font-family: Calibri;")
        self.ui.LevelValueLabel.setText(LabelsStyling.format(user_data.get("level", "")))
        self.ui.LevelValueLabel.setStyleSheet("font-family: Calibri;")
        self.ui.EmailValueLabel.setText(LabelsStyling.format(user_data.get("email", "")))
        self.ui.EmailValueLabel.setStyleSheet("font-family: Calibri;")
        self.ui.DepartmentValueLabel.setText(LabelsStyling.format(user_data.get("department_name", "")))
        self.ui.DepartmentValueLabel.setStyleSheet("font-family: Calibri;")

        self.ui.CreditsAttemptedValueLabel.setText(CreditsLabelsStyling.format(user_data.get("Credit Attempted", 0)))
        self.ui.CreditsPassedValueLabel.setText(CreditsLabelsStyling.format(user_data.get("Credit Passed", 0)))
        self.ui.CreditsFailedValueLabel.setText(CreditsLabelsStyling.format(user_data.get("Credit Failed", 0)))
        self.ui.CreditsRemainingValueLabel.setText(CreditsLabelsStyling.format(user_data.get("Remaining hours", 0)))
        self.user_data = user_data

        if hasattr(self, 'passed_courses_data') and self.passed_courses_data:
            gpa = self._compute_gpa_from_passed(self.passed_courses_data)
            self.current_gpa = gpa
            letter, name = self._gpa_to_letter_and_name(gpa)
            self.ui.GPAValueLabel.setText(GPAStyling.format(f"{gpa:.2f}"))
            self.ui.GPAScoreCodeValueLabel.setText(f"({letter})")
            self.ui.GPAScoreNameValueLabel.setText(name)
            if gpa < 2:
                self.ui.GPACardWidget.setStyleSheet(self.GPABadSign)
            elif gpa <= 3:
                self.ui.GPACardWidget.setStyleSheet(self.GPAMediocreSign)
            else:
                self.ui.GPACardWidget.setStyleSheet(self.GPAGreatSign)

        SuccessRates = user_data.get("success rates", {})
        self.ui.MATHValueLabel.setText(RatesLabelsStyling.format(int(SuccessRates.get("math_rate", 0))))
        self.ui.STATValueLabel.setText(RatesLabelsStyling.format(int(SuccessRates.get("stat_rate", 0))))
        self.ui.COMPValueLabel.setText(RatesLabelsStyling.format(int(SuccessRates.get("cs_rate", 0))))
        self.ui.CHEMValueLabel.setText(RatesLabelsStyling.format(int(SuccessRates.get("chem_rate", 0))))
        self.ui.PHYSValueLabel.setText(RatesLabelsStyling.format(int(SuccessRates.get("phys_rate", 0))))
        self.ui.OthersValueLabel.setText(RatesLabelsStyling.format(int(SuccessRates.get("others_rate", 0))))

        BadSign = """
            QProgressBar { border-radius: 5px; background-color: #F8C9CE; }
            QProgressBar::chunk { background-color: qlineargradient(x1:0, x2:1, y1:0, y2:1, stop:0 rgb(128, 15, 28), stop:1 black); border-radius: 5px; margin: 0px; }
            QLabel{ border-radius: 5px; background-color: qlineargradient(x1:0, x2:1, y1:0, y2:1, stop:0 rgb(128, 15, 28), stop:1 black); color: "white"; }
        """
        GPABadSign = """
            QWidget{
                border-radius: 10px;
                background-color: qlineargradient(x1:0, x2:1, y1:0, y2:1, stop:0 rgb(128, 15, 28), stop:1 black);
                color: "white";
            }
            QLabel{ background-color: none; }
        """
        MediocreSign = """
            QProgressBar { border-radius: 5px; background-color: #CFDBF2; }
            QProgressBar::chunk { background-color: qlineargradient(x1:0, x2:1, y1:0, y2:1, stop:0 rgb(27, 49, 96), stop:1 black); border-radius: 5px; margin: 0px; }
            QLabel{ border-radius: 5px; background-color: qlineargradient(x1:0, x2:1, y1:0, y2:1, stop:0 rgb(27, 49, 96), stop:1 black); color: "white"; }
        """
        GPAMediocreSign = """
            QWidget{
                border-radius: 10px;
                background-color: qlineargradient(x1:0, x2:1, y1:0, y2:1, stop:0 rgb(27, 49, 96), stop:1 black);
                color: "white";
            }
            QLabel{ background-color: none; }
        """
        GreatSign = """
            QProgressBar { border-radius: 5px; background-color: #BCDCC3; }
            QProgressBar::chunk { background-color: qlineargradient(x1:0, x2:1, y1:0, y2:1, stop:0 rgb(7, 74, 45), stop:1 black); border-radius: 5px; margin: 0px; }
            QLabel{ border-radius: 5px; background-color: qlineargradient(x1:0, x2:1, y1:0, y2:1, stop:0 rgb(7, 74, 45), stop:1 black); color: "white"; }
        """
        GPAGreatSign = """
            QWidget{
                border-radius: 10px;
                background-color: qlineargradient(x1:0, x2:1, y1:0, y2:1, stop:0 rgb(7, 74, 45), stop:1 "black");
                color: "white";
            }
            QLabel{ background-color: none; }
        """

        for value_label, (progress_bar, category_label, val_label) in self.progress_bars.items():
            number = self._extract_number(value_label.text())
            progress_bar.setValue(number)
            if number < 50:
                progress_bar.setStyleSheet(BadSign)
                category_label.setStyleSheet(BadSign)
                val_label.setStyleSheet(BadSign)
            elif number < 75:
                progress_bar.setStyleSheet(MediocreSign)
                category_label.setStyleSheet(MediocreSign)
                val_label.setStyleSheet(MediocreSign)
            else:
                progress_bar.setStyleSheet(GreatSign)
                category_label.setStyleSheet(GreatSign)
                val_label.setStyleSheet(GreatSign)

        self.CourseStyling = '<html><head/><body><p><span style=" font-size:14pt;">{}</span></p></body></html>'
        CurrentCourses = user_data.get("courses", [])

        self.current_course_cards = []
        for i in range(5):
            card_widget = getattr(self.ui, f"CurrentCourse_{i+1}", None)
            if card_widget:
                self.current_course_cards.append(card_widget)

        CourseWidgets = []
        for i in range(5):
            CourseWidget = {
                "ID": getattr(self.ui, f"CurrentCourseIDValueLabel_{i+1}"),
                "Hours": getattr(self.ui, f"CurrentCourseHoursValueLabel_{i+1}"),
                "Type": getattr(self.ui, f"CurrentCoursePermissionValueLabel_{i+1}"),
                "Doctor": getattr(self.ui, f"CurrentCourseDoctorValueLabel_{i+1}"),
            }
            CourseWidgets.append(CourseWidget)

        for i, CourseWidget in enumerate(CourseWidgets):
            if i < len(CurrentCourses):
                CurrentCourse = CurrentCourses[i]
                CourseName = CurrentCourse.get("course_name", "")
                CourseCode = CurrentCourse.get("course_code", "")
                display_id = f"{CourseName} {CourseCode}".strip()
                CourseWidget["ID"].setText(self.CourseStyling.format(display_id))
                CourseWidget["ID"].setStyleSheet("background-color: none; font-family: Calibri;")
                CourseWidget["Hours"].setText(self.CourseStyling.format(CurrentCourse.get("course_hours", "")))
                CourseWidget["Hours"].setStyleSheet("background-color: none; font-family: Calibri;")
                CourseWidget["Type"].setText(self.CourseStyling.format(CurrentCourse.get("permission", "")))
                CourseWidget["Type"].setStyleSheet("background-color: none; font-family: Calibri;")
                CourseWidget["Doctor"].setText(self.CourseStyling.format(CurrentCourse.get("course_instructor", "")))
                CourseWidget["Doctor"].setStyleSheet("background-color: none; font-family: Calibri;")
                if i < len(self.current_course_cards):
                    card = self.current_course_cards[i]
                    card.show()
                    card.course_code = CourseCode
                    card.course_display = display_id
            else:
                if i < len(self.current_course_cards):
                    self.current_course_cards[i].hide()

        self.current_courses_data = CurrentCourses

        if hasattr(self, 'passed_course_cards') and hasattr(self, 'failed_course_cards'):
            self._rebuild_all_course_cards()

    def _on_login_success(self, user_data: dict):
            self.user_data = user_data
            self.passed_courses_data = []
            self.current_gpa = 0.0
            self.ui.GPAValueLabel.setText(self.GPAStyling.format("—"))
            self.ui.GPAScoreCodeValueLabel.setText("")
            self.ui.GPAScoreNameValueLabel.setText("")
            self.ui.GPACardWidget.setStyleSheet(self.GPAMediocreSign)

    @staticmethod
    def _extract_number(text):
        match = re.search(r'(\d+)%', text)
        return int(match.group(1)) if match else 0

    def _compute_gpa_from_passed(self, passed_courses):
        numerator = 0.0
        for c in passed_courses or []:
            hours = c.get("credit_hours", c.get("course_hours", 0)) or 0
            try:
                hours = float(hours)
            except Exception:
                hours = 0.0
            grade = c.get("grade", "")
            grade = grade.strip().upper() if isinstance(grade, str) else ""
            points = self._GRADE_POINTS.get(grade, 0.0)
            numerator += points * hours

        total_attempted = 0.0
        if hasattr(self, 'user_data'):
            try:
                total_attempted = float(self.user_data.get("Credit Attempted", 0) or 0)
            except Exception:
                total_attempted = 0.0

        if not total_attempted:
            total_attempted = 0.0
            for lst in (getattr(self, 'passed_courses_data', []) or [],
                        getattr(self, 'failed_courses_data', []) or [],
                        getattr(self, 'current_courses_data', []) or []):
                for item in lst:
                    h = item.get("credit_hours", item.get("course_hours", 0)) or 0
                    try:
                        total_attempted += float(h)
                    except Exception:
                        pass

        if total_attempted <= 0:
            return 0.0
        return numerator / total_attempted

    def _gpa_to_letter_and_name(self, gpa):
        if gpa < 2.0:
            return 'F', self._GRADE_NAMES.get('F', 'FAILED')
        candidates = [(letter, abs(gpa - pts)) for letter, pts in self._GRADE_POINTS.items() if letter != 'F']
        best = min(candidates, key=lambda x: (x[1], -self._GRADE_POINTS[x[0]]))
        letter = best[0]
        name = self._GRADE_NAMES.get(letter, '')
        return letter, name

    def _check_streamlit_alive(self):
        if self.streamlit.process and self.streamlit.process.poll() is not None:
            pass

    def _setup_analysis_page(self):
        self.analysis_web_view = QWebEngineView()
        self.analysis_web_view.page().printRequested.connect(self._on_print_requested)
        self.ui.AnalysisPageWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.ui.AnalysisPageWidget_Layout.setSpacing(0)
        self.ui.AnalysisPageWidget_Layout.addWidget(self.analysis_web_view)

    def _on_print_requested(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save Report", f"report_{self.student_id}.pdf", "PDF (*.pdf)")
        if path:
            self.analysis_web_view.page().printToPdf(path)

    def _on_logout_clicked(self):
        self.reset_ui()
        self.logout_requested.emit()

    def _populate_courses(self, data: dict):
        passed = data.get("passed", [])
        failed = data.get("failed", [])
        remaining = data.get("remaining", [])

        CreditsLabelsStyling = '<html><head/><body><p align="center"><span style=" font-size:28pt;">{}</span></p></body></html>'

        self.ui.PassedCoursesValueLabel.setText(CreditsLabelsStyling.format(len(passed)))
        self._clear_layout(self.passed_courses_layout)
        self.passed_course_cards = []
        for course in passed:
            card = self._create_passed_course_card(course, self.CourseStyling)
            course_code = course.get("course_code", "")
            course_name = course.get("course_name", "")
            display_id = f"{course_name} {course_code}".strip() if course_name or course_code else course_code
            card.course_code = course_code
            card.course_display = display_id
            self.passed_course_cards.append(card)
            self.passed_courses_layout.insertWidget(self.passed_courses_layout.count() - 1, card)

        self.ui.FailedCoursesValueLabel.setText(CreditsLabelsStyling.format(len(failed)))
        self._clear_layout(self.failed_courses_layout)
        self.failed_course_cards = []
        for course in failed:
            card = self._create_failed_course_card(course, self.CourseStyling)
            course_code = course.get("course_code", "")
            course_name = course.get("course_name", "")
            display_id = f"{course_name} {course_code}".strip() if course_name or course_code else course_code
            card.course_code = course_code
            card.course_display = display_id
            self.failed_course_cards.append(card)
            self.failed_courses_layout.insertWidget(self.failed_courses_layout.count() - 1, card)

        self.ui.RemainingCoursesValueLabel.setText(CreditsLabelsStyling.format(len(remaining)))
        self._clear_remaining_layout()
        self.remaining_course_cards = []
        for course in remaining:
            card = self._create_remaining_course_card(course, self.CourseStyling)
            course_code = course.get("course_code", "")
            course_name = course.get("course_name", "")
            display_id = f"{course_name} {course_code}".strip() if course_name or course_code else course_code
            card.course_code = course_code
            card.course_display = display_id
            self.remaining_course_cards.append(card)
            self.remaining_courses_layout.insertWidget(self.remaining_courses_layout.count() - 1, card)

        current_courses = data.get("current_courses", []) or data.get("courses", [])
        CourseStyling = getattr(self, 'CourseStyling', '<html><head/><body><p><span style=" font-size:14pt;">{}</span></p></body></html>')
        self.current_course_cards = []
        for i in range(5):
            card_widget = getattr(self.ui, f"CurrentCourse_{i+1}", None)
            if card_widget:
                self.current_course_cards.append(card_widget)

        CourseWidgets = []
        for i in range(5):
            CourseWidget = {
                "ID": getattr(self.ui, f"CurrentCourseIDValueLabel_{i+1}"),
                "Hours": getattr(self.ui, f"CurrentCourseHoursValueLabel_{i+1}"),
                "Type": getattr(self.ui, f"CurrentCoursePermissionValueLabel_{i+1}"),
                "Doctor": getattr(self.ui, f"CurrentCourseDoctorValueLabel_{i+1}"),
            }
            CourseWidgets.append(CourseWidget)

        for i, CourseWidget in enumerate(CourseWidgets):
            if i < len(current_courses):
                CurrentCourse = current_courses[i]
                CourseName = CurrentCourse.get("course_name", "")
                CourseCode = CurrentCourse.get("course_code", "")
                display_id = f"{CourseName} {CourseCode}".strip()
                CourseWidget["ID"].setText(CourseStyling.format(display_id))
                CourseWidget["ID"].setStyleSheet("background-color: none; font-family: Calibri;")
                CourseWidget["Hours"].setText(CourseStyling.format(CurrentCourse.get("course_hours", "")))
                CourseWidget["Hours"].setStyleSheet("background-color: none; font-family: Calibri;")
                CourseWidget["Type"].setText(CourseStyling.format(CurrentCourse.get("permission", "")))
                CourseWidget["Type"].setStyleSheet("background-color: none; font-family: Calibri;")
                CourseWidget["Doctor"].setText(CourseStyling.format(CurrentCourse.get("course_instructor", "")))
                CourseWidget["Doctor"].setStyleSheet("background-color: none; font-family: Calibri;")
                if i < len(self.current_course_cards):
                    card = self.current_course_cards[i]
                    card.show()
                    card.course_code = CourseCode
                    card.course_display = display_id
            else:
                if i < len(self.current_course_cards):
                    self.current_course_cards[i].hide()

        self.current_courses_data = current_courses
        self.passed_courses_data = passed
        self.failed_courses_data = failed
        self.remaining_courses_data = remaining

        try:
            gpa = self._compute_gpa_from_passed(self.passed_courses_data)
            self.current_gpa = gpa
            letter, name = self._gpa_to_letter_and_name(gpa)
            self.ui.GPAValueLabel.setText(self.GPAStyling.format(f"{gpa:.2f}"))
            self.ui.GPAScoreCodeValueLabel.setText(f"({letter})")
            self.ui.GPAScoreNameValueLabel.setText(name)
            if gpa < 2:
                self.ui.GPACardWidget.setStyleSheet(self.GPABadSign)
            elif gpa <= 3:
                self.ui.GPACardWidget.setStyleSheet(self.GPAMediocreSign)
            else:
                self.ui.GPACardWidget.setStyleSheet(self.GPAGreatSign)
        except Exception:
            self.current_gpa = 0.0
            self.ui.GPAValueLabel.setText(self.GPAStyling.format("0.00"))
            self.ui.GPAScoreCodeValueLabel.setText("(F)")
            self.ui.GPAScoreNameValueLabel.setText("FAILED")
            self.ui.GPACardWidget.setStyleSheet(self.GPABadSign)

        self._rebuild_all_course_cards()
        self._adjust_scroll_heights(len(passed), len(failed), len(remaining))

    def _adjust_scroll_heights(self, passed_count, failed_count, remaining_count):
        if passed_count > 0:
            passed_actual_height = passed_count * 170 + (passed_count - 1) * 5
            if passed_count % 2 == 1:
                passed_container_height = (passed_count + 1) * 170 + (passed_count - 1) * 5
            else:
                passed_container_height = passed_count * 170 + (passed_count - 1) * 5
        else:
            passed_actual_height = passed_container_height = 0
        self.ui.PassedCoursesActualScrollAreaWidget.setMinimumHeight(passed_actual_height)
        self.ui.PassedCoursesActualScrollAreaWidget.setMaximumHeight(passed_actual_height)
        self.ui.PassedCoursesScrollAreaWidget.setMinimumHeight(passed_container_height)
        self.ui.PassedCoursesScrollAreaWidget.setMaximumHeight(passed_container_height)
        self.ui.PassedCoursesActualScrollAreaWidget.setGeometry(0, 0, 250, passed_actual_height)
        self.ui.PassedCoursesScrollAreaWidget.setGeometry(0, 0, 250, passed_container_height)

        if failed_count > 0:
            failed_actual_height = failed_count * 195 + (failed_count - 1) * 5
            if failed_count % 2 == 1:
                failed_container_height = (failed_count + 1) * 195 + (failed_count - 1) * 5
            else:
                failed_container_height = failed_count * 195 + (failed_count - 1) * 5
        else:
            failed_actual_height = failed_container_height = 0
        self.ui.FailedCoursesActualScrollAreaWidget.setMinimumHeight(failed_actual_height)
        self.ui.FailedCoursesActualScrollAreaWidget.setMaximumHeight(failed_actual_height)
        self.ui.FailedCoursesScrollAreaWidget.setMinimumHeight(failed_container_height)
        self.ui.FailedCoursesScrollAreaWidget.setMaximumHeight(failed_container_height)
        self.ui.FailedCoursesActualScrollAreaWidget.setGeometry(0, 0, 255, failed_actual_height)
        self.ui.FailedCoursesScrollAreaWidget.setGeometry(0, 0, 255, failed_container_height)

        rem_card_height = 140
        spacing = 5
        if remaining_count > 0:
            rem_actual_height = remaining_count * rem_card_height + (remaining_count - 1) * spacing
            if remaining_count % 2 == 1:
                rem_container_height = (remaining_count + 1) * rem_card_height + (remaining_count - 1) * spacing
            else:
                rem_container_height = remaining_count * rem_card_height + (remaining_count - 1) * spacing
        else:
            rem_actual_height = rem_container_height = 0
        self.ui.RemainingCoursesActualScrollAreaWidget.setMinimumHeight(rem_actual_height)
        self.ui.RemainingCoursesActualScrollAreaWidget.setMaximumHeight(rem_actual_height)
        self.ui.RemainingCoursesScrollAreaWidget.setMinimumHeight(rem_container_height)
        self.ui.RemainingCoursesScrollAreaWidget.setMaximumHeight(rem_container_height)
        self.ui.RemainingCoursesActualScrollAreaWidget.setGeometry(0, 0, 250, rem_actual_height)
        self.ui.RemainingCoursesScrollAreaWidget.setGeometry(0, 0, 250, rem_container_height)

    def _create_passed_course_card(self, course: dict, LabelsStyling: str):
        PassedCourse = QWidget()
        PassedCourse.setMinimumSize(250, 170)
        PassedCourse.setMaximumSize(250, 170)
        PassedCourse.setStyleSheet("""
            border-radius: 10px;
            background-color: qlineargradient(x1:0, x2:1, y1:0, y2:1, stop:0 rgb(7, 74, 45), stop:1 black);
            color: white;
        """)
        PassedCourse_Layout = QVBoxLayout(PassedCourse)
        PassedCourse_Layout.setSpacing(0)
        PassedCourse_Layout.setContentsMargins(10, 5, 10, 10)

        PassedCourseID_Hours_Layout = QHBoxLayout()
        PassedCourseID_Hours_Layout.setSpacing(5)
        PassedCourseID_Hours_Layout.setContentsMargins(0, 0, 0, 0)
        PassedCourseIDLabel = QLabel(LabelsStyling.format("ID:"))
        PassedCourseIDLabel.setStyleSheet("background-color: none; font-weight: bold; font-family: Calibri;")
        course_name = course.get("course_name", "")
        course_code = course.get("course_code", "")
        id_text = f"{course_name} {course_code}".strip() if course_name or course_code else course_code
        PassedCourseIDValueLabel = QLabel(LabelsStyling.format(id_text))
        PassedCourseIDValueLabel.setStyleSheet("background-color: none; font-family: Calibri;")
        PassedCourseHoursLabel = QLabel(LabelsStyling.format("Hours:"))
        PassedCourseHoursLabel.setStyleSheet("background-color: none; font-weight: bold; font-family: Calibri;")
        PassedCourseHoursValueLabel = QLabel(LabelsStyling.format(str(course.get("credit_hours", ""))))
        PassedCourseHoursValueLabel.setStyleSheet("background-color: none; font-family: Calibri;")
        PassedCourseID_Hours_Layout.addWidget(PassedCourseIDLabel)
        PassedCourseID_Hours_Layout.addWidget(PassedCourseIDValueLabel)
        PassedCourseID_Hours_Layout.addStretch()
        PassedCourseID_Hours_Layout.addWidget(PassedCourseHoursLabel)
        PassedCourseID_Hours_Layout.addWidget(PassedCourseHoursValueLabel)
        PassedCourse_Layout.addLayout(PassedCourseID_Hours_Layout)

        PassedCoursePermission_Layout = QHBoxLayout()
        PassedCoursePermission_Layout.setSpacing(5)
        PassedCoursePermission_Layout.setContentsMargins(0, 0, 0, 0)
        PassedCoursePermissionLabel = QLabel(LabelsStyling.format("Permission:"))
        PassedCoursePermissionLabel.setStyleSheet("background-color: none; font-weight: bold; font-family: Calibri;")
        PassedCoursePermissionValueLabel = QLabel(LabelsStyling.format(course.get("permission", "N/A")))
        PassedCoursePermissionValueLabel.setStyleSheet("background-color: none; font-family: Calibri;")
        PassedCoursePermission_Layout.addWidget(PassedCoursePermissionLabel)
        PassedCoursePermission_Layout.addWidget(PassedCoursePermissionValueLabel)
        PassedCoursePermission_Layout.addStretch()
        PassedCourse_Layout.addLayout(PassedCoursePermission_Layout)

        PassedCourseDoctor_Layout = QHBoxLayout()
        PassedCourseDoctor_Layout.setSpacing(5)
        PassedCourseDoctor_Layout.setContentsMargins(0, 0, 0, 0)
        PassedCourseDoctorLabel = QLabel(LabelsStyling.format("Doctor:"))
        PassedCourseDoctorLabel.setStyleSheet("background-color: none; font-weight: bold; font-family: Calibri;")
        PassedCourseDoctorValueLabel = QLabel(LabelsStyling.format(course.get("instructor", "N/A")))
        PassedCourseDoctorValueLabel.setStyleSheet("background-color: none; font-family: Calibri;")
        PassedCourseDoctor_Layout.addWidget(PassedCourseDoctorLabel)
        PassedCourseDoctor_Layout.addWidget(PassedCourseDoctorValueLabel)
        PassedCourseDoctor_Layout.addStretch()
        PassedCourse_Layout.addLayout(PassedCourseDoctor_Layout)

        PassedCourseLine_Layout = QHBoxLayout()
        PassedCourseLine_Layout.setContentsMargins(0, 13, 0, 13)
        PassedCourseLine_Layout.addStretch()
        PassedCourseLine = QFrame()
        PassedCourseLine.setMinimumSize(100, 1)
        PassedCourseLine.setMaximumSize(100, 1)
        PassedCourseLine.setStyleSheet("background-color: rgb(239, 233, 231);")
        PassedCourseLine.setFrameShape(QFrame.Shape.HLine)
        PassedCourseLine_Layout.addWidget(PassedCourseLine)
        PassedCourseLine_Layout.addStretch()
        PassedCourse_Layout.addLayout(PassedCourseLine_Layout)

        PassedCourseDegree_Grade_Layout = QHBoxLayout()
        PassedCourseDegree_Grade_Layout.setSpacing(5)
        PassedCourseDegree_Grade_Layout.setContentsMargins(0, 0, 0, 0)
        PassedCourseDegreeLabel = QLabel(LabelsStyling.format("Degree:"))
        PassedCourseDegreeLabel.setStyleSheet("background-color: none; font-weight: bold; font-family: Calibri;")
        PassedCourseDegreeValueLabel = QLabel(LabelsStyling.format(str(course.get("student_grade", ""))))
        PassedCourseDegreeValueLabel.setStyleSheet("background-color: none; font-family: Calibri;")
        PassedCourseGradeLabel = QLabel(LabelsStyling.format("Grade:"))
        PassedCourseGradeLabel.setStyleSheet("background-color: none; font-weight: bold; font-family: Calibri;")
        PassedCourseGradeValueLabel = QLabel(LabelsStyling.format(course.get("grade", "")))
        PassedCourseGradeValueLabel.setStyleSheet("background-color: none; font-family: Calibri;")
        PassedCourseDegree_Grade_Layout.addWidget(PassedCourseDegreeLabel)
        PassedCourseDegree_Grade_Layout.addWidget(PassedCourseDegreeValueLabel)
        PassedCourseDegree_Grade_Layout.addStretch()
        PassedCourseDegree_Grade_Layout.addWidget(PassedCourseGradeLabel)
        PassedCourseDegree_Grade_Layout.addWidget(PassedCourseGradeValueLabel)
        PassedCourse_Layout.addLayout(PassedCourseDegree_Grade_Layout)

        PassedCourseAttendance_Layout = QHBoxLayout()
        PassedCourseAttendance_Layout.setSpacing(5)
        PassedCourseAttendance_Layout.setContentsMargins(0, 0, 0, 0)
        PassedCourseAttendanceLabel = QLabel(LabelsStyling.format("Attendance:"))
        PassedCourseAttendanceLabel.setStyleSheet("background-color: none; font-weight: bold; font-family: Calibri;")
        PassedCourseAttendanceValueLabel = QLabel(LabelsStyling.format(str(course.get("attendance", ""))))
        PassedCourseAttendanceValueLabel.setStyleSheet("background-color: none; font-family: Calibri;")
        PassedCourseAttendance_Layout.addWidget(PassedCourseAttendanceLabel)
        PassedCourseAttendance_Layout.addWidget(PassedCourseAttendanceValueLabel)
        PassedCourseAttendance_Layout.addStretch()
        PassedCourse_Layout.addLayout(PassedCourseAttendance_Layout)

        return PassedCourse

    def _create_failed_course_card(self, course: dict, LabelsStyling: str):
        FailedCourse = QWidget()
        FailedCourse.setMinimumSize(255, 195)
        FailedCourse.setMaximumSize(255, 195)
        FailedCourse.setStyleSheet("""
            border-radius: 10px;
            background-color: qlineargradient(x1:0, x2:1, y1:0, y2:1, stop:0 rgb(128, 15, 28), stop:1 black);
            color: white;
        """)
        FailedCourse_Layout = QVBoxLayout(FailedCourse)
        FailedCourse_Layout.setSpacing(0)
        FailedCourse_Layout.setContentsMargins(10, 5, 10, 10)

        FailedCourseID_Hours_Layout = QHBoxLayout()
        FailedCourseID_Hours_Layout.setSpacing(5)
        FailedCourseID_Hours_Layout.setContentsMargins(0, 0, 0, 0)
        FailedCourseIDLabel = QLabel(LabelsStyling.format("ID:"))
        FailedCourseIDLabel.setStyleSheet("background-color: none; font-weight: bold; font-family: Calibri;")
        course_name = course.get("course_name", "")
        course_code = course.get("course_code", "")
        id_text = f"{course_name} {course_code}".strip() if course_name or course_code else course_code
        FailedCourseIDValueLabel = QLabel(LabelsStyling.format(id_text))
        FailedCourseIDValueLabel.setStyleSheet("background-color: none; font-family: Calibri;")
        FailedCourseHoursLabel = QLabel(LabelsStyling.format("Hours:"))
        FailedCourseHoursLabel.setStyleSheet("background-color: none; font-weight: bold; font-family: Calibri;")
        FailedCourseHoursValueLabel = QLabel(LabelsStyling.format(str(course.get("credit_hours", ""))))
        FailedCourseHoursValueLabel.setStyleSheet("background-color: none; font-family: Calibri;")
        FailedCourseID_Hours_Layout.addWidget(FailedCourseIDLabel)
        FailedCourseID_Hours_Layout.addWidget(FailedCourseIDValueLabel)
        FailedCourseID_Hours_Layout.addStretch()
        FailedCourseID_Hours_Layout.addWidget(FailedCourseHoursLabel)
        FailedCourseID_Hours_Layout.addWidget(FailedCourseHoursValueLabel)
        FailedCourse_Layout.addLayout(FailedCourseID_Hours_Layout)

        FailedCoursePermission_Layout = QHBoxLayout()
        FailedCoursePermission_Layout.setSpacing(5)
        FailedCoursePermission_Layout.setContentsMargins(0, 0, 0, 0)
        FailedCoursePermissionLabel = QLabel(LabelsStyling.format("Permission:"))
        FailedCoursePermissionLabel.setStyleSheet("background-color: none; font-weight: bold; font-family: Calibri;")
        FailedCoursePermissionValueLabel = QLabel(LabelsStyling.format(course.get("permission", "N/A")))
        FailedCoursePermissionValueLabel.setStyleSheet("background-color: none; font-family: Calibri;")
        FailedCoursePermission_Layout.addWidget(FailedCoursePermissionLabel)
        FailedCoursePermission_Layout.addWidget(FailedCoursePermissionValueLabel)
        FailedCoursePermission_Layout.addStretch()
        FailedCourse_Layout.addLayout(FailedCoursePermission_Layout)

        FailedCourseDoctor_Layout = QHBoxLayout()
        FailedCourseDoctor_Layout.setSpacing(5)
        FailedCourseDoctor_Layout.setContentsMargins(0, 0, 0, 0)
        FailedCourseDoctorLabel = QLabel(LabelsStyling.format("Doctor:"))
        FailedCourseDoctorLabel.setStyleSheet("background-color: none; font-weight: bold; font-family: Calibri;")
        FailedCourseDoctorValueLabel = QLabel(LabelsStyling.format(course.get("instructor", "N/A")))
        FailedCourseDoctorValueLabel.setStyleSheet("background-color: none; font-family: Calibri;")
        FailedCourseDoctor_Layout.addWidget(FailedCourseDoctorLabel)
        FailedCourseDoctor_Layout.addWidget(FailedCourseDoctorValueLabel)
        FailedCourseDoctor_Layout.addStretch()
        FailedCourse_Layout.addLayout(FailedCourseDoctor_Layout)

        FailedCourseLine_Layout = QHBoxLayout()
        FailedCourseLine_Layout.setContentsMargins(0, 13, 0, 13)
        FailedCourseLine_Layout.addStretch()
        FailedCourseLine = QFrame()
        FailedCourseLine.setMinimumSize(100, 1)
        FailedCourseLine.setMaximumSize(100, 1)
        FailedCourseLine.setStyleSheet("background-color: rgb(239, 233, 231);")
        FailedCourseLine.setFrameShape(QFrame.Shape.HLine)
        FailedCourseLine_Layout.addWidget(FailedCourseLine)
        FailedCourseLine_Layout.addStretch()
        FailedCourse_Layout.addLayout(FailedCourseLine_Layout)

        FailedCourseDegree_Attendance_Layout = QHBoxLayout()
        FailedCourseDegree_Attendance_Layout.setSpacing(5)
        FailedCourseDegree_Attendance_Layout.setContentsMargins(0, 0, 0, 0)
        FailedCourseDegreeLabel = QLabel(LabelsStyling.format("Degree:"))
        FailedCourseDegreeLabel.setStyleSheet("background-color: none; font-weight: bold; font-family: Calibri;")
        FailedCourseDegreeValueLabel = QLabel(LabelsStyling.format(str(course.get("student_grade", ""))))
        FailedCourseDegreeValueLabel.setStyleSheet("background-color: none; font-family: Calibri;")
        FailedCourseAttendanceLabel = QLabel(LabelsStyling.format("Attendance:"))
        FailedCourseAttendanceLabel.setStyleSheet("background-color: none; font-weight: bold; font-family: Calibri;")
        FailedCourseAttendanceValueLabel = QLabel(LabelsStyling.format(str(course.get("attendance", ""))))
        FailedCourseAttendanceValueLabel.setStyleSheet("background-color: none; font-family: Calibri;")
        FailedCourseDegree_Attendance_Layout.addWidget(FailedCourseDegreeLabel)
        FailedCourseDegree_Attendance_Layout.addWidget(FailedCourseDegreeValueLabel)
        FailedCourseDegree_Attendance_Layout.addStretch()
        FailedCourseDegree_Attendance_Layout.addWidget(FailedCourseAttendanceLabel)
        FailedCourseDegree_Attendance_Layout.addWidget(FailedCourseAttendanceValueLabel)
        FailedCourse_Layout.addLayout(FailedCourseDegree_Attendance_Layout)

        FailedCourseRemainingStudents_Layout = QHBoxLayout()
        FailedCourseRemainingStudents_Layout.setSpacing(5)
        FailedCourseRemainingStudents_Layout.setContentsMargins(0, 0, 0, 0)
        FailedCourseRemainingStudentsLabel = QLabel(LabelsStyling.format("Remaining Students:"))
        FailedCourseRemainingStudentsLabel.setStyleSheet("background-color: none; font-weight: bold; font-family: Calibri;")
        FailedCourseRemainingStudentsValueLabel = QLabel(LabelsStyling.format(str(course.get("Number_of_students_who_failed", "N/A"))))
        FailedCourseRemainingStudentsValueLabel.setStyleSheet("background-color: none; font-family: Calibri;")
        FailedCourseRemainingStudents_Layout.addWidget(FailedCourseRemainingStudentsLabel)
        FailedCourseRemainingStudents_Layout.addWidget(FailedCourseRemainingStudentsValueLabel)
        FailedCourseRemainingStudents_Layout.addStretch()
        FailedCourse_Layout.addLayout(FailedCourseRemainingStudents_Layout)

        FailedCoursePassRate_Layout = QHBoxLayout()
        FailedCoursePassRate_Layout.setSpacing(5)
        FailedCoursePassRate_Layout.setContentsMargins(0, 0, 0, 0)
        FailedCoursePassRateLabel = QLabel(LabelsStyling.format("Pass Rate (at Time):"))
        FailedCoursePassRateLabel.setStyleSheet("background-color: none; font-weight: bold; font-family: Calibri;")
        FailedCoursePassRateValueLabel = QLabel(LabelsStyling.format(str(course.get("success_rate_this_semester", "N/A"))))
        FailedCoursePassRateValueLabel.setStyleSheet("background-color: none; font-family: Calibri;")
        FailedCoursePassRate_Layout.addWidget(FailedCoursePassRateLabel)
        FailedCoursePassRate_Layout.addWidget(FailedCoursePassRateValueLabel)
        FailedCoursePassRate_Layout.addStretch()
        FailedCourse_Layout.addLayout(FailedCoursePassRate_Layout)

        return FailedCourse

    def _create_remaining_course_card(self, course: dict, LabelsStyling: str):
        RemainingCourse = QWidget()
        RemainingCourse.setMinimumSize(250, 140)
        RemainingCourse.setMaximumSize(250, 140)
        RemainingCourse.setStyleSheet("""
            border-radius: 10px;
            background-color: qlineargradient(x1:0, x2:1, y1:0, y2:1, stop:0 rgb(27, 49, 96), stop:1 black);
            color: white;
        """)
        RemainingCourse_Layout = QVBoxLayout(RemainingCourse)
        RemainingCourse_Layout.setSpacing(0)
        RemainingCourse_Layout.setContentsMargins(10, 5, 10, 10)

        RemainingCourseID_Hours_Layout = QHBoxLayout()
        RemainingCourseID_Hours_Layout.setSpacing(5)
        RemainingCourseIDLabel = QLabel(LabelsStyling.format("ID:"))
        RemainingCourseIDLabel.setStyleSheet("background-color: none; font-weight: bold; font-family: Calibri;")
        course_name = course.get("course_name", "")
        course_code = course.get("course_code", "")
        id_text = f"{course_name} {course_code}".strip() if course_name or course_code else course_code
        RemainingCourseIDValueLabel = QLabel(LabelsStyling.format(id_text))
        RemainingCourseIDValueLabel.setStyleSheet("background-color: none; font-family: Calibri;")
        RemainingCourseHoursLabel = QLabel(LabelsStyling.format("Hours:"))
        RemainingCourseHoursLabel.setStyleSheet("background-color: none; font-weight: bold; font-family: Calibri;")
        RemainingCourseHoursValueLabel = QLabel(LabelsStyling.format(str(course.get("credit_hours", ""))))
        RemainingCourseHoursValueLabel.setStyleSheet("background-color: none; font-family: Calibri;")
        RemainingCourseID_Hours_Layout.addWidget(RemainingCourseIDLabel)
        RemainingCourseID_Hours_Layout.addWidget(RemainingCourseIDValueLabel)
        RemainingCourseID_Hours_Layout.addStretch()
        RemainingCourseID_Hours_Layout.addWidget(RemainingCourseHoursLabel)
        RemainingCourseID_Hours_Layout.addWidget(RemainingCourseHoursValueLabel)
        RemainingCourse_Layout.addLayout(RemainingCourseID_Hours_Layout)

        RemainingCoursePermission_Layout = QHBoxLayout()
        RemainingCoursePermission_Layout.setSpacing(5)
        RemainingCoursePermissionLabel = QLabel(LabelsStyling.format("Permission:"))
        RemainingCoursePermissionLabel.setStyleSheet("background-color: none; font-weight: bold; font-family: Calibri;")
        RemainingCoursePermissionValueLabel = QLabel(LabelsStyling.format(course.get("permission", "N/A")))
        RemainingCoursePermissionValueLabel.setStyleSheet("background-color: none; font-family: Calibri;")
        RemainingCoursePermission_Layout.addWidget(RemainingCoursePermissionLabel)
        RemainingCoursePermission_Layout.addWidget(RemainingCoursePermissionValueLabel)
        RemainingCoursePermission_Layout.addStretch()
        RemainingCourse_Layout.addLayout(RemainingCoursePermission_Layout)

        RemainingCourseLine_Layout = QHBoxLayout()
        RemainingCourseLine_Layout.setContentsMargins(0, 13, 0, 13)
        RemainingCourseLine_Layout.addStretch()
        RemainingCourseLine = QFrame()
        RemainingCourseLine.setMinimumSize(100, 1)
        RemainingCourseLine.setMaximumSize(100, 1)
        RemainingCourseLine.setStyleSheet("background-color: rgb(239, 233, 231);")
        RemainingCourseLine.setFrameShape(QFrame.Shape.HLine)
        RemainingCourseLine_Layout.addWidget(RemainingCourseLine)
        RemainingCourseLine_Layout.addStretch()
        RemainingCourse_Layout.addLayout(RemainingCourseLine_Layout)

        RemainingCourseRemainingStudents_Layout = QHBoxLayout()
        RemainingCourseRemainingStudents_Layout.setSpacing(5)
        RemainingCourseRemainingStudentsLabel = QLabel(LabelsStyling.format("Remaining Students:"))
        RemainingCourseRemainingStudentsLabel.setStyleSheet("background-color: none; font-weight: bold; font-family: Calibri;")
        RemainingCourseRemainingStudentsValueLabel = QLabel(
            LabelsStyling.format(str(course.get("overall_number_failed", "N/A")))
        )
        RemainingCourseRemainingStudentsValueLabel.setStyleSheet("background-color: none; font-family: Calibri;")
        RemainingCourseRemainingStudents_Layout.addWidget(RemainingCourseRemainingStudentsLabel)
        RemainingCourseRemainingStudents_Layout.addWidget(RemainingCourseRemainingStudentsValueLabel)
        RemainingCourseRemainingStudents_Layout.addStretch()
        RemainingCourse_Layout.addLayout(RemainingCourseRemainingStudents_Layout)

        RemainingCoursePassRate_Layout = QHBoxLayout()
        RemainingCoursePassRate_Layout.setSpacing(5)
        RemainingCoursePassRateLabel = QLabel(LabelsStyling.format("Pass Rate:"))
        RemainingCoursePassRateLabel.setStyleSheet("background-color: none; font-weight: bold; font-family: Calibri;")
        RemainingCoursePassRateValueLabel = QLabel(LabelsStyling.format(str(course.get("overall_success_rate", "N/A"))))
        RemainingCoursePassRateValueLabel.setStyleSheet("background-color: none; font-family: Calibri;")
        RemainingCoursePassRate_Layout.addWidget(RemainingCoursePassRateLabel)
        RemainingCoursePassRate_Layout.addWidget(RemainingCoursePassRateValueLabel)
        RemainingCoursePassRate_Layout.addStretch()
        RemainingCourse_Layout.addLayout(RemainingCoursePassRate_Layout)

        return RemainingCourse

    def _set_scroll_enabled(self, enabled):
        self.ui.CurrentCoursesScrollArea.horizontalScrollBar().setEnabled(enabled)
        self.ui.PassedCoursesScrollArea.verticalScrollBar().setEnabled(enabled)
        self.ui.FailedCoursesScrollArea.verticalScrollBar().setEnabled(enabled)
        self.ui.RemainingCoursesScrollArea.verticalScrollBar().setEnabled(enabled)

    def _scroll_all_to_top(self):
        self.ui.CurrentCoursesScrollArea.horizontalScrollBar().setValue(0)
        self.ui.PassedCoursesScrollArea.verticalScrollBar().setValue(0)
        self.ui.FailedCoursesScrollArea.verticalScrollBar().setValue(0)
        self.ui.RemainingCoursesScrollArea.verticalScrollBar().setValue(0)

    def _search_course(self):
        search_text = self.ui.SearchForCourseLineEdit.text().strip()
        if not search_text:
            self._undo_search()
            return

        if not self.all_course_cards:
            self._rebuild_all_course_cards()

        search_lower = search_text.lower()
        match_found = False
        for card in self.all_course_cards:
            display = getattr(card, 'course_display', '')
            if search_lower in display.lower():
                match_found = True
                break

        if match_found:
            self.ui.SearchForCourseLineEdit.setStyleSheet(self.default_line_edit_style)
            for card in self.all_course_cards:
                display = getattr(card, 'course_display', '')
                if search_lower in display.lower():
                    card.show()
                else:
                    card.hide()
            self._set_scroll_enabled(False)
            self.search_active = True
        else:
            self.ui.SearchForCourseLineEdit.setStyleSheet(self.error_line_edit_style)
            for card in self.all_course_cards:
                card.show()
            self._set_scroll_enabled(True)
            self.search_active = False

        self._scroll_all_to_top()

    def _undo_search(self):
        for card in self.all_course_cards:
            card.show()
        self.ui.SearchForCourseLineEdit.setStyleSheet(self.default_line_edit_style)
        self.ui.SearchForCourseLineEdit.clear()
        self._set_scroll_enabled(True)
        self._scroll_all_to_top()
        self.search_active = False

    def closeEvent(self, event):
        self.streamlit.terminate()
        event.accept()