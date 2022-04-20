import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Register(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(370, 377)
        Form.setStyleSheet("QWidget{\n"
                           "background-color: rgb(86, 86, 86);\n"
                           "    font: 63 14pt \"MS Shell Dlg 2\";\n"
                           "}\n"
                           "QLineEdit{\n"
                           "background-color: rgb(121, 167, 177);\n"
                           "border-radius:15px;\n"
                           "}\n"
                           "QPushButton{\n"
                           "background-color: rgb(121, 167, 177);\n"
                           "}\n"
                           "QLabel{\n"
                           "color: rgb(255, 255, 255);\n"
                           "}")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 160, 131, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 190, 261, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setInputMethodHints(
            QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhNoAutoUppercase | QtCore.Qt.ImhNoPredictiveText | QtCore.Qt.ImhSensitiveData)
        self.lineEdit_2.setMaxLength(22)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 131, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 260, 111, 41))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(50, 100, 261, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lineEdit.setFont(font)
        self.lineEdit.setStatusTip("")
        self.lineEdit.setWhatsThis("")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(25)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Password"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.label_2.setText(_translate("Form", "Username"))
        self.pushButton_2.setText(_translate("Form", "Sign up"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Username"))
        self.label.setText(_translate("Form", "Sign up"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Register()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
