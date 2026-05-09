import os
import sys
import subprocess
import socket
from urllib.parse import urlparse
from API_URL import API_URL

parsed = urlparse(API_URL)
API_PORT = parsed.port or 80
STREAMLIT_PORT = API_PORT + 500
STREAMLIT_URL = f"http://localhost:{STREAMLIT_PORT}"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class StreamlitServer:
    def __init__(self):
        self.process = None

    def start(self):
        if self._is_port_open(STREAMLIT_PORT):
            return

        dashboard_path = os.path.join(BASE_DIR, "AnalysisDashboard.py")
        excel_path = os.path.join(BASE_DIR, "Data - Analysis, Database.xlsx")
        if not os.path.exists(dashboard_path):
            raise FileNotFoundError("AnalysisDashboard.py missing")
        if not os.path.exists(excel_path):
            raise FileNotFoundError("Excel data file missing")

        creation_flags = subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
        self.process = subprocess.Popen(
            [sys.executable, "-m", "streamlit", "run",
             "AnalysisDashboard.py",
             "--server.port", str(STREAMLIT_PORT),
             "--server.headless", "true",
             "--server.enableCORS", "false",
             "--server.enableXsrfProtection", "false",
             "--client.toolbarMode", "hidden"],
            cwd=BASE_DIR,
            stdout=None,
            stderr=None,
            creationflags=creation_flags
        )

    def _is_port_open(self, port, host='localhost'):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            return sock.connect_ex((host, port)) == 0

    def terminate(self):
        if self.process:
            self.process.terminate()
            self.process.wait()