import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi

class loginWidget(QDialog):
    def __init__(self):
        super(loginWidget, self).__init__()
        loadUi('login.ui', self)
        self.loginButton.clicked.connect(self.loginFunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.registerButton.clicked.connect(self.registerFunction)
        self.savedUserName = ""
        self.savedPassword = ""

    def registerFunction(self):
        registerForm = registerWidget(self)
        widgetStack.addWidget(registerForm)
        widgetStack.setCurrentIndex(widgetStack.currentIndex() + 1)

    def loginFunction(self):
        username = self.userName.text()
        password = self.password.text()

        if not username or not password:
            self.showWarning("You must fill all fields")
        else:
            self.checkLogin(username, password)

    def checkLogin(self, user, passw):
        if user == self.savedUserName and passw == self.savedPassword:
            self.showInfo("Login successful")
        else:
            self.showWarning("Wrong username or password")

    def showWarning(self, message):
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Warning)
        messageBox.setWindowTitle("Warning")
        messageBox.setText(message)
        messageBox.exec_()

    def showInfo(self, message):
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Information)
        messageBox.setWindowTitle("Information")
        messageBox.setText(message)
        messageBox.exec_()

class registerWidget(QDialog):
    def __init__(self, login_widget):
        super(registerWidget, self).__init__()
        loadUi('register.ui', self)
        self.signUpButton.clicked.connect(self.signUpFunction)
        self.loginWidget = login_widget
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)

    def signUpFunction(self):
        username = self.userName.text()
        password = self.password.text()

        if not username or not password:
            self.showWarning("You must fill all fields")
        elif self.password.text() == self.confirmPassword.text():
            self.loginWidget.savedUserName = username
            self.loginWidget.savedPassword = password
            widgetStack.setCurrentIndex(widgetStack.currentIndex() - 1)
        else:
            self.showWarning('Passwords did not match')

    def showWarning(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Warning")
        msg_box.setText(message)
        msg_box.exec_()

app = QApplication(sys.argv)
widgetStack = QtWidgets.QStackedWidget()
mainWindow = loginWidget()
widgetStack.addWidget(mainWindow)
widgetStack.show()
widgetStack.setFixedHeight(600)
widgetStack.setFixedWidth(600)
app.exec_()
