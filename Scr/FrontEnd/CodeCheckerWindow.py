from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QWidget
from CodeCheckerWindow_UI import Ui_CodeCheckerWindow


class CodeCheckerWindow(QWidget):
    login_attempt = Signal(str, str)

    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.ui = Ui_CodeCheckerWindow()
        self.ui.setupUi(self)
        self.ui.ErrorPhraseLabel.setHidden(True)

        try:
            self.ui.LogInButton.setCheckable(False)
            self.ui.LogInButton.setAutoDefault(False)
            if hasattr(self.ui.LogInButton, 'setDefault'):
                self.ui.LogInButton.setDefault(False)
        except Exception:
            pass

        self.ui.LogInButton.clicked.connect(self._on_login_clicked)

    def _on_login_clicked(self):
        user_id = self.ui.IDBox.text().strip()
        password = self.ui.PasswordBox.text().strip()
        if user_id and password:
            self.login_attempt.emit(user_id, password)
        try:
            if hasattr(self.ui.LogInButton, 'setChecked'):
                self.ui.LogInButton.setChecked(False)
        except Exception:
            pass
        try:
            if hasattr(self.ui.LogInButton, 'setDown'):
                self.ui.LogInButton.setDown(False)
        except Exception:
            pass

    def show_error(self, message: str = ""):
        self.ui.ErrorPhraseLabel.setText(message or "Login failed")
        self.ui.ErrorPhraseLabel.setHidden(False)

    def hide_error(self):
        self.ui.ErrorPhraseLabel.setHidden(True)

    def clear_fields(self):
        self.ui.IDBox.clear()
        self.ui.PasswordBox.clear()