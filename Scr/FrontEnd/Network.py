import json
from urllib.parse import urlencode
from PySide6.QtCore import QObject, Signal, QUrl
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

class NetworkClient(QObject):
    response_received = Signal(dict)

    def __init__(self):
        super().__init__()
        self.manager = QNetworkAccessManager()
        self.manager.finished.connect(self._handle_response)

    def post(self, url: str, data: dict = None):
        request = QNetworkRequest(QUrl(url))
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/x-www-form-urlencoded")
        post_data = urlencode(data).encode() if data else b''
        self.manager.post(request, post_data)

    def get(self, url: str, headers: dict = None):
        request = QNetworkRequest(QUrl(url))
        if headers:
            for k, v in headers.items():
                request.setRawHeader(k.encode(), v.encode())
        self.manager.get(request)

    def post_json(self, url: str, data: dict, headers: dict = None):
        request = QNetworkRequest(QUrl(url))
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        if headers:
            for k, v in headers.items():
                request.setRawHeader(k.encode(), v.encode())
        json_data = json.dumps(data).encode()
        self.manager.post(request, json_data)

    def _handle_response(self, reply: QNetworkReply):
        raw = reply.readAll().data()
        self.response_received.emit(json.loads(raw.decode()))
        reply.deleteLater()