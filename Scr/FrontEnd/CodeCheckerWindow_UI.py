from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget

class Ui_CodeCheckerWindow(object):
    def setupUi(self, CodeCheckerWindow):
        if not CodeCheckerWindow.objectName():
            CodeCheckerWindow.setObjectName(u"CodeCheckerWindow")
        CodeCheckerWindow.resize(900, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CodeCheckerWindow.sizePolicy().hasHeightForWidth())
        CodeCheckerWindow.setSizePolicy(sizePolicy)
        CodeCheckerWindow.setMinimumSize(QSize(900, 650))
        CodeCheckerWindow.setMaximumSize(QSize(900, 650))
        font = QFont()
        font.setFamilies([u"Calibri"])
        CodeCheckerWindow.setFont(font)
        CodeCheckerWindow.setStyleSheet(u"background-color: qlineargradient(\n"
"	y1:0, y2:1,x1:0, x2:1\n"
"	stop:0 rgb(128, 15, 28),\n"
"	stop:0.5 rgb(27, 49, 96),\n"
"	stop:1 rgb(7, 74, 45)\n"
");")
        self.CodeCheckerWindow_Layout = QVBoxLayout(CodeCheckerWindow)
        self.CodeCheckerWindow_Layout.setSpacing(5)
        self.CodeCheckerWindow_Layout.setObjectName(u"CodeCheckerWindow_Layout")
        self.CodeCheckerWindow_Layout.setContentsMargins(75, 0, 75, 0)
        self.CodeCheckerWindowTopSpacer = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.CodeCheckerWindow_Layout.addItem(self.CodeCheckerWindowTopSpacer)

        self.WelcomePhraseLabel = QLabel(CodeCheckerWindow)
        self.WelcomePhraseLabel.setObjectName(u"WelcomePhraseLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.WelcomePhraseLabel.sizePolicy().hasHeightForWidth())
        self.WelcomePhraseLabel.setSizePolicy(sizePolicy1)
        self.WelcomePhraseLabel.setMinimumSize(QSize(750, 50))
        self.WelcomePhraseLabel.setMaximumSize(QSize(750, 50))
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(50)
        font1.setBold(True)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.WelcomePhraseLabel.setFont(font1)
        self.WelcomePhraseLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.WelcomePhraseLabel.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.CodeCheckerWindow_Layout.addWidget(self.WelcomePhraseLabel)

        self.LineEditsWidget = QWidget(CodeCheckerWindow)
        self.LineEditsWidget.setObjectName(u"LineEditsWidget")
        self.LineEditsWidget.setMinimumSize(QSize(750, 200))
        self.LineEditsWidget.setMaximumSize(QSize(750, 200))
        self.LineEditsWidget.setStyleSheet(u"background-color: none;")
        self.LineEditsWidget_Layout = QVBoxLayout(self.LineEditsWidget)
        self.LineEditsWidget_Layout.setSpacing(5)
        self.LineEditsWidget_Layout.setObjectName(u"LineEditsWidget_Layout")
        self.LineEditsWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.IDBoxLabel = QLabel(self.LineEditsWidget)
        self.IDBoxLabel.setObjectName(u"IDBoxLabel")
        sizePolicy1.setHeightForWidth(self.IDBoxLabel.sizePolicy().hasHeightForWidth())
        self.IDBoxLabel.setSizePolicy(sizePolicy1)
        self.IDBoxLabel.setMinimumSize(QSize(750, 25))
        self.IDBoxLabel.setMaximumSize(QSize(750, 25))
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.IDBoxLabel.setFont(font2)
        self.IDBoxLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.IDBoxLabel.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.LineEditsWidget_Layout.addWidget(self.IDBoxLabel)

        self.IDBox = QLineEdit(self.LineEditsWidget)
        self.IDBox.setObjectName(u"IDBox")
        self.IDBox.setMinimumSize(QSize(750, 50))
        self.IDBox.setMaximumSize(QSize(750, 50))
        font3 = QFont()
        font3.setFamilies([u"Calibri"])
        font3.setPointSize(18)
        self.IDBox.setFont(font3)
        self.IDBox.setStyleSheet(u"background-color: \"white\";\n"
"border-radius: 10px;\n"
"color: \"black\";\n"
"padding-left: 10px;")
        self.IDBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.LineEditsWidget_Layout.addWidget(self.IDBox, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.PasswordBoxLabel = QLabel(self.LineEditsWidget)
        self.PasswordBoxLabel.setObjectName(u"PasswordBoxLabel")
        sizePolicy1.setHeightForWidth(self.PasswordBoxLabel.sizePolicy().hasHeightForWidth())
        self.PasswordBoxLabel.setSizePolicy(sizePolicy1)
        self.PasswordBoxLabel.setMinimumSize(QSize(750, 25))
        self.PasswordBoxLabel.setMaximumSize(QSize(750, 25))
        self.PasswordBoxLabel.setFont(font2)
        self.PasswordBoxLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.PasswordBoxLabel.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.LineEditsWidget_Layout.addWidget(self.PasswordBoxLabel)

        self.PasswordBox = QLineEdit(self.LineEditsWidget)
        self.PasswordBox.setObjectName(u"PasswordBox")
        self.PasswordBox.setMinimumSize(QSize(750, 50))
        self.PasswordBox.setMaximumSize(QSize(750, 50))
        font4 = QFont()
        font4.setFamilies([u"Calibri"])
        font4.setPointSize(18)
        font4.setBold(False)
        font4.setStyleStrategy(QFont.PreferAntialias)
        self.PasswordBox.setFont(font4)
        self.PasswordBox.setStyleSheet(u"background-color: \"white\";\n"
"border-radius: 10px;\n"
"color: \"black\";\n"
"padding-left: 10px;")
        self.PasswordBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.LineEditsWidget_Layout.addWidget(self.PasswordBox, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.ErrorPhraseLabel = QLabel(self.LineEditsWidget)
        self.ErrorPhraseLabel.setObjectName(u"ErrorPhraseLabel")
        sizePolicy1.setHeightForWidth(self.ErrorPhraseLabel.sizePolicy().hasHeightForWidth())
        self.ErrorPhraseLabel.setSizePolicy(sizePolicy1)
        self.ErrorPhraseLabel.setMinimumSize(QSize(750, 25))
        self.ErrorPhraseLabel.setMaximumSize(QSize(750, 25))
        self.ErrorPhraseLabel.setFont(font2)
        self.ErrorPhraseLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ErrorPhraseLabel.setStyleSheet(u"background-color: none;\n"
"color: \"white\";")

        self.LineEditsWidget_Layout.addWidget(self.ErrorPhraseLabel)

        self.LineEditsWidgetSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.LineEditsWidget_Layout.addItem(self.LineEditsWidgetSpacer)


        self.CodeCheckerWindow_Layout.addWidget(self.LineEditsWidget)

        self.LogInButtonWidget = QWidget(CodeCheckerWindow)
        self.LogInButtonWidget.setObjectName(u"LogInButtonWidget")
        self.LogInButtonWidget.setMinimumSize(QSize(750, 50))
        self.LogInButtonWidget.setMaximumSize(QSize(750, 50))
        self.LogInButtonWidget.setStyleSheet(u"background-color: none;")
        self.LogInButtonWidget_Layout = QHBoxLayout(self.LogInButtonWidget)
        self.LogInButtonWidget_Layout.setSpacing(0)
        self.LogInButtonWidget_Layout.setObjectName(u"LogInButtonWidget_Layout")
        self.LogInButtonWidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.LogInButton = QPushButton(self.LogInButtonWidget)
        self.LogInButton.setObjectName(u"LogInButton")
        self.LogInButton.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.LogInButton.sizePolicy().hasHeightForWidth())
        self.LogInButton.setSizePolicy(sizePolicy2)
        self.LogInButton.setMinimumSize(QSize(100, 50))
        self.LogInButton.setMaximumSize(QSize(100, 50))
        font5 = QFont()
        font5.setFamilies([u"Calibri"])
        font5.setPointSize(18)
        font5.setBold(True)
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.LogInButton.setFont(font5)
        self.LogInButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(235, 235, 235);\n"
"	border-radius: 10px;\n"
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
        self.LogInButton.setCheckable(True)

        self.LogInButtonWidget_Layout.addWidget(self.LogInButton)


        self.CodeCheckerWindow_Layout.addWidget(self.LogInButtonWidget)

        self.CodeCheckerWindowBottomSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.CodeCheckerWindow_Layout.addItem(self.CodeCheckerWindowBottomSpacer)


        self.retranslateUi(CodeCheckerWindow)

        QMetaObject.connectSlotsByName(CodeCheckerWindow)
    # setupUi

    def retranslateUi(self, CodeCheckerWindow):
        self.WelcomePhraseLabel.setText(QCoreApplication.translate("CodeCheckerWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Hello</span></p></body></html>", None))
        self.IDBoxLabel.setText(QCoreApplication.translate("CodeCheckerWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">ID:</span></p></body></html>", None))
        self.IDBox.setText("")
        self.PasswordBoxLabel.setText(QCoreApplication.translate("CodeCheckerWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Password:</span></p></body></html>", None))
        self.PasswordBox.setText("")
        self.ErrorPhraseLabel.setText(QCoreApplication.translate("CodeCheckerWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Wrong ID or Password</span></p></body></html>", None))
        self.LogInButton.setText(QCoreApplication.translate("CodeCheckerWindow", u"Login", None))
        pass
    # retranslateUi

