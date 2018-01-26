# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormMain.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
from CreateForm import Ui_FormCreate
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormMain(object):
    ######## Hiện form tạo mới nhân viên .
    def ShowCreateForm(self) :
            self.CreateForm= QtWidgets.QMainWindow()
            self.ui= Ui_FormCreate()
            self.ui.setupUi(self.CreateForm)
            self.CreateForm.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(694, 553)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 191, 141))
        self.groupBox.setObjectName("groupBox")
        self.btnDanhSach = QtWidgets.QPushButton(self.groupBox)
        self.btnDanhSach.setGeometry(QtCore.QRect(30, 30, 141, 31))
        self.btnDanhSach.setObjectName("btnDanhSach")
        self.btnThemMoi = QtWidgets.QPushButton(self.groupBox)
        self.btnThemMoi.setGeometry(QtCore.QRect(30, 80, 141, 31))
        self.btnThemMoi.setObjectName("btnThemMoi")
        ##########################################################3
        self.btnThemMoi.clicked.connect(self.ShowCreateForm)
        ################### Thêm mới nhân viên  ################3

        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 170, 191, 361))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnThongkeNhanVien = QtWidgets.QPushButton(self.groupBox_2)
        self.btnThongkeNhanVien.setGeometry(QtCore.QRect(30, 30, 141, 51))
        self.btnThongkeNhanVien.setObjectName("btnThongkeNhanVien")
        self.btnThongKeTheoNgay = QtWidgets.QPushButton(self.groupBox_2)
        self.btnThongKeTheoNgay.setGeometry(QtCore.QRect(30, 110, 141, 51))
        self.btnThongKeTheoNgay.setObjectName("btnThongKeTheoNgay")
        self.btnThongKeTheoThang = QtWidgets.QPushButton(self.groupBox_2)
        self.btnThongKeTheoThang.setGeometry(QtCore.QRect(30, 190, 141, 51))
        self.btnThongKeTheoThang.setObjectName("btnThongKeTheoThang")
        self.btnTinhLuong = QtWidgets.QPushButton(self.groupBox_2)
        self.btnTinhLuong.setGeometry(QtCore.QRect(30, 270, 141, 51))
        self.btnTinhLuong.setObjectName("btnTinhLuong")
        self.GroupParent = QtWidgets.QGroupBox(Form)
        self.GroupParent.setGeometry(QtCore.QRect(200, 10, 481, 521))
        self.GroupParent.setObjectName("GroupParent")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Quản lý điểm danh nhân viên"))
        self.groupBox.setTitle(_translate("Form", "Nhân viên "))
        self.btnDanhSach.setText(_translate("Form", "Danh sách nhân viên "))
        self.btnThemMoi.setText(_translate("Form", "Thêm mới "))
        self.groupBox_2.setTitle(_translate("Form", "Thống kê"))
        self.btnThongkeNhanVien.setText(_translate("Form", "Thống kê theo nhân viên"))
        self.btnThongKeTheoNgay.setText(_translate("Form", "Thống kê theo ngày "))
        self.btnThongKeTheoThang.setText(_translate("Form", "Thống kê theo tháng"))
        self.btnTinhLuong.setText(_translate("Form", "Tính lương nhân viên"))
        self.GroupParent.setTitle(_translate("Form", "Chi Tiết "))


if __name__ == "__main__":
    import sys
    import cv2
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_FormMain()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

