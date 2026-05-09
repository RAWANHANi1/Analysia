# Analysia
desktop application built with PySide6(using Qt Framework for Python)that serves as the primary user interface for students to view academic performance data, course information, and AI driven predictions. The frontend communicates with a FastAPI backend to retrieve data and with a local Streamlit server to render an interactive analysis dashboard.


🛠 Prerequisites and Dependencies
This project requires the following environment and libraries to run successfully.

1. Programming Language & Versions

Python: 3.13+ (The project is developed using Python 3.13.1)

3. Frameworks and Libraries

The project is divided into several modules, requiring the following libraries:

GUI & Frontend:

PySide6: For the main Desktop application interface.

QWebEngineView: For embedding web content within the Qt interface.

Streamlit: Powering the data analysis dashboard.

Backend & API:

FastAPI: High-performance web framework for the backend.

Uvicorn: ASGI server for running the FastAPI application.

PyJWT: For secure authentication (JSON Web Tokens).

Pydantic: For data validation and settings management.

Database & ORM:

SQLAlchemy: SQL toolkit and Object-Relational Mapper.

SQLite: Database engine (File-based).

Data Science & Machine Learning:

scikit-learn: For machine learning model implementation.

Pandas: For data manipulation and analysis.

NumPy: For numerical computations.
scipy: for sparse csr_matrix
scipy: for sparse.linalg svds

joblib: For loading and saving trained models (.pkl files).

Utility:

urllib & json: For handling API requests and data parsing.

3.Required Software & Tools

VS Code (Recommended): To open the project and run the source code.

Python Package Manager (pip): To install all the dependencies listed above.

4. System Requirements
   
Operating System: Windows 10/11 (Recommended for PySide6 compatibility).

RAM: 8 GB minimum (to handle data analysis and ML models smoothly).

Storage: At least 500 MB of free space for libraries and the database file.

5. External Services

Local Database: The project uses a local SQLite database (no external hosting required for evaluation).

⚙️ Installation & Environment Setup
Repeat these steps when ever you move the application folder from one place to another
Steps that has * is only performed once

*1- Download Python 3.13 from "https://www.python.org/ftp/python/3.13.13/python-3.13.13-amd64.exe", and then install it, while installing make sure you check the "Add Python.exe to PATH" Checkbox.

2- Download project folder in your PC "https://github.com/RAWANHANi1/Analysia/raw/refs/heads/main/Scr/Graduation%20Project%20-%20Analysia.zip"

3- Open the project folder in VSCode, Press (ctrl+shift+p), write create environment and choose it

4- select venv, select Python 3.13.13, press enter, select skip package installation

5- press (ctrl+j), if there's a green (.venv) before the terminal path then ignore step 5 your on the right track

6- press (ctrl+j) and paste this command ".\.venv\Scripts\Activate.ps1", if nothing appeared and you got a green (.venv) and then the path of the terminal then your in the right track

7- paste this command "python -m pip install --no-cache-dir -r "Requirements.txt"", and wait for the components to get installed, your pc must have an internet connection


#### Run Instructions

Steps that has * is only performed once

Step 1: Open the folder you extracted from the zip file in VS Code (Visual Studio Code)

Step 2: Open the terminal inside VS Code (Ctrl+J) and write "uvicorn Api:app --reload", you should see exactly 6 Green INFO: 
and the final INFO: is saying "Application startup complete." This means you started the Api.

*Step 3: Copy the Link appered in the terminal in the Second INFO: (Should be something like this, http://127.0.0.1:8000).

*Step 4: Open the "API_URL.py" file and change the link in it to the link you copied in Step 3.
Optional Step: if you wanna see how our Api Functions, just write /docs after the link in any web browser, and you'll see (Should be something like this "http://127.0.0.1:8000/docs").

Step 5: Open the "main.py" file and click the run button in VS Code. If it didn't work open ANOTHER VS Code terminal (you can do it by pressing the + button presented in the terminal) and write "python main.py".

Step 6: Start using the App, after enjoying it, close VS Code and Everything will be closed with it.

