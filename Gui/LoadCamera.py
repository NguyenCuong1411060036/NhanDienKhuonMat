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


class Ui_FormCreate(object):
    def text(self):
        import CreateDataSet
    ########## Insert dữ liệu nhân viên vào cơ sở dữ liệu ##############################3
    def InsertOrUpdate (self,HoTen,Tuoi,DiaChi,Luong):
        conn= sqlite3.connect("DiemDanh.db")
        c=conn.cursor()
        cmd= "INSERT INTO NhanVien (HoTen,Tuoi, DiaChi, Luong) VALUES ('"+HoTen+"', '"+Tuoi+"','"+DiaChi+"','"+Luong+"')"
        c.execute(cmd)
        conn.commit()
        c.close()
        conn.close()

##### kiểm tra dữ liệu nhập vào : trống hay không ##############################################################


############# Chụp ảnh tạo cơ sở dữ liệu cho phần mềm ###########################################################
    def LoadCam(self):
        vid_cam = cv2.VideoCapture(0)
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        connection= sqlite3.connect("DiemDanh.db")
        result = connection.execute("select count(*) from Nhanvien")
        values= result.fetchone()
        if(values[0]>0):
            face_id= values[0] + 1
        else :
            face_id=1
        print("faceid "+str(face_id))
        count = 0
        while(True):
            _, image_frame = vid_cam.read()

            gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)

                count += 1
                cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

                cv2.imshow('frame', image_frame)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif count>100:
                break
        vid_cam.release()
        cv2.destroyAllWindows()
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
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(380, 20, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(330, 20, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 61, 16))
        self.label_3.setObjectName("label_3")
        self.txtHoTen_2 = QtWidgets.QLineEdit(Form)
        self.txtHoTen_2.setGeometry(QtCore.QRect(80, 110, 161, 20))
        self.txtHoTen_2.setObjectName("txtHoTen_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(270, 70, 81, 16))
        self.label_4.setObjectName("label_4")
        self.txtHoTen_3 = QtWidgets.QLineEdit(Form)
        self.txtHoTen_3.setGeometry(QtCore.QRect(360, 70, 161, 20))
        self.txtHoTen_3.setObjectName("txtHoTen_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 61, 16))
        self.label_5.setObjectName("label_5")
        self.txtHoTen_4 = QtWidgets.QLineEdit(Form)
        self.txtHoTen_4.setGeometry(QtCore.QRect(80, 160, 161, 20))
        self.txtHoTen_4.setObjectName("txtHoTen_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(280, 120, 61, 16))
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(360, 120, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(280, 160, 61, 16))
        self.label_7.setObjectName("label_7")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(360, 160, 161, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(80, 60, 131, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(376, 210, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        #####################  Kiểm tra Id ######################
        self.pushButton_2.clicked.connect(self.text)
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
        self.label_6.setText(_translate("Form", "Phòng ban:  "))
        self.comboBox.setItemText(0, _translate("Form", "Nhân sự "))
        self.comboBox.setItemText(1, _translate("Form", "Kinh Doanh"))
        self.comboBox.setItemText(2, _translate("Form", "Kế Hoạch "))
        self.label_7.setText(_translate("Form", "Chức vụ : "))
        self.comboBox_2.setItemText(0, _translate("Form", "Trưởng Phòng"))
        self.comboBox_2.setItemText(1, _translate("Form", "Phó Phòng"))
        self.comboBox_2.setItemText(2, _translate("Form", "Nhân viên "))
        self.comboBox_3.setItemText(0, _translate("Form", "Nam"))
        self.comboBox_3.setItemText(1, _translate("Form", "Nữ"))
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

