# Analysia
desktop application built with PySide6(using Qt Framework for Python)that serves as the primary user interface for students to view academic performance data, course information, and AI driven predictions. The frontend communicates with a FastAPI backend to retrieve data and with a local Streamlit server to render an interactive analysis dashboard.
🛠 Prerequisites and Dependencies
This project requires the following environment and libraries to run successfully.

1. Programming Language & Versions
Python: 3.13+ (The project is developed using Python 3.13.1)

2. Frameworks and Libraries
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

joblib: For loading and saving trained models (.pkl files).

Utility:

urllib & json: For handling API requests and data parsing.

3. Required Software & Tools
VS Code (Recommended): To open the project and run the source code.

Python Package Manager (pip): To install all the dependencies listed above.

4. System Requirements
Operating System: Windows 10/11 (Recommended for PySide6 compatibility).

RAM: 8 GB minimum (to handle data analysis and ML models smoothly).

Storage: At least 500 MB of free space for libraries and the database file.

5. External Services
Local Database: The project uses a local SQLite database (no external hosting required for evaluation).

#### Installation Steps

Step-by-step instructions:

1. Clone the repository
2. Install dependencies
3. Configure the environment

#### Compilation Steps

Provide exact commands to build the project.

#### Run Instructions

 Explain how to start the application after building.

#### Environment Setup & Configuration

Include all required setup:

- Environment variables
- Configuration files
- Database setup or connections
