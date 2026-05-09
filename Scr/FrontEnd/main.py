import sys
import os
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-gpu"

from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from CodeCheckerWindow import CodeCheckerWindow
from MainWindow import MainWindow
from AuthenticationService import get_auth_service


class ApplicationController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Analysia")
        self.setStyleSheet("background-color: rgb(223, 210, 206);")
        self.setMinimumSize(900, 650)
        self.setMaximumSize(900, 650)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.login_widget = CodeCheckerWindow()
        self.main_window  = MainWindow()

        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.addWidget(self.main_window)

        self.auth_service = get_auth_service()
        self.login_widget.login_attempt.connect(self.auth_service.login)
        self.auth_service.login_success.connect(self._on_login_success)
        self.auth_service.login_failed.connect(self._on_login_failed)

        self.main_window.logout_requested.connect(self._on_logout)
        self.stacked_widget.setCurrentIndex(0)

    def _on_login_success(self, user_data: dict):
        student_id = user_data.get('student_id', '')
        self.main_window.set_user_data(user_data)
        self.main_window.set_student_id(student_id)
        self.main_window.preload_analysis()
        self.stacked_widget.setCurrentIndex(1)
        self.login_widget.clear_fields()
        self.login_widget.hide_error()

    def _on_login_failed(self):
        self.login_widget.ui.ErrorPhraseLabel.setHidden(False)

    def _on_logout(self):
        self.stacked_widget.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = ApplicationController()
    controller.show()
    sys.exit(app.exec())