# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateForm.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import cv2
import sqlite3
from sqlite3 import Error
import sys
import os

class Ui_FormCreate(object):
    def ExitApp(self):
        self.destory()

    ########## Insert dữ liệu nhân viên vào cơ sở dữ liệu ##############################3
    def InsertOrUpdate (self):
        HoTen=self.txtHoTen.text()
        Tuoi=self.txtTuoi.text()
        GioiTinh=str(self.ComboGioiTinh.currentText())
        ChucVu = str(self.ComboChucVu.currentText())
        PhongBan= str(self.ComboPhongBan.currentText())
        DiaChi=self.txtDiaChi.text()
        SoDienThoai= self.txtSoDienThoai.text()
        Email= self.txtEmail.text()
        Task= (HoTen,Tuoi,GioiTinh,DiaChi,ChucVu,PhongBan,SoDienThoai,Email)
        conn= sqlite3.connect("DiemDanh.db")
        c=conn.cursor()
        cmd="INSERT INTO NhanVien ( HoTen, Tuoi, GioiTinh, DiaChi, ChucVu, PhongBan, SoDienThoai, Email ) VALUES (?,?,?,?,?,?,?,?)"
        c.execute(cmd,Task)
        conn.commit()
        c.close()
        conn.close()

##### kiểm tra dữ liệu nhập vào : trống hay không ##############################################################


############# Chụp ảnh tạo cơ sở dữ liệu cho phần mềm ###########################################################
    def LoadCam(self):
        import LoadCam
#################################################################################################################
############## kHỞI TẠO THÀNH PHẦN CHO FORM TẠO MỚI : BUTTON / LABEL / TEXTBOX
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(546, 247)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.label.setObjectName("label")
        self.txtHoTen = QtWidgets.QLineEdit(Form)
        self.txtHoTen.setGeometry(QtCore.QRect(80, 20, 161, 20))
        self.txtHoTen.setObjectName("txtHoTen")
        self.txtTuoi = QtWidgets.QSpinBox(Form)
        self.txtTuoi.setGeometry(QtCore.QRect(380, 20, 42, 22))
        self.txtTuoi.setObjectName("txtTuoi")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(330, 20, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 61, 16))
        self.label_3.setObjectName("label_3")
        self.txtDiaChi = QtWidgets.QLineEdit(Form)
        self.txtDiaChi.setGeometry(QtCore.QRect(80, 110, 161, 20))
        self.txtDiaChi.setObjectName("txtDiaChi")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(270, 70, 81, 16))
        self.label_4.setObjectName("label_4")
        self.txtSoDienThoai = QtWidgets.QLineEdit(Form)
        self.txtSoDienThoai.setGeometry(QtCore.QRect(360, 70, 161, 20))
        self.txtSoDienThoai.setObjectName("txtSoDienThoai")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 61, 16))
        self.label_5.setObjectName("label_5")
        self.txtEmail = QtWidgets.QLineEdit(Form)
        self.txtEmail.setGeometry(QtCore.QRect(80, 160, 161, 20))
        self.txtEmail.setObjectName("txtEmail")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(280, 120, 61, 16))
        self.label_6.setObjectName("label_6")
        self.ComboChucVu = QtWidgets.QComboBox(Form)
        self.ComboChucVu.setGeometry(QtCore.QRect(360, 120, 161, 22))
        self.ComboChucVu.setObjectName("comboBox")
        self.ComboChucVu.addItem("")
        self.ComboChucVu.addItem("")
        self.ComboChucVu.addItem("")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(280, 160, 61, 16))
        self.label_7.setObjectName("label_7")
        self.ComboPhongBan = QtWidgets.QComboBox(Form)
        self.ComboPhongBan.setGeometry(QtCore.QRect(360, 160, 161, 22))
        self.ComboPhongBan.setObjectName("comboBox_2")
        self.ComboPhongBan.addItem("")
        self.ComboPhongBan.addItem("")
        self.ComboPhongBan.addItem("")
        self.ComboPhongBan.addItem("")
        self.ComboGioiTinh = QtWidgets.QComboBox(Form)
        self.ComboGioiTinh.setGeometry(QtCore.QRect(80, 60, 131, 22))
        self.ComboGioiTinh.setObjectName("comboBox_3")
        self.ComboGioiTinh.addItem("")
        self.ComboGioiTinh.addItem("")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.InsertOrUpdate)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(376, 210, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        #####################  Kiểm tra Id ######################
        self.pushButton_2.clicked.connect(self.ExitApp)
        self.pushButton_3 = QtWidgets.QPushButton(Form)

        self.pushButton_3.setGeometry(QtCore.QRect(100, 210, 131, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        ############ nhân diện ##########33
        self.pushButton_3.clicked.connect(self.LoadCam)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form Tạo mới Nhân viên "))
        self.label.setText(_translate("Form", "Họ và tên : "))

        self.label_2.setText(_translate("Form", "Tuổi  : "))
        self.label_3.setText(_translate("Form", "Địa chỉ : "))
        self.label_4.setText(_translate("Form", "Số điện thoại : "))
        self.label_5.setText(_translate("Form", "Email : "))
        self.label_6.setText(_translate("Form", "Chức vụ:  "))
        self.ComboChucVu.setItemText(0, _translate("Form", "Trưởng phòng "))
        self.ComboChucVu.setItemText(1, _translate("Form", "Phó phòng"))
        self.ComboChucVu.setItemText(2, _translate("Form", "Nhân viên "))
        self.label_7.setText(_translate("Form", "Phòng ban : "))
        self.ComboPhongBan.setItemText(0, _translate("Form", "Kinh Doanh"))
        self.ComboPhongBan.setItemText(1, _translate("Form", "IT"))
        self.ComboPhongBan.setItemText(2, _translate("Form", "Nhân sự"))
        self.ComboPhongBan.setItemText(3, _translate("Form", "Đối ngoại"))
        self.ComboGioiTinh.setItemText(0, _translate("Form", "Nam"))
        self.ComboGioiTinh.setItemText(1, _translate("Form", "Nữ"))
        self.label_8.setText(_translate("Form", "Giới Tính : "))
        self.pushButton.setText(_translate("Form", "Thêm mới "))
        self.pushButton_2.setText(_translate("Form", "Hủy "))
        self.pushButton_3.setText(_translate("Form", "Chụp ảnh Nhận diện "))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_FormCreate()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

