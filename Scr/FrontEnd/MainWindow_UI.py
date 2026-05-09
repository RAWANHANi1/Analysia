from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QFormLayout, QFrame, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout, QWidget
import MainWindow_Resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(900, 650))
        MainWindow.setMaximumSize(QSize(900, 650))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setStyleStrategy(QFont.PreferAntialias)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(239, 233, 231);")
        self.MainWidget = QWidget(MainWindow)
        self.MainWidget.setObjectName(u"MainWidget")
        self.MainWidget.setGeometry(QRect(70, 5, 825, 640))
        sizePolicy.setHeightForWidth(self.MainWidget.sizePolicy().hasHeightForWidth())
        self.MainWidget.setSizePolicy(sizePolicy)
        self.MainWidget.setMinimumSize(QSize(825, 640))
        self.MainWidget.setMaximumSize(QSize(825, 640))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.MainWidget.setFont(font1)
        self.MainWidget.setStyleSheet(u"border-radius: 10px;")
        self.StackedWidget = QStackedWidget(self.MainWidget)
        self.StackedWidget.setObjectName(u"StackedWidget")
        self.StackedWidget.setGeometry(QRect(0, 0, 825, 640))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.StackedWidget.sizePolicy().hasHeightForWidth())
        self.StackedWidget.setSizePolicy(sizePolicy1)
        self.StackedWidget.setMinimumSize(QSize(825, 640))
        self.StackedWidget.setMaximumSize(QSize(825, 640))
        font2 = QFont()
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.StackedWidget.setFont(font2)
        self.StackedWidget.setAutoFillBackground(False)
        self.StackedWidget.setStyleSheet(u"background-color: none;")
        self.StackedWidget.setLineWidth(0)
        self.ProfilePage = QWidget()
        self.ProfilePage.setObjectName(u"ProfilePage")
        self.ProfilePage.setMinimumSize(QSize(825, 640))
        self.ProfilePage.setMaximumSize(QSize(825, 640))
        self.ProfilePage.setFont(font2)
        self.ProfilePage.setAutoFillBackground(False)
        self.ProfilePage.setStyleSheet(u"")
        self.ProfilePageWidget = QWidget(self.ProfilePage)
        self.ProfilePageWidget.setObjectName(u"ProfilePageWidget")
        self.ProfilePageWidget.setGeometry(QRect(0, 0, 825, 640))
        self.ProfilePageWidget.setMinimumSize(QSize(825, 640))
        self.ProfilePageWidget.setMaximumSize(QSize(825, 640))
        self.ProfilePageWidget.setAutoFillBackground(False)
        self.ProfilePageWidget.setStyleSheet(u"")
        self.ProfilePageWidget_Layout = QGridLayout(self.ProfilePageWidget)
        self.ProfilePageWidget_Layout.setSpacing(5)
        self.ProfilePageWidget_Layout.setObjectName(u"ProfilePageWidget_Layout")
        self.ProfilePageWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.UsersProfilePhoto = QPushButton(self.ProfilePageWidget)
        self.UsersProfilePhoto.setObjectName(u"UsersProfilePhoto")
        self.UsersProfilePhoto.setMinimumSize(QSize(185, 185))
        self.UsersProfilePhoto.setMaximumSize(QSize(180, 185))
        self.UsersProfilePhoto.setFont(font2)
        self.UsersProfilePhoto.setStyleSheet(u"background-color: \"white\";")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/User.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.UsersProfilePhoto.setIcon(icon)
        self.UsersProfilePhoto.setIconSize(QSize(150, 150))
        self.UsersProfilePhoto.setCheckable(True)
        self.UsersProfilePhoto.setChecked(False)

        self.ProfilePageWidget_Layout.addWidget(self.UsersProfilePhoto, 0, 0, 1, 1)

        self.CreditsWidget = QWidget(self.ProfilePageWidget)
        self.CreditsWidget.setObjectName(u"CreditsWidget")
        self.CreditsWidget.setMinimumSize(QSize(425, 250))
        self.CreditsWidget.setMaximumSize(QSize(425, 250))
        self.CreditsWidget.setStyleSheet(u"border-radius: 10px;\n"
"background-color: \"white\";\n"
"color: \"black\";")
        self.CreditsWidget_Layout = QFormLayout(self.CreditsWidget)
        self.CreditsWidget_Layout.setObjectName(u"CreditsWidget_Layout")
        self.CreditsWidget_Layout.setHorizontalSpacing(5)
        self.CreditsWidget_Layout.setVerticalSpacing(5)
        self.CreditsWidget_Layout.setContentsMargins(10, 5, 10, 10)
        self.CreditsRemainingWidget = QWidget(self.CreditsWidget)
        self.CreditsRemainingWidget.setObjectName(u"CreditsRemainingWidget")
        self.CreditsRemainingWidget.setMinimumSize(QSize(200, 100))
        self.CreditsRemainingWidget.setMaximumSize(QSize(200, 100))
        self.CreditsRemainingWidget.setFont(font2)
        self.CreditsRemainingWidget.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(27, 49, 96),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.CreditsRemainingWidget_Layout = QVBoxLayout(self.CreditsRemainingWidget)
        self.CreditsRemainingWidget_Layout.setSpacing(5)
        self.CreditsRemainingWidget_Layout.setObjectName(u"CreditsRemainingWidget_Layout")
        self.CreditsRemainingWidget_Layout.setContentsMargins(10, 5, 10, 10)
        self.CreditsRemainingLabel = QLabel(self.CreditsRemainingWidget)
        self.CreditsRemainingLabel.setObjectName(u"CreditsRemainingLabel")
        font3 = QFont()
        font3.setFamilies([u"Calibri"])
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.CreditsRemainingLabel.setFont(font3)
        self.CreditsRemainingLabel.setStyleSheet(u"background-color: none;")

        self.CreditsRemainingWidget_Layout.addWidget(self.CreditsRemainingLabel)

        self.CreditsRemainingValueLabel = QLabel(self.CreditsRemainingWidget)
        self.CreditsRemainingValueLabel.setObjectName(u"CreditsRemainingValueLabel")
        font4 = QFont()
        font4.setFamilies([u"Calibri"])
        font4.setPointSize(15)
        font4.setBold(False)
        font4.setStyleStrategy(QFont.PreferAntialias)
        self.CreditsRemainingValueLabel.setFont(font4)
        self.CreditsRemainingValueLabel.setStyleSheet(u"background-color: none;")

        self.CreditsRemainingWidget_Layout.addWidget(self.CreditsRemainingValueLabel)


        self.CreditsWidget_Layout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.CreditsRemainingWidget)

        self.CreditsAttemptedWidget = QWidget(self.CreditsWidget)
        self.CreditsAttemptedWidget.setObjectName(u"CreditsAttemptedWidget")
        self.CreditsAttemptedWidget.setMinimumSize(QSize(200, 100))
        self.CreditsAttemptedWidget.setMaximumSize(QSize(200, 100))
        self.CreditsAttemptedWidget.setFont(font2)
        self.CreditsAttemptedWidget.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(106, 69, 57),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.CreditsAttemptedWidget_Layout = QVBoxLayout(self.CreditsAttemptedWidget)
        self.CreditsAttemptedWidget_Layout.setSpacing(5)
        self.CreditsAttemptedWidget_Layout.setObjectName(u"CreditsAttemptedWidget_Layout")
        self.CreditsAttemptedWidget_Layout.setContentsMargins(10, 5, 10, 10)
        self.CreditsAttemptedLabel = QLabel(self.CreditsAttemptedWidget)
        self.CreditsAttemptedLabel.setObjectName(u"CreditsAttemptedLabel")
        self.CreditsAttemptedLabel.setFont(font3)
        self.CreditsAttemptedLabel.setStyleSheet(u"background-color: none;")

        self.CreditsAttemptedWidget_Layout.addWidget(self.CreditsAttemptedLabel)

        self.CreditsAttemptedValueLabel = QLabel(self.CreditsAttemptedWidget)
        self.CreditsAttemptedValueLabel.setObjectName(u"CreditsAttemptedValueLabel")
        self.CreditsAttemptedValueLabel.setFont(font4)
        self.CreditsAttemptedValueLabel.setStyleSheet(u"background-color: none;")

        self.CreditsAttemptedWidget_Layout.addWidget(self.CreditsAttemptedValueLabel)


        self.CreditsWidget_Layout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.CreditsAttemptedWidget)

        self.CreditsPassedWidget = QWidget(self.CreditsWidget)
        self.CreditsPassedWidget.setObjectName(u"CreditsPassedWidget")
        self.CreditsPassedWidget.setMinimumSize(QSize(200, 100))
        self.CreditsPassedWidget.setMaximumSize(QSize(200, 100))
        self.CreditsPassedWidget.setFont(font2)
        self.CreditsPassedWidget.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(7, 74, 45),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.CreditsPassedWidget_Layout = QVBoxLayout(self.CreditsPassedWidget)
        self.CreditsPassedWidget_Layout.setSpacing(5)
        self.CreditsPassedWidget_Layout.setObjectName(u"CreditsPassedWidget_Layout")
        self.CreditsPassedWidget_Layout.setContentsMargins(10, 5, 10, 10)
        self.CreditsPassedLabel = QLabel(self.CreditsPassedWidget)
        self.CreditsPassedLabel.setObjectName(u"CreditsPassedLabel")
        self.CreditsPassedLabel.setFont(font3)
        self.CreditsPassedLabel.setStyleSheet(u"background-color: none;")

        self.CreditsPassedWidget_Layout.addWidget(self.CreditsPassedLabel)

        self.CreditsPassedValueLabel = QLabel(self.CreditsPassedWidget)
        self.CreditsPassedValueLabel.setObjectName(u"CreditsPassedValueLabel")
        self.CreditsPassedValueLabel.setFont(font4)
        self.CreditsPassedValueLabel.setStyleSheet(u"background-color: none;")

        self.CreditsPassedWidget_Layout.addWidget(self.CreditsPassedValueLabel)


        self.CreditsWidget_Layout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.CreditsPassedWidget)

        self.CreditsFailedWidget = QWidget(self.CreditsWidget)
        self.CreditsFailedWidget.setObjectName(u"CreditsFailedWidget")
        self.CreditsFailedWidget.setMinimumSize(QSize(200, 100))
        self.CreditsFailedWidget.setMaximumSize(QSize(200, 100))
        self.CreditsFailedWidget.setFont(font2)
        self.CreditsFailedWidget.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(128, 15, 28),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.CreditsFailedWidget_Layout = QVBoxLayout(self.CreditsFailedWidget)
        self.CreditsFailedWidget_Layout.setSpacing(5)
        self.CreditsFailedWidget_Layout.setObjectName(u"CreditsFailedWidget_Layout")
        self.CreditsFailedWidget_Layout.setContentsMargins(10, 5, 10, 10)
        self.CreditsFailedLabel = QLabel(self.CreditsFailedWidget)
        self.CreditsFailedLabel.setObjectName(u"CreditsFailedLabel")
        self.CreditsFailedLabel.setFont(font3)
        self.CreditsFailedLabel.setStyleSheet(u"background-color: none;")

        self.CreditsFailedWidget_Layout.addWidget(self.CreditsFailedLabel)

        self.CreditsFailedValueLabel = QLabel(self.CreditsFailedWidget)
        self.CreditsFailedValueLabel.setObjectName(u"CreditsFailedValueLabel")
        self.CreditsFailedValueLabel.setFont(font4)
        self.CreditsFailedValueLabel.setStyleSheet(u"background-color: none;")

        self.CreditsFailedWidget_Layout.addWidget(self.CreditsFailedValueLabel)


        self.CreditsWidget_Layout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.CreditsFailedWidget)

        self.CreditsLabel = QLabel(self.CreditsWidget)
        self.CreditsLabel.setObjectName(u"CreditsLabel")
        self.CreditsLabel.setFont(font3)
        self.CreditsLabel.setStyleSheet(u"background-color: none;")

        self.CreditsWidget_Layout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.CreditsLabel)


        self.ProfilePageWidget_Layout.addWidget(self.CreditsWidget, 1, 0, 1, 2)

        self.PersonalInformationWidget = QWidget(self.ProfilePageWidget)
        self.PersonalInformationWidget.setObjectName(u"PersonalInformationWidget")
        self.PersonalInformationWidget.setMinimumSize(QSize(635, 185))
        self.PersonalInformationWidget.setMaximumSize(QSize(635, 185))
        self.PersonalInformationWidget.setFont(font2)
        self.PersonalInformationWidget.setStyleSheet(u"border-radius: 10px;\n"
"background-color: \"white\";\n"
"color: \"black\";")
        self.PersonalInformationWidget_Layout = QVBoxLayout(self.PersonalInformationWidget)
        self.PersonalInformationWidget_Layout.setSpacing(5)
        self.PersonalInformationWidget_Layout.setObjectName(u"PersonalInformationWidget_Layout")
        self.PersonalInformationWidget_Layout.setContentsMargins(10, 5, 10, 10)
        self.PersonalInformationLabel = QLabel(self.PersonalInformationWidget)
        self.PersonalInformationLabel.setObjectName(u"PersonalInformationLabel")
        self.PersonalInformationLabel.setFont(font3)
        self.PersonalInformationLabel.setStyleSheet(u"background-color: none;")

        self.PersonalInformationWidget_Layout.addWidget(self.PersonalInformationLabel)

        self.FullName_Layout = QHBoxLayout()
        self.FullName_Layout.setSpacing(5)
        self.FullName_Layout.setObjectName(u"FullName_Layout")
        self.FullNameLabel = QLabel(self.PersonalInformationWidget)
        self.FullNameLabel.setObjectName(u"FullNameLabel")
        self.FullNameLabel.setFont(font3)
        self.FullNameLabel.setStyleSheet(u"background-color: none;")

        self.FullName_Layout.addWidget(self.FullNameLabel)

        self.FullNameValueLabel = QLabel(self.PersonalInformationWidget)
        self.FullNameValueLabel.setObjectName(u"FullNameValueLabel")
        self.FullNameValueLabel.setFont(font4)
        self.FullNameValueLabel.setStyleSheet(u"background-color: none;")

        self.FullName_Layout.addWidget(self.FullNameValueLabel)

        self.FullNameSpacer = QSpacerItem(356, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.FullName_Layout.addItem(self.FullNameSpacer)


        self.PersonalInformationWidget_Layout.addLayout(self.FullName_Layout)

        self.ID_Layout = QHBoxLayout()
        self.ID_Layout.setSpacing(5)
        self.ID_Layout.setObjectName(u"ID_Layout")
        self.IDLabel = QLabel(self.PersonalInformationWidget)
        self.IDLabel.setObjectName(u"IDLabel")
        self.IDLabel.setFont(font3)
        self.IDLabel.setStyleSheet(u"background-color: none;")

        self.ID_Layout.addWidget(self.IDLabel)

        self.IDValueLabel = QLabel(self.PersonalInformationWidget)
        self.IDValueLabel.setObjectName(u"IDValueLabel")
        self.IDValueLabel.setFont(font4)
        self.IDValueLabel.setStyleSheet(u"background-color: none;")

        self.ID_Layout.addWidget(self.IDValueLabel)

        self.IDSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.ID_Layout.addItem(self.IDSpacer)


        self.PersonalInformationWidget_Layout.addLayout(self.ID_Layout)

        self.Level_Layout = QHBoxLayout()
        self.Level_Layout.setSpacing(5)
        self.Level_Layout.setObjectName(u"Level_Layout")
        self.LevelLabel = QLabel(self.PersonalInformationWidget)
        self.LevelLabel.setObjectName(u"LevelLabel")
        self.LevelLabel.setFont(font3)
        self.LevelLabel.setStyleSheet(u"background-color: none;")

        self.Level_Layout.addWidget(self.LevelLabel)

        self.LevelValueLabel = QLabel(self.PersonalInformationWidget)
        self.LevelValueLabel.setObjectName(u"LevelValueLabel")
        self.LevelValueLabel.setFont(font4)
        self.LevelValueLabel.setStyleSheet(u"background-color: none;")

        self.Level_Layout.addWidget(self.LevelValueLabel)

        self.LevelSpacer = QSpacerItem(500, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Level_Layout.addItem(self.LevelSpacer)


        self.PersonalInformationWidget_Layout.addLayout(self.Level_Layout)

        self.Department_Layout = QHBoxLayout()
        self.Department_Layout.setSpacing(5)
        self.Department_Layout.setObjectName(u"Department_Layout")
        self.DepartmentLabel = QLabel(self.PersonalInformationWidget)
        self.DepartmentLabel.setObjectName(u"DepartmentLabel")
        self.DepartmentLabel.setFont(font3)
        self.DepartmentLabel.setStyleSheet(u"background-color: none;")

        self.Department_Layout.addWidget(self.DepartmentLabel)

        self.DepartmentValueLabel = QLabel(self.PersonalInformationWidget)
        self.DepartmentValueLabel.setObjectName(u"DepartmentValueLabel")
        self.DepartmentValueLabel.setFont(font4)
        self.DepartmentValueLabel.setStyleSheet(u"background-color: none;")

        self.Department_Layout.addWidget(self.DepartmentValueLabel)

        self.DepartmentSpacer = QSpacerItem(436, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Department_Layout.addItem(self.DepartmentSpacer)


        self.PersonalInformationWidget_Layout.addLayout(self.Department_Layout)

        self.Email_Layout = QHBoxLayout()
        self.Email_Layout.setSpacing(5)
        self.Email_Layout.setObjectName(u"Email_Layout")
        self.EmailLabel = QLabel(self.PersonalInformationWidget)
        self.EmailLabel.setObjectName(u"EmailLabel")
        self.EmailLabel.setFont(font3)
        self.EmailLabel.setStyleSheet(u"background-color: none;")

        self.Email_Layout.addWidget(self.EmailLabel)

        self.EmailValueLabel = QLabel(self.PersonalInformationWidget)
        self.EmailValueLabel.setObjectName(u"EmailValueLabel")
        self.EmailValueLabel.setFont(font4)
        self.EmailValueLabel.setStyleSheet(u"background-color: none;")

        self.Email_Layout.addWidget(self.EmailValueLabel)

        self.EmailSpacer = QSpacerItem(298, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Email_Layout.addItem(self.EmailSpacer)


        self.PersonalInformationWidget_Layout.addLayout(self.Email_Layout)


        self.ProfilePageWidget_Layout.addWidget(self.PersonalInformationWidget, 0, 1, 1, 2)

        self.SuccessRatesWidget = QWidget(self.ProfilePageWidget)
        self.SuccessRatesWidget.setObjectName(u"SuccessRatesWidget")
        self.SuccessRatesWidget.setMinimumSize(QSize(395, 250))
        self.SuccessRatesWidget.setMaximumSize(QSize(395, 250))
        self.SuccessRatesWidget.setFont(font2)
        self.SuccessRatesWidget.setStyleSheet(u"border-radius: 10px;\n"
"background-color: \"white\";\n"
"color: \"black\";")
        self.SuccessRatesWidget_Layout = QVBoxLayout(self.SuccessRatesWidget)
        self.SuccessRatesWidget_Layout.setSpacing(5)
        self.SuccessRatesWidget_Layout.setObjectName(u"SuccessRatesWidget_Layout")
        self.SuccessRatesWidget_Layout.setContentsMargins(10, 5, 10, 10)
        self.SuccessRatesLabel = QLabel(self.SuccessRatesWidget)
        self.SuccessRatesLabel.setObjectName(u"SuccessRatesLabel")
        self.SuccessRatesLabel.setFont(font3)
        self.SuccessRatesLabel.setStyleSheet(u"background-color: none;")

        self.SuccessRatesWidget_Layout.addWidget(self.SuccessRatesLabel)

        self.COMP_Layout = QHBoxLayout()
        self.COMP_Layout.setSpacing(5)
        self.COMP_Layout.setObjectName(u"COMP_Layout")
        self.COMPLabel = QLabel(self.SuccessRatesWidget)
        self.COMPLabel.setObjectName(u"COMPLabel")
        self.COMPLabel.setMinimumSize(QSize(75, 0))
        self.COMPLabel.setMaximumSize(QSize(75, 16777215))
        self.COMPLabel.setFont(font3)
        self.COMPLabel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(7, 74, 45),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")

        self.COMP_Layout.addWidget(self.COMPLabel)

        self.COMPProgressBar = QWidget(self.SuccessRatesWidget)
        self.COMPProgressBar.setObjectName(u"COMPProgressBar")
        self.COMPProgressBar_Layout = QHBoxLayout(self.COMPProgressBar)
        self.COMPProgressBar_Layout.setSpacing(0)
        self.COMPProgressBar_Layout.setObjectName(u"COMPProgressBar_Layout")
        self.COMPProgressBar_Layout.setContentsMargins(0, 0, 0, 0)

        self.COMP_Layout.addWidget(self.COMPProgressBar)

        self.COMPValueLabel = QLabel(self.SuccessRatesWidget)
        self.COMPValueLabel.setObjectName(u"COMPValueLabel")
        self.COMPValueLabel.setMinimumSize(QSize(50, 0))
        self.COMPValueLabel.setMaximumSize(QSize(50, 16777215))
        self.COMPValueLabel.setFont(font4)
        self.COMPValueLabel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(7, 74, 45),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")

        self.COMP_Layout.addWidget(self.COMPValueLabel)


        self.SuccessRatesWidget_Layout.addLayout(self.COMP_Layout)

        self.STAT_Layout = QHBoxLayout()
        self.STAT_Layout.setSpacing(5)
        self.STAT_Layout.setObjectName(u"STAT_Layout")
        self.STATLabel = QLabel(self.SuccessRatesWidget)
        self.STATLabel.setObjectName(u"STATLabel")
        self.STATLabel.setMinimumSize(QSize(75, 0))
        self.STATLabel.setMaximumSize(QSize(75, 16777215))
        self.STATLabel.setFont(font3)
        self.STATLabel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(7, 74, 45),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")

        self.STAT_Layout.addWidget(self.STATLabel)

        self.STATProgressBar = QWidget(self.SuccessRatesWidget)
        self.STATProgressBar.setObjectName(u"STATProgressBar")
        self.STATProgressBar_Layout = QHBoxLayout(self.STATProgressBar)
        self.STATProgressBar_Layout.setSpacing(0)
        self.STATProgressBar_Layout.setObjectName(u"STATProgressBar_Layout")
        self.STATProgressBar_Layout.setContentsMargins(0, 0, 0, 0)

        self.STAT_Layout.addWidget(self.STATProgressBar)

        self.STATValueLabel = QLabel(self.SuccessRatesWidget)
        self.STATValueLabel.setObjectName(u"STATValueLabel")
        self.STATValueLabel.setMinimumSize(QSize(50, 0))
        self.STATValueLabel.setMaximumSize(QSize(50, 16777215))
        self.STATValueLabel.setFont(font4)
        self.STATValueLabel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(7, 74, 45),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")

        self.STAT_Layout.addWidget(self.STATValueLabel)


        self.SuccessRatesWidget_Layout.addLayout(self.STAT_Layout)

        self.MATH_Layout = QHBoxLayout()
        self.MATH_Layout.setSpacing(5)
        self.MATH_Layout.setObjectName(u"MATH_Layout")
        self.MATHLabel = QLabel(self.SuccessRatesWidget)
        self.MATHLabel.setObjectName(u"MATHLabel")
        self.MATHLabel.setMinimumSize(QSize(75, 0))
        self.MATHLabel.setMaximumSize(QSize(75, 16777215))
        self.MATHLabel.setFont(font3)
        self.MATHLabel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(7, 74, 45),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")

        self.MATH_Layout.addWidget(self.MATHLabel)

        self.MATHProgressBar = QWidget(self.SuccessRatesWidget)
        self.MATHProgressBar.setObjectName(u"MATHProgressBar")
        self.MATHProgressBar_Layout = QHBoxLayout(self.MATHProgressBar)
        self.MATHProgressBar_Layout.setSpacing(0)
        self.MATHProgressBar_Layout.setObjectName(u"MATHProgressBar_Layout")
        self.MATHProgressBar_Layout.setContentsMargins(0, 0, 0, 0)

        self.MATH_Layout.addWidget(self.MATHProgressBar)

        self.MATHValueLabel = QLabel(self.SuccessRatesWidget)
        self.MATHValueLabel.setObjectName(u"MATHValueLabel")
        self.MATHValueLabel.setMinimumSize(QSize(50, 0))
        self.MATHValueLabel.setMaximumSize(QSize(50, 16777215))
        self.MATHValueLabel.setFont(font4)
        self.MATHValueLabel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(7, 74, 45),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")

        self.MATH_Layout.addWidget(self.MATHValueLabel)


        self.SuccessRatesWidget_Layout.addLayout(self.MATH_Layout)

        self.PHYS_Layout = QHBoxLayout()
        self.PHYS_Layout.setSpacing(5)
        self.PHYS_Layout.setObjectName(u"PHYS_Layout")
        self.PHYSLabel = QLabel(self.SuccessRatesWidget)
        self.PHYSLabel.setObjectName(u"PHYSLabel")
        self.PHYSLabel.setMinimumSize(QSize(75, 0))
        self.PHYSLabel.setMaximumSize(QSize(75, 16777215))
        self.PHYSLabel.setFont(font3)
        self.PHYSLabel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(7, 74, 45),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")

        self.PHYS_Layout.addWidget(self.PHYSLabel)

        self.PHYSProgressBar = QWidget(self.SuccessRatesWidget)
        self.PHYSProgressBar.setObjectName(u"PHYSProgressBar")
        self.PHYSProgressBar_Layout = QHBoxLayout(self.PHYSProgressBar)
        self.PHYSProgressBar_Layout.setSpacing(0)
        self.PHYSProgressBar_Layout.setObjectName(u"PHYSProgressBar_Layout")
        self.PHYSProgressBar_Layout.setContentsMargins(0, 0, 0, 0)

        self.PHYS_Layout.addWidget(self.PHYSProgressBar)

        self.PHYSValueLabel = QLabel(self.SuccessRatesWidget)
        self.PHYSValueLabel.setObjectName(u"PHYSValueLabel")
        self.PHYSValueLabel.setMinimumSize(QSize(50, 0))
        self.PHYSValueLabel.setMaximumSize(QSize(50, 16777215))
        self.PHYSValueLabel.setFont(font4)
        self.PHYSValueLabel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(7, 74, 45),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")

        self.PHYS_Layout.addWidget(self.PHYSValueLabel)


        self.SuccessRatesWidget_Layout.addLayout(self.PHYS_Layout)

        self.CHEM_Layout = QHBoxLayout()
        self.CHEM_Layout.setSpacing(5)
        self.CHEM_Layout.setObjectName(u"CHEM_Layout")
        self.CHEMLabel = QLabel(self.SuccessRatesWidget)
        self.CHEMLabel.setObjectName(u"CHEMLabel")
        self.CHEMLabel.setMinimumSize(QSize(75, 0))
        self.CHEMLabel.setMaximumSize(QSize(75, 16777215))
        self.CHEMLabel.setFont(font3)
        self.CHEMLabel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(7, 74, 45),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")

        self.CHEM_Layout.addWidget(self.CHEMLabel)

        self.CHEMProgressBar = QWidget(self.SuccessRatesWidget)
        self.CHEMProgressBar.setObjectName(u"CHEMProgressBar")
        self.CHEMProgressBar_Layout = QHBoxLayout(self.CHEMProgressBar)
        self.CHEMProgressBar_Layout.setSpacing(0)
        self.CHEMProgressBar_Layout.setObjectName(u"CHEMProgressBar_Layout")
        self.CHEMProgressBar_Layout.setContentsMargins(0, 0, 0, 0)

        self.CHEM_Layout.addWidget(self.CHEMProgressBar)

        self.CHEMValueLabel = QLabel(self.SuccessRatesWidget)
        self.CHEMValueLabel.setObjectName(u"CHEMValueLabel")
        self.CHEMValueLabel.setMinimumSize(QSize(50, 0))
        self.CHEMValueLabel.setMaximumSize(QSize(50, 16777215))
        self.CHEMValueLabel.setFont(font4)
        self.CHEMValueLabel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(7, 74, 45),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")

        self.CHEM_Layout.addWidget(self.CHEMValueLabel)


        self.SuccessRatesWidget_Layout.addLayout(self.CHEM_Layout)

        self.Others_Layout = QHBoxLayout()
        self.Others_Layout.setSpacing(5)
        self.Others_Layout.setObjectName(u"Others_Layout")
        self.OthersLabel = QLabel(self.SuccessRatesWidget)
        self.OthersLabel.setObjectName(u"OthersLabel")
        self.OthersLabel.setMinimumSize(QSize(75, 0))
        self.OthersLabel.setMaximumSize(QSize(75, 16777215))
        self.OthersLabel.setFont(font3)
        self.OthersLabel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(7, 74, 45),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")

        self.Others_Layout.addWidget(self.OthersLabel)

        self.OthersProgressBar = QWidget(self.SuccessRatesWidget)
        self.OthersProgressBar.setObjectName(u"OthersProgressBar")
        self.OthersProgressBar_Layout = QHBoxLayout(self.OthersProgressBar)
        self.OthersProgressBar_Layout.setSpacing(0)
        self.OthersProgressBar_Layout.setObjectName(u"OthersProgressBar_Layout")
        self.OthersProgressBar_Layout.setContentsMargins(0, 0, 0, 0)

        self.Others_Layout.addWidget(self.OthersProgressBar)

        self.OthersValueLabel = QLabel(self.SuccessRatesWidget)
        self.OthersValueLabel.setObjectName(u"OthersValueLabel")
        self.OthersValueLabel.setMinimumSize(QSize(50, 0))
        self.OthersValueLabel.setMaximumSize(QSize(50, 16777215))
        self.OthersValueLabel.setFont(font4)
        self.OthersValueLabel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(7, 74, 45),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")

        self.Others_Layout.addWidget(self.OthersValueLabel)


        self.SuccessRatesWidget_Layout.addLayout(self.Others_Layout)


        self.ProfilePageWidget_Layout.addWidget(self.SuccessRatesWidget, 1, 2, 1, 1)

        self.GPAWidget = QWidget(self.ProfilePageWidget)
        self.GPAWidget.setObjectName(u"GPAWidget")
        self.GPAWidget.setMinimumSize(QSize(825, 195))
        self.GPAWidget.setMaximumSize(QSize(825, 195))
        self.GPAWidget.setFont(font2)
        self.GPAWidget.setStyleSheet(u"border-radius: 10px;\n"
"background-color: \"white\";\n"
"color: \"black\";")
        self.GPAWidget_Layout = QVBoxLayout(self.GPAWidget)
        self.GPAWidget_Layout.setSpacing(5)
        self.GPAWidget_Layout.setObjectName(u"GPAWidget_Layout")
        self.GPAWidget_Layout.setContentsMargins(10, 5, 10, 10)
        self.GPALabel = QLabel(self.GPAWidget)
        self.GPALabel.setObjectName(u"GPALabel")
        self.GPALabel.setFont(font3)
        self.GPALabel.setStyleSheet(u"background-color: none;")

        self.GPAWidget_Layout.addWidget(self.GPALabel)

        self.GPACardWidget = QWidget(self.GPAWidget)
        self.GPACardWidget.setObjectName(u"GPACardWidget")
        self.GPACardWidget.setMinimumSize(QSize(805, 150))
        self.GPACardWidget.setMaximumSize(QSize(805, 150))
        self.GPACardWidget.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(7, 74, 45),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.GPACardWidget_Layout = QVBoxLayout(self.GPACardWidget)
        self.GPACardWidget_Layout.setSpacing(0)
        self.GPACardWidget_Layout.setObjectName(u"GPACardWidget_Layout")
        self.GPACardWidget_Layout.setContentsMargins(10, 25, 10, 25)
        self.GPAValueLabel = QLabel(self.GPACardWidget)
        self.GPAValueLabel.setObjectName(u"GPAValueLabel")
        self.GPAValueLabel.setFont(font4)
        self.GPAValueLabel.setStyleSheet(u"background-color: none;")

        self.GPACardWidget_Layout.addWidget(self.GPAValueLabel)

        self.GPACardLine_Layout = QHBoxLayout()
        self.GPACardLine_Layout.setSpacing(0)
        self.GPACardLine_Layout.setObjectName(u"GPACardLine_Layout")
        self.GPACardLineLeftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.GPACardLine_Layout.addItem(self.GPACardLineLeftSpacer)

        self.GPACardLine = QFrame(self.GPACardWidget)
        self.GPACardLine.setObjectName(u"GPACardLine")
        self.GPACardLine.setMinimumSize(QSize(200, 1))
        self.GPACardLine.setMaximumSize(QSize(200, 1))
        self.GPACardLine.setFont(font2)
        self.GPACardLine.setStyleSheet(u"background-color: \"white\";")
        self.GPACardLine.setFrameShape(QFrame.Shape.HLine)
        self.GPACardLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.GPACardLine_Layout.addWidget(self.GPACardLine)

        self.GPACardLineRightSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.GPACardLine_Layout.addItem(self.GPACardLineRightSpacer)


        self.GPACardWidget_Layout.addLayout(self.GPACardLine_Layout)

        self.GPAScore_Layout = QHBoxLayout()
        self.GPAScore_Layout.setSpacing(5)
        self.GPAScore_Layout.setObjectName(u"GPAScore_Layout")
        self.GPAScore_Layout.setContentsMargins(-1, -1, -1, 0)
        self.GPAScoreLeftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.GPAScore_Layout.addItem(self.GPAScoreLeftSpacer)

        self.GPAScoreNameValueLabel = QLabel(self.GPACardWidget)
        self.GPAScoreNameValueLabel.setObjectName(u"GPAScoreNameValueLabel")
        self.GPAScoreNameValueLabel.setFont(font3)
        self.GPAScoreNameValueLabel.setStyleSheet(u"background-color: none;")

        self.GPAScore_Layout.addWidget(self.GPAScoreNameValueLabel)

        self.GPAScoreCodeValueLabel = QLabel(self.GPACardWidget)
        self.GPAScoreCodeValueLabel.setObjectName(u"GPAScoreCodeValueLabel")
        self.GPAScoreCodeValueLabel.setFont(font3)
        self.GPAScoreCodeValueLabel.setStyleSheet(u"background-color: none;")

        self.GPAScore_Layout.addWidget(self.GPAScoreCodeValueLabel)

        self.GPAScoreRightSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.GPAScore_Layout.addItem(self.GPAScoreRightSpacer)


        self.GPACardWidget_Layout.addLayout(self.GPAScore_Layout)


        self.GPAWidget_Layout.addWidget(self.GPACardWidget)


        self.ProfilePageWidget_Layout.addWidget(self.GPAWidget, 2, 0, 1, 3)

        self.StackedWidget.addWidget(self.ProfilePage)
        self.AnalysisPage = QWidget()
        self.AnalysisPage.setObjectName(u"AnalysisPage")
        self.AnalysisPageWidget = QWidget(self.AnalysisPage)
        self.AnalysisPageWidget.setObjectName(u"AnalysisPageWidget")
        self.AnalysisPageWidget.setGeometry(QRect(0, 0, 825, 640))
        self.AnalysisPageWidget.setMinimumSize(QSize(825, 640))
        self.AnalysisPageWidget.setMaximumSize(QSize(825, 640))
        self.AnalysisPageWidget.setStyleSheet(u"border-radius: 10px;;")
        self.AnalysisPageWidget_Layout = QVBoxLayout(self.AnalysisPageWidget)
        self.AnalysisPageWidget_Layout.setSpacing(0)
        self.AnalysisPageWidget_Layout.setObjectName(u"AnalysisPageWidget_Layout")
        self.AnalysisPageWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget.addWidget(self.AnalysisPage)
        self.AIPage = QWidget()
        self.AIPage.setObjectName(u"AIPage")
        self.AIPageWidget = QWidget(self.AIPage)
        self.AIPageWidget.setObjectName(u"AIPageWidget")
        self.AIPageWidget.setGeometry(QRect(0, 0, 825, 640))
        self.AIPageWidget.setMinimumSize(QSize(825, 640))
        self.AIPageWidget.setMaximumSize(QSize(825, 640))
        self.AIPageWidget.setAutoFillBackground(False)
        self.AIPageWidget.setStyleSheet(u"")
        self.AIPageWidget_Layout = QGridLayout(self.AIPageWidget)
        self.AIPageWidget_Layout.setSpacing(5)
        self.AIPageWidget_Layout.setObjectName(u"AIPageWidget_Layout")
        self.AIPageWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.FinalGradeCalculatorButton = QPushButton(self.AIPageWidget)
        self.FinalGradeCalculatorButton.setObjectName(u"FinalGradeCalculatorButton")
        self.FinalGradeCalculatorButton.setMinimumSize(QSize(270, 50))
        self.FinalGradeCalculatorButton.setMaximumSize(QSize(270, 50))
        font5 = QFont()
        font5.setFamilies([u"Calibri"])
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.FinalGradeCalculatorButton.setFont(font5)
        self.FinalGradeCalculatorButton.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(\n"
"		x1:0, x2:1, y1:0, y2:1\n"
"		stop:0 rgb(27, 49, 96),\n"
"		stop:1 \"black\"\n"
"	);\n"
"	color: \"white\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(\n"
"		x1:0, x2:1, y1:0, y2:1\n"
"		stop:0 rgb(40, 73, 143),\n"
"		stop:1 \"black\"\n"
"	);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: qlineargradient(\n"
"		x1:0, x2:1, y1:0, y2:1\n"
"		stop:0 rgb(40, 73, 143),\n"
"		stop:1 \"black\"\n"
"	);\n"
"}")
        self.FinalGradeCalculatorButton.setCheckable(True)
        self.FinalGradeCalculatorButton.setChecked(False)

        self.AIPageWidget_Layout.addWidget(self.FinalGradeCalculatorButton, 0, 0, 1, 1)

        self.WhatToRegesterButton = QPushButton(self.AIPageWidget)
        self.WhatToRegesterButton.setObjectName(u"WhatToRegesterButton")
        self.WhatToRegesterButton.setMinimumSize(QSize(275, 50))
        self.WhatToRegesterButton.setMaximumSize(QSize(275, 50))
        self.WhatToRegesterButton.setFont(font5)
        self.WhatToRegesterButton.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(\n"
"		x1:0, x2:1, y1:0, y2:1\n"
"		stop:0 rgb(27, 49, 96),\n"
"		stop:1 \"black\"\n"
"	);\n"
"	color: \"white\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(\n"
"		x1:0, x2:1, y1:0, y2:1\n"
"		stop:0 rgb(40, 73, 143),\n"
"		stop:1 \"black\"\n"
"	);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: qlineargradient(\n"
"		x1:0, x2:1, y1:0, y2:1\n"
"		stop:0 rgb(40, 73, 143),\n"
"		stop:1 \"black\"\n"
"	);\n"
"}")
        self.WhatToRegesterButton.setCheckable(True)

        self.AIPageWidget_Layout.addWidget(self.WhatToRegesterButton, 0, 1, 1, 1)

        self.FinalGPAPredictorButton = QPushButton(self.AIPageWidget)
        self.FinalGPAPredictorButton.setObjectName(u"FinalGPAPredictorButton")
        self.FinalGPAPredictorButton.setMinimumSize(QSize(270, 50))
        self.FinalGPAPredictorButton.setMaximumSize(QSize(270, 50))
        self.FinalGPAPredictorButton.setFont(font5)
        self.FinalGPAPredictorButton.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(\n"
"		x1:0, x2:1, y1:0, y2:1\n"
"		stop:0 rgb(27, 49, 96),\n"
"		stop:1 \"black\"\n"
"	);\n"
"	color: \"white\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(\n"
"		x1:0, x2:1, y1:0, y2:1\n"
"		stop:0 rgb(40, 73, 143),\n"
"		stop:1 \"black\"\n"
"	);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: qlineargradient(\n"
"		x1:0, x2:1, y1:0, y2:1\n"
"		stop:0 rgb(40, 73, 143),\n"
"		stop:1 \"black\"\n"
"	);\n"
"}")
        self.FinalGPAPredictorButton.setCheckable(True)

        self.AIPageWidget_Layout.addWidget(self.FinalGPAPredictorButton, 0, 2, 1, 1)

        self.AIPageStackedWidget = QStackedWidget(self.AIPageWidget)
        self.AIPageStackedWidget.setObjectName(u"AIPageStackedWidget")
        self.AIPageStackedWidget.setMinimumSize(QSize(825, 585))
        self.AIPageStackedWidget.setMaximumSize(QSize(825, 585))
        self.FinalGradeCalculatorPage = QWidget()
        self.FinalGradeCalculatorPage.setObjectName(u"FinalGradeCalculatorPage")
        self.FinalGradeCalculatorPage.setStyleSheet(u"border-radius: 10px;\n"
"background-color: \"white\";")
        self.FinalGradeCalculatorPage_Layout = QVBoxLayout(self.FinalGradeCalculatorPage)
        self.FinalGradeCalculatorPage_Layout.setSpacing(5)
        self.FinalGradeCalculatorPage_Layout.setObjectName(u"FinalGradeCalculatorPage_Layout")
        self.FinalGradeCalculatorPage_Layout.setContentsMargins(10, 5, 10, 5)
        self.FinalGradeCalculatorInputWidget = QWidget(self.FinalGradeCalculatorPage)
        self.FinalGradeCalculatorInputWidget.setObjectName(u"FinalGradeCalculatorInputWidget")
        self.FinalGradeCalculatorInputWidget.setMinimumSize(QSize(805, 295))
        self.FinalGradeCalculatorInputWidget.setMaximumSize(QSize(805, 295))
        self.FinalGradeCalculatorInputWidget.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(27, 49, 96),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.FinalGradeCalculatorInputWidget_Layout = QVBoxLayout(self.FinalGradeCalculatorInputWidget)
        self.FinalGradeCalculatorInputWidget_Layout.setSpacing(5)
        self.FinalGradeCalculatorInputWidget_Layout.setObjectName(u"FinalGradeCalculatorInputWidget_Layout")
        self.FinalGradeCalculatorInputWidget_Layout.setContentsMargins(10, 10, 10, 10)
        self.CourseIDBoxLabel = QLabel(self.FinalGradeCalculatorInputWidget)
        self.CourseIDBoxLabel.setObjectName(u"CourseIDBoxLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.CourseIDBoxLabel.sizePolicy().hasHeightForWidth())
        self.CourseIDBoxLabel.setSizePolicy(sizePolicy2)
        self.CourseIDBoxLabel.setMinimumSize(QSize(785, 25))
        self.CourseIDBoxLabel.setMaximumSize(QSize(785, 25))
        font6 = QFont()
        font6.setFamilies([u"Calibri"])
        font6.setPointSize(15)
        font6.setBold(True)
        font6.setKerning(True)
        font6.setStyleStrategy(QFont.PreferAntialias)
        self.CourseIDBoxLabel.setFont(font6)
        self.CourseIDBoxLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CourseIDBoxLabel.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.FinalGradeCalculatorInputWidget_Layout.addWidget(self.CourseIDBoxLabel)

        self.CourseIDBox = QLineEdit(self.FinalGradeCalculatorInputWidget)
        self.CourseIDBox.setObjectName(u"CourseIDBox")
        self.CourseIDBox.setMinimumSize(QSize(785, 50))
        self.CourseIDBox.setMaximumSize(QSize(785, 50))
        font7 = QFont()
        font7.setFamilies([u"calibri"])
        font7.setPointSize(16)
        self.CourseIDBox.setFont(font7)
        self.CourseIDBox.setStyleSheet(u"background-color: \"white\";\n"
"border-radius: 5px;\n"
"color: \"black\";\n"
"padding-left: 10px;\n"
"font-size: 16pt;\n"
"font-family: calibri;")
        self.CourseIDBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.FinalGradeCalculatorInputWidget_Layout.addWidget(self.CourseIDBox, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.CourseIDErrorWidget = QWidget(self.FinalGradeCalculatorInputWidget)
        self.CourseIDErrorWidget.setObjectName(u"CourseIDErrorWidget")
        self.CourseIDErrorWidget.setStyleSheet(u"background-color: none;")
        self.CourseIDErrorWidget_Layout = QHBoxLayout(self.CourseIDErrorWidget)
        self.CourseIDErrorWidget_Layout.setSpacing(5)
        self.CourseIDErrorWidget_Layout.setObjectName(u"CourseIDErrorWidget_Layout")
        self.CourseIDErrorWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.CourseIDErrorLabel = QLabel(self.CourseIDErrorWidget)
        self.CourseIDErrorLabel.setObjectName(u"CourseIDErrorLabel")
        sizePolicy2.setHeightForWidth(self.CourseIDErrorLabel.sizePolicy().hasHeightForWidth())
        self.CourseIDErrorLabel.setSizePolicy(sizePolicy2)
        self.CourseIDErrorLabel.setMinimumSize(QSize(0, 25))
        self.CourseIDErrorLabel.setMaximumSize(QSize(16777215, 25))
        self.CourseIDErrorLabel.setFont(font6)
        self.CourseIDErrorLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CourseIDErrorLabel.setStyleSheet(u"background-color: none;\n"
"padding-left: 10px;")

        self.CourseIDErrorWidget_Layout.addWidget(self.CourseIDErrorLabel)

        self.CourseIDErrorWidgetSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CourseIDErrorWidget_Layout.addItem(self.CourseIDErrorWidgetSpacer)


        self.FinalGradeCalculatorInputWidget_Layout.addWidget(self.CourseIDErrorWidget)

        self.CourseWork_Attendance_Layout = QHBoxLayout()
        self.CourseWork_Attendance_Layout.setSpacing(5)
        self.CourseWork_Attendance_Layout.setObjectName(u"CourseWork_Attendance_Layout")
        self.CourseWork_Layout = QVBoxLayout()
        self.CourseWork_Layout.setSpacing(5)
        self.CourseWork_Layout.setObjectName(u"CourseWork_Layout")
        self.CourseWorkBoxLabel = QLabel(self.FinalGradeCalculatorInputWidget)
        self.CourseWorkBoxLabel.setObjectName(u"CourseWorkBoxLabel")
        sizePolicy2.setHeightForWidth(self.CourseWorkBoxLabel.sizePolicy().hasHeightForWidth())
        self.CourseWorkBoxLabel.setSizePolicy(sizePolicy2)
        self.CourseWorkBoxLabel.setMinimumSize(QSize(390, 25))
        self.CourseWorkBoxLabel.setMaximumSize(QSize(390, 25))
        self.CourseWorkBoxLabel.setFont(font6)
        self.CourseWorkBoxLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CourseWorkBoxLabel.setStyleSheet(u"background-color: none;")

        self.CourseWork_Layout.addWidget(self.CourseWorkBoxLabel)

        self.CourseWorkBox = QLineEdit(self.FinalGradeCalculatorInputWidget)
        self.CourseWorkBox.setObjectName(u"CourseWorkBox")
        self.CourseWorkBox.setMinimumSize(QSize(390, 50))
        self.CourseWorkBox.setMaximumSize(QSize(390, 50))
        font8 = QFont()
        font8.setFamilies([u"calibri"])
        font8.setPointSize(16)
        font8.setBold(False)
        font8.setStyleStrategy(QFont.PreferAntialias)
        self.CourseWorkBox.setFont(font8)
        self.CourseWorkBox.setStyleSheet(u"background-color: \"white\";\n"
"border-radius: 5px;\n"
"color: \"black\";\n"
"padding-left: 10px;\n"
"font-size: 16pt;\n"
"font-family: calibri;")
        self.CourseWorkBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.CourseWork_Layout.addWidget(self.CourseWorkBox, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.CourseWorkErrorWidget = QWidget(self.FinalGradeCalculatorInputWidget)
        self.CourseWorkErrorWidget.setObjectName(u"CourseWorkErrorWidget")
        self.CourseWorkErrorWidget.setStyleSheet(u"background-color: none;")
        self.CourseWorkErrorWidget_Layout = QHBoxLayout(self.CourseWorkErrorWidget)
        self.CourseWorkErrorWidget_Layout.setSpacing(5)
        self.CourseWorkErrorWidget_Layout.setObjectName(u"CourseWorkErrorWidget_Layout")
        self.CourseWorkErrorWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.CourseWorkErrorLabel = QLabel(self.CourseWorkErrorWidget)
        self.CourseWorkErrorLabel.setObjectName(u"CourseWorkErrorLabel")
        sizePolicy1.setHeightForWidth(self.CourseWorkErrorLabel.sizePolicy().hasHeightForWidth())
        self.CourseWorkErrorLabel.setSizePolicy(sizePolicy1)
        self.CourseWorkErrorLabel.setMinimumSize(QSize(0, 25))
        self.CourseWorkErrorLabel.setMaximumSize(QSize(16777215, 25))
        self.CourseWorkErrorLabel.setFont(font6)
        self.CourseWorkErrorLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CourseWorkErrorLabel.setStyleSheet(u"background-color: none;\n"
"padding-left: 10px;")

        self.CourseWorkErrorWidget_Layout.addWidget(self.CourseWorkErrorLabel)

        self.CourseWorkErrorValueLabel = QLabel(self.CourseWorkErrorWidget)
        self.CourseWorkErrorValueLabel.setObjectName(u"CourseWorkErrorValueLabel")
        sizePolicy1.setHeightForWidth(self.CourseWorkErrorValueLabel.sizePolicy().hasHeightForWidth())
        self.CourseWorkErrorValueLabel.setSizePolicy(sizePolicy1)
        self.CourseWorkErrorValueLabel.setMinimumSize(QSize(0, 25))
        self.CourseWorkErrorValueLabel.setMaximumSize(QSize(16777215, 25))
        self.CourseWorkErrorValueLabel.setFont(font6)
        self.CourseWorkErrorValueLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CourseWorkErrorValueLabel.setStyleSheet(u"background-color: none;")

        self.CourseWorkErrorWidget_Layout.addWidget(self.CourseWorkErrorValueLabel)

        self.CourseWorkErrorWidgetSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CourseWorkErrorWidget_Layout.addItem(self.CourseWorkErrorWidgetSpacer)


        self.CourseWork_Layout.addWidget(self.CourseWorkErrorWidget)

        self.CourseWork_LayoutSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.CourseWork_Layout.addItem(self.CourseWork_LayoutSpacer)


        self.CourseWork_Attendance_Layout.addLayout(self.CourseWork_Layout)

        self.Attendance_Layout = QVBoxLayout()
        self.Attendance_Layout.setSpacing(5)
        self.Attendance_Layout.setObjectName(u"Attendance_Layout")
        self.AttendanceBoxLabel = QLabel(self.FinalGradeCalculatorInputWidget)
        self.AttendanceBoxLabel.setObjectName(u"AttendanceBoxLabel")
        sizePolicy2.setHeightForWidth(self.AttendanceBoxLabel.sizePolicy().hasHeightForWidth())
        self.AttendanceBoxLabel.setSizePolicy(sizePolicy2)
        self.AttendanceBoxLabel.setMinimumSize(QSize(390, 25))
        self.AttendanceBoxLabel.setMaximumSize(QSize(390, 25))
        self.AttendanceBoxLabel.setFont(font6)
        self.AttendanceBoxLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.AttendanceBoxLabel.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Attendance_Layout.addWidget(self.AttendanceBoxLabel)

        self.AttendanceBox = QLineEdit(self.FinalGradeCalculatorInputWidget)
        self.AttendanceBox.setObjectName(u"AttendanceBox")
        self.AttendanceBox.setMinimumSize(QSize(390, 50))
        self.AttendanceBox.setMaximumSize(QSize(390, 50))
        self.AttendanceBox.setFont(font8)
        self.AttendanceBox.setStyleSheet(u"background-color: \"white\";\n"
"border-radius: 5px;\n"
"color: \"black\";\n"
"padding-left: 10px;\n"
"font-size: 16pt;\n"
"font-family: calibri;")
        self.AttendanceBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.Attendance_Layout.addWidget(self.AttendanceBox, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.AttendanceErrorWidget = QWidget(self.FinalGradeCalculatorInputWidget)
        self.AttendanceErrorWidget.setObjectName(u"AttendanceErrorWidget")
        self.AttendanceErrorWidget.setStyleSheet(u"background-color: none;")
        self.CourseWorkErrorWidget_Layout_2 = QHBoxLayout(self.AttendanceErrorWidget)
        self.CourseWorkErrorWidget_Layout_2.setSpacing(5)
        self.CourseWorkErrorWidget_Layout_2.setObjectName(u"CourseWorkErrorWidget_Layout_2")
        self.CourseWorkErrorWidget_Layout_2.setContentsMargins(0, 0, 0, 0)
        self.AttendanceErrorLabel = QLabel(self.AttendanceErrorWidget)
        self.AttendanceErrorLabel.setObjectName(u"AttendanceErrorLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.AttendanceErrorLabel.sizePolicy().hasHeightForWidth())
        self.AttendanceErrorLabel.setSizePolicy(sizePolicy3)
        self.AttendanceErrorLabel.setMinimumSize(QSize(0, 25))
        self.AttendanceErrorLabel.setMaximumSize(QSize(11111111, 25))
        self.AttendanceErrorLabel.setFont(font6)
        self.AttendanceErrorLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.AttendanceErrorLabel.setStyleSheet(u"background-color: none;\n"
"padding-left: 10px;")

        self.CourseWorkErrorWidget_Layout_2.addWidget(self.AttendanceErrorLabel)


        self.Attendance_Layout.addWidget(self.AttendanceErrorWidget)

        self.Attendance_LayoutSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.Attendance_Layout.addItem(self.Attendance_LayoutSpacer_2)


        self.CourseWork_Attendance_Layout.addLayout(self.Attendance_Layout)


        self.FinalGradeCalculatorInputWidget_Layout.addLayout(self.CourseWork_Attendance_Layout)

        self.FinalGradeCalculatorInputWidgetSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.FinalGradeCalculatorInputWidget_Layout.addItem(self.FinalGradeCalculatorInputWidgetSpacer)

        self.FinalGradeCalculateButton = QPushButton(self.FinalGradeCalculatorInputWidget)
        self.FinalGradeCalculateButton.setObjectName(u"FinalGradeCalculateButton")
        self.FinalGradeCalculateButton.setEnabled(True)
        sizePolicy.setHeightForWidth(self.FinalGradeCalculateButton.sizePolicy().hasHeightForWidth())
        self.FinalGradeCalculateButton.setSizePolicy(sizePolicy)
        self.FinalGradeCalculateButton.setMinimumSize(QSize(785, 40))
        self.FinalGradeCalculateButton.setMaximumSize(QSize(785, 40))
        font9 = QFont()
        font9.setFamilies([u"Calibri"])
        font9.setPointSize(18)
        font9.setBold(True)
        font9.setStyleStrategy(QFont.PreferAntialias)
        self.FinalGradeCalculateButton.setFont(font9)
        self.FinalGradeCalculateButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(235, 235, 235);\n"
"	border-radius: 5px;\n"
"	color: \"black\";\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: \"white\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: \"white\";\n"
"}")
        self.FinalGradeCalculateButton.setCheckable(True)

        self.FinalGradeCalculatorInputWidget_Layout.addWidget(self.FinalGradeCalculateButton)


        self.FinalGradeCalculatorPage_Layout.addWidget(self.FinalGradeCalculatorInputWidget)

        self.FinalGradeCalculatorOutput_Layout = QGridLayout()
        self.FinalGradeCalculatorOutput_Layout.setSpacing(5)
        self.FinalGradeCalculatorOutput_Layout.setObjectName(u"FinalGradeCalculatorOutput_Layout")
        self.FinalGradeCalculatorOutputWidget_3 = QWidget(self.FinalGradeCalculatorPage)
        self.FinalGradeCalculatorOutputWidget_3.setObjectName(u"FinalGradeCalculatorOutputWidget_3")
        self.FinalGradeCalculatorOutputWidget_3.setMinimumSize(QSize(400, 75))
        self.FinalGradeCalculatorOutputWidget_3.setMaximumSize(QSize(400, 75))
        self.FinalGradeCalculatorOutputWidget_3.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(128, 15, 28),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.FinalGradeCalculatorOutputWidget_Layout_3 = QVBoxLayout(self.FinalGradeCalculatorOutputWidget_3)
        self.FinalGradeCalculatorOutputWidget_Layout_3.setSpacing(5)
        self.FinalGradeCalculatorOutputWidget_Layout_3.setObjectName(u"FinalGradeCalculatorOutputWidget_Layout_3")
        self.FinalGradeCalculatorOutputWidget_Layout_3.setContentsMargins(10, 10, 10, 10)
        self.InputSummary_Layout_3 = QHBoxLayout()
        self.InputSummary_Layout_3.setSpacing(5)
        self.InputSummary_Layout_3.setObjectName(u"InputSummary_Layout_3")
        self.IDLabel_3 = QLabel(self.FinalGradeCalculatorOutputWidget_3)
        self.IDLabel_3.setObjectName(u"IDLabel_3")
        sizePolicy2.setHeightForWidth(self.IDLabel_3.sizePolicy().hasHeightForWidth())
        self.IDLabel_3.setSizePolicy(sizePolicy2)
        self.IDLabel_3.setMinimumSize(QSize(0, 25))
        self.IDLabel_3.setMaximumSize(QSize(16777215, 25))
        self.IDLabel_3.setFont(font6)
        self.IDLabel_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.IDLabel_3.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_3.addWidget(self.IDLabel_3)

        self.IDValueLabel_3 = QLabel(self.FinalGradeCalculatorOutputWidget_3)
        self.IDValueLabel_3.setObjectName(u"IDValueLabel_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.IDValueLabel_3.sizePolicy().hasHeightForWidth())
        self.IDValueLabel_3.setSizePolicy(sizePolicy4)
        self.IDValueLabel_3.setMinimumSize(QSize(83, 25))
        self.IDValueLabel_3.setMaximumSize(QSize(16777215, 25))
        self.IDValueLabel_3.setFont(font6)
        self.IDValueLabel_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.IDValueLabel_3.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_3.addWidget(self.IDValueLabel_3)

        self.InputSummaryFirstSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.InputSummary_Layout_3.addItem(self.InputSummaryFirstSpacer_3)

        self.CourseWorkLabel_3 = QLabel(self.FinalGradeCalculatorOutputWidget_3)
        self.CourseWorkLabel_3.setObjectName(u"CourseWorkLabel_3")
        sizePolicy4.setHeightForWidth(self.CourseWorkLabel_3.sizePolicy().hasHeightForWidth())
        self.CourseWorkLabel_3.setSizePolicy(sizePolicy4)
        self.CourseWorkLabel_3.setMinimumSize(QSize(0, 25))
        self.CourseWorkLabel_3.setMaximumSize(QSize(16777215, 25))
        self.CourseWorkLabel_3.setFont(font6)
        self.CourseWorkLabel_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CourseWorkLabel_3.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_3.addWidget(self.CourseWorkLabel_3)

        self.CourseWorkValueLabel_3 = QLabel(self.FinalGradeCalculatorOutputWidget_3)
        self.CourseWorkValueLabel_3.setObjectName(u"CourseWorkValueLabel_3")
        sizePolicy4.setHeightForWidth(self.CourseWorkValueLabel_3.sizePolicy().hasHeightForWidth())
        self.CourseWorkValueLabel_3.setSizePolicy(sizePolicy4)
        self.CourseWorkValueLabel_3.setMinimumSize(QSize(0, 25))
        self.CourseWorkValueLabel_3.setMaximumSize(QSize(16777215, 25))
        self.CourseWorkValueLabel_3.setFont(font6)
        self.CourseWorkValueLabel_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CourseWorkValueLabel_3.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_3.addWidget(self.CourseWorkValueLabel_3)

        self.InputSummarySecondSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.InputSummary_Layout_3.addItem(self.InputSummarySecondSpacer_3)

        self.AttendanceLabel_3 = QLabel(self.FinalGradeCalculatorOutputWidget_3)
        self.AttendanceLabel_3.setObjectName(u"AttendanceLabel_3")
        sizePolicy4.setHeightForWidth(self.AttendanceLabel_3.sizePolicy().hasHeightForWidth())
        self.AttendanceLabel_3.setSizePolicy(sizePolicy4)
        self.AttendanceLabel_3.setMinimumSize(QSize(0, 25))
        self.AttendanceLabel_3.setMaximumSize(QSize(16777215, 25))
        self.AttendanceLabel_3.setFont(font6)
        self.AttendanceLabel_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.AttendanceLabel_3.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_3.addWidget(self.AttendanceLabel_3)

        self.AttendanceValueLabel_3 = QLabel(self.FinalGradeCalculatorOutputWidget_3)
        self.AttendanceValueLabel_3.setObjectName(u"AttendanceValueLabel_3")
        sizePolicy4.setHeightForWidth(self.AttendanceValueLabel_3.sizePolicy().hasHeightForWidth())
        self.AttendanceValueLabel_3.setSizePolicy(sizePolicy4)
        self.AttendanceValueLabel_3.setMinimumSize(QSize(0, 25))
        self.AttendanceValueLabel_3.setMaximumSize(QSize(16777215, 25))
        self.AttendanceValueLabel_3.setFont(font6)
        self.AttendanceValueLabel_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.AttendanceValueLabel_3.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_3.addWidget(self.AttendanceValueLabel_3)


        self.FinalGradeCalculatorOutputWidget_Layout_3.addLayout(self.InputSummary_Layout_3)

        self.Output_Layout_3 = QHBoxLayout()
        self.Output_Layout_3.setSpacing(5)
        self.Output_Layout_3.setObjectName(u"Output_Layout_3")
        self.MinExpectedFinalGradeLabel_3 = QLabel(self.FinalGradeCalculatorOutputWidget_3)
        self.MinExpectedFinalGradeLabel_3.setObjectName(u"MinExpectedFinalGradeLabel_3")
        sizePolicy4.setHeightForWidth(self.MinExpectedFinalGradeLabel_3.sizePolicy().hasHeightForWidth())
        self.MinExpectedFinalGradeLabel_3.setSizePolicy(sizePolicy4)
        self.MinExpectedFinalGradeLabel_3.setMinimumSize(QSize(0, 25))
        self.MinExpectedFinalGradeLabel_3.setMaximumSize(QSize(16777215, 25))
        self.MinExpectedFinalGradeLabel_3.setFont(font6)
        self.MinExpectedFinalGradeLabel_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MinExpectedFinalGradeLabel_3.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_3.addWidget(self.MinExpectedFinalGradeLabel_3)

        self.MinExpectedFinalGradeValueLabel_3 = QLabel(self.FinalGradeCalculatorOutputWidget_3)
        self.MinExpectedFinalGradeValueLabel_3.setObjectName(u"MinExpectedFinalGradeValueLabel_3")
        sizePolicy4.setHeightForWidth(self.MinExpectedFinalGradeValueLabel_3.sizePolicy().hasHeightForWidth())
        self.MinExpectedFinalGradeValueLabel_3.setSizePolicy(sizePolicy4)
        self.MinExpectedFinalGradeValueLabel_3.setMinimumSize(QSize(0, 25))
        self.MinExpectedFinalGradeValueLabel_3.setMaximumSize(QSize(16777215, 25))
        self.MinExpectedFinalGradeValueLabel_3.setFont(font6)
        self.MinExpectedFinalGradeValueLabel_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MinExpectedFinalGradeValueLabel_3.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_3.addWidget(self.MinExpectedFinalGradeValueLabel_3)

        self.OutputSpacer_3 = QSpacerItem(57, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Output_Layout_3.addItem(self.OutputSpacer_3)

        self.MaxExpectedFinalGradeLabel_3 = QLabel(self.FinalGradeCalculatorOutputWidget_3)
        self.MaxExpectedFinalGradeLabel_3.setObjectName(u"MaxExpectedFinalGradeLabel_3")
        sizePolicy4.setHeightForWidth(self.MaxExpectedFinalGradeLabel_3.sizePolicy().hasHeightForWidth())
        self.MaxExpectedFinalGradeLabel_3.setSizePolicy(sizePolicy4)
        self.MaxExpectedFinalGradeLabel_3.setMinimumSize(QSize(0, 25))
        self.MaxExpectedFinalGradeLabel_3.setMaximumSize(QSize(16777215, 25))
        self.MaxExpectedFinalGradeLabel_3.setFont(font6)
        self.MaxExpectedFinalGradeLabel_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MaxExpectedFinalGradeLabel_3.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_3.addWidget(self.MaxExpectedFinalGradeLabel_3)

        self.MaxExpectedFinalGradeValueLabel_3 = QLabel(self.FinalGradeCalculatorOutputWidget_3)
        self.MaxExpectedFinalGradeValueLabel_3.setObjectName(u"MaxExpectedFinalGradeValueLabel_3")
        sizePolicy4.setHeightForWidth(self.MaxExpectedFinalGradeValueLabel_3.sizePolicy().hasHeightForWidth())
        self.MaxExpectedFinalGradeValueLabel_3.setSizePolicy(sizePolicy4)
        self.MaxExpectedFinalGradeValueLabel_3.setMinimumSize(QSize(0, 25))
        self.MaxExpectedFinalGradeValueLabel_3.setMaximumSize(QSize(16777215, 25))
        self.MaxExpectedFinalGradeValueLabel_3.setFont(font6)
        self.MaxExpectedFinalGradeValueLabel_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MaxExpectedFinalGradeValueLabel_3.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_3.addWidget(self.MaxExpectedFinalGradeValueLabel_3)


        self.FinalGradeCalculatorOutputWidget_Layout_3.addLayout(self.Output_Layout_3)


        self.FinalGradeCalculatorOutput_Layout.addWidget(self.FinalGradeCalculatorOutputWidget_3, 1, 0, 1, 1)

        self.FinalGradeCalculatorOutputWidget_1 = QWidget(self.FinalGradeCalculatorPage)
        self.FinalGradeCalculatorOutputWidget_1.setObjectName(u"FinalGradeCalculatorOutputWidget_1")
        self.FinalGradeCalculatorOutputWidget_1.setMinimumSize(QSize(400, 75))
        self.FinalGradeCalculatorOutputWidget_1.setMaximumSize(QSize(400, 75))
        self.FinalGradeCalculatorOutputWidget_1.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(128, 15, 28),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.FinalGradeCalculatorOutputWidget_Layout_1 = QVBoxLayout(self.FinalGradeCalculatorOutputWidget_1)
        self.FinalGradeCalculatorOutputWidget_Layout_1.setSpacing(5)
        self.FinalGradeCalculatorOutputWidget_Layout_1.setObjectName(u"FinalGradeCalculatorOutputWidget_Layout_1")
        self.FinalGradeCalculatorOutputWidget_Layout_1.setContentsMargins(10, 10, 10, 10)
        self.InputSummary_Layout_1 = QHBoxLayout()
        self.InputSummary_Layout_1.setSpacing(5)
        self.InputSummary_Layout_1.setObjectName(u"InputSummary_Layout_1")
        self.IDLabel_1 = QLabel(self.FinalGradeCalculatorOutputWidget_1)
        self.IDLabel_1.setObjectName(u"IDLabel_1")
        sizePolicy2.setHeightForWidth(self.IDLabel_1.sizePolicy().hasHeightForWidth())
        self.IDLabel_1.setSizePolicy(sizePolicy2)
        self.IDLabel_1.setMinimumSize(QSize(0, 25))
        self.IDLabel_1.setMaximumSize(QSize(16777215, 25))
        self.IDLabel_1.setFont(font6)
        self.IDLabel_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.IDLabel_1.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_1.addWidget(self.IDLabel_1)

        self.IDValueLabel_1 = QLabel(self.FinalGradeCalculatorOutputWidget_1)
        self.IDValueLabel_1.setObjectName(u"IDValueLabel_1")
        sizePolicy4.setHeightForWidth(self.IDValueLabel_1.sizePolicy().hasHeightForWidth())
        self.IDValueLabel_1.setSizePolicy(sizePolicy4)
        self.IDValueLabel_1.setMinimumSize(QSize(83, 25))
        self.IDValueLabel_1.setMaximumSize(QSize(16777215, 25))
        self.IDValueLabel_1.setFont(font6)
        self.IDValueLabel_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.IDValueLabel_1.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_1.addWidget(self.IDValueLabel_1)

        self.InputSummaryFirstSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.InputSummary_Layout_1.addItem(self.InputSummaryFirstSpacer_1)

        self.CourseWorkLabel_1 = QLabel(self.FinalGradeCalculatorOutputWidget_1)
        self.CourseWorkLabel_1.setObjectName(u"CourseWorkLabel_1")
        sizePolicy4.setHeightForWidth(self.CourseWorkLabel_1.sizePolicy().hasHeightForWidth())
        self.CourseWorkLabel_1.setSizePolicy(sizePolicy4)
        self.CourseWorkLabel_1.setMinimumSize(QSize(0, 25))
        self.CourseWorkLabel_1.setMaximumSize(QSize(16777215, 25))
        self.CourseWorkLabel_1.setFont(font6)
        self.CourseWorkLabel_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CourseWorkLabel_1.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_1.addWidget(self.CourseWorkLabel_1)

        self.CourseWorkValueLabel_1 = QLabel(self.FinalGradeCalculatorOutputWidget_1)
        self.CourseWorkValueLabel_1.setObjectName(u"CourseWorkValueLabel_1")
        sizePolicy4.setHeightForWidth(self.CourseWorkValueLabel_1.sizePolicy().hasHeightForWidth())
        self.CourseWorkValueLabel_1.setSizePolicy(sizePolicy4)
        self.CourseWorkValueLabel_1.setMinimumSize(QSize(0, 25))
        self.CourseWorkValueLabel_1.setMaximumSize(QSize(16777215, 25))
        self.CourseWorkValueLabel_1.setFont(font6)
        self.CourseWorkValueLabel_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CourseWorkValueLabel_1.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_1.addWidget(self.CourseWorkValueLabel_1)

        self.InputSummarySecondSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.InputSummary_Layout_1.addItem(self.InputSummarySecondSpacer_1)

        self.AttendanceLabel_1 = QLabel(self.FinalGradeCalculatorOutputWidget_1)
        self.AttendanceLabel_1.setObjectName(u"AttendanceLabel_1")
        sizePolicy4.setHeightForWidth(self.AttendanceLabel_1.sizePolicy().hasHeightForWidth())
        self.AttendanceLabel_1.setSizePolicy(sizePolicy4)
        self.AttendanceLabel_1.setMinimumSize(QSize(0, 25))
        self.AttendanceLabel_1.setMaximumSize(QSize(16777215, 25))
        self.AttendanceLabel_1.setFont(font6)
        self.AttendanceLabel_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.AttendanceLabel_1.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_1.addWidget(self.AttendanceLabel_1)

        self.AttendanceValueLabel_1 = QLabel(self.FinalGradeCalculatorOutputWidget_1)
        self.AttendanceValueLabel_1.setObjectName(u"AttendanceValueLabel_1")
        sizePolicy4.setHeightForWidth(self.AttendanceValueLabel_1.sizePolicy().hasHeightForWidth())
        self.AttendanceValueLabel_1.setSizePolicy(sizePolicy4)
        self.AttendanceValueLabel_1.setMinimumSize(QSize(0, 25))
        self.AttendanceValueLabel_1.setMaximumSize(QSize(16777215, 25))
        self.AttendanceValueLabel_1.setFont(font6)
        self.AttendanceValueLabel_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.AttendanceValueLabel_1.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_1.addWidget(self.AttendanceValueLabel_1)


        self.FinalGradeCalculatorOutputWidget_Layout_1.addLayout(self.InputSummary_Layout_1)

        self.Output_Layout_1 = QHBoxLayout()
        self.Output_Layout_1.setSpacing(5)
        self.Output_Layout_1.setObjectName(u"Output_Layout_1")
        self.MinExpectedFinalGradeLabel_1 = QLabel(self.FinalGradeCalculatorOutputWidget_1)
        self.MinExpectedFinalGradeLabel_1.setObjectName(u"MinExpectedFinalGradeLabel_1")
        sizePolicy4.setHeightForWidth(self.MinExpectedFinalGradeLabel_1.sizePolicy().hasHeightForWidth())
        self.MinExpectedFinalGradeLabel_1.setSizePolicy(sizePolicy4)
        self.MinExpectedFinalGradeLabel_1.setMinimumSize(QSize(0, 25))
        self.MinExpectedFinalGradeLabel_1.setMaximumSize(QSize(16777215, 25))
        self.MinExpectedFinalGradeLabel_1.setFont(font6)
        self.MinExpectedFinalGradeLabel_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MinExpectedFinalGradeLabel_1.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_1.addWidget(self.MinExpectedFinalGradeLabel_1)

        self.MinExpectedFinalGradeValueLabel_1 = QLabel(self.FinalGradeCalculatorOutputWidget_1)
        self.MinExpectedFinalGradeValueLabel_1.setObjectName(u"MinExpectedFinalGradeValueLabel_1")
        sizePolicy4.setHeightForWidth(self.MinExpectedFinalGradeValueLabel_1.sizePolicy().hasHeightForWidth())
        self.MinExpectedFinalGradeValueLabel_1.setSizePolicy(sizePolicy4)
        self.MinExpectedFinalGradeValueLabel_1.setMinimumSize(QSize(0, 25))
        self.MinExpectedFinalGradeValueLabel_1.setMaximumSize(QSize(16777215, 25))
        self.MinExpectedFinalGradeValueLabel_1.setFont(font6)
        self.MinExpectedFinalGradeValueLabel_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MinExpectedFinalGradeValueLabel_1.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_1.addWidget(self.MinExpectedFinalGradeValueLabel_1)

        self.OutputSpacer_1 = QSpacerItem(57, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Output_Layout_1.addItem(self.OutputSpacer_1)

        self.MaxExpectedFinalGradeLabel_1 = QLabel(self.FinalGradeCalculatorOutputWidget_1)
        self.MaxExpectedFinalGradeLabel_1.setObjectName(u"MaxExpectedFinalGradeLabel_1")
        sizePolicy4.setHeightForWidth(self.MaxExpectedFinalGradeLabel_1.sizePolicy().hasHeightForWidth())
        self.MaxExpectedFinalGradeLabel_1.setSizePolicy(sizePolicy4)
        self.MaxExpectedFinalGradeLabel_1.setMinimumSize(QSize(0, 25))
        self.MaxExpectedFinalGradeLabel_1.setMaximumSize(QSize(16777215, 25))
        self.MaxExpectedFinalGradeLabel_1.setFont(font6)
        self.MaxExpectedFinalGradeLabel_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MaxExpectedFinalGradeLabel_1.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_1.addWidget(self.MaxExpectedFinalGradeLabel_1)

        self.MaxExpectedFinalGradeValueLabel_1 = QLabel(self.FinalGradeCalculatorOutputWidget_1)
        self.MaxExpectedFinalGradeValueLabel_1.setObjectName(u"MaxExpectedFinalGradeValueLabel_1")
        sizePolicy4.setHeightForWidth(self.MaxExpectedFinalGradeValueLabel_1.sizePolicy().hasHeightForWidth())
        self.MaxExpectedFinalGradeValueLabel_1.setSizePolicy(sizePolicy4)
        self.MaxExpectedFinalGradeValueLabel_1.setMinimumSize(QSize(0, 25))
        self.MaxExpectedFinalGradeValueLabel_1.setMaximumSize(QSize(16777215, 25))
        self.MaxExpectedFinalGradeValueLabel_1.setFont(font6)
        self.MaxExpectedFinalGradeValueLabel_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MaxExpectedFinalGradeValueLabel_1.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_1.addWidget(self.MaxExpectedFinalGradeValueLabel_1)


        self.FinalGradeCalculatorOutputWidget_Layout_1.addLayout(self.Output_Layout_1)


        self.FinalGradeCalculatorOutput_Layout.addWidget(self.FinalGradeCalculatorOutputWidget_1, 0, 0, 1, 1)

        self.FinalGradeCalculatorOutputWidget_2 = QWidget(self.FinalGradeCalculatorPage)
        self.FinalGradeCalculatorOutputWidget_2.setObjectName(u"FinalGradeCalculatorOutputWidget_2")
        self.FinalGradeCalculatorOutputWidget_2.setMinimumSize(QSize(400, 75))
        self.FinalGradeCalculatorOutputWidget_2.setMaximumSize(QSize(400, 75))
        self.FinalGradeCalculatorOutputWidget_2.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(128, 15, 28),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.FinalGradeCalculatorOutputWidget_Layout_2 = QVBoxLayout(self.FinalGradeCalculatorOutputWidget_2)
        self.FinalGradeCalculatorOutputWidget_Layout_2.setSpacing(5)
        self.FinalGradeCalculatorOutputWidget_Layout_2.setObjectName(u"FinalGradeCalculatorOutputWidget_Layout_2")
        self.FinalGradeCalculatorOutputWidget_Layout_2.setContentsMargins(10, 10, 10, 10)
        self.InputSummary_Layout_2 = QHBoxLayout()
        self.InputSummary_Layout_2.setSpacing(5)
        self.InputSummary_Layout_2.setObjectName(u"InputSummary_Layout_2")
        self.IDLabel_2 = QLabel(self.FinalGradeCalculatorOutputWidget_2)
        self.IDLabel_2.setObjectName(u"IDLabel_2")
        sizePolicy2.setHeightForWidth(self.IDLabel_2.sizePolicy().hasHeightForWidth())
        self.IDLabel_2.setSizePolicy(sizePolicy2)
        self.IDLabel_2.setMinimumSize(QSize(0, 25))
        self.IDLabel_2.setMaximumSize(QSize(16777215, 25))
        self.IDLabel_2.setFont(font6)
        self.IDLabel_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.IDLabel_2.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_2.addWidget(self.IDLabel_2)

        self.IDValueLabel_2 = QLabel(self.FinalGradeCalculatorOutputWidget_2)
        self.IDValueLabel_2.setObjectName(u"IDValueLabel_2")
        sizePolicy4.setHeightForWidth(self.IDValueLabel_2.sizePolicy().hasHeightForWidth())
        self.IDValueLabel_2.setSizePolicy(sizePolicy4)
        self.IDValueLabel_2.setMinimumSize(QSize(83, 25))
        self.IDValueLabel_2.setMaximumSize(QSize(16777215, 25))
        self.IDValueLabel_2.setFont(font6)
        self.IDValueLabel_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.IDValueLabel_2.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_2.addWidget(self.IDValueLabel_2)

        self.InputSummaryFirstSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.InputSummary_Layout_2.addItem(self.InputSummaryFirstSpacer_2)

        self.CourseWorkLabel_2 = QLabel(self.FinalGradeCalculatorOutputWidget_2)
        self.CourseWorkLabel_2.setObjectName(u"CourseWorkLabel_2")
        sizePolicy4.setHeightForWidth(self.CourseWorkLabel_2.sizePolicy().hasHeightForWidth())
        self.CourseWorkLabel_2.setSizePolicy(sizePolicy4)
        self.CourseWorkLabel_2.setMinimumSize(QSize(0, 25))
        self.CourseWorkLabel_2.setMaximumSize(QSize(16777215, 25))
        self.CourseWorkLabel_2.setFont(font6)
        self.CourseWorkLabel_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CourseWorkLabel_2.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_2.addWidget(self.CourseWorkLabel_2)

        self.CourseWorkValueLabel_2 = QLabel(self.FinalGradeCalculatorOutputWidget_2)
        self.CourseWorkValueLabel_2.setObjectName(u"CourseWorkValueLabel_2")
        sizePolicy4.setHeightForWidth(self.CourseWorkValueLabel_2.sizePolicy().hasHeightForWidth())
        self.CourseWorkValueLabel_2.setSizePolicy(sizePolicy4)
        self.CourseWorkValueLabel_2.setMinimumSize(QSize(0, 25))
        self.CourseWorkValueLabel_2.setMaximumSize(QSize(16777215, 25))
        self.CourseWorkValueLabel_2.setFont(font6)
        self.CourseWorkValueLabel_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CourseWorkValueLabel_2.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_2.addWidget(self.CourseWorkValueLabel_2)

        self.InputSummarySecondSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.InputSummary_Layout_2.addItem(self.InputSummarySecondSpacer_2)

        self.AttendanceLabel_2 = QLabel(self.FinalGradeCalculatorOutputWidget_2)
        self.AttendanceLabel_2.setObjectName(u"AttendanceLabel_2")
        sizePolicy4.setHeightForWidth(self.AttendanceLabel_2.sizePolicy().hasHeightForWidth())
        self.AttendanceLabel_2.setSizePolicy(sizePolicy4)
        self.AttendanceLabel_2.setMinimumSize(QSize(0, 25))
        self.AttendanceLabel_2.setMaximumSize(QSize(16777215, 25))
        self.AttendanceLabel_2.setFont(font6)
        self.AttendanceLabel_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.AttendanceLabel_2.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_2.addWidget(self.AttendanceLabel_2)

        self.AttendanceValueLabel_2 = QLabel(self.FinalGradeCalculatorOutputWidget_2)
        self.AttendanceValueLabel_2.setObjectName(u"AttendanceValueLabel_2")
        sizePolicy4.setHeightForWidth(self.AttendanceValueLabel_2.sizePolicy().hasHeightForWidth())
        self.AttendanceValueLabel_2.setSizePolicy(sizePolicy4)
        self.AttendanceValueLabel_2.setMinimumSize(QSize(0, 25))
        self.AttendanceValueLabel_2.setMaximumSize(QSize(16777215, 25))
        self.AttendanceValueLabel_2.setFont(font6)
        self.AttendanceValueLabel_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.AttendanceValueLabel_2.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_2.addWidget(self.AttendanceValueLabel_2)


        self.FinalGradeCalculatorOutputWidget_Layout_2.addLayout(self.InputSummary_Layout_2)

        self.Output_Layout_2 = QHBoxLayout()
        self.Output_Layout_2.setSpacing(5)
        self.Output_Layout_2.setObjectName(u"Output_Layout_2")
        self.MinExpectedFinalGradeLabel_2 = QLabel(self.FinalGradeCalculatorOutputWidget_2)
        self.MinExpectedFinalGradeLabel_2.setObjectName(u"MinExpectedFinalGradeLabel_2")
        sizePolicy4.setHeightForWidth(self.MinExpectedFinalGradeLabel_2.sizePolicy().hasHeightForWidth())
        self.MinExpectedFinalGradeLabel_2.setSizePolicy(sizePolicy4)
        self.MinExpectedFinalGradeLabel_2.setMinimumSize(QSize(0, 25))
        self.MinExpectedFinalGradeLabel_2.setMaximumSize(QSize(16777215, 25))
        self.MinExpectedFinalGradeLabel_2.setFont(font6)
        self.MinExpectedFinalGradeLabel_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MinExpectedFinalGradeLabel_2.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_2.addWidget(self.MinExpectedFinalGradeLabel_2)

        self.MinExpectedFinalGradeValueLabel_2 = QLabel(self.FinalGradeCalculatorOutputWidget_2)
        self.MinExpectedFinalGradeValueLabel_2.setObjectName(u"MinExpectedFinalGradeValueLabel_2")
        sizePolicy4.setHeightForWidth(self.MinExpectedFinalGradeValueLabel_2.sizePolicy().hasHeightForWidth())
        self.MinExpectedFinalGradeValueLabel_2.setSizePolicy(sizePolicy4)
        self.MinExpectedFinalGradeValueLabel_2.setMinimumSize(QSize(0, 25))
        self.MinExpectedFinalGradeValueLabel_2.setMaximumSize(QSize(16777215, 25))
        self.MinExpectedFinalGradeValueLabel_2.setFont(font6)
        self.MinExpectedFinalGradeValueLabel_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MinExpectedFinalGradeValueLabel_2.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_2.addWidget(self.MinExpectedFinalGradeValueLabel_2)

        self.OutputSpacer_2 = QSpacerItem(57, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Output_Layout_2.addItem(self.OutputSpacer_2)

        self.MaxExpectedFinalGradeLabel_2 = QLabel(self.FinalGradeCalculatorOutputWidget_2)
        self.MaxExpectedFinalGradeLabel_2.setObjectName(u"MaxExpectedFinalGradeLabel_2")
        sizePolicy4.setHeightForWidth(self.MaxExpectedFinalGradeLabel_2.sizePolicy().hasHeightForWidth())
        self.MaxExpectedFinalGradeLabel_2.setSizePolicy(sizePolicy4)
        self.MaxExpectedFinalGradeLabel_2.setMinimumSize(QSize(0, 25))
        self.MaxExpectedFinalGradeLabel_2.setMaximumSize(QSize(16777215, 25))
        self.MaxExpectedFinalGradeLabel_2.setFont(font6)
        self.MaxExpectedFinalGradeLabel_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MaxExpectedFinalGradeLabel_2.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_2.addWidget(self.MaxExpectedFinalGradeLabel_2)

        self.MaxExpectedFinalGradeValueLabel_2 = QLabel(self.FinalGradeCalculatorOutputWidget_2)
        self.MaxExpectedFinalGradeValueLabel_2.setObjectName(u"MaxExpectedFinalGradeValueLabel_2")
        sizePolicy4.setHeightForWidth(self.MaxExpectedFinalGradeValueLabel_2.sizePolicy().hasHeightForWidth())
        self.MaxExpectedFinalGradeValueLabel_2.setSizePolicy(sizePolicy4)
        self.MaxExpectedFinalGradeValueLabel_2.setMinimumSize(QSize(0, 25))
        self.MaxExpectedFinalGradeValueLabel_2.setMaximumSize(QSize(16777215, 25))
        self.MaxExpectedFinalGradeValueLabel_2.setFont(font6)
        self.MaxExpectedFinalGradeValueLabel_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MaxExpectedFinalGradeValueLabel_2.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_2.addWidget(self.MaxExpectedFinalGradeValueLabel_2)


        self.FinalGradeCalculatorOutputWidget_Layout_2.addLayout(self.Output_Layout_2)


        self.FinalGradeCalculatorOutput_Layout.addWidget(self.FinalGradeCalculatorOutputWidget_2, 0, 1, 1, 1)

        self.FinalGradeCalculatorOutputWidget_4 = QWidget(self.FinalGradeCalculatorPage)
        self.FinalGradeCalculatorOutputWidget_4.setObjectName(u"FinalGradeCalculatorOutputWidget_4")
        self.FinalGradeCalculatorOutputWidget_4.setMinimumSize(QSize(400, 75))
        self.FinalGradeCalculatorOutputWidget_4.setMaximumSize(QSize(400, 75))
        self.FinalGradeCalculatorOutputWidget_4.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(128, 15, 28),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.FinalGradeCalculatorOutputWidget_Layout_4 = QVBoxLayout(self.FinalGradeCalculatorOutputWidget_4)
        self.FinalGradeCalculatorOutputWidget_Layout_4.setSpacing(5)
        self.FinalGradeCalculatorOutputWidget_Layout_4.setObjectName(u"FinalGradeCalculatorOutputWidget_Layout_4")
        self.FinalGradeCalculatorOutputWidget_Layout_4.setContentsMargins(10, 10, 10, 10)
        self.InputSummary_Layout_4 = QHBoxLayout()
        self.InputSummary_Layout_4.setSpacing(5)
        self.InputSummary_Layout_4.setObjectName(u"InputSummary_Layout_4")
        self.IDLabel_4 = QLabel(self.FinalGradeCalculatorOutputWidget_4)
        self.IDLabel_4.setObjectName(u"IDLabel_4")
        sizePolicy2.setHeightForWidth(self.IDLabel_4.sizePolicy().hasHeightForWidth())
        self.IDLabel_4.setSizePolicy(sizePolicy2)
        self.IDLabel_4.setMinimumSize(QSize(0, 25))
        self.IDLabel_4.setMaximumSize(QSize(16777215, 25))
        self.IDLabel_4.setFont(font6)
        self.IDLabel_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.IDLabel_4.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_4.addWidget(self.IDLabel_4)

        self.IDValueLabel_4 = QLabel(self.FinalGradeCalculatorOutputWidget_4)
        self.IDValueLabel_4.setObjectName(u"IDValueLabel_4")
        sizePolicy4.setHeightForWidth(self.IDValueLabel_4.sizePolicy().hasHeightForWidth())
        self.IDValueLabel_4.setSizePolicy(sizePolicy4)
        self.IDValueLabel_4.setMinimumSize(QSize(83, 25))
        self.IDValueLabel_4.setMaximumSize(QSize(16777215, 25))
        self.IDValueLabel_4.setFont(font6)
        self.IDValueLabel_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.IDValueLabel_4.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_4.addWidget(self.IDValueLabel_4)

        self.InputSummaryFirstSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.InputSummary_Layout_4.addItem(self.InputSummaryFirstSpacer_4)

        self.CourseWorkLabel_4 = QLabel(self.FinalGradeCalculatorOutputWidget_4)
        self.CourseWorkLabel_4.setObjectName(u"CourseWorkLabel_4")
        sizePolicy4.setHeightForWidth(self.CourseWorkLabel_4.sizePolicy().hasHeightForWidth())
        self.CourseWorkLabel_4.setSizePolicy(sizePolicy4)
        self.CourseWorkLabel_4.setMinimumSize(QSize(0, 25))
        self.CourseWorkLabel_4.setMaximumSize(QSize(16777215, 25))
        self.CourseWorkLabel_4.setFont(font6)
        self.CourseWorkLabel_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CourseWorkLabel_4.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_4.addWidget(self.CourseWorkLabel_4)

        self.CourseWorkValueLabel_4 = QLabel(self.FinalGradeCalculatorOutputWidget_4)
        self.CourseWorkValueLabel_4.setObjectName(u"CourseWorkValueLabel_4")
        sizePolicy4.setHeightForWidth(self.CourseWorkValueLabel_4.sizePolicy().hasHeightForWidth())
        self.CourseWorkValueLabel_4.setSizePolicy(sizePolicy4)
        self.CourseWorkValueLabel_4.setMinimumSize(QSize(0, 25))
        self.CourseWorkValueLabel_4.setMaximumSize(QSize(16777215, 25))
        self.CourseWorkValueLabel_4.setFont(font6)
        self.CourseWorkValueLabel_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CourseWorkValueLabel_4.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_4.addWidget(self.CourseWorkValueLabel_4)

        self.InputSummarySecondSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.InputSummary_Layout_4.addItem(self.InputSummarySecondSpacer_4)

        self.AttendanceLabel_4 = QLabel(self.FinalGradeCalculatorOutputWidget_4)
        self.AttendanceLabel_4.setObjectName(u"AttendanceLabel_4")
        sizePolicy4.setHeightForWidth(self.AttendanceLabel_4.sizePolicy().hasHeightForWidth())
        self.AttendanceLabel_4.setSizePolicy(sizePolicy4)
        self.AttendanceLabel_4.setMinimumSize(QSize(0, 25))
        self.AttendanceLabel_4.setMaximumSize(QSize(16777215, 25))
        self.AttendanceLabel_4.setFont(font6)
        self.AttendanceLabel_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.AttendanceLabel_4.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_4.addWidget(self.AttendanceLabel_4)

        self.AttendanceValueLabel_4 = QLabel(self.FinalGradeCalculatorOutputWidget_4)
        self.AttendanceValueLabel_4.setObjectName(u"AttendanceValueLabel_4")
        sizePolicy4.setHeightForWidth(self.AttendanceValueLabel_4.sizePolicy().hasHeightForWidth())
        self.AttendanceValueLabel_4.setSizePolicy(sizePolicy4)
        self.AttendanceValueLabel_4.setMinimumSize(QSize(0, 25))
        self.AttendanceValueLabel_4.setMaximumSize(QSize(16777215, 25))
        self.AttendanceValueLabel_4.setFont(font6)
        self.AttendanceValueLabel_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.AttendanceValueLabel_4.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_4.addWidget(self.AttendanceValueLabel_4)


        self.FinalGradeCalculatorOutputWidget_Layout_4.addLayout(self.InputSummary_Layout_4)

        self.Output_Layout_4 = QHBoxLayout()
        self.Output_Layout_4.setSpacing(5)
        self.Output_Layout_4.setObjectName(u"Output_Layout_4")
        self.MinExpectedFinalGradeLabel_4 = QLabel(self.FinalGradeCalculatorOutputWidget_4)
        self.MinExpectedFinalGradeLabel_4.setObjectName(u"MinExpectedFinalGradeLabel_4")
        sizePolicy4.setHeightForWidth(self.MinExpectedFinalGradeLabel_4.sizePolicy().hasHeightForWidth())
        self.MinExpectedFinalGradeLabel_4.setSizePolicy(sizePolicy4)
        self.MinExpectedFinalGradeLabel_4.setMinimumSize(QSize(0, 25))
        self.MinExpectedFinalGradeLabel_4.setMaximumSize(QSize(16777215, 25))
        self.MinExpectedFinalGradeLabel_4.setFont(font6)
        self.MinExpectedFinalGradeLabel_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MinExpectedFinalGradeLabel_4.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_4.addWidget(self.MinExpectedFinalGradeLabel_4)

        self.MinExpectedFinalGradeValueLabel_4 = QLabel(self.FinalGradeCalculatorOutputWidget_4)
        self.MinExpectedFinalGradeValueLabel_4.setObjectName(u"MinExpectedFinalGradeValueLabel_4")
        sizePolicy4.setHeightForWidth(self.MinExpectedFinalGradeValueLabel_4.sizePolicy().hasHeightForWidth())
        self.MinExpectedFinalGradeValueLabel_4.setSizePolicy(sizePolicy4)
        self.MinExpectedFinalGradeValueLabel_4.setMinimumSize(QSize(0, 25))
        self.MinExpectedFinalGradeValueLabel_4.setMaximumSize(QSize(16777215, 25))
        self.MinExpectedFinalGradeValueLabel_4.setFont(font6)
        self.MinExpectedFinalGradeValueLabel_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MinExpectedFinalGradeValueLabel_4.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_4.addWidget(self.MinExpectedFinalGradeValueLabel_4)

        self.OutputSpacer_4 = QSpacerItem(57, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Output_Layout_4.addItem(self.OutputSpacer_4)

        self.MaxExpectedFinalGradeLabel_4 = QLabel(self.FinalGradeCalculatorOutputWidget_4)
        self.MaxExpectedFinalGradeLabel_4.setObjectName(u"MaxExpectedFinalGradeLabel_4")
        sizePolicy4.setHeightForWidth(self.MaxExpectedFinalGradeLabel_4.sizePolicy().hasHeightForWidth())
        self.MaxExpectedFinalGradeLabel_4.setSizePolicy(sizePolicy4)
        self.MaxExpectedFinalGradeLabel_4.setMinimumSize(QSize(0, 25))
        self.MaxExpectedFinalGradeLabel_4.setMaximumSize(QSize(16777215, 25))
        self.MaxExpectedFinalGradeLabel_4.setFont(font6)
        self.MaxExpectedFinalGradeLabel_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MaxExpectedFinalGradeLabel_4.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_4.addWidget(self.MaxExpectedFinalGradeLabel_4)

        self.MaxExpectedFinalGradeValueLabel_4 = QLabel(self.FinalGradeCalculatorOutputWidget_4)
        self.MaxExpectedFinalGradeValueLabel_4.setObjectName(u"MaxExpectedFinalGradeValueLabel_4")
        sizePolicy4.setHeightForWidth(self.MaxExpectedFinalGradeValueLabel_4.sizePolicy().hasHeightForWidth())
        self.MaxExpectedFinalGradeValueLabel_4.setSizePolicy(sizePolicy4)
        self.MaxExpectedFinalGradeValueLabel_4.setMinimumSize(QSize(0, 25))
        self.MaxExpectedFinalGradeValueLabel_4.setMaximumSize(QSize(16777215, 25))
        self.MaxExpectedFinalGradeValueLabel_4.setFont(font6)
        self.MaxExpectedFinalGradeValueLabel_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MaxExpectedFinalGradeValueLabel_4.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_4.addWidget(self.MaxExpectedFinalGradeValueLabel_4)


        self.FinalGradeCalculatorOutputWidget_Layout_4.addLayout(self.Output_Layout_4)


        self.FinalGradeCalculatorOutput_Layout.addWidget(self.FinalGradeCalculatorOutputWidget_4, 1, 1, 1, 1)

        self.FinalGradeCalculatorOutputWidget_5 = QWidget(self.FinalGradeCalculatorPage)
        self.FinalGradeCalculatorOutputWidget_5.setObjectName(u"FinalGradeCalculatorOutputWidget_5")
        self.FinalGradeCalculatorOutputWidget_5.setMinimumSize(QSize(400, 75))
        self.FinalGradeCalculatorOutputWidget_5.setMaximumSize(QSize(400, 75))
        self.FinalGradeCalculatorOutputWidget_5.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(128, 15, 28),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.FinalGradeCalculatorOutputWidget_Layout_5 = QVBoxLayout(self.FinalGradeCalculatorOutputWidget_5)
        self.FinalGradeCalculatorOutputWidget_Layout_5.setSpacing(5)
        self.FinalGradeCalculatorOutputWidget_Layout_5.setObjectName(u"FinalGradeCalculatorOutputWidget_Layout_5")
        self.FinalGradeCalculatorOutputWidget_Layout_5.setContentsMargins(10, 10, 10, 10)
        self.InputSummary_Layout_5 = QHBoxLayout()
        self.InputSummary_Layout_5.setSpacing(5)
        self.InputSummary_Layout_5.setObjectName(u"InputSummary_Layout_5")
        self.IDLabel_5 = QLabel(self.FinalGradeCalculatorOutputWidget_5)
        self.IDLabel_5.setObjectName(u"IDLabel_5")
        sizePolicy2.setHeightForWidth(self.IDLabel_5.sizePolicy().hasHeightForWidth())
        self.IDLabel_5.setSizePolicy(sizePolicy2)
        self.IDLabel_5.setMinimumSize(QSize(0, 25))
        self.IDLabel_5.setMaximumSize(QSize(16777215, 25))
        self.IDLabel_5.setFont(font6)
        self.IDLabel_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.IDLabel_5.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_5.addWidget(self.IDLabel_5)

        self.IDValueLabel_5 = QLabel(self.FinalGradeCalculatorOutputWidget_5)
        self.IDValueLabel_5.setObjectName(u"IDValueLabel_5")
        sizePolicy4.setHeightForWidth(self.IDValueLabel_5.sizePolicy().hasHeightForWidth())
        self.IDValueLabel_5.setSizePolicy(sizePolicy4)
        self.IDValueLabel_5.setMinimumSize(QSize(83, 25))
        self.IDValueLabel_5.setMaximumSize(QSize(16777215, 25))
        self.IDValueLabel_5.setFont(font6)
        self.IDValueLabel_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.IDValueLabel_5.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_5.addWidget(self.IDValueLabel_5)

        self.InputSummaryFirstSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.InputSummary_Layout_5.addItem(self.InputSummaryFirstSpacer_5)

        self.CourseWorkLabel_5 = QLabel(self.FinalGradeCalculatorOutputWidget_5)
        self.CourseWorkLabel_5.setObjectName(u"CourseWorkLabel_5")
        sizePolicy4.setHeightForWidth(self.CourseWorkLabel_5.sizePolicy().hasHeightForWidth())
        self.CourseWorkLabel_5.setSizePolicy(sizePolicy4)
        self.CourseWorkLabel_5.setMinimumSize(QSize(0, 25))
        self.CourseWorkLabel_5.setMaximumSize(QSize(16777215, 25))
        self.CourseWorkLabel_5.setFont(font6)
        self.CourseWorkLabel_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CourseWorkLabel_5.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_5.addWidget(self.CourseWorkLabel_5)

        self.CourseWorkValueLabel_5 = QLabel(self.FinalGradeCalculatorOutputWidget_5)
        self.CourseWorkValueLabel_5.setObjectName(u"CourseWorkValueLabel_5")
        sizePolicy4.setHeightForWidth(self.CourseWorkValueLabel_5.sizePolicy().hasHeightForWidth())
        self.CourseWorkValueLabel_5.setSizePolicy(sizePolicy4)
        self.CourseWorkValueLabel_5.setMinimumSize(QSize(0, 25))
        self.CourseWorkValueLabel_5.setMaximumSize(QSize(16777215, 25))
        self.CourseWorkValueLabel_5.setFont(font6)
        self.CourseWorkValueLabel_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CourseWorkValueLabel_5.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_5.addWidget(self.CourseWorkValueLabel_5)

        self.InputSummarySecondSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.InputSummary_Layout_5.addItem(self.InputSummarySecondSpacer_5)

        self.AttendanceLabel_5 = QLabel(self.FinalGradeCalculatorOutputWidget_5)
        self.AttendanceLabel_5.setObjectName(u"AttendanceLabel_5")
        sizePolicy4.setHeightForWidth(self.AttendanceLabel_5.sizePolicy().hasHeightForWidth())
        self.AttendanceLabel_5.setSizePolicy(sizePolicy4)
        self.AttendanceLabel_5.setMinimumSize(QSize(0, 25))
        self.AttendanceLabel_5.setMaximumSize(QSize(16777215, 25))
        self.AttendanceLabel_5.setFont(font6)
        self.AttendanceLabel_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.AttendanceLabel_5.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_5.addWidget(self.AttendanceLabel_5)

        self.AttendanceValueLabel_5 = QLabel(self.FinalGradeCalculatorOutputWidget_5)
        self.AttendanceValueLabel_5.setObjectName(u"AttendanceValueLabel_5")
        sizePolicy4.setHeightForWidth(self.AttendanceValueLabel_5.sizePolicy().hasHeightForWidth())
        self.AttendanceValueLabel_5.setSizePolicy(sizePolicy4)
        self.AttendanceValueLabel_5.setMinimumSize(QSize(0, 25))
        self.AttendanceValueLabel_5.setMaximumSize(QSize(16777215, 25))
        self.AttendanceValueLabel_5.setFont(font6)
        self.AttendanceValueLabel_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.AttendanceValueLabel_5.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_5.addWidget(self.AttendanceValueLabel_5)


        self.FinalGradeCalculatorOutputWidget_Layout_5.addLayout(self.InputSummary_Layout_5)

        self.Output_Layout_5 = QHBoxLayout()
        self.Output_Layout_5.setSpacing(5)
        self.Output_Layout_5.setObjectName(u"Output_Layout_5")
        self.MinExpectedFinalGradeLabel_5 = QLabel(self.FinalGradeCalculatorOutputWidget_5)
        self.MinExpectedFinalGradeLabel_5.setObjectName(u"MinExpectedFinalGradeLabel_5")
        sizePolicy4.setHeightForWidth(self.MinExpectedFinalGradeLabel_5.sizePolicy().hasHeightForWidth())
        self.MinExpectedFinalGradeLabel_5.setSizePolicy(sizePolicy4)
        self.MinExpectedFinalGradeLabel_5.setMinimumSize(QSize(0, 25))
        self.MinExpectedFinalGradeLabel_5.setMaximumSize(QSize(16777215, 25))
        self.MinExpectedFinalGradeLabel_5.setFont(font6)
        self.MinExpectedFinalGradeLabel_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MinExpectedFinalGradeLabel_5.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_5.addWidget(self.MinExpectedFinalGradeLabel_5)

        self.MinExpectedFinalGradeValueLabel_5 = QLabel(self.FinalGradeCalculatorOutputWidget_5)
        self.MinExpectedFinalGradeValueLabel_5.setObjectName(u"MinExpectedFinalGradeValueLabel_5")
        sizePolicy4.setHeightForWidth(self.MinExpectedFinalGradeValueLabel_5.sizePolicy().hasHeightForWidth())
        self.MinExpectedFinalGradeValueLabel_5.setSizePolicy(sizePolicy4)
        self.MinExpectedFinalGradeValueLabel_5.setMinimumSize(QSize(0, 25))
        self.MinExpectedFinalGradeValueLabel_5.setMaximumSize(QSize(16777215, 25))
        self.MinExpectedFinalGradeValueLabel_5.setFont(font6)
        self.MinExpectedFinalGradeValueLabel_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MinExpectedFinalGradeValueLabel_5.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_5.addWidget(self.MinExpectedFinalGradeValueLabel_5)

        self.OutputSpacer_5 = QSpacerItem(57, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Output_Layout_5.addItem(self.OutputSpacer_5)

        self.MaxExpectedFinalGradeLabel_5 = QLabel(self.FinalGradeCalculatorOutputWidget_5)
        self.MaxExpectedFinalGradeLabel_5.setObjectName(u"MaxExpectedFinalGradeLabel_5")
        sizePolicy4.setHeightForWidth(self.MaxExpectedFinalGradeLabel_5.sizePolicy().hasHeightForWidth())
        self.MaxExpectedFinalGradeLabel_5.setSizePolicy(sizePolicy4)
        self.MaxExpectedFinalGradeLabel_5.setMinimumSize(QSize(0, 25))
        self.MaxExpectedFinalGradeLabel_5.setMaximumSize(QSize(16777215, 25))
        self.MaxExpectedFinalGradeLabel_5.setFont(font6)
        self.MaxExpectedFinalGradeLabel_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MaxExpectedFinalGradeLabel_5.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_5.addWidget(self.MaxExpectedFinalGradeLabel_5)

        self.MaxExpectedFinalGradeValueLabel_5 = QLabel(self.FinalGradeCalculatorOutputWidget_5)
        self.MaxExpectedFinalGradeValueLabel_5.setObjectName(u"MaxExpectedFinalGradeValueLabel_5")
        sizePolicy4.setHeightForWidth(self.MaxExpectedFinalGradeValueLabel_5.sizePolicy().hasHeightForWidth())
        self.MaxExpectedFinalGradeValueLabel_5.setSizePolicy(sizePolicy4)
        self.MaxExpectedFinalGradeValueLabel_5.setMinimumSize(QSize(0, 25))
        self.MaxExpectedFinalGradeValueLabel_5.setMaximumSize(QSize(16777215, 25))
        self.MaxExpectedFinalGradeValueLabel_5.setFont(font6)
        self.MaxExpectedFinalGradeValueLabel_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MaxExpectedFinalGradeValueLabel_5.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_5.addWidget(self.MaxExpectedFinalGradeValueLabel_5)


        self.FinalGradeCalculatorOutputWidget_Layout_5.addLayout(self.Output_Layout_5)


        self.FinalGradeCalculatorOutput_Layout.addWidget(self.FinalGradeCalculatorOutputWidget_5, 2, 0, 1, 1)

        self.FinalGradeCalculatorOutputWidget_6 = QWidget(self.FinalGradeCalculatorPage)
        self.FinalGradeCalculatorOutputWidget_6.setObjectName(u"FinalGradeCalculatorOutputWidget_6")
        self.FinalGradeCalculatorOutputWidget_6.setMinimumSize(QSize(400, 75))
        self.FinalGradeCalculatorOutputWidget_6.setMaximumSize(QSize(400, 75))
        self.FinalGradeCalculatorOutputWidget_6.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(128, 15, 28),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.FinalGradeCalculatorOutputWidget_Layout_6 = QVBoxLayout(self.FinalGradeCalculatorOutputWidget_6)
        self.FinalGradeCalculatorOutputWidget_Layout_6.setSpacing(5)
        self.FinalGradeCalculatorOutputWidget_Layout_6.setObjectName(u"FinalGradeCalculatorOutputWidget_Layout_6")
        self.FinalGradeCalculatorOutputWidget_Layout_6.setContentsMargins(10, 10, 10, 10)
        self.InputSummary_Layout_6 = QHBoxLayout()
        self.InputSummary_Layout_6.setSpacing(5)
        self.InputSummary_Layout_6.setObjectName(u"InputSummary_Layout_6")
        self.IDLabel_6 = QLabel(self.FinalGradeCalculatorOutputWidget_6)
        self.IDLabel_6.setObjectName(u"IDLabel_6")
        sizePolicy2.setHeightForWidth(self.IDLabel_6.sizePolicy().hasHeightForWidth())
        self.IDLabel_6.setSizePolicy(sizePolicy2)
        self.IDLabel_6.setMinimumSize(QSize(0, 25))
        self.IDLabel_6.setMaximumSize(QSize(16777215, 25))
        self.IDLabel_6.setFont(font6)
        self.IDLabel_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.IDLabel_6.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_6.addWidget(self.IDLabel_6)

        self.IDValueLabel_6 = QLabel(self.FinalGradeCalculatorOutputWidget_6)
        self.IDValueLabel_6.setObjectName(u"IDValueLabel_6")
        sizePolicy4.setHeightForWidth(self.IDValueLabel_6.sizePolicy().hasHeightForWidth())
        self.IDValueLabel_6.setSizePolicy(sizePolicy4)
        self.IDValueLabel_6.setMinimumSize(QSize(83, 25))
        self.IDValueLabel_6.setMaximumSize(QSize(16777215, 25))
        self.IDValueLabel_6.setFont(font6)
        self.IDValueLabel_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.IDValueLabel_6.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_6.addWidget(self.IDValueLabel_6)

        self.InputSummaryFirstSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.InputSummary_Layout_6.addItem(self.InputSummaryFirstSpacer_6)

        self.CourseWorkLabel_6 = QLabel(self.FinalGradeCalculatorOutputWidget_6)
        self.CourseWorkLabel_6.setObjectName(u"CourseWorkLabel_6")
        sizePolicy4.setHeightForWidth(self.CourseWorkLabel_6.sizePolicy().hasHeightForWidth())
        self.CourseWorkLabel_6.setSizePolicy(sizePolicy4)
        self.CourseWorkLabel_6.setMinimumSize(QSize(0, 25))
        self.CourseWorkLabel_6.setMaximumSize(QSize(16777215, 25))
        self.CourseWorkLabel_6.setFont(font6)
        self.CourseWorkLabel_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CourseWorkLabel_6.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_6.addWidget(self.CourseWorkLabel_6)

        self.CourseWorkValueLabel_6 = QLabel(self.FinalGradeCalculatorOutputWidget_6)
        self.CourseWorkValueLabel_6.setObjectName(u"CourseWorkValueLabel_6")
        sizePolicy4.setHeightForWidth(self.CourseWorkValueLabel_6.sizePolicy().hasHeightForWidth())
        self.CourseWorkValueLabel_6.setSizePolicy(sizePolicy4)
        self.CourseWorkValueLabel_6.setMinimumSize(QSize(0, 25))
        self.CourseWorkValueLabel_6.setMaximumSize(QSize(16777215, 25))
        self.CourseWorkValueLabel_6.setFont(font6)
        self.CourseWorkValueLabel_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CourseWorkValueLabel_6.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_6.addWidget(self.CourseWorkValueLabel_6)

        self.InputSummarySecondSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.InputSummary_Layout_6.addItem(self.InputSummarySecondSpacer_6)

        self.AttendanceLabel_6 = QLabel(self.FinalGradeCalculatorOutputWidget_6)
        self.AttendanceLabel_6.setObjectName(u"AttendanceLabel_6")
        sizePolicy4.setHeightForWidth(self.AttendanceLabel_6.sizePolicy().hasHeightForWidth())
        self.AttendanceLabel_6.setSizePolicy(sizePolicy4)
        self.AttendanceLabel_6.setMinimumSize(QSize(0, 25))
        self.AttendanceLabel_6.setMaximumSize(QSize(16777215, 25))
        self.AttendanceLabel_6.setFont(font6)
        self.AttendanceLabel_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.AttendanceLabel_6.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_6.addWidget(self.AttendanceLabel_6)

        self.AttendanceValueLabel_6 = QLabel(self.FinalGradeCalculatorOutputWidget_6)
        self.AttendanceValueLabel_6.setObjectName(u"AttendanceValueLabel_6")
        sizePolicy4.setHeightForWidth(self.AttendanceValueLabel_6.sizePolicy().hasHeightForWidth())
        self.AttendanceValueLabel_6.setSizePolicy(sizePolicy4)
        self.AttendanceValueLabel_6.setMinimumSize(QSize(0, 25))
        self.AttendanceValueLabel_6.setMaximumSize(QSize(16777215, 25))
        self.AttendanceValueLabel_6.setFont(font6)
        self.AttendanceValueLabel_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.AttendanceValueLabel_6.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.InputSummary_Layout_6.addWidget(self.AttendanceValueLabel_6)


        self.FinalGradeCalculatorOutputWidget_Layout_6.addLayout(self.InputSummary_Layout_6)

        self.Output_Layout_6 = QHBoxLayout()
        self.Output_Layout_6.setSpacing(5)
        self.Output_Layout_6.setObjectName(u"Output_Layout_6")
        self.MinExpectedFinalGradeLabel_6 = QLabel(self.FinalGradeCalculatorOutputWidget_6)
        self.MinExpectedFinalGradeLabel_6.setObjectName(u"MinExpectedFinalGradeLabel_6")
        sizePolicy4.setHeightForWidth(self.MinExpectedFinalGradeLabel_6.sizePolicy().hasHeightForWidth())
        self.MinExpectedFinalGradeLabel_6.setSizePolicy(sizePolicy4)
        self.MinExpectedFinalGradeLabel_6.setMinimumSize(QSize(0, 25))
        self.MinExpectedFinalGradeLabel_6.setMaximumSize(QSize(16777215, 25))
        self.MinExpectedFinalGradeLabel_6.setFont(font6)
        self.MinExpectedFinalGradeLabel_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MinExpectedFinalGradeLabel_6.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_6.addWidget(self.MinExpectedFinalGradeLabel_6)

        self.MinExpectedFinalGradeValueLabel_6 = QLabel(self.FinalGradeCalculatorOutputWidget_6)
        self.MinExpectedFinalGradeValueLabel_6.setObjectName(u"MinExpectedFinalGradeValueLabel_6")
        sizePolicy4.setHeightForWidth(self.MinExpectedFinalGradeValueLabel_6.sizePolicy().hasHeightForWidth())
        self.MinExpectedFinalGradeValueLabel_6.setSizePolicy(sizePolicy4)
        self.MinExpectedFinalGradeValueLabel_6.setMinimumSize(QSize(0, 25))
        self.MinExpectedFinalGradeValueLabel_6.setMaximumSize(QSize(16777215, 25))
        self.MinExpectedFinalGradeValueLabel_6.setFont(font6)
        self.MinExpectedFinalGradeValueLabel_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MinExpectedFinalGradeValueLabel_6.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_6.addWidget(self.MinExpectedFinalGradeValueLabel_6)

        self.OutputSpacer_6 = QSpacerItem(57, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Output_Layout_6.addItem(self.OutputSpacer_6)

        self.MaxExpectedFinalGradeLabel_6 = QLabel(self.FinalGradeCalculatorOutputWidget_6)
        self.MaxExpectedFinalGradeLabel_6.setObjectName(u"MaxExpectedFinalGradeLabel_6")
        sizePolicy4.setHeightForWidth(self.MaxExpectedFinalGradeLabel_6.sizePolicy().hasHeightForWidth())
        self.MaxExpectedFinalGradeLabel_6.setSizePolicy(sizePolicy4)
        self.MaxExpectedFinalGradeLabel_6.setMinimumSize(QSize(0, 25))
        self.MaxExpectedFinalGradeLabel_6.setMaximumSize(QSize(16777215, 25))
        self.MaxExpectedFinalGradeLabel_6.setFont(font6)
        self.MaxExpectedFinalGradeLabel_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MaxExpectedFinalGradeLabel_6.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_6.addWidget(self.MaxExpectedFinalGradeLabel_6)

        self.MaxExpectedFinalGradeValueLabel_6 = QLabel(self.FinalGradeCalculatorOutputWidget_6)
        self.MaxExpectedFinalGradeValueLabel_6.setObjectName(u"MaxExpectedFinalGradeValueLabel_6")
        sizePolicy4.setHeightForWidth(self.MaxExpectedFinalGradeValueLabel_6.sizePolicy().hasHeightForWidth())
        self.MaxExpectedFinalGradeValueLabel_6.setSizePolicy(sizePolicy4)
        self.MaxExpectedFinalGradeValueLabel_6.setMinimumSize(QSize(0, 25))
        self.MaxExpectedFinalGradeValueLabel_6.setMaximumSize(QSize(16777215, 25))
        self.MaxExpectedFinalGradeValueLabel_6.setFont(font6)
        self.MaxExpectedFinalGradeValueLabel_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MaxExpectedFinalGradeValueLabel_6.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Output_Layout_6.addWidget(self.MaxExpectedFinalGradeValueLabel_6)


        self.FinalGradeCalculatorOutputWidget_Layout_6.addLayout(self.Output_Layout_6)


        self.FinalGradeCalculatorOutput_Layout.addWidget(self.FinalGradeCalculatorOutputWidget_6, 2, 1, 1, 1)


        self.FinalGradeCalculatorPage_Layout.addLayout(self.FinalGradeCalculatorOutput_Layout)

        self.FinalGradeCalculatorPageSpacer = QSpacerItem(20, 45, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.FinalGradeCalculatorPage_Layout.addItem(self.FinalGradeCalculatorPageSpacer)

        self.AIPageStackedWidget.addWidget(self.FinalGradeCalculatorPage)
        self.WhatToRegisterPage = QWidget()
        self.WhatToRegisterPage.setObjectName(u"WhatToRegisterPage")
        self.WhatToRegisterPage.setStyleSheet(u"border-radius: 10px;\n"
"background-color: \"white\";")
        self.WhatToRegesterPage_Layout = QHBoxLayout(self.WhatToRegisterPage)
        self.WhatToRegesterPage_Layout.setSpacing(5)
        self.WhatToRegesterPage_Layout.setObjectName(u"WhatToRegesterPage_Layout")
        self.WhatToRegesterPage_Layout.setContentsMargins(0, 0, 0, 0)
        self.WhatToRegisterPageSummaryWidget = QWidget(self.WhatToRegisterPage)
        self.WhatToRegisterPageSummaryWidget.setObjectName(u"WhatToRegisterPageSummaryWidget")
        self.WhatToRegisterPageSummaryWidget.setMinimumSize(QSize(235, 585))
        self.WhatToRegisterPageSummaryWidget.setMaximumSize(QSize(235, 585))
        self.WhatToRegisterPageSummaryWidget.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(106, 69, 57),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.WhatToRegesterSummaryWidget_Layout = QVBoxLayout(self.WhatToRegisterPageSummaryWidget)
        self.WhatToRegesterSummaryWidget_Layout.setSpacing(5)
        self.WhatToRegesterSummaryWidget_Layout.setObjectName(u"WhatToRegesterSummaryWidget_Layout")
        self.WhatToRegesterSummaryWidget_Layout.setContentsMargins(10, 10, 10, 10)
        self.WhatToRegisterCurrentLevelWidget = QWidget(self.WhatToRegisterPageSummaryWidget)
        self.WhatToRegisterCurrentLevelWidget.setObjectName(u"WhatToRegisterCurrentLevelWidget")
        self.WhatToRegisterCurrentLevelWidget.setMinimumSize(QSize(215, 25))
        self.WhatToRegisterCurrentLevelWidget.setMaximumSize(QSize(215, 25))
        self.WhatToRegisterCurrentLevelWidget.setStyleSheet(u"background-color: none;")
        self.WhatToRegisterCurrentLevelWidget_Layout = QHBoxLayout(self.WhatToRegisterCurrentLevelWidget)
        self.WhatToRegisterCurrentLevelWidget_Layout.setSpacing(5)
        self.WhatToRegisterCurrentLevelWidget_Layout.setObjectName(u"WhatToRegisterCurrentLevelWidget_Layout")
        self.WhatToRegisterCurrentLevelWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.WhatToRegisterCurrentLevelLabel = QLabel(self.WhatToRegisterCurrentLevelWidget)
        self.WhatToRegisterCurrentLevelLabel.setObjectName(u"WhatToRegisterCurrentLevelLabel")
        sizePolicy2.setHeightForWidth(self.WhatToRegisterCurrentLevelLabel.sizePolicy().hasHeightForWidth())
        self.WhatToRegisterCurrentLevelLabel.setSizePolicy(sizePolicy2)
        self.WhatToRegisterCurrentLevelLabel.setMinimumSize(QSize(0, 25))
        self.WhatToRegisterCurrentLevelLabel.setMaximumSize(QSize(16777215, 25))
        self.WhatToRegisterCurrentLevelLabel.setFont(font6)
        self.WhatToRegisterCurrentLevelLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.WhatToRegisterCurrentLevelLabel.setStyleSheet(u"background-color: none;")

        self.WhatToRegisterCurrentLevelWidget_Layout.addWidget(self.WhatToRegisterCurrentLevelLabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.WhatToRegisterCurrentLevelValueLabel = QLabel(self.WhatToRegisterCurrentLevelWidget)
        self.WhatToRegisterCurrentLevelValueLabel.setObjectName(u"WhatToRegisterCurrentLevelValueLabel")
        sizePolicy1.setHeightForWidth(self.WhatToRegisterCurrentLevelValueLabel.sizePolicy().hasHeightForWidth())
        self.WhatToRegisterCurrentLevelValueLabel.setSizePolicy(sizePolicy1)
        self.WhatToRegisterCurrentLevelValueLabel.setMinimumSize(QSize(0, 25))
        self.WhatToRegisterCurrentLevelValueLabel.setMaximumSize(QSize(16777215, 25))
        self.WhatToRegisterCurrentLevelValueLabel.setFont(font6)
        self.WhatToRegisterCurrentLevelValueLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.WhatToRegisterCurrentLevelValueLabel.setStyleSheet(u"background-color: none;")

        self.WhatToRegisterCurrentLevelWidget_Layout.addWidget(self.WhatToRegisterCurrentLevelValueLabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.WhatToRegisterCurrentLevelWidgetSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.WhatToRegisterCurrentLevelWidget_Layout.addItem(self.WhatToRegisterCurrentLevelWidgetSpacer)


        self.WhatToRegesterSummaryWidget_Layout.addWidget(self.WhatToRegisterCurrentLevelWidget)

        self.AvailableHoursWidget = QWidget(self.WhatToRegisterPageSummaryWidget)
        self.AvailableHoursWidget.setObjectName(u"AvailableHoursWidget")
        self.AvailableHoursWidget.setMinimumSize(QSize(215, 25))
        self.AvailableHoursWidget.setMaximumSize(QSize(215, 25))
        self.AvailableHoursWidget.setStyleSheet(u"background-color: none;")
        self.AvailableHoursWidget_Layout = QHBoxLayout(self.AvailableHoursWidget)
        self.AvailableHoursWidget_Layout.setSpacing(5)
        self.AvailableHoursWidget_Layout.setObjectName(u"AvailableHoursWidget_Layout")
        self.AvailableHoursWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.AvailableHoursLabel = QLabel(self.AvailableHoursWidget)
        self.AvailableHoursLabel.setObjectName(u"AvailableHoursLabel")
        sizePolicy2.setHeightForWidth(self.AvailableHoursLabel.sizePolicy().hasHeightForWidth())
        self.AvailableHoursLabel.setSizePolicy(sizePolicy2)
        self.AvailableHoursLabel.setMinimumSize(QSize(0, 25))
        self.AvailableHoursLabel.setMaximumSize(QSize(16777215, 25))
        self.AvailableHoursLabel.setFont(font6)
        self.AvailableHoursLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.AvailableHoursLabel.setStyleSheet(u"background-color: none;")

        self.AvailableHoursWidget_Layout.addWidget(self.AvailableHoursLabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.AvailableHoursValueLabel = QLabel(self.AvailableHoursWidget)
        self.AvailableHoursValueLabel.setObjectName(u"AvailableHoursValueLabel")
        sizePolicy1.setHeightForWidth(self.AvailableHoursValueLabel.sizePolicy().hasHeightForWidth())
        self.AvailableHoursValueLabel.setSizePolicy(sizePolicy1)
        self.AvailableHoursValueLabel.setMinimumSize(QSize(0, 25))
        self.AvailableHoursValueLabel.setMaximumSize(QSize(16777215, 25))
        self.AvailableHoursValueLabel.setFont(font6)
        self.AvailableHoursValueLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.AvailableHoursValueLabel.setStyleSheet(u"background-color: none;")

        self.AvailableHoursWidget_Layout.addWidget(self.AvailableHoursValueLabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.AvailableHoursWidgetSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.AvailableHoursWidget_Layout.addItem(self.AvailableHoursWidgetSpacer)


        self.WhatToRegesterSummaryWidget_Layout.addWidget(self.AvailableHoursWidget)

        self.CoursesToRegisterWidget = QWidget(self.WhatToRegisterPageSummaryWidget)
        self.CoursesToRegisterWidget.setObjectName(u"CoursesToRegisterWidget")
        self.CoursesToRegisterWidget.setMinimumSize(QSize(215, 25))
        self.CoursesToRegisterWidget.setMaximumSize(QSize(215, 25))
        self.CoursesToRegisterWidget.setStyleSheet(u"background-color: none;")
        self.CoursesToRegisterWidget_Layout = QHBoxLayout(self.CoursesToRegisterWidget)
        self.CoursesToRegisterWidget_Layout.setSpacing(5)
        self.CoursesToRegisterWidget_Layout.setObjectName(u"CoursesToRegisterWidget_Layout")
        self.CoursesToRegisterWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.CoursesToRegisterLabel = QLabel(self.CoursesToRegisterWidget)
        self.CoursesToRegisterLabel.setObjectName(u"CoursesToRegisterLabel")
        sizePolicy2.setHeightForWidth(self.CoursesToRegisterLabel.sizePolicy().hasHeightForWidth())
        self.CoursesToRegisterLabel.setSizePolicy(sizePolicy2)
        self.CoursesToRegisterLabel.setMinimumSize(QSize(0, 25))
        self.CoursesToRegisterLabel.setMaximumSize(QSize(16777215, 25))
        self.CoursesToRegisterLabel.setFont(font6)
        self.CoursesToRegisterLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CoursesToRegisterLabel.setStyleSheet(u"background-color: none;")

        self.CoursesToRegisterWidget_Layout.addWidget(self.CoursesToRegisterLabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.CoursesToRegisterValueLabel = QLabel(self.CoursesToRegisterWidget)
        self.CoursesToRegisterValueLabel.setObjectName(u"CoursesToRegisterValueLabel")
        sizePolicy1.setHeightForWidth(self.CoursesToRegisterValueLabel.sizePolicy().hasHeightForWidth())
        self.CoursesToRegisterValueLabel.setSizePolicy(sizePolicy1)
        self.CoursesToRegisterValueLabel.setMinimumSize(QSize(0, 25))
        self.CoursesToRegisterValueLabel.setMaximumSize(QSize(16777215, 25))
        self.CoursesToRegisterValueLabel.setFont(font6)
        self.CoursesToRegisterValueLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CoursesToRegisterValueLabel.setStyleSheet(u"background-color: none;")

        self.CoursesToRegisterWidget_Layout.addWidget(self.CoursesToRegisterValueLabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.CoursesToRegisterWidgetSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CoursesToRegisterWidget_Layout.addItem(self.CoursesToRegisterWidgetSpacer)


        self.WhatToRegesterSummaryWidget_Layout.addWidget(self.CoursesToRegisterWidget)

        self.WhatToRegisterPageSummaryWidgetSpacer = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.WhatToRegesterSummaryWidget_Layout.addItem(self.WhatToRegisterPageSummaryWidgetSpacer)

        self.RegistrationSummary_Layout = QHBoxLayout()
        self.RegistrationSummary_Layout.setSpacing(5)
        self.RegistrationSummary_Layout.setObjectName(u"RegistrationSummary_Layout")
        self.RegesteredCOMPWidget = QWidget(self.WhatToRegisterPageSummaryWidget)
        self.RegesteredCOMPWidget.setObjectName(u"RegesteredCOMPWidget")
        self.RegesteredCOMPWidget.setMinimumSize(QSize(50, 0))
        self.RegesteredCOMPWidget.setMaximumSize(QSize(50, 16777215))
        self.RegesteredCOMPWidget.setStyleSheet(u"background-color: none;")
        self.RegesteredCOMPWidget_Layout = QVBoxLayout(self.RegesteredCOMPWidget)
        self.RegesteredCOMPWidget_Layout.setSpacing(5)
        self.RegesteredCOMPWidget_Layout.setObjectName(u"RegesteredCOMPWidget_Layout")
        self.RegesteredCOMPWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.RegesteredCOMPValueLabel = QLabel(self.RegesteredCOMPWidget)
        self.RegesteredCOMPValueLabel.setObjectName(u"RegesteredCOMPValueLabel")
        self.RegesteredCOMPValueLabel.setMinimumSize(QSize(50, 25))
        self.RegesteredCOMPValueLabel.setMaximumSize(QSize(50, 25))
        self.RegesteredCOMPValueLabel.setFont(font4)
        self.RegesteredCOMPValueLabel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: \"white\";\n"
"color: \"black\";")

        self.RegesteredCOMPWidget_Layout.addWidget(self.RegesteredCOMPValueLabel)

        self.RegesteredCOMPProgressBar_ActualLayout = QHBoxLayout()
        self.RegesteredCOMPProgressBar_ActualLayout.setSpacing(5)
        self.RegesteredCOMPProgressBar_ActualLayout.setObjectName(u"RegesteredCOMPProgressBar_ActualLayout")
        self.RegesteredCOMPProgressBarLeftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.RegesteredCOMPProgressBar_ActualLayout.addItem(self.RegesteredCOMPProgressBarLeftSpacer)

        self.RegesteredCOMPProgressBar = QWidget(self.RegesteredCOMPWidget)
        self.RegesteredCOMPProgressBar.setObjectName(u"RegesteredCOMPProgressBar")
        self.RegesteredCOMPProgressBar.setMinimumSize(QSize(25, 0))
        self.RegesteredCOMPProgressBar.setMaximumSize(QSize(25, 16777215))
        self.RegesteredCOMPProgressBar_Layout = QHBoxLayout(self.RegesteredCOMPProgressBar)
        self.RegesteredCOMPProgressBar_Layout.setSpacing(0)
        self.RegesteredCOMPProgressBar_Layout.setObjectName(u"RegesteredCOMPProgressBar_Layout")
        self.RegesteredCOMPProgressBar_Layout.setContentsMargins(0, 0, 0, 0)

        self.RegesteredCOMPProgressBar_ActualLayout.addWidget(self.RegesteredCOMPProgressBar)

        self.RegesteredCOMPProgressBarRightSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.RegesteredCOMPProgressBar_ActualLayout.addItem(self.RegesteredCOMPProgressBarRightSpacer)


        self.RegesteredCOMPWidget_Layout.addLayout(self.RegesteredCOMPProgressBar_ActualLayout)

        self.RegesteredCOMPLabel = QLabel(self.RegesteredCOMPWidget)
        self.RegesteredCOMPLabel.setObjectName(u"RegesteredCOMPLabel")
        self.RegesteredCOMPLabel.setMinimumSize(QSize(50, 25))
        self.RegesteredCOMPLabel.setMaximumSize(QSize(50, 25))
        self.RegesteredCOMPLabel.setFont(font3)
        self.RegesteredCOMPLabel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: \"white\";\n"
"color: \"black\";")

        self.RegesteredCOMPWidget_Layout.addWidget(self.RegesteredCOMPLabel)


        self.RegistrationSummary_Layout.addWidget(self.RegesteredCOMPWidget)

        self.RegesteredSTATWidget = QWidget(self.WhatToRegisterPageSummaryWidget)
        self.RegesteredSTATWidget.setObjectName(u"RegesteredSTATWidget")
        self.RegesteredSTATWidget.setMinimumSize(QSize(50, 0))
        self.RegesteredSTATWidget.setMaximumSize(QSize(50, 16777215))
        self.RegesteredSTATWidget.setStyleSheet(u"background-color: none;")
        self.RegesteredSTATWidget_Layout = QVBoxLayout(self.RegesteredSTATWidget)
        self.RegesteredSTATWidget_Layout.setSpacing(5)
        self.RegesteredSTATWidget_Layout.setObjectName(u"RegesteredSTATWidget_Layout")
        self.RegesteredSTATWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.RegesteredSTATValueLabel = QLabel(self.RegesteredSTATWidget)
        self.RegesteredSTATValueLabel.setObjectName(u"RegesteredSTATValueLabel")
        self.RegesteredSTATValueLabel.setMinimumSize(QSize(50, 25))
        self.RegesteredSTATValueLabel.setMaximumSize(QSize(50, 25))
        self.RegesteredSTATValueLabel.setFont(font4)
        self.RegesteredSTATValueLabel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: \"white\";\n"
"color: \"black\";")

        self.RegesteredSTATWidget_Layout.addWidget(self.RegesteredSTATValueLabel)

        self.RegesteredSTATProgressBar_ActualLayout = QHBoxLayout()
        self.RegesteredSTATProgressBar_ActualLayout.setSpacing(5)
        self.RegesteredSTATProgressBar_ActualLayout.setObjectName(u"RegesteredSTATProgressBar_ActualLayout")
        self.RegesteredSTATProgressBarLeftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.RegesteredSTATProgressBar_ActualLayout.addItem(self.RegesteredSTATProgressBarLeftSpacer)

        self.RegesteredSTATProgressBar = QWidget(self.RegesteredSTATWidget)
        self.RegesteredSTATProgressBar.setObjectName(u"RegesteredSTATProgressBar")
        self.RegesteredSTATProgressBar.setMinimumSize(QSize(25, 0))
        self.RegesteredSTATProgressBar.setMaximumSize(QSize(25, 16777215))
        self.RegesteredSTATProgressBar_Layout = QHBoxLayout(self.RegesteredSTATProgressBar)
        self.RegesteredSTATProgressBar_Layout.setSpacing(0)
        self.RegesteredSTATProgressBar_Layout.setObjectName(u"RegesteredSTATProgressBar_Layout")
        self.RegesteredSTATProgressBar_Layout.setContentsMargins(0, 0, 0, 0)

        self.RegesteredSTATProgressBar_ActualLayout.addWidget(self.RegesteredSTATProgressBar)

        self.RegesteredSTATProgressBarRightSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.RegesteredSTATProgressBar_ActualLayout.addItem(self.RegesteredSTATProgressBarRightSpacer)


        self.RegesteredSTATWidget_Layout.addLayout(self.RegesteredSTATProgressBar_ActualLayout)

        self.RegesteredSTATLabel = QLabel(self.RegesteredSTATWidget)
        self.RegesteredSTATLabel.setObjectName(u"RegesteredSTATLabel")
        self.RegesteredSTATLabel.setMinimumSize(QSize(50, 25))
        self.RegesteredSTATLabel.setMaximumSize(QSize(50, 25))
        self.RegesteredSTATLabel.setFont(font3)
        self.RegesteredSTATLabel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: \"white\";\n"
"color: \"black\";")

        self.RegesteredSTATWidget_Layout.addWidget(self.RegesteredSTATLabel)


        self.RegistrationSummary_Layout.addWidget(self.RegesteredSTATWidget)

        self.RegesteredMATHWidget = QWidget(self.WhatToRegisterPageSummaryWidget)
        self.RegesteredMATHWidget.setObjectName(u"RegesteredMATHWidget")
        self.RegesteredMATHWidget.setMinimumSize(QSize(50, 0))
        self.RegesteredMATHWidget.setMaximumSize(QSize(50, 16777215))
        self.RegesteredMATHWidget.setStyleSheet(u"background-color: none;")
        self.RegesteredMATHWidget_Layout = QVBoxLayout(self.RegesteredMATHWidget)
        self.RegesteredMATHWidget_Layout.setSpacing(5)
        self.RegesteredMATHWidget_Layout.setObjectName(u"RegesteredMATHWidget_Layout")
        self.RegesteredMATHWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.RegesteredMATHValueLabel = QLabel(self.RegesteredMATHWidget)
        self.RegesteredMATHValueLabel.setObjectName(u"RegesteredMATHValueLabel")
        self.RegesteredMATHValueLabel.setMinimumSize(QSize(50, 25))
        self.RegesteredMATHValueLabel.setMaximumSize(QSize(50, 25))
        self.RegesteredMATHValueLabel.setFont(font4)
        self.RegesteredMATHValueLabel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: \"white\";\n"
"color: \"black\";")

        self.RegesteredMATHWidget_Layout.addWidget(self.RegesteredMATHValueLabel)

        self.RegesteredMATHProgressBar_ActualLayout = QHBoxLayout()
        self.RegesteredMATHProgressBar_ActualLayout.setSpacing(5)
        self.RegesteredMATHProgressBar_ActualLayout.setObjectName(u"RegesteredMATHProgressBar_ActualLayout")
        self.RegesteredMATHProgressBarLeftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.RegesteredMATHProgressBar_ActualLayout.addItem(self.RegesteredMATHProgressBarLeftSpacer)

        self.RegesteredMATHProgressBar = QWidget(self.RegesteredMATHWidget)
        self.RegesteredMATHProgressBar.setObjectName(u"RegesteredMATHProgressBar")
        self.RegesteredMATHProgressBar.setMinimumSize(QSize(25, 0))
        self.RegesteredMATHProgressBar.setMaximumSize(QSize(25, 16777215))
        self.RegesteredMATHProgressBar_Layout = QHBoxLayout(self.RegesteredMATHProgressBar)
        self.RegesteredMATHProgressBar_Layout.setSpacing(0)
        self.RegesteredMATHProgressBar_Layout.setObjectName(u"RegesteredMATHProgressBar_Layout")
        self.RegesteredMATHProgressBar_Layout.setContentsMargins(0, 0, 0, 0)

        self.RegesteredMATHProgressBar_ActualLayout.addWidget(self.RegesteredMATHProgressBar)

        self.RegesteredMATHProgressBarRightSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.RegesteredMATHProgressBar_ActualLayout.addItem(self.RegesteredMATHProgressBarRightSpacer)


        self.RegesteredMATHWidget_Layout.addLayout(self.RegesteredMATHProgressBar_ActualLayout)

        self.RegesteredMATHLabel = QLabel(self.RegesteredMATHWidget)
        self.RegesteredMATHLabel.setObjectName(u"RegesteredMATHLabel")
        self.RegesteredMATHLabel.setMinimumSize(QSize(50, 25))
        self.RegesteredMATHLabel.setMaximumSize(QSize(50, 25))
        self.RegesteredMATHLabel.setFont(font3)
        self.RegesteredMATHLabel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: \"white\";\n"
"color: \"black\";")

        self.RegesteredMATHWidget_Layout.addWidget(self.RegesteredMATHLabel)


        self.RegistrationSummary_Layout.addWidget(self.RegesteredMATHWidget)

        self.RegesteredOthersWidget = QWidget(self.WhatToRegisterPageSummaryWidget)
        self.RegesteredOthersWidget.setObjectName(u"RegesteredOthersWidget")
        self.RegesteredOthersWidget.setMinimumSize(QSize(50, 0))
        self.RegesteredOthersWidget.setMaximumSize(QSize(50, 16777215))
        self.RegesteredOthersWidget.setStyleSheet(u"background-color: none;")
        self.RegesteredOthersWidget_Layout = QVBoxLayout(self.RegesteredOthersWidget)
        self.RegesteredOthersWidget_Layout.setSpacing(5)
        self.RegesteredOthersWidget_Layout.setObjectName(u"RegesteredOthersWidget_Layout")
        self.RegesteredOthersWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.RegesteredOthersValueLabel = QLabel(self.RegesteredOthersWidget)
        self.RegesteredOthersValueLabel.setObjectName(u"RegesteredOthersValueLabel")
        self.RegesteredOthersValueLabel.setMinimumSize(QSize(50, 25))
        self.RegesteredOthersValueLabel.setMaximumSize(QSize(50, 25))
        self.RegesteredOthersValueLabel.setFont(font4)
        self.RegesteredOthersValueLabel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: \"white\";\n"
"color: \"black\";")

        self.RegesteredOthersWidget_Layout.addWidget(self.RegesteredOthersValueLabel)

        self.RegesteredOthersProgressBar_ActualLayout = QHBoxLayout()
        self.RegesteredOthersProgressBar_ActualLayout.setSpacing(5)
        self.RegesteredOthersProgressBar_ActualLayout.setObjectName(u"RegesteredOthersProgressBar_ActualLayout")
        self.RegesteredOthersProgressBarLeftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.RegesteredOthersProgressBar_ActualLayout.addItem(self.RegesteredOthersProgressBarLeftSpacer)

        self.RegesteredOthersProgressBar = QWidget(self.RegesteredOthersWidget)
        self.RegesteredOthersProgressBar.setObjectName(u"RegesteredOthersProgressBar")
        self.RegesteredOthersProgressBar.setMinimumSize(QSize(25, 0))
        self.RegesteredOthersProgressBar.setMaximumSize(QSize(25, 16777215))
        self.RegesteredOthersProgressBar_Layout = QHBoxLayout(self.RegesteredOthersProgressBar)
        self.RegesteredOthersProgressBar_Layout.setSpacing(0)
        self.RegesteredOthersProgressBar_Layout.setObjectName(u"RegesteredOthersProgressBar_Layout")
        self.RegesteredOthersProgressBar_Layout.setContentsMargins(0, 0, 0, 0)

        self.RegesteredOthersProgressBar_ActualLayout.addWidget(self.RegesteredOthersProgressBar)

        self.RegesteredOthersProgressBarRightSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.RegesteredOthersProgressBar_ActualLayout.addItem(self.RegesteredOthersProgressBarRightSpacer)


        self.RegesteredOthersWidget_Layout.addLayout(self.RegesteredOthersProgressBar_ActualLayout)

        self.RegesteredOthersLabel = QLabel(self.RegesteredOthersWidget)
        self.RegesteredOthersLabel.setObjectName(u"RegesteredOthersLabel")
        self.RegesteredOthersLabel.setMinimumSize(QSize(50, 25))
        self.RegesteredOthersLabel.setMaximumSize(QSize(50, 25))
        self.RegesteredOthersLabel.setFont(font3)
        self.RegesteredOthersLabel.setStyleSheet(u"border-radius: 5px;\n"
"background-color: \"white\";\n"
"color: \"black\";")

        self.RegesteredOthersWidget_Layout.addWidget(self.RegesteredOthersLabel)


        self.RegistrationSummary_Layout.addWidget(self.RegesteredOthersWidget)


        self.WhatToRegesterSummaryWidget_Layout.addLayout(self.RegistrationSummary_Layout)


        self.WhatToRegesterPage_Layout.addWidget(self.WhatToRegisterPageSummaryWidget)

        self.WhatToRegisterPageScrollArea = QScrollArea(self.WhatToRegisterPage)
        self.WhatToRegisterPageScrollArea.setObjectName(u"WhatToRegisterPageScrollArea")
        self.WhatToRegisterPageScrollArea.setMinimumSize(QSize(585, 585))
        self.WhatToRegisterPageScrollArea.setMaximumSize(QSize(585, 585))
        self.WhatToRegisterPageScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.WhatToRegisterPageScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.WhatToRegisterPageScrollArea.setWidgetResizable(False)
        self.WhatToRegisterPageScrollAreaWidget = QWidget()
        self.WhatToRegisterPageScrollAreaWidget.setObjectName(u"WhatToRegisterPageScrollAreaWidget")
        self.WhatToRegisterPageScrollAreaWidget.setGeometry(QRect(0, 0, 585, 1500))
        self.WhatToRegisterPageScrollAreaWidget.setMinimumSize(QSize(585, 1500))
        self.WhatToRegisterPageScrollAreaWidget.setMaximumSize(QSize(585, 1500))
        self.WhatToRegisterPageScrollAreaWidget.setStyleSheet(u"background-color: none;")
        self.WhatToRegisterPageScrollAreaActualWidget = QWidget(self.WhatToRegisterPageScrollAreaWidget)
        self.WhatToRegisterPageScrollAreaActualWidget.setObjectName(u"WhatToRegisterPageScrollAreaActualWidget")
        self.WhatToRegisterPageScrollAreaActualWidget.setGeometry(QRect(0, 0, 585, 1200))
        self.WhatToRegisterPageScrollAreaActualWidget.setMinimumSize(QSize(585, 1200))
        self.WhatToRegisterPageScrollAreaActualWidget.setMaximumSize(QSize(585, 1200))
        self.WhatToRegisterPageScrollAreaActualWidget.setStyleSheet(u"")
        self.layoutWidget = QWidget(self.WhatToRegisterPageScrollAreaActualWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 634, 107))
        self.SuggestedCourse_Layout_1 = QHBoxLayout(self.layoutWidget)
        self.SuggestedCourse_Layout_1.setSpacing(5)
        self.SuggestedCourse_Layout_1.setObjectName(u"SuggestedCourse_Layout_1")
        self.SuggestedCourse_Layout_1.setContentsMargins(0, 0, 0, 0)
        self.SuggestedCourseRankWidget_1 = QWidget(self.layoutWidget)
        self.SuggestedCourseRankWidget_1.setObjectName(u"SuggestedCourseRankWidget_1")
        self.SuggestedCourseRankWidget_1.setMinimumSize(QSize(50, 50))
        self.SuggestedCourseRankWidget_1.setMaximumSize(QSize(50, 50))
        self.SuggestedCourseRankWidget_1.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(27, 49, 96),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.SuggestedCourseRankWidget_Layout_1 = QVBoxLayout(self.SuggestedCourseRankWidget_1)
        self.SuggestedCourseRankWidget_Layout_1.setSpacing(0)
        self.SuggestedCourseRankWidget_Layout_1.setObjectName(u"SuggestedCourseRankWidget_Layout_1")
        self.SuggestedCourseRankWidget_Layout_1.setContentsMargins(0, 0, 0, 0)
        self.SuggestedCourseRankLabel_1 = QLabel(self.SuggestedCourseRankWidget_1)
        self.SuggestedCourseRankLabel_1.setObjectName(u"SuggestedCourseRankLabel_1")
        self.SuggestedCourseRankLabel_1.setFont(font)

        self.SuggestedCourseRankWidget_Layout_1.addWidget(self.SuggestedCourseRankLabel_1, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.SuggestedCourse_Layout_1.addWidget(self.SuggestedCourseRankWidget_1)

        self.SuggestedCourseWidget_1 = QWidget(self.layoutWidget)
        self.SuggestedCourseWidget_1.setObjectName(u"SuggestedCourseWidget_1")
        self.SuggestedCourseWidget_1.setMinimumSize(QSize(530, 105))
        self.SuggestedCourseWidget_1.setMaximumSize(QSize(530, 105))
        self.SuggestedCourseWidget_1.setFont(font2)
        self.SuggestedCourseWidget_1.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(27, 49, 96),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.horizontalLayout = QHBoxLayout(self.SuggestedCourseWidget_1)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.SuggestedCourseSummary_Layout_1 = QVBoxLayout()
        self.SuggestedCourseSummary_Layout_1.setSpacing(0)
        self.SuggestedCourseSummary_Layout_1.setObjectName(u"SuggestedCourseSummary_Layout_1")
        self.SuggestedCourseID_Hours_Layout_1 = QHBoxLayout()
        self.SuggestedCourseID_Hours_Layout_1.setSpacing(5)
        self.SuggestedCourseID_Hours_Layout_1.setObjectName(u"SuggestedCourseID_Hours_Layout_1")
        self.SuggestedCourseIDLabel_1 = QLabel(self.SuggestedCourseWidget_1)
        self.SuggestedCourseIDLabel_1.setObjectName(u"SuggestedCourseIDLabel_1")
        self.SuggestedCourseIDLabel_1.setFont(font3)
        self.SuggestedCourseIDLabel_1.setStyleSheet(u"background-color: none;")

        self.SuggestedCourseID_Hours_Layout_1.addWidget(self.SuggestedCourseIDLabel_1)

        self.SuggestedCourseIDValueLabel_1 = QLabel(self.SuggestedCourseWidget_1)
        self.SuggestedCourseIDValueLabel_1.setObjectName(u"SuggestedCourseIDValueLabel_1")
        self.SuggestedCourseIDValueLabel_1.setFont(font4)
        self.SuggestedCourseIDValueLabel_1.setStyleSheet(u"background-color: none;")

        self.SuggestedCourseID_Hours_Layout_1.addWidget(self.SuggestedCourseIDValueLabel_1)

        self.SuggestedCourseID_HoursSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.SuggestedCourseID_Hours_Layout_1.addItem(self.SuggestedCourseID_HoursSpacer_1)


        self.SuggestedCourseSummary_Layout_1.addLayout(self.SuggestedCourseID_Hours_Layout_1)

        self.SuggestedCoursePermission_Layout_1 = QHBoxLayout()
        self.SuggestedCoursePermission_Layout_1.setSpacing(5)
        self.SuggestedCoursePermission_Layout_1.setObjectName(u"SuggestedCoursePermission_Layout_1")
        self.SuggestedCoursePermissionLabel_1 = QLabel(self.SuggestedCourseWidget_1)
        self.SuggestedCoursePermissionLabel_1.setObjectName(u"SuggestedCoursePermissionLabel_1")
        self.SuggestedCoursePermissionLabel_1.setFont(font3)
        self.SuggestedCoursePermissionLabel_1.setStyleSheet(u"background-color: none;")

        self.SuggestedCoursePermission_Layout_1.addWidget(self.SuggestedCoursePermissionLabel_1)

        self.SuggestedCoursePermissionValueLabel_1 = QLabel(self.SuggestedCourseWidget_1)
        self.SuggestedCoursePermissionValueLabel_1.setObjectName(u"SuggestedCoursePermissionValueLabel_1")
        self.SuggestedCoursePermissionValueLabel_1.setFont(font4)
        self.SuggestedCoursePermissionValueLabel_1.setStyleSheet(u"background-color: none;")

        self.SuggestedCoursePermission_Layout_1.addWidget(self.SuggestedCoursePermissionValueLabel_1)

        self.SuggestedCoursePermissionSpacer_1 = QSpacerItem(75, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.SuggestedCoursePermission_Layout_1.addItem(self.SuggestedCoursePermissionSpacer_1)


        self.SuggestedCourseSummary_Layout_1.addLayout(self.SuggestedCoursePermission_Layout_1)

        self.SuggestedCoursePermission_Layout_2 = QHBoxLayout()
        self.SuggestedCoursePermission_Layout_2.setSpacing(5)
        self.SuggestedCoursePermission_Layout_2.setObjectName(u"SuggestedCoursePermission_Layout_2")
        self.SuggestedCourseHoursLabel_1 = QLabel(self.SuggestedCourseWidget_1)
        self.SuggestedCourseHoursLabel_1.setObjectName(u"SuggestedCourseHoursLabel_1")
        self.SuggestedCourseHoursLabel_1.setFont(font3)
        self.SuggestedCourseHoursLabel_1.setStyleSheet(u"background-color: none;")

        self.SuggestedCoursePermission_Layout_2.addWidget(self.SuggestedCourseHoursLabel_1)

        self.SuggestedCourseHoursValueLabel_1 = QLabel(self.SuggestedCourseWidget_1)
        self.SuggestedCourseHoursValueLabel_1.setObjectName(u"SuggestedCourseHoursValueLabel_1")
        self.SuggestedCourseHoursValueLabel_1.setFont(font4)
        self.SuggestedCourseHoursValueLabel_1.setStyleSheet(u"background-color: none;")

        self.SuggestedCoursePermission_Layout_2.addWidget(self.SuggestedCourseHoursValueLabel_1)

        self.SuggestedCoursePermissionSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.SuggestedCoursePermission_Layout_2.addItem(self.SuggestedCoursePermissionSpacer_2)


        self.SuggestedCourseSummary_Layout_1.addLayout(self.SuggestedCoursePermission_Layout_2)


        self.horizontalLayout.addLayout(self.SuggestedCourseSummary_Layout_1)

        self.SuggestedCourseWidgetLine = QFrame(self.SuggestedCourseWidget_1)
        self.SuggestedCourseWidgetLine.setObjectName(u"SuggestedCourseWidgetLine")
        self.SuggestedCourseWidgetLine.setMinimumSize(QSize(1, 50))
        self.SuggestedCourseWidgetLine.setMaximumSize(QSize(1, 50))
        self.SuggestedCourseWidgetLine.setStyleSheet(u"background-color: \"white\";")
        self.SuggestedCourseWidgetLine.setFrameShape(QFrame.Shape.VLine)
        self.SuggestedCourseWidgetLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.SuggestedCourseWidgetLine)

        self.SuggestedCourseWidgetSpacer_1 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.SuggestedCourseWidgetSpacer_1)

        self.SuggestedCourseDetails_Layout_1 = QVBoxLayout()
        self.SuggestedCourseDetails_Layout_1.setSpacing(0)
        self.SuggestedCourseDetails_Layout_1.setObjectName(u"SuggestedCourseDetails_Layout_1")
        self.SuggestedCourseRemainingStudents_Layout_1 = QHBoxLayout()
        self.SuggestedCourseRemainingStudents_Layout_1.setSpacing(5)
        self.SuggestedCourseRemainingStudents_Layout_1.setObjectName(u"SuggestedCourseRemainingStudents_Layout_1")
        self.SuggestedCourseRemainingStudentsLabel_1 = QLabel(self.SuggestedCourseWidget_1)
        self.SuggestedCourseRemainingStudentsLabel_1.setObjectName(u"SuggestedCourseRemainingStudentsLabel_1")
        self.SuggestedCourseRemainingStudentsLabel_1.setFont(font3)
        self.SuggestedCourseRemainingStudentsLabel_1.setStyleSheet(u"background-color: none;")

        self.SuggestedCourseRemainingStudents_Layout_1.addWidget(self.SuggestedCourseRemainingStudentsLabel_1)

        self.SuggestedCourseRemainingStudentsValueLabel_1 = QLabel(self.SuggestedCourseWidget_1)
        self.SuggestedCourseRemainingStudentsValueLabel_1.setObjectName(u"SuggestedCourseRemainingStudentsValueLabel_1")
        self.SuggestedCourseRemainingStudentsValueLabel_1.setFont(font4)
        self.SuggestedCourseRemainingStudentsValueLabel_1.setStyleSheet(u"background-color: none;")

        self.SuggestedCourseRemainingStudents_Layout_1.addWidget(self.SuggestedCourseRemainingStudentsValueLabel_1)

        self.SuggestedCourseRemainingStudentsSpacer_1 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.SuggestedCourseRemainingStudents_Layout_1.addItem(self.SuggestedCourseRemainingStudentsSpacer_1)


        self.SuggestedCourseDetails_Layout_1.addLayout(self.SuggestedCourseRemainingStudents_Layout_1)

        self.SuggestedCoursePassRate_Layout_1 = QHBoxLayout()
        self.SuggestedCoursePassRate_Layout_1.setSpacing(5)
        self.SuggestedCoursePassRate_Layout_1.setObjectName(u"SuggestedCoursePassRate_Layout_1")
        self.SuggestedCoursePassRateLabel_1 = QLabel(self.SuggestedCourseWidget_1)
        self.SuggestedCoursePassRateLabel_1.setObjectName(u"SuggestedCoursePassRateLabel_1")
        self.SuggestedCoursePassRateLabel_1.setFont(font3)
        self.SuggestedCoursePassRateLabel_1.setStyleSheet(u"background-color: none;")

        self.SuggestedCoursePassRate_Layout_1.addWidget(self.SuggestedCoursePassRateLabel_1)

        self.SuggestedCoursePassRateValueLabel_1 = QLabel(self.SuggestedCourseWidget_1)
        self.SuggestedCoursePassRateValueLabel_1.setObjectName(u"SuggestedCoursePassRateValueLabel_1")
        self.SuggestedCoursePassRateValueLabel_1.setFont(font4)
        self.SuggestedCoursePassRateValueLabel_1.setStyleSheet(u"background-color: none;")

        self.SuggestedCoursePassRate_Layout_1.addWidget(self.SuggestedCoursePassRateValueLabel_1)

        self.SuggestedCoursePassRateSpacer_1 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.SuggestedCoursePassRate_Layout_1.addItem(self.SuggestedCoursePassRateSpacer_1)


        self.SuggestedCourseDetails_Layout_1.addLayout(self.SuggestedCoursePassRate_Layout_1)

        self.SuggestedCourseDetails_LayoutSpacer_1 = QSpacerItem(20, 35, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.SuggestedCourseDetails_Layout_1.addItem(self.SuggestedCourseDetails_LayoutSpacer_1)


        self.horizontalLayout.addLayout(self.SuggestedCourseDetails_Layout_1)


        self.SuggestedCourse_Layout_1.addWidget(self.SuggestedCourseWidget_1)

        self.SuggestedCourseL_LayoutSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.SuggestedCourse_Layout_1.addItem(self.SuggestedCourseL_LayoutSpacer_1)

        self.WhatToRegisterPageScrollArea.setWidget(self.WhatToRegisterPageScrollAreaWidget)

        self.WhatToRegesterPage_Layout.addWidget(self.WhatToRegisterPageScrollArea)

        self.AIPageStackedWidget.addWidget(self.WhatToRegisterPage)
        self.FinalGPAPredictorPage = QWidget()
        self.FinalGPAPredictorPage.setObjectName(u"FinalGPAPredictorPage")
        self.FinalGPAPredictorPage.setStyleSheet(u"border-radius: 10px;\n"
"background-color: \"white\";")
        self.FinalGPAPredictorPage_Layout = QVBoxLayout(self.FinalGPAPredictorPage)
        self.FinalGPAPredictorPage_Layout.setSpacing(5)
        self.FinalGPAPredictorPage_Layout.setObjectName(u"FinalGPAPredictorPage_Layout")
        self.FinalGPAPredictorPage_Layout.setContentsMargins(10, 5, 10, 10)
        self.FinalGPAPredictorInputWidget = QWidget(self.FinalGPAPredictorPage)
        self.FinalGPAPredictorInputWidget.setObjectName(u"FinalGPAPredictorInputWidget")
        self.FinalGPAPredictorInputWidget.setMinimumSize(QSize(805, 245))
        self.FinalGPAPredictorInputWidget.setMaximumSize(QSize(805, 245))
        self.FinalGPAPredictorInputWidget.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(27, 49, 96),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.FinalGPAPredictorInputWidget_Layout = QVBoxLayout(self.FinalGPAPredictorInputWidget)
        self.FinalGPAPredictorInputWidget_Layout.setSpacing(5)
        self.FinalGPAPredictorInputWidget_Layout.setObjectName(u"FinalGPAPredictorInputWidget_Layout")
        self.FinalGPAPredictorInputWidget_Layout.setContentsMargins(10, 10, 10, 10)
        self.FinalGPAPredictorCurrentLevelWidget = QWidget(self.FinalGPAPredictorInputWidget)
        self.FinalGPAPredictorCurrentLevelWidget.setObjectName(u"FinalGPAPredictorCurrentLevelWidget")
        self.FinalGPAPredictorCurrentLevelWidget.setMinimumSize(QSize(0, 25))
        self.FinalGPAPredictorCurrentLevelWidget.setMaximumSize(QSize(16777215, 25))
        self.FinalGPAPredictorCurrentLevelWidget.setStyleSheet(u"background-color: none;")
        self.FinalGPAPredictorCurrentLevelWidget_Layout = QHBoxLayout(self.FinalGPAPredictorCurrentLevelWidget)
        self.FinalGPAPredictorCurrentLevelWidget_Layout.setSpacing(5)
        self.FinalGPAPredictorCurrentLevelWidget_Layout.setObjectName(u"FinalGPAPredictorCurrentLevelWidget_Layout")
        self.FinalGPAPredictorCurrentLevelWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.FinalGPAPredictorCurrentLevelLabel = QLabel(self.FinalGPAPredictorCurrentLevelWidget)
        self.FinalGPAPredictorCurrentLevelLabel.setObjectName(u"FinalGPAPredictorCurrentLevelLabel")
        sizePolicy1.setHeightForWidth(self.FinalGPAPredictorCurrentLevelLabel.sizePolicy().hasHeightForWidth())
        self.FinalGPAPredictorCurrentLevelLabel.setSizePolicy(sizePolicy1)
        self.FinalGPAPredictorCurrentLevelLabel.setMinimumSize(QSize(0, 25))
        self.FinalGPAPredictorCurrentLevelLabel.setMaximumSize(QSize(16777215, 25))
        self.FinalGPAPredictorCurrentLevelLabel.setFont(font6)
        self.FinalGPAPredictorCurrentLevelLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.FinalGPAPredictorCurrentLevelLabel.setStyleSheet(u"background-color: none;")

        self.FinalGPAPredictorCurrentLevelWidget_Layout.addWidget(self.FinalGPAPredictorCurrentLevelLabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.FinalGPAPredictorCurrentLevelValueLabel = QLabel(self.FinalGPAPredictorCurrentLevelWidget)
        self.FinalGPAPredictorCurrentLevelValueLabel.setObjectName(u"FinalGPAPredictorCurrentLevelValueLabel")
        sizePolicy1.setHeightForWidth(self.FinalGPAPredictorCurrentLevelValueLabel.sizePolicy().hasHeightForWidth())
        self.FinalGPAPredictorCurrentLevelValueLabel.setSizePolicy(sizePolicy1)
        self.FinalGPAPredictorCurrentLevelValueLabel.setMinimumSize(QSize(0, 25))
        self.FinalGPAPredictorCurrentLevelValueLabel.setMaximumSize(QSize(16777215, 25))
        self.FinalGPAPredictorCurrentLevelValueLabel.setFont(font6)
        self.FinalGPAPredictorCurrentLevelValueLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.FinalGPAPredictorCurrentLevelValueLabel.setStyleSheet(u"background-color: none;")

        self.FinalGPAPredictorCurrentLevelWidget_Layout.addWidget(self.FinalGPAPredictorCurrentLevelValueLabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.FinalGPAPredictorCurrentLevelWidgetSpacer = QSpacerItem(57, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.FinalGPAPredictorCurrentLevelWidget_Layout.addItem(self.FinalGPAPredictorCurrentLevelWidgetSpacer)


        self.FinalGPAPredictorInputWidget_Layout.addWidget(self.FinalGPAPredictorCurrentLevelWidget)

        self.CurrentGPAWidget = QWidget(self.FinalGPAPredictorInputWidget)
        self.CurrentGPAWidget.setObjectName(u"CurrentGPAWidget")
        self.CurrentGPAWidget.setMinimumSize(QSize(0, 25))
        self.CurrentGPAWidget.setMaximumSize(QSize(16777215, 25))
        self.CurrentGPAWidget.setStyleSheet(u"background-color: none;")
        self.CurrentGPAWidget_Layout = QHBoxLayout(self.CurrentGPAWidget)
        self.CurrentGPAWidget_Layout.setSpacing(5)
        self.CurrentGPAWidget_Layout.setObjectName(u"CurrentGPAWidget_Layout")
        self.CurrentGPAWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.CurrentGPALabel = QLabel(self.CurrentGPAWidget)
        self.CurrentGPALabel.setObjectName(u"CurrentGPALabel")
        sizePolicy1.setHeightForWidth(self.CurrentGPALabel.sizePolicy().hasHeightForWidth())
        self.CurrentGPALabel.setSizePolicy(sizePolicy1)
        self.CurrentGPALabel.setMinimumSize(QSize(0, 25))
        self.CurrentGPALabel.setMaximumSize(QSize(16777215, 25))
        self.CurrentGPALabel.setFont(font6)
        self.CurrentGPALabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CurrentGPALabel.setStyleSheet(u"background-color: none;")

        self.CurrentGPAWidget_Layout.addWidget(self.CurrentGPALabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.CurrentGPAValueLabel = QLabel(self.CurrentGPAWidget)
        self.CurrentGPAValueLabel.setObjectName(u"CurrentGPAValueLabel")
        sizePolicy1.setHeightForWidth(self.CurrentGPAValueLabel.sizePolicy().hasHeightForWidth())
        self.CurrentGPAValueLabel.setSizePolicy(sizePolicy1)
        self.CurrentGPAValueLabel.setMinimumSize(QSize(0, 25))
        self.CurrentGPAValueLabel.setMaximumSize(QSize(16777215, 25))
        self.CurrentGPAValueLabel.setFont(font6)
        self.CurrentGPAValueLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.CurrentGPAValueLabel.setStyleSheet(u"background-color: none;")

        self.CurrentGPAWidget_Layout.addWidget(self.CurrentGPAValueLabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.CurrentGPAWidgetSpacer = QSpacerItem(649, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CurrentGPAWidget_Layout.addItem(self.CurrentGPAWidgetSpacer)


        self.FinalGPAPredictorInputWidget_Layout.addWidget(self.CurrentGPAWidget)

        self.LevelsGPA_Layout = QHBoxLayout()
        self.LevelsGPA_Layout.setSpacing(5)
        self.LevelsGPA_Layout.setObjectName(u"LevelsGPA_Layout")
        self.Level_1_GPA_Layout = QVBoxLayout()
        self.Level_1_GPA_Layout.setSpacing(5)
        self.Level_1_GPA_Layout.setObjectName(u"Level_1_GPA_Layout")
        self.Level_1_GPABoxLabel = QLabel(self.FinalGPAPredictorInputWidget)
        self.Level_1_GPABoxLabel.setObjectName(u"Level_1_GPABoxLabel")
        sizePolicy2.setHeightForWidth(self.Level_1_GPABoxLabel.sizePolicy().hasHeightForWidth())
        self.Level_1_GPABoxLabel.setSizePolicy(sizePolicy2)
        self.Level_1_GPABoxLabel.setMinimumSize(QSize(390, 25))
        self.Level_1_GPABoxLabel.setMaximumSize(QSize(390, 25))
        self.Level_1_GPABoxLabel.setFont(font6)
        self.Level_1_GPABoxLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Level_1_GPABoxLabel.setStyleSheet(u"background-color: none;")

        self.Level_1_GPA_Layout.addWidget(self.Level_1_GPABoxLabel)

        self.Level_1_GPABox = QLineEdit(self.FinalGPAPredictorInputWidget)
        self.Level_1_GPABox.setObjectName(u"Level_1_GPABox")
        self.Level_1_GPABox.setMinimumSize(QSize(390, 50))
        self.Level_1_GPABox.setMaximumSize(QSize(390, 50))
        self.Level_1_GPABox.setFont(font8)
        self.Level_1_GPABox.setStyleSheet(u"background-color: \"white\";\n"
"border-radius: 5px;\n"
"color: \"black\";\n"
"padding-left: 10px;\n"
"font-size: 16pt;\n"
"font-family: calibri;")
        self.Level_1_GPABox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.Level_1_GPA_Layout.addWidget(self.Level_1_GPABox)

        self.Level_1_GPAErrorLabel = QLabel(self.FinalGPAPredictorInputWidget)
        self.Level_1_GPAErrorLabel.setObjectName(u"Level_1_GPAErrorLabel")
        sizePolicy1.setHeightForWidth(self.Level_1_GPAErrorLabel.sizePolicy().hasHeightForWidth())
        self.Level_1_GPAErrorLabel.setSizePolicy(sizePolicy1)
        self.Level_1_GPAErrorLabel.setMinimumSize(QSize(0, 25))
        self.Level_1_GPAErrorLabel.setMaximumSize(QSize(16777215, 25))
        self.Level_1_GPAErrorLabel.setFont(font6)
        self.Level_1_GPAErrorLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Level_1_GPAErrorLabel.setStyleSheet(u"background-color: none;\n"
"padding-left: 10px;")

        self.Level_1_GPA_Layout.addWidget(self.Level_1_GPAErrorLabel)

        self.Level_1_GPA_LayoutSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.Level_1_GPA_Layout.addItem(self.Level_1_GPA_LayoutSpacer)


        self.LevelsGPA_Layout.addLayout(self.Level_1_GPA_Layout)

        self.Level_2_GPA_Layout = QVBoxLayout()
        self.Level_2_GPA_Layout.setSpacing(5)
        self.Level_2_GPA_Layout.setObjectName(u"Level_2_GPA_Layout")
        self.Level_2_GPABoxLabel = QLabel(self.FinalGPAPredictorInputWidget)
        self.Level_2_GPABoxLabel.setObjectName(u"Level_2_GPABoxLabel")
        sizePolicy2.setHeightForWidth(self.Level_2_GPABoxLabel.sizePolicy().hasHeightForWidth())
        self.Level_2_GPABoxLabel.setSizePolicy(sizePolicy2)
        self.Level_2_GPABoxLabel.setMinimumSize(QSize(390, 25))
        self.Level_2_GPABoxLabel.setMaximumSize(QSize(390, 25))
        self.Level_2_GPABoxLabel.setFont(font6)
        self.Level_2_GPABoxLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Level_2_GPABoxLabel.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.Level_2_GPA_Layout.addWidget(self.Level_2_GPABoxLabel)

        self.Level_2_GPABox = QLineEdit(self.FinalGPAPredictorInputWidget)
        self.Level_2_GPABox.setObjectName(u"Level_2_GPABox")
        self.Level_2_GPABox.setMinimumSize(QSize(390, 50))
        self.Level_2_GPABox.setMaximumSize(QSize(390, 50))
        self.Level_2_GPABox.setFont(font8)
        self.Level_2_GPABox.setStyleSheet(u"background-color: \"white\";\n"
"border-radius: 5px;\n"
"color: \"black\";\n"
"padding-left: 10px;\n"
"font-size: 16pt;\n"
"font-family: calibri;")
        self.Level_2_GPABox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.Level_2_GPA_Layout.addWidget(self.Level_2_GPABox)

        self.Level_2_GPAErrorLabel = QLabel(self.FinalGPAPredictorInputWidget)
        self.Level_2_GPAErrorLabel.setObjectName(u"Level_2_GPAErrorLabel")
        sizePolicy1.setHeightForWidth(self.Level_2_GPAErrorLabel.sizePolicy().hasHeightForWidth())
        self.Level_2_GPAErrorLabel.setSizePolicy(sizePolicy1)
        self.Level_2_GPAErrorLabel.setMinimumSize(QSize(0, 25))
        self.Level_2_GPAErrorLabel.setMaximumSize(QSize(16777215, 25))
        self.Level_2_GPAErrorLabel.setFont(font6)
        self.Level_2_GPAErrorLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Level_2_GPAErrorLabel.setStyleSheet(u"background-color: none;\n"
"padding-left: 10px;")

        self.Level_2_GPA_Layout.addWidget(self.Level_2_GPAErrorLabel)

        self.Level_2_GPA_LayoutSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.Level_2_GPA_Layout.addItem(self.Level_2_GPA_LayoutSpacer)


        self.LevelsGPA_Layout.addLayout(self.Level_2_GPA_Layout)

        self.LevelsGPA_LayoutSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.LevelsGPA_Layout.addItem(self.LevelsGPA_LayoutSpacer)


        self.FinalGPAPredictorInputWidget_Layout.addLayout(self.LevelsGPA_Layout)

        self.FinalGPAPredictorInputWidgetSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.FinalGPAPredictorInputWidget_Layout.addItem(self.FinalGPAPredictorInputWidgetSpacer)

        self.FinalGPAPredictorPredictButton = QPushButton(self.FinalGPAPredictorInputWidget)
        self.FinalGPAPredictorPredictButton.setObjectName(u"FinalGPAPredictorPredictButton")
        self.FinalGPAPredictorPredictButton.setEnabled(True)
        sizePolicy.setHeightForWidth(self.FinalGPAPredictorPredictButton.sizePolicy().hasHeightForWidth())
        self.FinalGPAPredictorPredictButton.setSizePolicy(sizePolicy)
        self.FinalGPAPredictorPredictButton.setMinimumSize(QSize(785, 40))
        self.FinalGPAPredictorPredictButton.setMaximumSize(QSize(785, 40))
        self.FinalGPAPredictorPredictButton.setFont(font9)
        self.FinalGPAPredictorPredictButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(235, 235, 235);\n"
"	border-radius: 5px;\n"
"	color: \"black\";\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: \"white\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: \"white\";\n"
"}")
        self.FinalGPAPredictorPredictButton.setCheckable(True)

        self.FinalGPAPredictorInputWidget_Layout.addWidget(self.FinalGPAPredictorPredictButton)


        self.FinalGPAPredictorPage_Layout.addWidget(self.FinalGPAPredictorInputWidget)

        self.ExpectedGPACard = QWidget(self.FinalGPAPredictorPage)
        self.ExpectedGPACard.setObjectName(u"ExpectedGPACard")
        self.ExpectedGPACard.setMinimumSize(QSize(805, 100))
        self.ExpectedGPACard.setMaximumSize(QSize(805, 100))
        self.ExpectedGPACard.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(7, 74, 45),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.ExpectedGPACard_Layout = QHBoxLayout(self.ExpectedGPACard)
        self.ExpectedGPACard_Layout.setSpacing(5)
        self.ExpectedGPACard_Layout.setObjectName(u"ExpectedGPACard_Layout")
        self.ExpectedGPACard_Layout.setContentsMargins(10, 10, 10, 10)
        self.ExpectedGPA_Layout = QVBoxLayout()
        self.ExpectedGPA_Layout.setSpacing(0)
        self.ExpectedGPA_Layout.setObjectName(u"ExpectedGPA_Layout")
        self.ExpectedGPALabel = QLabel(self.ExpectedGPACard)
        self.ExpectedGPALabel.setObjectName(u"ExpectedGPALabel")
        font10 = QFont()
        font10.setFamilies([u"Calibri"])
        self.ExpectedGPALabel.setFont(font10)
        self.ExpectedGPALabel.setStyleSheet(u"background-color: none;")

        self.ExpectedGPA_Layout.addWidget(self.ExpectedGPALabel)

        self.ExpectedGPAValueLabel = QLabel(self.ExpectedGPACard)
        self.ExpectedGPAValueLabel.setObjectName(u"ExpectedGPAValueLabel")
        self.ExpectedGPAValueLabel.setFont(font4)
        self.ExpectedGPAValueLabel.setStyleSheet(u"background-color: none;")

        self.ExpectedGPA_Layout.addWidget(self.ExpectedGPAValueLabel)


        self.ExpectedGPACard_Layout.addLayout(self.ExpectedGPA_Layout)

        self.ExpectedGPACardLine = QFrame(self.ExpectedGPACard)
        self.ExpectedGPACardLine.setObjectName(u"ExpectedGPACardLine")
        self.ExpectedGPACardLine.setMinimumSize(QSize(1, 50))
        self.ExpectedGPACardLine.setMaximumSize(QSize(1, 50))
        self.ExpectedGPACardLine.setStyleSheet(u"background-color: \"white\";")
        self.ExpectedGPACardLine.setFrameShape(QFrame.Shape.VLine)
        self.ExpectedGPACardLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.ExpectedGPACard_Layout.addWidget(self.ExpectedGPACardLine)

        self.ExpectedGPAScore_Layout = QVBoxLayout()
        self.ExpectedGPAScore_Layout.setSpacing(0)
        self.ExpectedGPAScore_Layout.setObjectName(u"ExpectedGPAScore_Layout")
        self.ExpectedGPAScoreNameValueLabel = QLabel(self.ExpectedGPACard)
        self.ExpectedGPAScoreNameValueLabel.setObjectName(u"ExpectedGPAScoreNameValueLabel")
        self.ExpectedGPAScoreNameValueLabel.setFont(font3)
        self.ExpectedGPAScoreNameValueLabel.setStyleSheet(u"background-color: none;")

        self.ExpectedGPAScore_Layout.addWidget(self.ExpectedGPAScoreNameValueLabel)

        self.ExpectedGPAScoreCodeValueLabel = QLabel(self.ExpectedGPACard)
        self.ExpectedGPAScoreCodeValueLabel.setObjectName(u"ExpectedGPAScoreCodeValueLabel")
        self.ExpectedGPAScoreCodeValueLabel.setFont(font3)
        self.ExpectedGPAScoreCodeValueLabel.setStyleSheet(u"background-color: none;")

        self.ExpectedGPAScore_Layout.addWidget(self.ExpectedGPAScoreCodeValueLabel)


        self.ExpectedGPACard_Layout.addLayout(self.ExpectedGPAScore_Layout)


        self.FinalGPAPredictorPage_Layout.addWidget(self.ExpectedGPACard)

        self.FinalGPAPredictorPageSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.FinalGPAPredictorPage_Layout.addItem(self.FinalGPAPredictorPageSpacer)

        self.AIPageStackedWidget.addWidget(self.FinalGPAPredictorPage)

        self.AIPageWidget_Layout.addWidget(self.AIPageStackedWidget, 1, 0, 1, 3)

        self.StackedWidget.addWidget(self.AIPage)
        self.CoursesPage = QWidget()
        self.CoursesPage.setObjectName(u"CoursesPage")
        self.CoursesPage.setMinimumSize(QSize(825, 640))
        self.CoursesPage.setMaximumSize(QSize(825, 640))
        self.CoursesPage.setFont(font2)
        self.CoursesPage.setStyleSheet(u"")
        self.CoursesPageWidget = QWidget(self.CoursesPage)
        self.CoursesPageWidget.setObjectName(u"CoursesPageWidget")
        self.CoursesPageWidget.setGeometry(QRect(0, 0, 825, 640))
        self.CoursesPageWidget.setMinimumSize(QSize(825, 640))
        self.CoursesPageWidget.setMaximumSize(QSize(825, 640))
        self.CoursesPageWidget.setAutoFillBackground(False)
        self.CoursesPageWidget.setStyleSheet(u"")
        self.CoursesPageWidget_Layout = QGridLayout(self.CoursesPageWidget)
        self.CoursesPageWidget_Layout.setSpacing(5)
        self.CoursesPageWidget_Layout.setObjectName(u"CoursesPageWidget_Layout")
        self.CoursesPageWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.CurrentCoursesWidget = QWidget(self.CoursesPageWidget)
        self.CurrentCoursesWidget.setObjectName(u"CurrentCoursesWidget")
        self.CurrentCoursesWidget.setMinimumSize(QSize(825, 145))
        self.CurrentCoursesWidget.setMaximumSize(QSize(825, 145))
        self.CurrentCoursesWidget.setFont(font2)
        self.CurrentCoursesWidget.setStyleSheet(u"border-radius: 10px;\n"
"background-color: \"white\";\n"
"color: \"black\";")
        self.CurrentCoursesWidget_Layout = QVBoxLayout(self.CurrentCoursesWidget)
        self.CurrentCoursesWidget_Layout.setSpacing(5)
        self.CurrentCoursesWidget_Layout.setObjectName(u"CurrentCoursesWidget_Layout")
        self.CurrentCoursesWidget_Layout.setContentsMargins(10, 5, 10, 10)
        self.CurrentCoursesLabel = QLabel(self.CurrentCoursesWidget)
        self.CurrentCoursesLabel.setObjectName(u"CurrentCoursesLabel")
        self.CurrentCoursesLabel.setFont(font3)
        self.CurrentCoursesLabel.setStyleSheet(u"background-color: none;")

        self.CurrentCoursesWidget_Layout.addWidget(self.CurrentCoursesLabel)

        self.CurrentCoursesScrollArea = QScrollArea(self.CurrentCoursesWidget)
        self.CurrentCoursesScrollArea.setObjectName(u"CurrentCoursesScrollArea")
        self.CurrentCoursesScrollArea.setMinimumSize(QSize(805, 100))
        self.CurrentCoursesScrollArea.setMaximumSize(QSize(805, 100))
        self.CurrentCoursesScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.CurrentCoursesScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.CurrentCoursesScrollArea.setWidgetResizable(False)
        self.CurrentCoursesScrollAreaWidget = QWidget()
        self.CurrentCoursesScrollAreaWidget.setObjectName(u"CurrentCoursesScrollAreaWidget")
        self.CurrentCoursesScrollAreaWidget.setGeometry(QRect(0, 0, 1610, 100))
        self.CurrentCoursesScrollAreaWidget.setMinimumSize(QSize(1610, 100))
        self.CurrentCoursesScrollAreaWidget.setMaximumSize(QSize(1610, 100))
        self.CurrentCoursesScrollAreaWidget.setStyleSheet(u"background-color: none;")
        self.CurrentCoursesScrollAreaActualWidget = QWidget(self.CurrentCoursesScrollAreaWidget)
        self.CurrentCoursesScrollAreaActualWidget.setObjectName(u"CurrentCoursesScrollAreaActualWidget")
        self.CurrentCoursesScrollAreaActualWidget.setGeometry(QRect(0, 0, 1345, 100))
        self.CurrentCoursesScrollAreaActualWidget.setMinimumSize(QSize(1345, 100))
        self.CurrentCoursesScrollAreaActualWidget.setMaximumSize(QSize(1345, 100))
        self.CurrentCoursesScrollAreaActualWidget.setStyleSheet(u"")
        self.CurrentCoursesScrollAreaActualWidget_Layout = QHBoxLayout(self.CurrentCoursesScrollAreaActualWidget)
        self.CurrentCoursesScrollAreaActualWidget_Layout.setSpacing(5)
        self.CurrentCoursesScrollAreaActualWidget_Layout.setObjectName(u"CurrentCoursesScrollAreaActualWidget_Layout")
        self.CurrentCoursesScrollAreaActualWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.CurrentCourse_1 = QWidget(self.CurrentCoursesScrollAreaActualWidget)
        self.CurrentCourse_1.setObjectName(u"CurrentCourse_1")
        self.CurrentCourse_1.setMinimumSize(QSize(265, 100))
        self.CurrentCourse_1.setMaximumSize(QSize(265, 100))
        self.CurrentCourse_1.setFont(font2)
        self.CurrentCourse_1.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(106, 69, 57),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.CurrentCourse_Layout_1 = QVBoxLayout(self.CurrentCourse_1)
        self.CurrentCourse_Layout_1.setSpacing(0)
        self.CurrentCourse_Layout_1.setObjectName(u"CurrentCourse_Layout_1")
        self.CurrentCourse_Layout_1.setContentsMargins(10, 5, 10, 10)
        self.CurrentCourseID_Hours_Layout_1 = QHBoxLayout()
        self.CurrentCourseID_Hours_Layout_1.setSpacing(5)
        self.CurrentCourseID_Hours_Layout_1.setObjectName(u"CurrentCourseID_Hours_Layout_1")
        self.CurrentCourseIDLabel_1 = QLabel(self.CurrentCourse_1)
        self.CurrentCourseIDLabel_1.setObjectName(u"CurrentCourseIDLabel_1")
        self.CurrentCourseIDLabel_1.setFont(font3)
        self.CurrentCourseIDLabel_1.setStyleSheet(u"background-color: none;")

        self.CurrentCourseID_Hours_Layout_1.addWidget(self.CurrentCourseIDLabel_1)

        self.CurrentCourseIDValueLabel_1 = QLabel(self.CurrentCourse_1)
        self.CurrentCourseIDValueLabel_1.setObjectName(u"CurrentCourseIDValueLabel_1")
        self.CurrentCourseIDValueLabel_1.setFont(font4)
        self.CurrentCourseIDValueLabel_1.setStyleSheet(u"background-color: none;")

        self.CurrentCourseID_Hours_Layout_1.addWidget(self.CurrentCourseIDValueLabel_1)

        self.CurrentCourseID_HoursSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CurrentCourseID_Hours_Layout_1.addItem(self.CurrentCourseID_HoursSpacer_1)

        self.CurrentCourseHoursLabel_1 = QLabel(self.CurrentCourse_1)
        self.CurrentCourseHoursLabel_1.setObjectName(u"CurrentCourseHoursLabel_1")
        self.CurrentCourseHoursLabel_1.setFont(font3)
        self.CurrentCourseHoursLabel_1.setStyleSheet(u"background-color: none;")

        self.CurrentCourseID_Hours_Layout_1.addWidget(self.CurrentCourseHoursLabel_1)

        self.CurrentCourseHoursValueLabel_1 = QLabel(self.CurrentCourse_1)
        self.CurrentCourseHoursValueLabel_1.setObjectName(u"CurrentCourseHoursValueLabel_1")
        self.CurrentCourseHoursValueLabel_1.setFont(font4)
        self.CurrentCourseHoursValueLabel_1.setStyleSheet(u"background-color: none;")

        self.CurrentCourseID_Hours_Layout_1.addWidget(self.CurrentCourseHoursValueLabel_1)


        self.CurrentCourse_Layout_1.addLayout(self.CurrentCourseID_Hours_Layout_1)

        self.CurrentCoursePermission_Layout_1 = QHBoxLayout()
        self.CurrentCoursePermission_Layout_1.setSpacing(5)
        self.CurrentCoursePermission_Layout_1.setObjectName(u"CurrentCoursePermission_Layout_1")
        self.CurrentCoursePermissionLabel_1 = QLabel(self.CurrentCourse_1)
        self.CurrentCoursePermissionLabel_1.setObjectName(u"CurrentCoursePermissionLabel_1")
        self.CurrentCoursePermissionLabel_1.setFont(font3)
        self.CurrentCoursePermissionLabel_1.setStyleSheet(u"background-color: none;")

        self.CurrentCoursePermission_Layout_1.addWidget(self.CurrentCoursePermissionLabel_1)

        self.CurrentCoursePermissionValueLabel_1 = QLabel(self.CurrentCourse_1)
        self.CurrentCoursePermissionValueLabel_1.setObjectName(u"CurrentCoursePermissionValueLabel_1")
        self.CurrentCoursePermissionValueLabel_1.setFont(font4)
        self.CurrentCoursePermissionValueLabel_1.setStyleSheet(u"background-color: none;")

        self.CurrentCoursePermission_Layout_1.addWidget(self.CurrentCoursePermissionValueLabel_1)

        self.CurrentCoursePermissionSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CurrentCoursePermission_Layout_1.addItem(self.CurrentCoursePermissionSpacer_1)


        self.CurrentCourse_Layout_1.addLayout(self.CurrentCoursePermission_Layout_1)

        self.CurrentCourseDoctor_Layout_1 = QHBoxLayout()
        self.CurrentCourseDoctor_Layout_1.setSpacing(5)
        self.CurrentCourseDoctor_Layout_1.setObjectName(u"CurrentCourseDoctor_Layout_1")
        self.CurrentCourseDoctorLabel_1 = QLabel(self.CurrentCourse_1)
        self.CurrentCourseDoctorLabel_1.setObjectName(u"CurrentCourseDoctorLabel_1")
        self.CurrentCourseDoctorLabel_1.setFont(font3)
        self.CurrentCourseDoctorLabel_1.setStyleSheet(u"background-color: none;")

        self.CurrentCourseDoctor_Layout_1.addWidget(self.CurrentCourseDoctorLabel_1)

        self.CurrentCourseDoctorValueLabel_1 = QLabel(self.CurrentCourse_1)
        self.CurrentCourseDoctorValueLabel_1.setObjectName(u"CurrentCourseDoctorValueLabel_1")
        self.CurrentCourseDoctorValueLabel_1.setFont(font4)
        self.CurrentCourseDoctorValueLabel_1.setStyleSheet(u"background-color: none;")

        self.CurrentCourseDoctor_Layout_1.addWidget(self.CurrentCourseDoctorValueLabel_1)

        self.CurrentCourseDoctorSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CurrentCourseDoctor_Layout_1.addItem(self.CurrentCourseDoctorSpacer_1)


        self.CurrentCourse_Layout_1.addLayout(self.CurrentCourseDoctor_Layout_1)


        self.CurrentCoursesScrollAreaActualWidget_Layout.addWidget(self.CurrentCourse_1)

        self.CurrentCourse_2 = QWidget(self.CurrentCoursesScrollAreaActualWidget)
        self.CurrentCourse_2.setObjectName(u"CurrentCourse_2")
        self.CurrentCourse_2.setMinimumSize(QSize(265, 100))
        self.CurrentCourse_2.setMaximumSize(QSize(265, 100))
        self.CurrentCourse_2.setFont(font2)
        self.CurrentCourse_2.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(106, 69, 57),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.CurrentCourse_Layout_2 = QVBoxLayout(self.CurrentCourse_2)
        self.CurrentCourse_Layout_2.setSpacing(0)
        self.CurrentCourse_Layout_2.setObjectName(u"CurrentCourse_Layout_2")
        self.CurrentCourse_Layout_2.setContentsMargins(10, 5, 10, 10)
        self.CurrentCourseID_Hours_Layout_2 = QHBoxLayout()
        self.CurrentCourseID_Hours_Layout_2.setSpacing(5)
        self.CurrentCourseID_Hours_Layout_2.setObjectName(u"CurrentCourseID_Hours_Layout_2")
        self.CurrentCourseIDLabel_2 = QLabel(self.CurrentCourse_2)
        self.CurrentCourseIDLabel_2.setObjectName(u"CurrentCourseIDLabel_2")
        self.CurrentCourseIDLabel_2.setFont(font3)
        self.CurrentCourseIDLabel_2.setStyleSheet(u"background-color: none;")

        self.CurrentCourseID_Hours_Layout_2.addWidget(self.CurrentCourseIDLabel_2)

        self.CurrentCourseIDValueLabel_2 = QLabel(self.CurrentCourse_2)
        self.CurrentCourseIDValueLabel_2.setObjectName(u"CurrentCourseIDValueLabel_2")
        self.CurrentCourseIDValueLabel_2.setFont(font4)
        self.CurrentCourseIDValueLabel_2.setStyleSheet(u"background-color: none;")

        self.CurrentCourseID_Hours_Layout_2.addWidget(self.CurrentCourseIDValueLabel_2)

        self.CurrentCourseIDSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CurrentCourseID_Hours_Layout_2.addItem(self.CurrentCourseIDSpacer_2)

        self.CurrentCourseHoursLabel_2 = QLabel(self.CurrentCourse_2)
        self.CurrentCourseHoursLabel_2.setObjectName(u"CurrentCourseHoursLabel_2")
        self.CurrentCourseHoursLabel_2.setFont(font3)
        self.CurrentCourseHoursLabel_2.setStyleSheet(u"background-color: none;")

        self.CurrentCourseID_Hours_Layout_2.addWidget(self.CurrentCourseHoursLabel_2)

        self.CurrentCourseHoursValueLabel_2 = QLabel(self.CurrentCourse_2)
        self.CurrentCourseHoursValueLabel_2.setObjectName(u"CurrentCourseHoursValueLabel_2")
        self.CurrentCourseHoursValueLabel_2.setFont(font4)
        self.CurrentCourseHoursValueLabel_2.setStyleSheet(u"background-color: none;")

        self.CurrentCourseID_Hours_Layout_2.addWidget(self.CurrentCourseHoursValueLabel_2)


        self.CurrentCourse_Layout_2.addLayout(self.CurrentCourseID_Hours_Layout_2)

        self.CurrentCoursePermission_Layout_2 = QHBoxLayout()
        self.CurrentCoursePermission_Layout_2.setSpacing(5)
        self.CurrentCoursePermission_Layout_2.setObjectName(u"CurrentCoursePermission_Layout_2")
        self.CurrentCoursePermissionLabel_2 = QLabel(self.CurrentCourse_2)
        self.CurrentCoursePermissionLabel_2.setObjectName(u"CurrentCoursePermissionLabel_2")
        self.CurrentCoursePermissionLabel_2.setFont(font3)
        self.CurrentCoursePermissionLabel_2.setStyleSheet(u"background-color: none;")

        self.CurrentCoursePermission_Layout_2.addWidget(self.CurrentCoursePermissionLabel_2)

        self.CurrentCoursePermissionValueLabel_2 = QLabel(self.CurrentCourse_2)
        self.CurrentCoursePermissionValueLabel_2.setObjectName(u"CurrentCoursePermissionValueLabel_2")
        self.CurrentCoursePermissionValueLabel_2.setFont(font4)
        self.CurrentCoursePermissionValueLabel_2.setStyleSheet(u"background-color: none;")

        self.CurrentCoursePermission_Layout_2.addWidget(self.CurrentCoursePermissionValueLabel_2)

        self.CurrentCoursePermissionSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CurrentCoursePermission_Layout_2.addItem(self.CurrentCoursePermissionSpacer_2)


        self.CurrentCourse_Layout_2.addLayout(self.CurrentCoursePermission_Layout_2)

        self.CurrentCourseDoctor_Layout_2 = QHBoxLayout()
        self.CurrentCourseDoctor_Layout_2.setSpacing(5)
        self.CurrentCourseDoctor_Layout_2.setObjectName(u"CurrentCourseDoctor_Layout_2")
        self.CurrentCourseDoctorLabel_2 = QLabel(self.CurrentCourse_2)
        self.CurrentCourseDoctorLabel_2.setObjectName(u"CurrentCourseDoctorLabel_2")
        self.CurrentCourseDoctorLabel_2.setFont(font3)
        self.CurrentCourseDoctorLabel_2.setStyleSheet(u"background-color: none;")

        self.CurrentCourseDoctor_Layout_2.addWidget(self.CurrentCourseDoctorLabel_2)

        self.CurrentCourseDoctorValueLabel_2 = QLabel(self.CurrentCourse_2)
        self.CurrentCourseDoctorValueLabel_2.setObjectName(u"CurrentCourseDoctorValueLabel_2")
        self.CurrentCourseDoctorValueLabel_2.setFont(font4)
        self.CurrentCourseDoctorValueLabel_2.setStyleSheet(u"background-color: none;")

        self.CurrentCourseDoctor_Layout_2.addWidget(self.CurrentCourseDoctorValueLabel_2)

        self.CurrentCourseDoctorSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CurrentCourseDoctor_Layout_2.addItem(self.CurrentCourseDoctorSpacer_2)


        self.CurrentCourse_Layout_2.addLayout(self.CurrentCourseDoctor_Layout_2)


        self.CurrentCoursesScrollAreaActualWidget_Layout.addWidget(self.CurrentCourse_2)

        self.CurrentCourse_3 = QWidget(self.CurrentCoursesScrollAreaActualWidget)
        self.CurrentCourse_3.setObjectName(u"CurrentCourse_3")
        self.CurrentCourse_3.setMinimumSize(QSize(265, 100))
        self.CurrentCourse_3.setMaximumSize(QSize(265, 100))
        self.CurrentCourse_3.setFont(font2)
        self.CurrentCourse_3.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(106, 69, 57),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.CurrentCourse_Layout_3 = QVBoxLayout(self.CurrentCourse_3)
        self.CurrentCourse_Layout_3.setSpacing(0)
        self.CurrentCourse_Layout_3.setObjectName(u"CurrentCourse_Layout_3")
        self.CurrentCourse_Layout_3.setContentsMargins(10, 5, 10, 10)
        self.CurrentCourseID_Hours_Layout_3 = QHBoxLayout()
        self.CurrentCourseID_Hours_Layout_3.setSpacing(5)
        self.CurrentCourseID_Hours_Layout_3.setObjectName(u"CurrentCourseID_Hours_Layout_3")
        self.CurrentCourseIDLabel_3 = QLabel(self.CurrentCourse_3)
        self.CurrentCourseIDLabel_3.setObjectName(u"CurrentCourseIDLabel_3")
        self.CurrentCourseIDLabel_3.setFont(font3)
        self.CurrentCourseIDLabel_3.setStyleSheet(u"background-color: none;")

        self.CurrentCourseID_Hours_Layout_3.addWidget(self.CurrentCourseIDLabel_3)

        self.CurrentCourseIDValueLabel_3 = QLabel(self.CurrentCourse_3)
        self.CurrentCourseIDValueLabel_3.setObjectName(u"CurrentCourseIDValueLabel_3")
        self.CurrentCourseIDValueLabel_3.setFont(font4)
        self.CurrentCourseIDValueLabel_3.setStyleSheet(u"background-color: none;")

        self.CurrentCourseID_Hours_Layout_3.addWidget(self.CurrentCourseIDValueLabel_3)

        self.CurrentCourseIDSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CurrentCourseID_Hours_Layout_3.addItem(self.CurrentCourseIDSpacer_3)

        self.CurrentCourseHoursLabel_3 = QLabel(self.CurrentCourse_3)
        self.CurrentCourseHoursLabel_3.setObjectName(u"CurrentCourseHoursLabel_3")
        self.CurrentCourseHoursLabel_3.setFont(font3)
        self.CurrentCourseHoursLabel_3.setStyleSheet(u"background-color: none;")

        self.CurrentCourseID_Hours_Layout_3.addWidget(self.CurrentCourseHoursLabel_3)

        self.CurrentCourseHoursValueLabel_3 = QLabel(self.CurrentCourse_3)
        self.CurrentCourseHoursValueLabel_3.setObjectName(u"CurrentCourseHoursValueLabel_3")
        self.CurrentCourseHoursValueLabel_3.setFont(font4)
        self.CurrentCourseHoursValueLabel_3.setStyleSheet(u"background-color: none;")

        self.CurrentCourseID_Hours_Layout_3.addWidget(self.CurrentCourseHoursValueLabel_3)


        self.CurrentCourse_Layout_3.addLayout(self.CurrentCourseID_Hours_Layout_3)

        self.CurrentCoursePermission_Layout_3 = QHBoxLayout()
        self.CurrentCoursePermission_Layout_3.setSpacing(5)
        self.CurrentCoursePermission_Layout_3.setObjectName(u"CurrentCoursePermission_Layout_3")
        self.CurrentCoursePermissionLabel_3 = QLabel(self.CurrentCourse_3)
        self.CurrentCoursePermissionLabel_3.setObjectName(u"CurrentCoursePermissionLabel_3")
        self.CurrentCoursePermissionLabel_3.setFont(font3)
        self.CurrentCoursePermissionLabel_3.setStyleSheet(u"background-color: none;")

        self.CurrentCoursePermission_Layout_3.addWidget(self.CurrentCoursePermissionLabel_3)

        self.CurrentCoursePermissionValueLabel_3 = QLabel(self.CurrentCourse_3)
        self.CurrentCoursePermissionValueLabel_3.setObjectName(u"CurrentCoursePermissionValueLabel_3")
        self.CurrentCoursePermissionValueLabel_3.setFont(font4)
        self.CurrentCoursePermissionValueLabel_3.setStyleSheet(u"background-color: none;")

        self.CurrentCoursePermission_Layout_3.addWidget(self.CurrentCoursePermissionValueLabel_3)

        self.CurrentCoursePermissionSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CurrentCoursePermission_Layout_3.addItem(self.CurrentCoursePermissionSpacer_3)


        self.CurrentCourse_Layout_3.addLayout(self.CurrentCoursePermission_Layout_3)

        self.CurrentCourseDoctor_Layout_3 = QHBoxLayout()
        self.CurrentCourseDoctor_Layout_3.setSpacing(5)
        self.CurrentCourseDoctor_Layout_3.setObjectName(u"CurrentCourseDoctor_Layout_3")
        self.CurrentCourseDoctorLabel_3 = QLabel(self.CurrentCourse_3)
        self.CurrentCourseDoctorLabel_3.setObjectName(u"CurrentCourseDoctorLabel_3")
        self.CurrentCourseDoctorLabel_3.setFont(font3)
        self.CurrentCourseDoctorLabel_3.setStyleSheet(u"background-color: none;")

        self.CurrentCourseDoctor_Layout_3.addWidget(self.CurrentCourseDoctorLabel_3)

        self.CurrentCourseDoctorValueLabel_3 = QLabel(self.CurrentCourse_3)
        self.CurrentCourseDoctorValueLabel_3.setObjectName(u"CurrentCourseDoctorValueLabel_3")
        self.CurrentCourseDoctorValueLabel_3.setFont(font4)
        self.CurrentCourseDoctorValueLabel_3.setStyleSheet(u"background-color: none;")

        self.CurrentCourseDoctor_Layout_3.addWidget(self.CurrentCourseDoctorValueLabel_3)

        self.CurrentCourseDoctorSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CurrentCourseDoctor_Layout_3.addItem(self.CurrentCourseDoctorSpacer_3)


        self.CurrentCourse_Layout_3.addLayout(self.CurrentCourseDoctor_Layout_3)


        self.CurrentCoursesScrollAreaActualWidget_Layout.addWidget(self.CurrentCourse_3)

        self.CurrentCourse_4 = QWidget(self.CurrentCoursesScrollAreaActualWidget)
        self.CurrentCourse_4.setObjectName(u"CurrentCourse_4")
        self.CurrentCourse_4.setMinimumSize(QSize(265, 100))
        self.CurrentCourse_4.setMaximumSize(QSize(265, 100))
        self.CurrentCourse_4.setFont(font2)
        self.CurrentCourse_4.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(106, 69, 57),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.CurrentCourse_Layout_4 = QVBoxLayout(self.CurrentCourse_4)
        self.CurrentCourse_Layout_4.setSpacing(0)
        self.CurrentCourse_Layout_4.setObjectName(u"CurrentCourse_Layout_4")
        self.CurrentCourse_Layout_4.setContentsMargins(10, 5, 10, 10)
        self.CurrentCourseID_Hours_Layout_4 = QHBoxLayout()
        self.CurrentCourseID_Hours_Layout_4.setSpacing(5)
        self.CurrentCourseID_Hours_Layout_4.setObjectName(u"CurrentCourseID_Hours_Layout_4")
        self.CurrentCourseIDLabel_4 = QLabel(self.CurrentCourse_4)
        self.CurrentCourseIDLabel_4.setObjectName(u"CurrentCourseIDLabel_4")
        self.CurrentCourseIDLabel_4.setFont(font3)
        self.CurrentCourseIDLabel_4.setStyleSheet(u"background-color: none;")

        self.CurrentCourseID_Hours_Layout_4.addWidget(self.CurrentCourseIDLabel_4)

        self.CurrentCourseIDValueLabel_4 = QLabel(self.CurrentCourse_4)
        self.CurrentCourseIDValueLabel_4.setObjectName(u"CurrentCourseIDValueLabel_4")
        self.CurrentCourseIDValueLabel_4.setFont(font4)
        self.CurrentCourseIDValueLabel_4.setStyleSheet(u"background-color: none;")

        self.CurrentCourseID_Hours_Layout_4.addWidget(self.CurrentCourseIDValueLabel_4)

        self.CurrentCourseIDSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CurrentCourseID_Hours_Layout_4.addItem(self.CurrentCourseIDSpacer_4)

        self.CurrentCourseHoursLabel_4 = QLabel(self.CurrentCourse_4)
        self.CurrentCourseHoursLabel_4.setObjectName(u"CurrentCourseHoursLabel_4")
        self.CurrentCourseHoursLabel_4.setFont(font3)
        self.CurrentCourseHoursLabel_4.setStyleSheet(u"background-color: none;")

        self.CurrentCourseID_Hours_Layout_4.addWidget(self.CurrentCourseHoursLabel_4)

        self.CurrentCourseHoursValueLabel_4 = QLabel(self.CurrentCourse_4)
        self.CurrentCourseHoursValueLabel_4.setObjectName(u"CurrentCourseHoursValueLabel_4")
        self.CurrentCourseHoursValueLabel_4.setFont(font4)
        self.CurrentCourseHoursValueLabel_4.setStyleSheet(u"background-color: none;")

        self.CurrentCourseID_Hours_Layout_4.addWidget(self.CurrentCourseHoursValueLabel_4)


        self.CurrentCourse_Layout_4.addLayout(self.CurrentCourseID_Hours_Layout_4)

        self.CurrentCoursePermission_Layout_4 = QHBoxLayout()
        self.CurrentCoursePermission_Layout_4.setSpacing(5)
        self.CurrentCoursePermission_Layout_4.setObjectName(u"CurrentCoursePermission_Layout_4")
        self.CurrentCoursePermissionLabel_4 = QLabel(self.CurrentCourse_4)
        self.CurrentCoursePermissionLabel_4.setObjectName(u"CurrentCoursePermissionLabel_4")
        self.CurrentCoursePermissionLabel_4.setFont(font3)
        self.CurrentCoursePermissionLabel_4.setStyleSheet(u"background-color: none;")

        self.CurrentCoursePermission_Layout_4.addWidget(self.CurrentCoursePermissionLabel_4)

        self.CurrentCoursePermissionValueLabel_4 = QLabel(self.CurrentCourse_4)
        self.CurrentCoursePermissionValueLabel_4.setObjectName(u"CurrentCoursePermissionValueLabel_4")
        self.CurrentCoursePermissionValueLabel_4.setFont(font4)
        self.CurrentCoursePermissionValueLabel_4.setStyleSheet(u"background-color: none;")

        self.CurrentCoursePermission_Layout_4.addWidget(self.CurrentCoursePermissionValueLabel_4)

        self.CurrentCoursePermissionSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CurrentCoursePermission_Layout_4.addItem(self.CurrentCoursePermissionSpacer_4)


        self.CurrentCourse_Layout_4.addLayout(self.CurrentCoursePermission_Layout_4)

        self.CurrentCourseDoctor_Layout_4 = QHBoxLayout()
        self.CurrentCourseDoctor_Layout_4.setSpacing(5)
        self.CurrentCourseDoctor_Layout_4.setObjectName(u"CurrentCourseDoctor_Layout_4")
        self.CurrentCourseDoctorLabel_4 = QLabel(self.CurrentCourse_4)
        self.CurrentCourseDoctorLabel_4.setObjectName(u"CurrentCourseDoctorLabel_4")
        self.CurrentCourseDoctorLabel_4.setFont(font3)
        self.CurrentCourseDoctorLabel_4.setStyleSheet(u"background-color: none;")

        self.CurrentCourseDoctor_Layout_4.addWidget(self.CurrentCourseDoctorLabel_4)

        self.CurrentCourseDoctorValueLabel_4 = QLabel(self.CurrentCourse_4)
        self.CurrentCourseDoctorValueLabel_4.setObjectName(u"CurrentCourseDoctorValueLabel_4")
        self.CurrentCourseDoctorValueLabel_4.setFont(font4)
        self.CurrentCourseDoctorValueLabel_4.setStyleSheet(u"background-color: none;")

        self.CurrentCourseDoctor_Layout_4.addWidget(self.CurrentCourseDoctorValueLabel_4)

        self.CurrentCourseDoctorSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CurrentCourseDoctor_Layout_4.addItem(self.CurrentCourseDoctorSpacer_4)


        self.CurrentCourse_Layout_4.addLayout(self.CurrentCourseDoctor_Layout_4)


        self.CurrentCoursesScrollAreaActualWidget_Layout.addWidget(self.CurrentCourse_4)

        self.CurrentCourse_5 = QWidget(self.CurrentCoursesScrollAreaActualWidget)
        self.CurrentCourse_5.setObjectName(u"CurrentCourse_5")
        self.CurrentCourse_5.setMinimumSize(QSize(265, 100))
        self.CurrentCourse_5.setMaximumSize(QSize(265, 100))
        self.CurrentCourse_5.setFont(font2)
        self.CurrentCourse_5.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(106, 69, 57),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.CurrentCourse_Layout_5 = QVBoxLayout(self.CurrentCourse_5)
        self.CurrentCourse_Layout_5.setSpacing(0)
        self.CurrentCourse_Layout_5.setObjectName(u"CurrentCourse_Layout_5")
        self.CurrentCourse_Layout_5.setContentsMargins(10, 5, 10, 10)
        self.CurrentCourseID_Hours_Layout_5 = QHBoxLayout()
        self.CurrentCourseID_Hours_Layout_5.setSpacing(5)
        self.CurrentCourseID_Hours_Layout_5.setObjectName(u"CurrentCourseID_Hours_Layout_5")
        self.CurrentCourseIDLabel_5 = QLabel(self.CurrentCourse_5)
        self.CurrentCourseIDLabel_5.setObjectName(u"CurrentCourseIDLabel_5")
        self.CurrentCourseIDLabel_5.setFont(font3)
        self.CurrentCourseIDLabel_5.setStyleSheet(u"background-color: none;")

        self.CurrentCourseID_Hours_Layout_5.addWidget(self.CurrentCourseIDLabel_5)

        self.CurrentCourseIDValueLabel_5 = QLabel(self.CurrentCourse_5)
        self.CurrentCourseIDValueLabel_5.setObjectName(u"CurrentCourseIDValueLabel_5")
        self.CurrentCourseIDValueLabel_5.setFont(font4)
        self.CurrentCourseIDValueLabel_5.setStyleSheet(u"background-color: none;")

        self.CurrentCourseID_Hours_Layout_5.addWidget(self.CurrentCourseIDValueLabel_5)

        self.CurrentCourseIDSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CurrentCourseID_Hours_Layout_5.addItem(self.CurrentCourseIDSpacer_5)

        self.CurrentCourseHoursLabel_5 = QLabel(self.CurrentCourse_5)
        self.CurrentCourseHoursLabel_5.setObjectName(u"CurrentCourseHoursLabel_5")
        self.CurrentCourseHoursLabel_5.setFont(font3)
        self.CurrentCourseHoursLabel_5.setStyleSheet(u"background-color: none;")

        self.CurrentCourseID_Hours_Layout_5.addWidget(self.CurrentCourseHoursLabel_5)

        self.CurrentCourseHoursValueLabel_5 = QLabel(self.CurrentCourse_5)
        self.CurrentCourseHoursValueLabel_5.setObjectName(u"CurrentCourseHoursValueLabel_5")
        self.CurrentCourseHoursValueLabel_5.setFont(font4)
        self.CurrentCourseHoursValueLabel_5.setStyleSheet(u"background-color: none;")

        self.CurrentCourseID_Hours_Layout_5.addWidget(self.CurrentCourseHoursValueLabel_5)


        self.CurrentCourse_Layout_5.addLayout(self.CurrentCourseID_Hours_Layout_5)

        self.CurrentCoursePermission_Layout_5 = QHBoxLayout()
        self.CurrentCoursePermission_Layout_5.setSpacing(5)
        self.CurrentCoursePermission_Layout_5.setObjectName(u"CurrentCoursePermission_Layout_5")
        self.CurrentCoursePermissionLabel_5 = QLabel(self.CurrentCourse_5)
        self.CurrentCoursePermissionLabel_5.setObjectName(u"CurrentCoursePermissionLabel_5")
        self.CurrentCoursePermissionLabel_5.setFont(font3)
        self.CurrentCoursePermissionLabel_5.setStyleSheet(u"background-color: none;")

        self.CurrentCoursePermission_Layout_5.addWidget(self.CurrentCoursePermissionLabel_5)

        self.CurrentCoursePermissionValueLabel_5 = QLabel(self.CurrentCourse_5)
        self.CurrentCoursePermissionValueLabel_5.setObjectName(u"CurrentCoursePermissionValueLabel_5")
        self.CurrentCoursePermissionValueLabel_5.setFont(font4)
        self.CurrentCoursePermissionValueLabel_5.setStyleSheet(u"background-color: none;")

        self.CurrentCoursePermission_Layout_5.addWidget(self.CurrentCoursePermissionValueLabel_5)

        self.CurrentCoursePermissionSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CurrentCoursePermission_Layout_5.addItem(self.CurrentCoursePermissionSpacer_5)


        self.CurrentCourse_Layout_5.addLayout(self.CurrentCoursePermission_Layout_5)

        self.CurrentCourseDoctor_Layout_5 = QHBoxLayout()
        self.CurrentCourseDoctor_Layout_5.setSpacing(5)
        self.CurrentCourseDoctor_Layout_5.setObjectName(u"CurrentCourseDoctor_Layout_5")
        self.CurrentCourseDoctorLabel_5 = QLabel(self.CurrentCourse_5)
        self.CurrentCourseDoctorLabel_5.setObjectName(u"CurrentCourseDoctorLabel_5")
        self.CurrentCourseDoctorLabel_5.setFont(font3)
        self.CurrentCourseDoctorLabel_5.setStyleSheet(u"background-color: none;")

        self.CurrentCourseDoctor_Layout_5.addWidget(self.CurrentCourseDoctorLabel_5)

        self.CurrentCourseDoctorValueLabel_5 = QLabel(self.CurrentCourse_5)
        self.CurrentCourseDoctorValueLabel_5.setObjectName(u"CurrentCourseDoctorValueLabel_5")
        self.CurrentCourseDoctorValueLabel_5.setFont(font4)
        self.CurrentCourseDoctorValueLabel_5.setStyleSheet(u"background-color: none;")

        self.CurrentCourseDoctor_Layout_5.addWidget(self.CurrentCourseDoctorValueLabel_5)

        self.CurrentCourseDoctorSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CurrentCourseDoctor_Layout_5.addItem(self.CurrentCourseDoctorSpacer_5)


        self.CurrentCourse_Layout_5.addLayout(self.CurrentCourseDoctor_Layout_5)


        self.CurrentCoursesScrollAreaActualWidget_Layout.addWidget(self.CurrentCourse_5)

        self.CurrentCoursesScrollAreaSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CurrentCoursesScrollAreaActualWidget_Layout.addItem(self.CurrentCoursesScrollAreaSpacer)

        self.CurrentCoursesScrollArea.setWidget(self.CurrentCoursesScrollAreaWidget)

        self.CurrentCoursesWidget_Layout.addWidget(self.CurrentCoursesScrollArea)


        self.CoursesPageWidget_Layout.addWidget(self.CurrentCoursesWidget, 0, 0, 1, 4)

        self.RemainingCoursesWidget = QWidget(self.CoursesPageWidget)
        self.RemainingCoursesWidget.setObjectName(u"RemainingCoursesWidget")
        self.RemainingCoursesWidget.setMinimumSize(QSize(270, 380))
        self.RemainingCoursesWidget.setMaximumSize(QSize(270, 380))
        self.RemainingCoursesWidget.setFont(font2)
        self.RemainingCoursesWidget.setStyleSheet(u"border-radius: 10px;\n"
"background-color: \"white\";\n"
"color: \"black\";")
        self.RemainingCoursesWidget_Layout = QVBoxLayout(self.RemainingCoursesWidget)
        self.RemainingCoursesWidget_Layout.setSpacing(5)
        self.RemainingCoursesWidget_Layout.setObjectName(u"RemainingCoursesWidget_Layout")
        self.RemainingCoursesWidget_Layout.setContentsMargins(10, 5, 10, 10)
        self.RemainingCoursesLabel = QLabel(self.RemainingCoursesWidget)
        self.RemainingCoursesLabel.setObjectName(u"RemainingCoursesLabel")
        self.RemainingCoursesLabel.setFont(font3)
        self.RemainingCoursesLabel.setStyleSheet(u"background-color: none;")

        self.RemainingCoursesWidget_Layout.addWidget(self.RemainingCoursesLabel)

        self.RemainingCoursesValueLabel = QLabel(self.RemainingCoursesWidget)
        self.RemainingCoursesValueLabel.setObjectName(u"RemainingCoursesValueLabel")
        self.RemainingCoursesValueLabel.setFont(font4)
        self.RemainingCoursesValueLabel.setStyleSheet(u"background-color: none;")

        self.RemainingCoursesWidget_Layout.addWidget(self.RemainingCoursesValueLabel)

        self.RemainingCoursesScrollArea = QScrollArea(self.RemainingCoursesWidget)
        self.RemainingCoursesScrollArea.setObjectName(u"RemainingCoursesScrollArea")
        self.RemainingCoursesScrollArea.setMinimumSize(QSize(250, 285))
        self.RemainingCoursesScrollArea.setMaximumSize(QSize(250, 285))
        self.RemainingCoursesScrollArea.setStyleSheet(u"")
        self.RemainingCoursesScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.RemainingCoursesScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.RemainingCoursesScrollArea.setWidgetResizable(False)
        self.RemainingCoursesScrollArea.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.RemainingCoursesScrollAreaWidget = QWidget()
        self.RemainingCoursesScrollAreaWidget.setObjectName(u"RemainingCoursesScrollAreaWidget")
        self.RemainingCoursesScrollAreaWidget.setGeometry(QRect(0, 0, 250, 285))
        sizePolicy3.setHeightForWidth(self.RemainingCoursesScrollAreaWidget.sizePolicy().hasHeightForWidth())
        self.RemainingCoursesScrollAreaWidget.setSizePolicy(sizePolicy3)
        self.RemainingCoursesScrollAreaWidget.setMinimumSize(QSize(250, 285))
        self.RemainingCoursesScrollAreaWidget.setMaximumSize(QSize(250, 285))
        self.RemainingCoursesScrollAreaWidget.setStyleSheet(u"background-color: none;")
        self.RemainingCoursesActualScrollAreaWidget = QWidget(self.RemainingCoursesScrollAreaWidget)
        self.RemainingCoursesActualScrollAreaWidget.setObjectName(u"RemainingCoursesActualScrollAreaWidget")
        self.RemainingCoursesActualScrollAreaWidget.setGeometry(QRect(0, 0, 250, 285))
        sizePolicy3.setHeightForWidth(self.RemainingCoursesActualScrollAreaWidget.sizePolicy().hasHeightForWidth())
        self.RemainingCoursesActualScrollAreaWidget.setSizePolicy(sizePolicy3)
        self.RemainingCoursesActualScrollAreaWidget.setMinimumSize(QSize(250, 285))
        self.RemainingCoursesActualScrollAreaWidget.setMaximumSize(QSize(250, 285))
        self.RemainingCoursesActualScrollAreaWidget.setFont(font2)
        self.RemainingCoursesActualScrollAreaWidget.setStyleSheet(u"")
        self.RemainingCoursesActualScrollAreaWidget_Layout = QVBoxLayout(self.RemainingCoursesActualScrollAreaWidget)
        self.RemainingCoursesActualScrollAreaWidget_Layout.setSpacing(5)
        self.RemainingCoursesActualScrollAreaWidget_Layout.setObjectName(u"RemainingCoursesActualScrollAreaWidget_Layout")
        self.RemainingCoursesActualScrollAreaWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.RemainingCourse_1 = QWidget(self.RemainingCoursesActualScrollAreaWidget)
        self.RemainingCourse_1.setObjectName(u"RemainingCourse_1")
        self.RemainingCourse_1.setMinimumSize(QSize(250, 140))
        self.RemainingCourse_1.setMaximumSize(QSize(250, 140))
        self.RemainingCourse_1.setFont(font2)
        self.RemainingCourse_1.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(27, 49, 96),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.PendingCourse_1_Widget_Layout = QVBoxLayout(self.RemainingCourse_1)
        self.PendingCourse_1_Widget_Layout.setSpacing(0)
        self.PendingCourse_1_Widget_Layout.setObjectName(u"PendingCourse_1_Widget_Layout")
        self.PendingCourse_1_Widget_Layout.setContentsMargins(10, 5, 10, 10)
        self.RemainingCourseID_Hours_Layout_1 = QHBoxLayout()
        self.RemainingCourseID_Hours_Layout_1.setSpacing(5)
        self.RemainingCourseID_Hours_Layout_1.setObjectName(u"RemainingCourseID_Hours_Layout_1")
        self.RemainingCourseIDLabel_1 = QLabel(self.RemainingCourse_1)
        self.RemainingCourseIDLabel_1.setObjectName(u"RemainingCourseIDLabel_1")
        self.RemainingCourseIDLabel_1.setFont(font3)
        self.RemainingCourseIDLabel_1.setStyleSheet(u"background-color: none;")

        self.RemainingCourseID_Hours_Layout_1.addWidget(self.RemainingCourseIDLabel_1)

        self.RemainingCourseIDValueLabel_1 = QLabel(self.RemainingCourse_1)
        self.RemainingCourseIDValueLabel_1.setObjectName(u"RemainingCourseIDValueLabel_1")
        self.RemainingCourseIDValueLabel_1.setFont(font4)
        self.RemainingCourseIDValueLabel_1.setStyleSheet(u"background-color: none;")

        self.RemainingCourseID_Hours_Layout_1.addWidget(self.RemainingCourseIDValueLabel_1)

        self.RemainingCourseID_HoursHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.RemainingCourseID_Hours_Layout_1.addItem(self.RemainingCourseID_HoursHorizontalSpacer_1)

        self.RemainingCourseHoursLabel_1 = QLabel(self.RemainingCourse_1)
        self.RemainingCourseHoursLabel_1.setObjectName(u"RemainingCourseHoursLabel_1")
        self.RemainingCourseHoursLabel_1.setFont(font3)
        self.RemainingCourseHoursLabel_1.setStyleSheet(u"background-color: none;")

        self.RemainingCourseID_Hours_Layout_1.addWidget(self.RemainingCourseHoursLabel_1)

        self.RemainingCourseHoursValueLabel_1 = QLabel(self.RemainingCourse_1)
        self.RemainingCourseHoursValueLabel_1.setObjectName(u"RemainingCourseHoursValueLabel_1")
        self.RemainingCourseHoursValueLabel_1.setFont(font4)
        self.RemainingCourseHoursValueLabel_1.setStyleSheet(u"background-color: none;")

        self.RemainingCourseID_Hours_Layout_1.addWidget(self.RemainingCourseHoursValueLabel_1)


        self.PendingCourse_1_Widget_Layout.addLayout(self.RemainingCourseID_Hours_Layout_1)

        self.RemainingCoursePermission_Layout_1 = QHBoxLayout()
        self.RemainingCoursePermission_Layout_1.setSpacing(5)
        self.RemainingCoursePermission_Layout_1.setObjectName(u"RemainingCoursePermission_Layout_1")
        self.RemainingCoursePermissionLabel_1 = QLabel(self.RemainingCourse_1)
        self.RemainingCoursePermissionLabel_1.setObjectName(u"RemainingCoursePermissionLabel_1")
        self.RemainingCoursePermissionLabel_1.setFont(font3)
        self.RemainingCoursePermissionLabel_1.setStyleSheet(u"background-color: none;")

        self.RemainingCoursePermission_Layout_1.addWidget(self.RemainingCoursePermissionLabel_1)

        self.RemainingCoursePermissionValueLabel_1 = QLabel(self.RemainingCourse_1)
        self.RemainingCoursePermissionValueLabel_1.setObjectName(u"RemainingCoursePermissionValueLabel_1")
        self.RemainingCoursePermissionValueLabel_1.setFont(font4)
        self.RemainingCoursePermissionValueLabel_1.setStyleSheet(u"background-color: none;")

        self.RemainingCoursePermission_Layout_1.addWidget(self.RemainingCoursePermissionValueLabel_1)

        self.RemainingCoursePermissionHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.RemainingCoursePermission_Layout_1.addItem(self.RemainingCoursePermissionHorizontalSpacer_1)


        self.PendingCourse_1_Widget_Layout.addLayout(self.RemainingCoursePermission_Layout_1)

        self.RemainingCourseLine_Layout_1 = QHBoxLayout()
        self.RemainingCourseLine_Layout_1.setSpacing(0)
        self.RemainingCourseLine_Layout_1.setObjectName(u"RemainingCourseLine_Layout_1")
        self.RemainingCourseLineLeftHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.RemainingCourseLine_Layout_1.addItem(self.RemainingCourseLineLeftHorizontalSpacer_1)

        self.RemainingCourseLine_1 = QFrame(self.RemainingCourse_1)
        self.RemainingCourseLine_1.setObjectName(u"RemainingCourseLine_1")
        self.RemainingCourseLine_1.setMinimumSize(QSize(100, 1))
        self.RemainingCourseLine_1.setMaximumSize(QSize(100, 1))
        self.RemainingCourseLine_1.setFont(font2)
        self.RemainingCourseLine_1.setStyleSheet(u"background-color: \"white\"")
        self.RemainingCourseLine_1.setFrameShape(QFrame.Shape.HLine)
        self.RemainingCourseLine_1.setFrameShadow(QFrame.Shadow.Sunken)

        self.RemainingCourseLine_Layout_1.addWidget(self.RemainingCourseLine_1)

        self.RemainingCourseLineRightHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.RemainingCourseLine_Layout_1.addItem(self.RemainingCourseLineRightHorizontalSpacer_1)


        self.PendingCourse_1_Widget_Layout.addLayout(self.RemainingCourseLine_Layout_1)

        self.RemainingCourseRemainingStudents_Layout_1 = QHBoxLayout()
        self.RemainingCourseRemainingStudents_Layout_1.setSpacing(5)
        self.RemainingCourseRemainingStudents_Layout_1.setObjectName(u"RemainingCourseRemainingStudents_Layout_1")
        self.RemainingCourseRemainingStudentsLabel_1 = QLabel(self.RemainingCourse_1)
        self.RemainingCourseRemainingStudentsLabel_1.setObjectName(u"RemainingCourseRemainingStudentsLabel_1")
        self.RemainingCourseRemainingStudentsLabel_1.setFont(font3)
        self.RemainingCourseRemainingStudentsLabel_1.setStyleSheet(u"background-color: none;")

        self.RemainingCourseRemainingStudents_Layout_1.addWidget(self.RemainingCourseRemainingStudentsLabel_1)

        self.RemainingCourseRemainingStudentsValueLabel_1 = QLabel(self.RemainingCourse_1)
        self.RemainingCourseRemainingStudentsValueLabel_1.setObjectName(u"RemainingCourseRemainingStudentsValueLabel_1")
        self.RemainingCourseRemainingStudentsValueLabel_1.setFont(font4)
        self.RemainingCourseRemainingStudentsValueLabel_1.setStyleSheet(u"background-color: none;")

        self.RemainingCourseRemainingStudents_Layout_1.addWidget(self.RemainingCourseRemainingStudentsValueLabel_1)

        self.RemainingCourseRemainingStudentsHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.RemainingCourseRemainingStudents_Layout_1.addItem(self.RemainingCourseRemainingStudentsHorizontalSpacer_1)


        self.PendingCourse_1_Widget_Layout.addLayout(self.RemainingCourseRemainingStudents_Layout_1)

        self.RemainingCoursePassRate_Layout_1 = QHBoxLayout()
        self.RemainingCoursePassRate_Layout_1.setSpacing(5)
        self.RemainingCoursePassRate_Layout_1.setObjectName(u"RemainingCoursePassRate_Layout_1")
        self.RemainingCoursePassRateLabel_1 = QLabel(self.RemainingCourse_1)
        self.RemainingCoursePassRateLabel_1.setObjectName(u"RemainingCoursePassRateLabel_1")
        self.RemainingCoursePassRateLabel_1.setFont(font3)
        self.RemainingCoursePassRateLabel_1.setStyleSheet(u"background-color: none;")

        self.RemainingCoursePassRate_Layout_1.addWidget(self.RemainingCoursePassRateLabel_1)

        self.RemainingCoursePassRateValueLabel_1 = QLabel(self.RemainingCourse_1)
        self.RemainingCoursePassRateValueLabel_1.setObjectName(u"RemainingCoursePassRateValueLabel_1")
        self.RemainingCoursePassRateValueLabel_1.setFont(font4)
        self.RemainingCoursePassRateValueLabel_1.setStyleSheet(u"background-color: none;")

        self.RemainingCoursePassRate_Layout_1.addWidget(self.RemainingCoursePassRateValueLabel_1)

        self.RemainingCoursePassRateHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.RemainingCoursePassRate_Layout_1.addItem(self.RemainingCoursePassRateHorizontalSpacer_1)


        self.PendingCourse_1_Widget_Layout.addLayout(self.RemainingCoursePassRate_Layout_1)


        self.RemainingCoursesActualScrollAreaWidget_Layout.addWidget(self.RemainingCourse_1)

        self.RemainingCoursesScrollAreaSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.RemainingCoursesActualScrollAreaWidget_Layout.addItem(self.RemainingCoursesScrollAreaSpacer)

        self.RemainingCoursesScrollArea.setWidget(self.RemainingCoursesScrollAreaWidget)

        self.RemainingCoursesWidget_Layout.addWidget(self.RemainingCoursesScrollArea)


        self.CoursesPageWidget_Layout.addWidget(self.RemainingCoursesWidget, 1, 0, 1, 2)

        self.PassedCoursesWidget = QWidget(self.CoursesPageWidget)
        self.PassedCoursesWidget.setObjectName(u"PassedCoursesWidget")
        self.PassedCoursesWidget.setMinimumSize(QSize(270, 440))
        self.PassedCoursesWidget.setMaximumSize(QSize(270, 440))
        self.PassedCoursesWidget.setFont(font2)
        self.PassedCoursesWidget.setStyleSheet(u"border-radius: 10px;\n"
"background-color: \"white\";\n"
"color: \"black\";")
        self.PassedCoursesWidget_Layout = QVBoxLayout(self.PassedCoursesWidget)
        self.PassedCoursesWidget_Layout.setSpacing(5)
        self.PassedCoursesWidget_Layout.setObjectName(u"PassedCoursesWidget_Layout")
        self.PassedCoursesWidget_Layout.setContentsMargins(10, 5, 10, 10)
        self.PassedCoursesLabel = QLabel(self.PassedCoursesWidget)
        self.PassedCoursesLabel.setObjectName(u"PassedCoursesLabel")
        self.PassedCoursesLabel.setFont(font3)
        self.PassedCoursesLabel.setStyleSheet(u"background-color: none;")

        self.PassedCoursesWidget_Layout.addWidget(self.PassedCoursesLabel)

        self.PassedCoursesValueLabel = QLabel(self.PassedCoursesWidget)
        self.PassedCoursesValueLabel.setObjectName(u"PassedCoursesValueLabel")
        self.PassedCoursesValueLabel.setFont(font4)
        self.PassedCoursesValueLabel.setStyleSheet(u"background-color: none;")

        self.PassedCoursesWidget_Layout.addWidget(self.PassedCoursesValueLabel)

        self.PassedCoursesScrollArea = QScrollArea(self.PassedCoursesWidget)
        self.PassedCoursesScrollArea.setObjectName(u"PassedCoursesScrollArea")
        self.PassedCoursesScrollArea.setMinimumSize(QSize(250, 345))
        self.PassedCoursesScrollArea.setMaximumSize(QSize(250, 345))
        self.PassedCoursesScrollArea.setStyleSheet(u"")
        self.PassedCoursesScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.PassedCoursesScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.PassedCoursesScrollArea.setWidgetResizable(False)
        self.PassedCoursesScrollArea.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.PassedCoursesScrollAreaWidget = QWidget()
        self.PassedCoursesScrollAreaWidget.setObjectName(u"PassedCoursesScrollAreaWidget")
        self.PassedCoursesScrollAreaWidget.setGeometry(QRect(0, 0, 250, 345))
        sizePolicy3.setHeightForWidth(self.PassedCoursesScrollAreaWidget.sizePolicy().hasHeightForWidth())
        self.PassedCoursesScrollAreaWidget.setSizePolicy(sizePolicy3)
        self.PassedCoursesScrollAreaWidget.setMinimumSize(QSize(250, 345))
        self.PassedCoursesScrollAreaWidget.setMaximumSize(QSize(250, 345))
        self.PassedCoursesScrollAreaWidget.setStyleSheet(u"background-color: none;")
        self.PassedCoursesActualScrollAreaWidget = QWidget(self.PassedCoursesScrollAreaWidget)
        self.PassedCoursesActualScrollAreaWidget.setObjectName(u"PassedCoursesActualScrollAreaWidget")
        self.PassedCoursesActualScrollAreaWidget.setGeometry(QRect(0, 0, 250, 345))
        sizePolicy3.setHeightForWidth(self.PassedCoursesActualScrollAreaWidget.sizePolicy().hasHeightForWidth())
        self.PassedCoursesActualScrollAreaWidget.setSizePolicy(sizePolicy3)
        self.PassedCoursesActualScrollAreaWidget.setMinimumSize(QSize(250, 345))
        self.PassedCoursesActualScrollAreaWidget.setMaximumSize(QSize(250, 345))
        self.PassedCoursesActualScrollAreaWidget.setFont(font2)
        self.PassedCoursesActualScrollAreaWidget.setStyleSheet(u"")
        self.PassedCoursesActualScrollAreaWidget_Layout = QVBoxLayout(self.PassedCoursesActualScrollAreaWidget)
        self.PassedCoursesActualScrollAreaWidget_Layout.setSpacing(5)
        self.PassedCoursesActualScrollAreaWidget_Layout.setObjectName(u"PassedCoursesActualScrollAreaWidget_Layout")
        self.PassedCoursesActualScrollAreaWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.PassedCourse_1 = QWidget(self.PassedCoursesActualScrollAreaWidget)
        self.PassedCourse_1.setObjectName(u"PassedCourse_1")
        self.PassedCourse_1.setMinimumSize(QSize(250, 170))
        self.PassedCourse_1.setMaximumSize(QSize(250, 170))
        self.PassedCourse_1.setFont(font2)
        self.PassedCourse_1.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(7, 74, 45),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.PassedCourse_Layout_1 = QVBoxLayout(self.PassedCourse_1)
        self.PassedCourse_Layout_1.setSpacing(0)
        self.PassedCourse_Layout_1.setObjectName(u"PassedCourse_Layout_1")
        self.PassedCourse_Layout_1.setContentsMargins(10, 5, 10, 10)
        self.PassedCourseID_Hours_Layout_1 = QHBoxLayout()
        self.PassedCourseID_Hours_Layout_1.setSpacing(5)
        self.PassedCourseID_Hours_Layout_1.setObjectName(u"PassedCourseID_Hours_Layout_1")
        self.PassedCourseIDLabel_1 = QLabel(self.PassedCourse_1)
        self.PassedCourseIDLabel_1.setObjectName(u"PassedCourseIDLabel_1")
        self.PassedCourseIDLabel_1.setFont(font3)
        self.PassedCourseIDLabel_1.setStyleSheet(u"background-color: none;")

        self.PassedCourseID_Hours_Layout_1.addWidget(self.PassedCourseIDLabel_1)

        self.PassedCourseIDValueLabel_1 = QLabel(self.PassedCourse_1)
        self.PassedCourseIDValueLabel_1.setObjectName(u"PassedCourseIDValueLabel_1")
        self.PassedCourseIDValueLabel_1.setFont(font4)
        self.PassedCourseIDValueLabel_1.setStyleSheet(u"background-color: none;")

        self.PassedCourseID_Hours_Layout_1.addWidget(self.PassedCourseIDValueLabel_1)

        self.PassedCourseID_HoursHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.PassedCourseID_Hours_Layout_1.addItem(self.PassedCourseID_HoursHorizontalSpacer_1)

        self.PassedCourseHoursLabel_1 = QLabel(self.PassedCourse_1)
        self.PassedCourseHoursLabel_1.setObjectName(u"PassedCourseHoursLabel_1")
        self.PassedCourseHoursLabel_1.setFont(font3)
        self.PassedCourseHoursLabel_1.setStyleSheet(u"background-color: none;")

        self.PassedCourseID_Hours_Layout_1.addWidget(self.PassedCourseHoursLabel_1)

        self.PassedCourseHoursValueLabel_1 = QLabel(self.PassedCourse_1)
        self.PassedCourseHoursValueLabel_1.setObjectName(u"PassedCourseHoursValueLabel_1")
        self.PassedCourseHoursValueLabel_1.setFont(font4)
        self.PassedCourseHoursValueLabel_1.setStyleSheet(u"background-color: none;")

        self.PassedCourseID_Hours_Layout_1.addWidget(self.PassedCourseHoursValueLabel_1)


        self.PassedCourse_Layout_1.addLayout(self.PassedCourseID_Hours_Layout_1)

        self.PassedCoursePermission_Layout_1 = QHBoxLayout()
        self.PassedCoursePermission_Layout_1.setSpacing(5)
        self.PassedCoursePermission_Layout_1.setObjectName(u"PassedCoursePermission_Layout_1")
        self.PassedCoursePermissionLabel_1 = QLabel(self.PassedCourse_1)
        self.PassedCoursePermissionLabel_1.setObjectName(u"PassedCoursePermissionLabel_1")
        self.PassedCoursePermissionLabel_1.setFont(font3)
        self.PassedCoursePermissionLabel_1.setStyleSheet(u"background-color: none;")

        self.PassedCoursePermission_Layout_1.addWidget(self.PassedCoursePermissionLabel_1)

        self.PassedCoursePermissionValueLabel_1 = QLabel(self.PassedCourse_1)
        self.PassedCoursePermissionValueLabel_1.setObjectName(u"PassedCoursePermissionValueLabel_1")
        self.PassedCoursePermissionValueLabel_1.setFont(font4)
        self.PassedCoursePermissionValueLabel_1.setStyleSheet(u"background-color: none;")

        self.PassedCoursePermission_Layout_1.addWidget(self.PassedCoursePermissionValueLabel_1)

        self.PassedCoursePermissionHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.PassedCoursePermission_Layout_1.addItem(self.PassedCoursePermissionHorizontalSpacer_1)


        self.PassedCourse_Layout_1.addLayout(self.PassedCoursePermission_Layout_1)

        self.PassedCourseDoctor_Layout_1 = QHBoxLayout()
        self.PassedCourseDoctor_Layout_1.setSpacing(5)
        self.PassedCourseDoctor_Layout_1.setObjectName(u"PassedCourseDoctor_Layout_1")
        self.PassedCourseDoctorLabel_1 = QLabel(self.PassedCourse_1)
        self.PassedCourseDoctorLabel_1.setObjectName(u"PassedCourseDoctorLabel_1")
        self.PassedCourseDoctorLabel_1.setFont(font3)
        self.PassedCourseDoctorLabel_1.setStyleSheet(u"background-color: none;")

        self.PassedCourseDoctor_Layout_1.addWidget(self.PassedCourseDoctorLabel_1)

        self.PassedCourseDoctorValueLabel_1 = QLabel(self.PassedCourse_1)
        self.PassedCourseDoctorValueLabel_1.setObjectName(u"PassedCourseDoctorValueLabel_1")
        self.PassedCourseDoctorValueLabel_1.setFont(font4)
        self.PassedCourseDoctorValueLabel_1.setStyleSheet(u"background-color: none;")

        self.PassedCourseDoctor_Layout_1.addWidget(self.PassedCourseDoctorValueLabel_1)

        self.PassedCourseDoctorHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.PassedCourseDoctor_Layout_1.addItem(self.PassedCourseDoctorHorizontalSpacer_1)


        self.PassedCourse_Layout_1.addLayout(self.PassedCourseDoctor_Layout_1)

        self.PassedCourseLine_Layout_1 = QHBoxLayout()
        self.PassedCourseLine_Layout_1.setSpacing(0)
        self.PassedCourseLine_Layout_1.setObjectName(u"PassedCourseLine_Layout_1")
        self.PassedCourseLineLeftHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.PassedCourseLine_Layout_1.addItem(self.PassedCourseLineLeftHorizontalSpacer_1)

        self.PassedCourseLine_1 = QFrame(self.PassedCourse_1)
        self.PassedCourseLine_1.setObjectName(u"PassedCourseLine_1")
        self.PassedCourseLine_1.setMinimumSize(QSize(100, 1))
        self.PassedCourseLine_1.setMaximumSize(QSize(100, 1))
        self.PassedCourseLine_1.setFont(font2)
        self.PassedCourseLine_1.setStyleSheet(u"background-color: \"white\";")
        self.PassedCourseLine_1.setFrameShape(QFrame.Shape.HLine)
        self.PassedCourseLine_1.setFrameShadow(QFrame.Shadow.Sunken)

        self.PassedCourseLine_Layout_1.addWidget(self.PassedCourseLine_1)

        self.PassedCourseLineRightHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.PassedCourseLine_Layout_1.addItem(self.PassedCourseLineRightHorizontalSpacer_1)


        self.PassedCourse_Layout_1.addLayout(self.PassedCourseLine_Layout_1)

        self.PassedCourseDegree_Grade_Layout_1 = QHBoxLayout()
        self.PassedCourseDegree_Grade_Layout_1.setSpacing(5)
        self.PassedCourseDegree_Grade_Layout_1.setObjectName(u"PassedCourseDegree_Grade_Layout_1")
        self.PassedCourseDegreeLabel_1 = QLabel(self.PassedCourse_1)
        self.PassedCourseDegreeLabel_1.setObjectName(u"PassedCourseDegreeLabel_1")
        self.PassedCourseDegreeLabel_1.setFont(font3)
        self.PassedCourseDegreeLabel_1.setStyleSheet(u"background-color: none;")

        self.PassedCourseDegree_Grade_Layout_1.addWidget(self.PassedCourseDegreeLabel_1)

        self.PassedCourseDegreeValueLabel_1 = QLabel(self.PassedCourse_1)
        self.PassedCourseDegreeValueLabel_1.setObjectName(u"PassedCourseDegreeValueLabel_1")
        self.PassedCourseDegreeValueLabel_1.setFont(font4)
        self.PassedCourseDegreeValueLabel_1.setStyleSheet(u"background-color: none;")

        self.PassedCourseDegree_Grade_Layout_1.addWidget(self.PassedCourseDegreeValueLabel_1)

        self.PassedCourseDegree_GradeHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.PassedCourseDegree_Grade_Layout_1.addItem(self.PassedCourseDegree_GradeHorizontalSpacer_1)

        self.PassedCourseGradeLabel_1 = QLabel(self.PassedCourse_1)
        self.PassedCourseGradeLabel_1.setObjectName(u"PassedCourseGradeLabel_1")
        self.PassedCourseGradeLabel_1.setFont(font3)
        self.PassedCourseGradeLabel_1.setStyleSheet(u"background-color: none;")

        self.PassedCourseDegree_Grade_Layout_1.addWidget(self.PassedCourseGradeLabel_1)

        self.PassedCourseGradeValueLabel_1 = QLabel(self.PassedCourse_1)
        self.PassedCourseGradeValueLabel_1.setObjectName(u"PassedCourseGradeValueLabel_1")
        self.PassedCourseGradeValueLabel_1.setFont(font4)
        self.PassedCourseGradeValueLabel_1.setStyleSheet(u"background-color: none;")

        self.PassedCourseDegree_Grade_Layout_1.addWidget(self.PassedCourseGradeValueLabel_1)


        self.PassedCourse_Layout_1.addLayout(self.PassedCourseDegree_Grade_Layout_1)

        self.PassedCourseAttendance_Layout_1 = QHBoxLayout()
        self.PassedCourseAttendance_Layout_1.setSpacing(5)
        self.PassedCourseAttendance_Layout_1.setObjectName(u"PassedCourseAttendance_Layout_1")
        self.PassedCourseAttendanceLabel_1 = QLabel(self.PassedCourse_1)
        self.PassedCourseAttendanceLabel_1.setObjectName(u"PassedCourseAttendanceLabel_1")
        self.PassedCourseAttendanceLabel_1.setFont(font3)
        self.PassedCourseAttendanceLabel_1.setStyleSheet(u"background-color: none;")

        self.PassedCourseAttendance_Layout_1.addWidget(self.PassedCourseAttendanceLabel_1)

        self.PassedCourseAttendanceValueLabel_1 = QLabel(self.PassedCourse_1)
        self.PassedCourseAttendanceValueLabel_1.setObjectName(u"PassedCourseAttendanceValueLabel_1")
        self.PassedCourseAttendanceValueLabel_1.setFont(font4)
        self.PassedCourseAttendanceValueLabel_1.setStyleSheet(u"background-color: none;")

        self.PassedCourseAttendance_Layout_1.addWidget(self.PassedCourseAttendanceValueLabel_1)

        self.PassedCourseAttendanceHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.PassedCourseAttendance_Layout_1.addItem(self.PassedCourseAttendanceHorizontalSpacer_1)


        self.PassedCourse_Layout_1.addLayout(self.PassedCourseAttendance_Layout_1)


        self.PassedCoursesActualScrollAreaWidget_Layout.addWidget(self.PassedCourse_1)

        self.PassedCoursesScrollAreaSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.PassedCoursesActualScrollAreaWidget_Layout.addItem(self.PassedCoursesScrollAreaSpacer)

        self.PassedCoursesScrollArea.setWidget(self.PassedCoursesScrollAreaWidget)

        self.PassedCoursesWidget_Layout.addWidget(self.PassedCoursesScrollArea)


        self.CoursesPageWidget_Layout.addWidget(self.PassedCoursesWidget, 1, 2, 2, 1)

        self.FailedCoursesWidget = QWidget(self.CoursesPageWidget)
        self.FailedCoursesWidget.setObjectName(u"FailedCoursesWidget")
        self.FailedCoursesWidget.setMinimumSize(QSize(275, 490))
        self.FailedCoursesWidget.setMaximumSize(QSize(275, 490))
        self.FailedCoursesWidget.setFont(font2)
        self.FailedCoursesWidget.setStyleSheet(u"border-radius: 10px;\n"
"background-color: \"white\";\n"
"color: \"black\";")
        self.FailedCoursesWidget_Layout = QVBoxLayout(self.FailedCoursesWidget)
        self.FailedCoursesWidget_Layout.setSpacing(5)
        self.FailedCoursesWidget_Layout.setObjectName(u"FailedCoursesWidget_Layout")
        self.FailedCoursesWidget_Layout.setContentsMargins(10, 5, 10, 10)
        self.FailedCoursesLabel = QLabel(self.FailedCoursesWidget)
        self.FailedCoursesLabel.setObjectName(u"FailedCoursesLabel")
        self.FailedCoursesLabel.setFont(font3)
        self.FailedCoursesLabel.setStyleSheet(u"background-color: none;")

        self.FailedCoursesWidget_Layout.addWidget(self.FailedCoursesLabel)

        self.FailedCoursesValueLabel = QLabel(self.FailedCoursesWidget)
        self.FailedCoursesValueLabel.setObjectName(u"FailedCoursesValueLabel")
        self.FailedCoursesValueLabel.setFont(font4)
        self.FailedCoursesValueLabel.setStyleSheet(u"background-color: none;")

        self.FailedCoursesWidget_Layout.addWidget(self.FailedCoursesValueLabel)

        self.FailedCoursesScrollArea = QScrollArea(self.FailedCoursesWidget)
        self.FailedCoursesScrollArea.setObjectName(u"FailedCoursesScrollArea")
        self.FailedCoursesScrollArea.setMinimumSize(QSize(255, 395))
        self.FailedCoursesScrollArea.setMaximumSize(QSize(255, 395))
        self.FailedCoursesScrollArea.setStyleSheet(u"")
        self.FailedCoursesScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.FailedCoursesScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.FailedCoursesScrollArea.setWidgetResizable(False)
        self.FailedCoursesScrollArea.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.FailedCoursesScrollAreaWidget = QWidget()
        self.FailedCoursesScrollAreaWidget.setObjectName(u"FailedCoursesScrollAreaWidget")
        self.FailedCoursesScrollAreaWidget.setGeometry(QRect(0, 0, 255, 395))
        sizePolicy2.setHeightForWidth(self.FailedCoursesScrollAreaWidget.sizePolicy().hasHeightForWidth())
        self.FailedCoursesScrollAreaWidget.setSizePolicy(sizePolicy2)
        self.FailedCoursesScrollAreaWidget.setMinimumSize(QSize(255, 395))
        self.FailedCoursesScrollAreaWidget.setMaximumSize(QSize(255, 395))
        self.FailedCoursesScrollAreaWidget.setStyleSheet(u"background-color: none;")
        self.FailedCoursesActualScrollAreaWidget = QWidget(self.FailedCoursesScrollAreaWidget)
        self.FailedCoursesActualScrollAreaWidget.setObjectName(u"FailedCoursesActualScrollAreaWidget")
        self.FailedCoursesActualScrollAreaWidget.setGeometry(QRect(0, 0, 255, 395))
        sizePolicy2.setHeightForWidth(self.FailedCoursesActualScrollAreaWidget.sizePolicy().hasHeightForWidth())
        self.FailedCoursesActualScrollAreaWidget.setSizePolicy(sizePolicy2)
        self.FailedCoursesActualScrollAreaWidget.setMinimumSize(QSize(255, 395))
        self.FailedCoursesActualScrollAreaWidget.setMaximumSize(QSize(255, 395))
        self.FailedCoursesActualScrollAreaWidget.setFont(font2)
        self.FailedCoursesActualScrollAreaWidget.setStyleSheet(u"")
        self.FailedCoursesActualScrollAreaWidget_Layout = QVBoxLayout(self.FailedCoursesActualScrollAreaWidget)
        self.FailedCoursesActualScrollAreaWidget_Layout.setSpacing(5)
        self.FailedCoursesActualScrollAreaWidget_Layout.setObjectName(u"FailedCoursesActualScrollAreaWidget_Layout")
        self.FailedCoursesActualScrollAreaWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.FailedCourse_1 = QWidget(self.FailedCoursesActualScrollAreaWidget)
        self.FailedCourse_1.setObjectName(u"FailedCourse_1")
        self.FailedCourse_1.setMinimumSize(QSize(255, 195))
        self.FailedCourse_1.setMaximumSize(QSize(255, 195))
        self.FailedCourse_1.setFont(font2)
        self.FailedCourse_1.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1, y1:0, y2:1\n"
"	stop:0 rgb(128, 15, 28),\n"
"	stop:1 \"black\"\n"
");\n"
"color: \"white\";")
        self.FailedCourse_Layout_1 = QVBoxLayout(self.FailedCourse_1)
        self.FailedCourse_Layout_1.setSpacing(0)
        self.FailedCourse_Layout_1.setObjectName(u"FailedCourse_Layout_1")
        self.FailedCourse_Layout_1.setContentsMargins(10, 5, 10, 10)
        self.FailedCourseID_Hours_Layout_1 = QHBoxLayout()
        self.FailedCourseID_Hours_Layout_1.setSpacing(5)
        self.FailedCourseID_Hours_Layout_1.setObjectName(u"FailedCourseID_Hours_Layout_1")
        self.FailedCourseIDLabel_1 = QLabel(self.FailedCourse_1)
        self.FailedCourseIDLabel_1.setObjectName(u"FailedCourseIDLabel_1")
        self.FailedCourseIDLabel_1.setFont(font3)
        self.FailedCourseIDLabel_1.setStyleSheet(u"background-color: none;")

        self.FailedCourseID_Hours_Layout_1.addWidget(self.FailedCourseIDLabel_1)

        self.FailedCourseIDValueLabel_1 = QLabel(self.FailedCourse_1)
        self.FailedCourseIDValueLabel_1.setObjectName(u"FailedCourseIDValueLabel_1")
        self.FailedCourseIDValueLabel_1.setFont(font4)
        self.FailedCourseIDValueLabel_1.setStyleSheet(u"background-color: none;")

        self.FailedCourseID_Hours_Layout_1.addWidget(self.FailedCourseIDValueLabel_1)

        self.FailedCourseID_HoursHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.FailedCourseID_Hours_Layout_1.addItem(self.FailedCourseID_HoursHorizontalSpacer_1)

        self.FailedCourseHoursLabel_1 = QLabel(self.FailedCourse_1)
        self.FailedCourseHoursLabel_1.setObjectName(u"FailedCourseHoursLabel_1")
        self.FailedCourseHoursLabel_1.setFont(font3)
        self.FailedCourseHoursLabel_1.setStyleSheet(u"background-color: none;")

        self.FailedCourseID_Hours_Layout_1.addWidget(self.FailedCourseHoursLabel_1)

        self.FailedCourseHoursValueLabel_1 = QLabel(self.FailedCourse_1)
        self.FailedCourseHoursValueLabel_1.setObjectName(u"FailedCourseHoursValueLabel_1")
        self.FailedCourseHoursValueLabel_1.setFont(font4)
        self.FailedCourseHoursValueLabel_1.setStyleSheet(u"background-color: none;")

        self.FailedCourseID_Hours_Layout_1.addWidget(self.FailedCourseHoursValueLabel_1)


        self.FailedCourse_Layout_1.addLayout(self.FailedCourseID_Hours_Layout_1)

        self.FailedCoursePermission_Layout_1 = QHBoxLayout()
        self.FailedCoursePermission_Layout_1.setSpacing(5)
        self.FailedCoursePermission_Layout_1.setObjectName(u"FailedCoursePermission_Layout_1")
        self.FailedCoursePermissionLabel_1 = QLabel(self.FailedCourse_1)
        self.FailedCoursePermissionLabel_1.setObjectName(u"FailedCoursePermissionLabel_1")
        self.FailedCoursePermissionLabel_1.setFont(font3)
        self.FailedCoursePermissionLabel_1.setStyleSheet(u"background-color: none;")

        self.FailedCoursePermission_Layout_1.addWidget(self.FailedCoursePermissionLabel_1)

        self.FailedCoursePermissionValueLabel_1 = QLabel(self.FailedCourse_1)
        self.FailedCoursePermissionValueLabel_1.setObjectName(u"FailedCoursePermissionValueLabel_1")
        self.FailedCoursePermissionValueLabel_1.setFont(font4)
        self.FailedCoursePermissionValueLabel_1.setStyleSheet(u"background-color: none;")

        self.FailedCoursePermission_Layout_1.addWidget(self.FailedCoursePermissionValueLabel_1)

        self.FailedCoursePermissionHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.FailedCoursePermission_Layout_1.addItem(self.FailedCoursePermissionHorizontalSpacer_1)


        self.FailedCourse_Layout_1.addLayout(self.FailedCoursePermission_Layout_1)

        self.FailedCourseDoctor_Layout_1 = QHBoxLayout()
        self.FailedCourseDoctor_Layout_1.setSpacing(5)
        self.FailedCourseDoctor_Layout_1.setObjectName(u"FailedCourseDoctor_Layout_1")
        self.FailedCourseDoctorLabel_1 = QLabel(self.FailedCourse_1)
        self.FailedCourseDoctorLabel_1.setObjectName(u"FailedCourseDoctorLabel_1")
        self.FailedCourseDoctorLabel_1.setFont(font3)
        self.FailedCourseDoctorLabel_1.setStyleSheet(u"background-color: none;")

        self.FailedCourseDoctor_Layout_1.addWidget(self.FailedCourseDoctorLabel_1)

        self.FailedCourseDoctorValueLabel_1 = QLabel(self.FailedCourse_1)
        self.FailedCourseDoctorValueLabel_1.setObjectName(u"FailedCourseDoctorValueLabel_1")
        self.FailedCourseDoctorValueLabel_1.setFont(font4)
        self.FailedCourseDoctorValueLabel_1.setStyleSheet(u"background-color: none;")

        self.FailedCourseDoctor_Layout_1.addWidget(self.FailedCourseDoctorValueLabel_1)

        self.FailedCourseDoctorHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.FailedCourseDoctor_Layout_1.addItem(self.FailedCourseDoctorHorizontalSpacer_1)


        self.FailedCourse_Layout_1.addLayout(self.FailedCourseDoctor_Layout_1)

        self.FailedCourseLine_Layout_1 = QHBoxLayout()
        self.FailedCourseLine_Layout_1.setSpacing(0)
        self.FailedCourseLine_Layout_1.setObjectName(u"FailedCourseLine_Layout_1")
        self.FailedCourseLineLeftHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.FailedCourseLine_Layout_1.addItem(self.FailedCourseLineLeftHorizontalSpacer_1)

        self.FailedCourseLine_1 = QFrame(self.FailedCourse_1)
        self.FailedCourseLine_1.setObjectName(u"FailedCourseLine_1")
        self.FailedCourseLine_1.setMinimumSize(QSize(100, 1))
        self.FailedCourseLine_1.setMaximumSize(QSize(100, 1))
        self.FailedCourseLine_1.setFont(font2)
        self.FailedCourseLine_1.setStyleSheet(u"background-color: \"white\";")
        self.FailedCourseLine_1.setFrameShape(QFrame.Shape.HLine)
        self.FailedCourseLine_1.setFrameShadow(QFrame.Shadow.Sunken)

        self.FailedCourseLine_Layout_1.addWidget(self.FailedCourseLine_1)

        self.FailedCourseLineRightHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.FailedCourseLine_Layout_1.addItem(self.FailedCourseLineRightHorizontalSpacer_1)


        self.FailedCourse_Layout_1.addLayout(self.FailedCourseLine_Layout_1)

        self.FailedCourseDegree_Attendance_Layout_1 = QHBoxLayout()
        self.FailedCourseDegree_Attendance_Layout_1.setSpacing(5)
        self.FailedCourseDegree_Attendance_Layout_1.setObjectName(u"FailedCourseDegree_Attendance_Layout_1")
        self.FailedCourseDegreeLabel_1 = QLabel(self.FailedCourse_1)
        self.FailedCourseDegreeLabel_1.setObjectName(u"FailedCourseDegreeLabel_1")
        self.FailedCourseDegreeLabel_1.setFont(font3)
        self.FailedCourseDegreeLabel_1.setStyleSheet(u"background-color: none;")

        self.FailedCourseDegree_Attendance_Layout_1.addWidget(self.FailedCourseDegreeLabel_1)

        self.FailedCourseDegreeValueLabel_1 = QLabel(self.FailedCourse_1)
        self.FailedCourseDegreeValueLabel_1.setObjectName(u"FailedCourseDegreeValueLabel_1")
        self.FailedCourseDegreeValueLabel_1.setFont(font4)
        self.FailedCourseDegreeValueLabel_1.setStyleSheet(u"background-color: none;")

        self.FailedCourseDegree_Attendance_Layout_1.addWidget(self.FailedCourseDegreeValueLabel_1)

        self.FailedCourseDegree_AttendanceHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.FailedCourseDegree_Attendance_Layout_1.addItem(self.FailedCourseDegree_AttendanceHorizontalSpacer_1)

        self.FailedCourseAttendanceLabel_1 = QLabel(self.FailedCourse_1)
        self.FailedCourseAttendanceLabel_1.setObjectName(u"FailedCourseAttendanceLabel_1")
        self.FailedCourseAttendanceLabel_1.setFont(font3)
        self.FailedCourseAttendanceLabel_1.setStyleSheet(u"background-color: none;")

        self.FailedCourseDegree_Attendance_Layout_1.addWidget(self.FailedCourseAttendanceLabel_1)

        self.FailedCourseAttendanceValueLabel_1 = QLabel(self.FailedCourse_1)
        self.FailedCourseAttendanceValueLabel_1.setObjectName(u"FailedCourseAttendanceValueLabel_1")
        self.FailedCourseAttendanceValueLabel_1.setFont(font4)
        self.FailedCourseAttendanceValueLabel_1.setStyleSheet(u"background-color: none;")

        self.FailedCourseDegree_Attendance_Layout_1.addWidget(self.FailedCourseAttendanceValueLabel_1)


        self.FailedCourse_Layout_1.addLayout(self.FailedCourseDegree_Attendance_Layout_1)

        self.FailedCourseRemainingStudents_Layout_1 = QHBoxLayout()
        self.FailedCourseRemainingStudents_Layout_1.setSpacing(5)
        self.FailedCourseRemainingStudents_Layout_1.setObjectName(u"FailedCourseRemainingStudents_Layout_1")
        self.FailedCourseRemainingStudentsLabel_1 = QLabel(self.FailedCourse_1)
        self.FailedCourseRemainingStudentsLabel_1.setObjectName(u"FailedCourseRemainingStudentsLabel_1")
        self.FailedCourseRemainingStudentsLabel_1.setFont(font3)
        self.FailedCourseRemainingStudentsLabel_1.setStyleSheet(u"background-color: none;")

        self.FailedCourseRemainingStudents_Layout_1.addWidget(self.FailedCourseRemainingStudentsLabel_1)

        self.FailedCourseRemainingStudentsValueLabel_1 = QLabel(self.FailedCourse_1)
        self.FailedCourseRemainingStudentsValueLabel_1.setObjectName(u"FailedCourseRemainingStudentsValueLabel_1")
        self.FailedCourseRemainingStudentsValueLabel_1.setFont(font4)
        self.FailedCourseRemainingStudentsValueLabel_1.setStyleSheet(u"background-color: none;")

        self.FailedCourseRemainingStudents_Layout_1.addWidget(self.FailedCourseRemainingStudentsValueLabel_1)

        self.FailedCourseRemainingStudentsHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.FailedCourseRemainingStudents_Layout_1.addItem(self.FailedCourseRemainingStudentsHorizontalSpacer_1)


        self.FailedCourse_Layout_1.addLayout(self.FailedCourseRemainingStudents_Layout_1)

        self.FailedCoursePassRate_Layout_1 = QHBoxLayout()
        self.FailedCoursePassRate_Layout_1.setSpacing(5)
        self.FailedCoursePassRate_Layout_1.setObjectName(u"FailedCoursePassRate_Layout_1")
        self.FailedCoursePassRateLabel_1 = QLabel(self.FailedCourse_1)
        self.FailedCoursePassRateLabel_1.setObjectName(u"FailedCoursePassRateLabel_1")
        self.FailedCoursePassRateLabel_1.setFont(font3)
        self.FailedCoursePassRateLabel_1.setStyleSheet(u"background-color: none;")

        self.FailedCoursePassRate_Layout_1.addWidget(self.FailedCoursePassRateLabel_1)

        self.FailedCoursePassRateValueLabel_1 = QLabel(self.FailedCourse_1)
        self.FailedCoursePassRateValueLabel_1.setObjectName(u"FailedCoursePassRateValueLabel_1")
        self.FailedCoursePassRateValueLabel_1.setFont(font4)
        self.FailedCoursePassRateValueLabel_1.setStyleSheet(u"background-color: none;")

        self.FailedCoursePassRate_Layout_1.addWidget(self.FailedCoursePassRateValueLabel_1)

        self.FailedCoursePassRateHorizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.FailedCoursePassRate_Layout_1.addItem(self.FailedCoursePassRateHorizontalSpacer_1)


        self.FailedCourse_Layout_1.addLayout(self.FailedCoursePassRate_Layout_1)


        self.FailedCoursesActualScrollAreaWidget_Layout.addWidget(self.FailedCourse_1)

        self.FailedCoursesScrollAreaSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.FailedCoursesActualScrollAreaWidget_Layout.addItem(self.FailedCoursesScrollAreaSpacer)

        self.FailedCoursesScrollArea.setWidget(self.FailedCoursesScrollAreaWidget)

        self.FailedCoursesWidget_Layout.addWidget(self.FailedCoursesScrollArea)


        self.CoursesPageWidget_Layout.addWidget(self.FailedCoursesWidget, 1, 3, 3, 1)

        self.SearchForCourseButton = QPushButton(self.CoursesPageWidget)
        self.SearchForCourseButton.setObjectName(u"SearchForCourseButton")
        sizePolicy.setHeightForWidth(self.SearchForCourseButton.sizePolicy().hasHeightForWidth())
        self.SearchForCourseButton.setSizePolicy(sizePolicy)
        self.SearchForCourseButton.setMinimumSize(QSize(210, 55))
        self.SearchForCourseButton.setMaximumSize(QSize(210, 55))
        font11 = QFont()
        font11.setFamilies([u"Calibri"])
        font11.setPointSize(14)
        font11.setBold(True)
        font11.setKerning(True)
        font11.setStyleStrategy(QFont.PreferAntialias)
        self.SearchForCourseButton.setFont(font11)
        self.SearchForCourseButton.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(27, 49, 96);\n"
"	color: \"white\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(36, 65, 127);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/Search.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SearchForCourseButton.setIcon(icon1)
        self.SearchForCourseButton.setIconSize(QSize(30, 30))
        self.SearchForCourseButton.setCheckable(True)
        self.SearchForCourseButton.setAutoRepeat(False)
        self.SearchForCourseButton.setAutoExclusive(False)

        self.CoursesPageWidget_Layout.addWidget(self.SearchForCourseButton, 2, 0, 1, 1)

        self.UndoButton = QPushButton(self.CoursesPageWidget)
        self.UndoButton.setObjectName(u"UndoButton")
        self.UndoButton.setMinimumSize(QSize(55, 55))
        self.UndoButton.setMaximumSize(QSize(55, 55))
        self.UndoButton.setFont(font2)
        self.UndoButton.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(27, 49, 96);\n"
"	color: \"white\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(36, 65, 127);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/Undo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.UndoButton.setIcon(icon2)
        self.UndoButton.setIconSize(QSize(25, 25))
        self.UndoButton.setCheckable(True)
        self.UndoButton.setAutoExclusive(False)

        self.CoursesPageWidget_Layout.addWidget(self.UndoButton, 2, 1, 1, 1)

        self.SearchForCourseLineEdit = QLineEdit(self.CoursesPageWidget)
        self.SearchForCourseLineEdit.setObjectName(u"SearchForCourseLineEdit")
        self.SearchForCourseLineEdit.setMinimumSize(QSize(545, 45))
        self.SearchForCourseLineEdit.setMaximumSize(QSize(545, 45))
        font12 = QFont()
        font12.setFamilies([u"calibri"])
        font12.setPointSize(16)
        font12.setStyleStrategy(QFont.PreferAntialias)
        self.SearchForCourseLineEdit.setFont(font12)
        self.SearchForCourseLineEdit.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	x1:0, x2:1\n"
"	stop:0 rgb(27, 49, 96),\n"
"	stop:1 rgb(7, 74, 45)\n"
");\n"
"color: \"white\";\n"
"padding-left: 10px;\n"
"font-size: 16pt;\n"
"font-family: calibri;")

        self.CoursesPageWidget_Layout.addWidget(self.SearchForCourseLineEdit, 3, 0, 1, 3)

        self.StackedWidget.addWidget(self.CoursesPage)
        self.SideBar = QWidget(MainWindow)
        self.SideBar.setObjectName(u"SideBar")
        self.SideBar.setGeometry(QRect(5, 5, 60, 640))
        self.SideBar.setMinimumSize(QSize(60, 640))
        self.SideBar.setMaximumSize(QSize(60, 640))
        self.SideBar.setFont(font1)
        self.SideBar.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(\n"
"	y1:0, y2:1\n"
"	stop:0 rgb(128, 15, 28),\n"
"	stop:0.5 rgb(27, 49, 96),\n"
"	stop:1 rgb(7, 74, 45)\n"
");")
        self.SideBar_Layout = QVBoxLayout(self.SideBar)
        self.SideBar_Layout.setSpacing(0)
        self.SideBar_Layout.setObjectName(u"SideBar_Layout")
        self.SideBar_Layout.setContentsMargins(5, 5, 5, 5)
        self.ProfileButton = QPushButton(self.SideBar)
        self.ProfileButton.setObjectName(u"ProfileButton")
        self.ProfileButton.setMinimumSize(QSize(50, 50))
        self.ProfileButton.setMaximumSize(QSize(50, 50))
        self.ProfileButton.setFont(font2)
        self.ProfileButton.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(239, 233, 231);\n"
"	icon: url(:/Icons/Icons/Profile-Clicked.ico);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(239, 233, 231);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: none;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Icons/Profile.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/Icons/Icons/Profile-Clicked.ico", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.ProfileButton.setIcon(icon3)
        self.ProfileButton.setIconSize(QSize(25, 25))
        self.ProfileButton.setCheckable(True)
        self.ProfileButton.setChecked(True)

        self.SideBar_Layout.addWidget(self.ProfileButton)

        self.SideBarVerticalTopSpacer = QSpacerItem(20, 82, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.SideBar_Layout.addItem(self.SideBarVerticalTopSpacer)

        self.SideBarButtons_Layout = QVBoxLayout()
        self.SideBarButtons_Layout.setSpacing(5)
        self.SideBarButtons_Layout.setObjectName(u"SideBarButtons_Layout")
        self.AnalysisButton = QPushButton(self.SideBar)
        self.AnalysisButton.setObjectName(u"AnalysisButton")
        self.AnalysisButton.setMinimumSize(QSize(50, 50))
        self.AnalysisButton.setMaximumSize(QSize(50, 50))
        self.AnalysisButton.setFont(font2)
        self.AnalysisButton.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(239, 233, 231);\n"
"	icon: url(:/Icons/Icons/Analysis-Clicked.ico);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(239, 233, 231);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:none;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Icons/Analysis.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/Icons/Icons/Analysis-Clicked.ico", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.AnalysisButton.setIcon(icon4)
        self.AnalysisButton.setIconSize(QSize(25, 25))
        self.AnalysisButton.setCheckable(True)
        self.AnalysisButton.setAutoExclusive(False)

        self.SideBarButtons_Layout.addWidget(self.AnalysisButton)

        self.CoursesButton = QPushButton(self.SideBar)
        self.CoursesButton.setObjectName(u"CoursesButton")
        self.CoursesButton.setMinimumSize(QSize(50, 50))
        self.CoursesButton.setMaximumSize(QSize(50, 50))
        self.CoursesButton.setFont(font2)
        self.CoursesButton.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(239, 233, 231);\n"
"	icon: url(:/Icons/Icons/Courses-Clicked.ico);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(239, 233, 231);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:none;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Icons/Courses.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/Icons/Icons/Courses-Clicked.ico", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.CoursesButton.setIcon(icon5)
        self.CoursesButton.setIconSize(QSize(25, 25))
        self.CoursesButton.setCheckable(True)
        self.CoursesButton.setAutoExclusive(False)

        self.SideBarButtons_Layout.addWidget(self.CoursesButton)

        self.AiButton = QPushButton(self.SideBar)
        self.AiButton.setObjectName(u"AiButton")
        self.AiButton.setMinimumSize(QSize(50, 50))
        self.AiButton.setMaximumSize(QSize(50, 50))
        self.AiButton.setFont(font2)
        self.AiButton.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(239, 233, 231);\n"
"	icon: url(:/Icons/Icons/AI-Clicked.ico);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(239, 233, 231);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:none;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Icons/AI.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/Icons/Icons/AI-Clicked.ico", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.AiButton.setIcon(icon6)
        self.AiButton.setIconSize(QSize(30, 30))
        self.AiButton.setCheckable(True)
        self.AiButton.setAutoExclusive(False)

        self.SideBarButtons_Layout.addWidget(self.AiButton)


        self.SideBar_Layout.addLayout(self.SideBarButtons_Layout)

        self.SideBarVerticalBottomSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.SideBar_Layout.addItem(self.SideBarVerticalBottomSpacer)

        self.Controls_Layout = QVBoxLayout()
        self.Controls_Layout.setSpacing(5)
        self.Controls_Layout.setObjectName(u"Controls_Layout")
        self.LogOutButton = QPushButton(self.SideBar)
        self.LogOutButton.setObjectName(u"LogOutButton")
        self.LogOutButton.setMinimumSize(QSize(50, 50))
        self.LogOutButton.setMaximumSize(QSize(50, 50))
        self.LogOutButton.setFont(font2)
        self.LogOutButton.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(239, 233, 231);\n"
"	icon: url(:/Icons/Icons/LogOut-Clicked.ico);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(239, 233, 231);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:none;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/Icons/LogOut.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/Icons/Icons/LogOut-Clicked.ico", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.LogOutButton.setIcon(icon7)
        self.LogOutButton.setIconSize(QSize(25, 25))
        self.LogOutButton.setCheckable(True)
        self.LogOutButton.setAutoExclusive(False)

        self.Controls_Layout.addWidget(self.LogOutButton)


        self.SideBar_Layout.addLayout(self.Controls_Layout)


        self.retranslateUi(MainWindow)

        self.StackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.UsersProfilePhoto.setText("")
        self.CreditsRemainingLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Credits Remaining</span></p></body></html>", None))
        self.CreditsRemainingValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">40</span></p></body></html>", None))
        self.CreditsAttemptedLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Credits Attempted</span></p></body></html>", None))
        self.CreditsAttemptedValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">40</span></p></body></html>", None))
        self.CreditsPassedLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Credits Passed</span></p></body></html>", None))
        self.CreditsPassedValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">35</span></p></body></html>", None))
        self.CreditsFailedLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Credits Failed</span></p></body></html>", None))
        self.CreditsFailedValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">5</span></p></body></html>", None))
        self.CreditsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Credits</span></p></body></html>", None))
        self.PersonalInformationLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Personal Information</span></p></body></html>", None))
        self.FullNameLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Full Name:</span></p></body></html>", None))
        self.FullNameValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Michael Moore</span></p></body></html>", None))
        self.IDLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">ID:</span></p></body></html>", None))
        self.IDValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">S0001</span></p></body></html>", None))
        self.LevelLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Level:</span></p></body></html>", None))
        self.LevelValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">1</span></p></body></html>", None))
        self.DepartmentLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Department:</span></p></body></html>", None))
        self.DepartmentValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">CS</span></p></body></html>", None))
        self.EmailLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Email:</span></p></body></html>", None))
        self.EmailValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">michael.moore@email.com</span></p></body></html>", None))
        self.SuccessRatesLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Success Rates</span></p></body></html>", None))
        self.COMPLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">COMP</span></p></body></html>", None))
        self.COMPValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">100%</span></p></body></html>", None))
        self.STATLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">STAT</span></p></body></html>", None))
        self.STATValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">75%</span></p></body></html>", None))
        self.MATHLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">MATH</span></p></body></html>", None))
        self.MATHValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">75%</span></p></body></html>", None))
        self.PHYSLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">PHYS</span></p></body></html>", None))
        self.PHYSValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">75%</span></p></body></html>", None))
        self.CHEMLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">CHEM</span></p></body></html>", None))
        self.CHEMValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">75%</span></p></body></html>", None))
        self.OthersLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Others</span></p></body></html>", None))
        self.OthersValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">75%</span></p></body></html>", None))
        self.GPALabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">GPA</span></p></body></html>", None))
        self.GPAValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">2.26</span></p></body></html>", None))
        self.GPAScoreNameValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">GREAT</span></p></body></html>", None))
        self.GPAScoreCodeValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">(A)</span></p></body></html>", None))
        self.FinalGradeCalculatorButton.setText(QCoreApplication.translate("MainWindow", u"Final Grade Calculator", None))
        self.WhatToRegesterButton.setText(QCoreApplication.translate("MainWindow", u"What to Register", None))
        self.FinalGPAPredictorButton.setText(QCoreApplication.translate("MainWindow", u"Final GPA Predictor", None))
        self.CourseIDBoxLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Course ID:</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.CourseIDBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">assssss</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CourseIDBox.setText("")
        self.CourseIDErrorLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Wrong Course ID</span></p></body></html>", None))
        self.CourseWorkBoxLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Coursework:</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.CourseWorkBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>assssssssss</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CourseWorkBox.setText("")
        self.CourseWorkErrorLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Maximume for this Course is:</span></p></body></html>", None))
        self.CourseWorkErrorValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">45</span></p></body></html>", None))
        self.AttendanceBoxLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Attendance:</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.AttendanceBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>assssssss</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.AttendanceBox.setText("")
        self.AttendanceErrorLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Maximume Attendance is 15</span></p></body></html>", None))
        self.FinalGradeCalculateButton.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.IDLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">ID:</span></p></body></html>", None))
        self.IDValueLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">COMP 207</span></p></body></html>", None))
        self.CourseWorkLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Coursework:</span></p></body></html>", None))
        self.CourseWorkValueLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">23</span></p></body></html>", None))
        self.AttendanceLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Attendance:</span></p></body></html>", None))
        self.AttendanceValueLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">12</span></p></body></html>", None))
        self.MinExpectedFinalGradeLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">MIN. Final Grade:</span></p></body></html>", None))
        self.MinExpectedFinalGradeValueLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">17</span></p></body></html>", None))
        self.MaxExpectedFinalGradeLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">MAX. Final Grade:</span></p></body></html>", None))
        self.MaxExpectedFinalGradeValueLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">17</span></p></body></html>", None))
        self.IDLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">ID:</span></p></body></html>", None))
        self.IDValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">COMP 207</span></p></body></html>", None))
        self.CourseWorkLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Coursework:</span></p></body></html>", None))
        self.CourseWorkValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">23</span></p></body></html>", None))
        self.AttendanceLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Attendance:</span></p></body></html>", None))
        self.AttendanceValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">12</span></p></body></html>", None))
        self.MinExpectedFinalGradeLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">MIN. Final Grade:</span></p></body></html>", None))
        self.MinExpectedFinalGradeValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">17</span></p></body></html>", None))
        self.MaxExpectedFinalGradeLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">MAX. Final Grade:</span></p></body></html>", None))
        self.MaxExpectedFinalGradeValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">17</span></p></body></html>", None))
        self.IDLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">ID:</span></p></body></html>", None))
        self.IDValueLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">COMP 207</span></p></body></html>", None))
        self.CourseWorkLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Coursework:</span></p></body></html>", None))
        self.CourseWorkValueLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">23</span></p></body></html>", None))
        self.AttendanceLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Attendance:</span></p></body></html>", None))
        self.AttendanceValueLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">12</span></p></body></html>", None))
        self.MinExpectedFinalGradeLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">MIN. Final Grade:</span></p></body></html>", None))
        self.MinExpectedFinalGradeValueLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">17</span></p></body></html>", None))
        self.MaxExpectedFinalGradeLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">MAX. Final Grade:</span></p></body></html>", None))
        self.MaxExpectedFinalGradeValueLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">17</span></p></body></html>", None))
        self.IDLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">ID:</span></p></body></html>", None))
        self.IDValueLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">COMP 207</span></p></body></html>", None))
        self.CourseWorkLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Coursework:</span></p></body></html>", None))
        self.CourseWorkValueLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">23</span></p></body></html>", None))
        self.AttendanceLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Attendance:</span></p></body></html>", None))
        self.AttendanceValueLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">12</span></p></body></html>", None))
        self.MinExpectedFinalGradeLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">MIN. Final Grade:</span></p></body></html>", None))
        self.MinExpectedFinalGradeValueLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">17</span></p></body></html>", None))
        self.MaxExpectedFinalGradeLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">MAX. Final Grade:</span></p></body></html>", None))
        self.MaxExpectedFinalGradeValueLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">17</span></p></body></html>", None))
        self.IDLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">ID:</span></p></body></html>", None))
        self.IDValueLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">COMP 207</span></p></body></html>", None))
        self.CourseWorkLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Coursework:</span></p></body></html>", None))
        self.CourseWorkValueLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">23</span></p></body></html>", None))
        self.AttendanceLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Attendance:</span></p></body></html>", None))
        self.AttendanceValueLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">12</span></p></body></html>", None))
        self.MinExpectedFinalGradeLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">MIN. Final Grade:</span></p></body></html>", None))
        self.MinExpectedFinalGradeValueLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">17</span></p></body></html>", None))
        self.MaxExpectedFinalGradeLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">MAX. Final Grade:</span></p></body></html>", None))
        self.MaxExpectedFinalGradeValueLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">17</span></p></body></html>", None))
        self.IDLabel_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">ID:</span></p></body></html>", None))
        self.IDValueLabel_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">COMP 207</span></p></body></html>", None))
        self.CourseWorkLabel_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Coursework:</span></p></body></html>", None))
        self.CourseWorkValueLabel_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">23</span></p></body></html>", None))
        self.AttendanceLabel_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Attendance:</span></p></body></html>", None))
        self.AttendanceValueLabel_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">12</span></p></body></html>", None))
        self.MinExpectedFinalGradeLabel_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">MIN. Final Grade:</span></p></body></html>", None))
        self.MinExpectedFinalGradeValueLabel_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">17</span></p></body></html>", None))
        self.MaxExpectedFinalGradeLabel_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">MAX. Final Grade:</span></p></body></html>", None))
        self.MaxExpectedFinalGradeValueLabel_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">17</span></p></body></html>", None))
        self.WhatToRegisterCurrentLevelLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Current Level:</span></p></body></html>", None))
        self.WhatToRegisterCurrentLevelValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">45</span></p></body></html>", None))
        self.AvailableHoursLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Available Hours</span><span style=\" font-size:14pt;\">:</span></p></body></html>", None))
        self.AvailableHoursValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">18</span></p></body></html>", None))
        self.CoursesToRegisterLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Courses to Register:</span></p></body></html>", None))
        self.CoursesToRegisterValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">7</span></p></body></html>", None))
        self.RegesteredCOMPValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">100%</span></p></body></html>", None))
        self.RegesteredCOMPLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">COMP</span></p></body></html>", None))
        self.RegesteredSTATValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">100%</span></p></body></html>", None))
        self.RegesteredSTATLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">STAT</span></p></body></html>", None))
        self.RegesteredMATHValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">100%</span></p></body></html>", None))
        self.RegesteredMATHLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">MATH</span></p></body></html>", None))
        self.RegesteredOthersValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">100%</span></p></body></html>", None))
        self.RegesteredOthersLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Others</span></p></body></html>", None))
        self.SuggestedCourseRankLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">#1</span></p></body></html>", None))
        self.SuggestedCourseIDLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">ID:</span></p></body></html>", None))
        self.SuggestedCourseIDValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">C110</span></p></body></html>", None))
        self.SuggestedCoursePermissionLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Permission:</span></p></body></html>", None))
        self.SuggestedCoursePermissionValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Required</span></p></body></html>", None))
        self.SuggestedCourseHoursLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Hours:</span></p></body></html>", None))
        self.SuggestedCourseHoursValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">3</span></p></body></html>", None))
        self.SuggestedCourseRemainingStudentsLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Remaining Students:</span></p></body></html>", None))
        self.SuggestedCourseRemainingStudentsValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">20</span></p></body></html>", None))
        self.SuggestedCoursePassRateLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Pass Rate:</span></p></body></html>", None))
        self.SuggestedCoursePassRateValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">75%</span></p></body></html>", None))
        self.FinalGPAPredictorCurrentLevelLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Current Level:</span></p></body></html>", None))
        self.FinalGPAPredictorCurrentLevelValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">15</span></p></body></html>", None))
        self.CurrentGPALabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Current GPA:</span></p></body></html>", None))
        self.CurrentGPAValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">15</span></p></body></html>", None))
        self.Level_1_GPABoxLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Level 1 GPA:</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.Level_1_GPABox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>assssssssss</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Level_1_GPABox.setText("")
        self.Level_1_GPAErrorLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Maximume Value is 4</span></p></body></html>", None))
        self.Level_2_GPABoxLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Level 2 GPA:</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.Level_2_GPABox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>assssssss</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Level_2_GPABox.setText("")
        self.Level_2_GPAErrorLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Maximume Value is 4</span></p></body></html>", None))
        self.FinalGPAPredictorPredictButton.setText(QCoreApplication.translate("MainWindow", u"Predict", None))
        self.ExpectedGPALabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Expected GPA</span></p></body></html>", None))
        self.ExpectedGPAValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">2.26</span></p></body></html>", None))
        self.ExpectedGPAScoreNameValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">GREAT</span></p></body></html>", None))
        self.ExpectedGPAScoreCodeValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:400;\">A</span></p></body></html>", None))
        self.CurrentCoursesLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Current Courses</span></p></body></html>", None))
        self.CurrentCourseIDLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">ID:</span></p></body></html>", None))
        self.CurrentCourseIDValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">COMP 414</span></p></body></html>", None))
        self.CurrentCourseHoursLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Hours:</span></p></body></html>", None))
        self.CurrentCourseHoursValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">3</span></p></body></html>", None))
        self.CurrentCoursePermissionLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Permission:</span></p></body></html>", None))
        self.CurrentCoursePermissionValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Required</span></p></body></html>", None))
        self.CurrentCourseDoctorLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Doctor:</span></p></body></html>", None))
        self.CurrentCourseDoctorValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Dr. Joseph Gonzalez</span></p></body></html>", None))
        self.CurrentCourseIDLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">ID:</span></p></body></html>", None))
        self.CurrentCourseIDValueLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">COMP 414</span></p></body></html>", None))
        self.CurrentCourseHoursLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Hours:</span></p></body></html>", None))
        self.CurrentCourseHoursValueLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">3</span></p></body></html>", None))
        self.CurrentCoursePermissionLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Permission:</span></p></body></html>", None))
        self.CurrentCoursePermissionValueLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Required</span></p></body></html>", None))
        self.CurrentCourseDoctorLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Doctor:</span></p></body></html>", None))
        self.CurrentCourseDoctorValueLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Dr. Joseph Gonzalez</span></p></body></html>", None))
        self.CurrentCourseIDLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">ID:</span></p></body></html>", None))
        self.CurrentCourseIDValueLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">COMP 414</span></p></body></html>", None))
        self.CurrentCourseHoursLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Hours:</span></p></body></html>", None))
        self.CurrentCourseHoursValueLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">3</span></p></body></html>", None))
        self.CurrentCoursePermissionLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Permission:</span></p></body></html>", None))
        self.CurrentCoursePermissionValueLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Required</span></p></body></html>", None))
        self.CurrentCourseDoctorLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Doctor:</span></p></body></html>", None))
        self.CurrentCourseDoctorValueLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Dr. Joseph Gonzalez</span></p></body></html>", None))
        self.CurrentCourseIDLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">ID:</span></p></body></html>", None))
        self.CurrentCourseIDValueLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">COMP 414</span></p></body></html>", None))
        self.CurrentCourseHoursLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Hours:</span></p></body></html>", None))
        self.CurrentCourseHoursValueLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">3</span></p></body></html>", None))
        self.CurrentCoursePermissionLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Permission:</span></p></body></html>", None))
        self.CurrentCoursePermissionValueLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Required</span></p></body></html>", None))
        self.CurrentCourseDoctorLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Doctor:</span></p></body></html>", None))
        self.CurrentCourseDoctorValueLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Dr. Joseph Gonzalez</span></p></body></html>", None))
        self.CurrentCourseIDLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">ID:</span></p></body></html>", None))
        self.CurrentCourseIDValueLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">COMP 414</span></p></body></html>", None))
        self.CurrentCourseHoursLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Hours:</span></p></body></html>", None))
        self.CurrentCourseHoursValueLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">3</span></p></body></html>", None))
        self.CurrentCoursePermissionLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Permission:</span></p></body></html>", None))
        self.CurrentCoursePermissionValueLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Required</span></p></body></html>", None))
        self.CurrentCourseDoctorLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Doctor:</span></p></body></html>", None))
        self.CurrentCourseDoctorValueLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Dr. Joseph Gonzalez</span></p></body></html>", None))
        self.RemainingCoursesLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Remaining Courses</span></p></body></html>", None))
        self.RemainingCoursesValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">25</span></p></body></html>", None))
        self.RemainingCourseIDLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">ID:</span></p></body></html>", None))
        self.RemainingCourseIDValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">C110</span></p></body></html>", None))
        self.RemainingCourseHoursLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Hours:</span></p></body></html>", None))
        self.RemainingCourseHoursValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">3</span></p></body></html>", None))
        self.RemainingCoursePermissionLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Permission:</span></p></body></html>", None))
        self.RemainingCoursePermissionValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Required</span></p></body></html>", None))
        self.RemainingCourseRemainingStudentsLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Remaining Students:</span></p></body></html>", None))
        self.RemainingCourseRemainingStudentsValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">20</span></p></body></html>", None))
        self.RemainingCoursePassRateLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Pass Rate:</span></p></body></html>", None))
        self.RemainingCoursePassRateValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">75%</span></p></body></html>", None))
        self.PassedCoursesLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Passed Courses</span></p></body></html>", None))
        self.PassedCoursesValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">10</span></p></body></html>", None))
        self.PassedCourseIDLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">ID:</span></p></body></html>", None))
        self.PassedCourseIDValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">C110</span></p></body></html>", None))
        self.PassedCourseHoursLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Hours:</span></p></body></html>", None))
        self.PassedCourseHoursValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">3</span></p></body></html>", None))
        self.PassedCoursePermissionLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Permission:</span></p></body></html>", None))
        self.PassedCoursePermissionValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Required</span></p></body></html>", None))
        self.PassedCourseDoctorLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Doctor:</span></p></body></html>", None))
        self.PassedCourseDoctorValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Dr. Joseph Gonzalez</span></p></body></html>", None))
        self.PassedCourseDegreeLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Degree:</span></p></body></html>", None))
        self.PassedCourseDegreeValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">120</span></p></body></html>", None))
        self.PassedCourseGradeLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Grade:</span></p></body></html>", None))
        self.PassedCourseGradeValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">B+</span></p></body></html>", None))
        self.PassedCourseAttendanceLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Attendance:</span></p></body></html>", None))
        self.PassedCourseAttendanceValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">60</span></p></body></html>", None))
        self.FailedCoursesLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Failed Courses</span></p></body></html>", None))
        self.FailedCoursesValueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">3</span></p></body></html>", None))
        self.FailedCourseIDLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">ID:</span></p></body></html>", None))
        self.FailedCourseIDValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">C110</span></p></body></html>", None))
        self.FailedCourseHoursLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Hours:</span></p></body></html>", None))
        self.FailedCourseHoursValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">3</span></p></body></html>", None))
        self.FailedCoursePermissionLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Permission:</span></p></body></html>", None))
        self.FailedCoursePermissionValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Required</span></p></body></html>", None))
        self.FailedCourseDoctorLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Doctor:</span></p></body></html>", None))
        self.FailedCourseDoctorValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Dr. Joseph Gonzalez</span></p></body></html>", None))
        self.FailedCourseDegreeLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Degree:</span></p></body></html>", None))
        self.FailedCourseDegreeValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">120</span></p></body></html>", None))
        self.FailedCourseAttendanceLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Attendance:</span></p></body></html>", None))
        self.FailedCourseAttendanceValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">60</span></p></body></html>", None))
        self.FailedCourseRemainingStudentsLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Remaining Students:</span></p></body></html>", None))
        self.FailedCourseRemainingStudentsValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">20</span></p></body></html>", None))
        self.FailedCoursePassRateLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Pass Rate (at Time):</span></p></body></html>", None))
        self.FailedCoursePassRateValueLabel_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">75%</span></p></body></html>", None))
        self.SearchForCourseButton.setText(QCoreApplication.translate("MainWindow", u"Search for Course", None))
        self.UndoButton.setText("")
        self.ProfileButton.setText("")
        self.AnalysisButton.setText("")
        self.CoursesButton.setText("")
        self.AiButton.setText("")
        self.LogOutButton.setText("")
        pass
    # retranslateUi

