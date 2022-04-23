import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QLineEdit, QWidget, QPushButton, QLabel, QApplication


class Register(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(370, 377)
        Form.setFixedSize(370, 377)
        Form.setStyleSheet("QWidget{\n"
                           "background-color: rgb(86, 86, 86);\n"
                           "font: 63 14pt \"MS Shell Dlg 2\";\n"
                           "}\n"

                           "QLineEdit{\n"
                           "background-color: rgb(0, 0, 0, 0);\n"
                           "border: none;\n"
                           "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                           "color: rgba(255,255,255,230);\n"
                           "padding-bottom: 7px;\n"
                           "}\n"

                           "QPushButton{\n"
                           "background-color: rgb(121, 167, 177);\n"
                           "border-radius: 5px;"
                           "}\n"

                           "QPushButton:hover{\n"
                           "background-color: rgb(52, 164, 235);\n"
                           "padding-left: 1px;"
                           "padding-top: 1px;"
                           "}\n"

                           "QPushButton:pressed{\n"
                           "background-color: rgb(52, 143, 235);\n"
                           "border-radius: 5px;"
                           "padding-left: 5px;"
                           "padding-top: 5px;"
                           "}\n"

                           "QLabel{\n"
                           "color: rgb(255, 255, 255);\n"
                           "}")

        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(50, 100, 261, 30))
        self.lineEdit.setFont(font)
        self.lineEdit.setStatusTip("")
        self.lineEdit.setWhatsThis("")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(25)
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 190, 261, 30))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setInputMethodHints(
            QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhNoAutoUppercase | QtCore.Qt.ImhNoPredictiveText | QtCore.Qt.ImhSensitiveData)
        self.lineEdit_2.setMaxLength(22)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 260, 111, 41))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.label = QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 10, 71, 31))
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton_2.setText(_translate("Form", "Sign up"))
        self.label.setText(_translate("Form", "Sign up"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Register()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())