from PySide6.QtCore import QObject, Signal
from Network import NetworkClient
from API_URL import API_URL

_instance = None

def get_auth_service():
    global _instance
    if _instance is None:
        _instance = AuthenticationService()
    return _instance


class AuthenticationService(QObject):
    login_success = Signal(dict)
    login_failed  = Signal()
    courses_loaded = Signal(dict)

    def __init__(self):
        super().__init__()
        self.network = NetworkClient()
        self.access_token = None
        self.user_data = None

    def login(self, user_id: str, password: str):
        url = f"{API_URL}/login?id={user_id}&passw={password}"
        self.network.response_received.connect(self._on_login_response)
        self.network.post(url)

    def _on_login_response(self, data: dict):
        self.network.response_received.disconnect(self._on_login_response)
        if 'access_token' in data:
            self.access_token = data['access_token']
            self._fetch_user_data()
        else:
            self.login_failed.emit()

    def _fetch_user_data(self):
        url = f"{API_URL}/get_data"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        self.network.response_received.connect(self._on_user_data)
        self.network.get(url, headers)

    def _on_user_data(self, data: dict):
        self.network.response_received.disconnect(self._on_user_data)
        self.user_data = data.get('user_data', {})
        if self.user_data:
            self._fetch_calculations()
        else:
            self.login_failed.emit()

    def _fetch_calculations(self):
        url = f"{API_URL}/calculations"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        self.network.response_received.connect(self._on_calculations)
        self.network.get(url, headers)

    def _on_calculations(self, data: dict):
        self.network.response_received.disconnect(self._on_calculations)
        if self.user_data:
            self.user_data.update(data)
        self.login_success.emit(self.user_data)
        self.fetch_courses()

    def fetch_courses(self):
        url = f"{API_URL}/get_courses"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        self.network.response_received.connect(self._on_courses_data)
        self.network.get(url, headers)

    def _on_courses_data(self, data: dict):
        self.network.response_received.disconnect(self._on_courses_data)
        self.courses_loaded.emit(data)