# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginForm.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from FormMain import Ui_FormMain
from sqlite3 import Error
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Ui_Form(object):
    ##### Hiện cảnh báo đăng nhập khi nhân nut ########################################################
    def ShowWarning(self):
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("tên đăng nhập và mật khẩu sai")
            self.msg.setWindowTitle("Cảnh báo ")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.exec()
    ###################################################################################################
    ## Hiện form quản lý
    def ShowMainForm(self):
            self.FormMain= QtWidgets.QMainWindow()
            self.ui= Ui_FormMain()
            self.ui.setupUi(self.FormMain)
            self.FormMain.show()

    ###################################################################################################
    ############### chức năng đăng nhập ###############################################################
    def LoginCheck(self) :
        username= self.txtUsername.text()
        password=self.txtPassWord.text()
        connection= sqlite3.connect("DiemDanh.db")
        result = connection.execute("select *  from TaiKhoan where Username=? and PassWord=?",(username,password))

        if(len(result.fetchall())>0):
            print("user found ")
            self.ShowMainForm()
        else :
            self.ShowWarning()
            ###############################################################################################
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(318, 204)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 10, 81, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 81, 16))
        self.label_2.setObjectName("label_2")
        self.txtUsername = QtWidgets.QLineEdit(Form)
        self.txtUsername.setGeometry(QtCore.QRect(120, 70, 131, 20))
        self.txtUsername.setObjectName("txtUsername")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 100, 81, 16))
        self.label_3.setObjectName("label_3")
        self.txtPassWord = QtWidgets.QLineEdit(Form)
        self.txtPassWord.setGeometry(QtCore.QRect(120, 100, 131, 20))
        self.txtPassWord.setObjectName("txtPassWord")
        self.btnDangNhap = QtWidgets.QPushButton(Form)
        self.btnDangNhap.setGeometry(QtCore.QRect(70, 150, 75, 23))
        self.btnDangNhap.setObjectName("btnDangNhap")
### gán chức năng co button đăng nhập###################################3#####################################
        self.btnDangNhap.clicked.connect(self.LoginCheck)
##########################################################################3#######################################
        self.btnHuy = QtWidgets.QPushButton(Form)
        self.btnHuy.setGeometry(QtCore.QRect(170, 150, 75, 23))
        self.btnHuy.setObjectName("btnHuy")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Đăng nhập quan lý"))
        self.label.setText(_translate("Form", "Đăng nhập "))
        self.label_2.setText(_translate("Form", "Username : "))
        self.label_3.setText(_translate("Form", "PassWord: "))
        self.btnDangNhap.setText(_translate("Form", "Đăng nhập "))
        self.btnHuy.setText(_translate("Form", "Hủy "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

