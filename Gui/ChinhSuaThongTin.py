# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChinhSuaThongTin.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormChinhSua(object):
    def setupUi(self, FormChinhSua):
        FormChinhSua.setObjectName("FormChinhSua")
        FormChinhSua.resize(609, 627)
        self.groupChucNang = QtWidgets.QGroupBox(FormChinhSua)
        self.groupChucNang.setGeometry(QtCore.QRect(30, 10, 551, 611))
        self.groupChucNang.setObjectName("groupChucNang")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupChucNang)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 531, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label.setObjectName("label")
        self.txtHoTen = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtHoTen.setGeometry(QtCore.QRect(90, 20, 171, 20))
        self.txtHoTen.setObjectName("txtHoTen")
        self.txtTuoi = QtWidgets.QSpinBox(self.groupBox_2)
        self.txtTuoi.setGeometry(QtCore.QRect(470, 20, 42, 22))
        self.txtTuoi.setObjectName("txtTuoi")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(420, 20, 47, 13))
        self.label_2.setObjectName("label_2")
        self.txtGioiTinh = QtWidgets.QComboBox(self.groupBox_2)
        self.txtGioiTinh.setGeometry(QtCore.QRect(90, 50, 69, 22))
        self.txtGioiTinh.setObjectName("txtGioiTinh")
        self.txtGioiTinh.addItem("")
        self.txtGioiTinh.addItem("")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(280, 60, 71, 16))
        self.label_4.setObjectName("label_4")
        self.txtSoDienThoai = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtSoDienThoai.setGeometry(QtCore.QRect(380, 60, 141, 20))
        self.txtSoDienThoai.setObjectName("txtSoDienThoai")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.label_5.setObjectName("label_5")
        self.txtDiaChi = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtDiaChi.setGeometry(QtCore.QRect(90, 90, 171, 20))
        self.txtDiaChi.setObjectName("txtDiaChi")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 71, 16))
        self.label_6.setObjectName("label_6")
        self.txtEmail = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtEmail.setGeometry(QtCore.QRect(90, 130, 171, 20))
        self.txtEmail.setObjectName("txtEmail")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(300, 100, 47, 13))
        self.label_7.setObjectName("label_7")
        self.txtChucVu = QtWidgets.QComboBox(self.groupBox_2)
        self.txtChucVu.setGeometry(QtCore.QRect(380, 100, 131, 22))
        self.txtChucVu.setObjectName("txtChucVu")
        self.txtChucVu.addItem("")
        self.txtChucVu.addItem("")
        self.txtChucVu.addItem("")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(290, 140, 61, 16))
        self.label_8.setObjectName("label_8")
        self.txtKinhDoanh = QtWidgets.QComboBox(self.groupBox_2)
        self.txtKinhDoanh.setGeometry(QtCore.QRect(380, 140, 131, 22))
        self.txtKinhDoanh.setObjectName("txtKinhDoanh")
        self.txtKinhDoanh.addItem("")
        self.txtKinhDoanh.addItem("")
        self.txtKinhDoanh.addItem("")
        self.txtKinhDoanh.addItem("")
        self.btnXoa = QtWidgets.QPushButton(self.groupBox_2)
        self.btnXoa.setGeometry(QtCore.QRect(70, 170, 75, 23))
        self.btnXoa.setObjectName("btnXoa")
        self.btnCapNhatKhuonMat = QtWidgets.QPushButton(self.groupBox_2)
        self.btnCapNhatKhuonMat.setGeometry(QtCore.QRect(170, 170, 111, 23))
        self.btnCapNhatKhuonMat.setObjectName("btnCapNhatKhuonMat")
        self.btnThoat = QtWidgets.QPushButton(self.groupBox_2)
        self.btnThoat.setGeometry(QtCore.QRect(410, 170, 75, 23))
        self.btnThoat.setObjectName("btnThoat")
        self.btnLuuLai = QtWidgets.QPushButton(self.groupBox_2)
        self.btnLuuLai.setGeometry(QtCore.QRect(310, 170, 75, 23))
        self.btnLuuLai.setObjectName("btnLuuLai")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(300, 20, 41, 16))
        self.label_9.setObjectName("label_9")
        self.LbID = QtWidgets.QLabel(self.groupBox_2)
        self.LbID.setGeometry(QtCore.QRect(350, 20, 47, 13))
        self.LbID.setObjectName("LbID")
        self.DanhsachNhanVien = QtWidgets.QGroupBox(self.groupChucNang)
        self.DanhsachNhanVien.setGeometry(QtCore.QRect(10, 240, 531, 321))
        self.DanhsachNhanVien.setObjectName("DanhsachNhanVien")
        self.tableDanhSachNhanVien = QtWidgets.QTableView(self.DanhsachNhanVien)
        self.tableDanhSachNhanVien.setGeometry(QtCore.QRect(10, 30, 521, 291))
        self.tableDanhSachNhanVien.setObjectName("tableDanhSachNhanVien")
        self.pushButton = QtWidgets.QPushButton(self.groupChucNang)
        self.pushButton.setGeometry(QtCore.QRect(230, 570, 91, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(FormChinhSua)
        QtCore.QMetaObject.connectSlotsByName(FormChinhSua)

    def retranslateUi(self, FormChinhSua):
        _translate = QtCore.QCoreApplication.translate
        FormChinhSua.setWindowTitle(_translate("FormChinhSua", "Chỉnh sửa thông tin nhân viên "))
        self.groupChucNang.setTitle(_translate("FormChinhSua", "GroupBox"))
        self.groupBox_2.setTitle(_translate("FormChinhSua", "GroupBox"))
        self.label.setText(_translate("FormChinhSua", "Họ Tên : "))
        self.label_2.setText(_translate("FormChinhSua", "Tuổi : "))
        self.txtGioiTinh.setItemText(0, _translate("FormChinhSua", "Nam"))
        self.txtGioiTinh.setItemText(1, _translate("FormChinhSua", "Nữ"))
        self.label_3.setText(_translate("FormChinhSua", "Giới tính : "))
        self.label_4.setText(_translate("FormChinhSua", "Số điện thoại : "))
        self.label_5.setText(_translate("FormChinhSua", "Địa chỉ : "))
        self.label_6.setText(_translate("FormChinhSua", "Email : "))
        self.label_7.setText(_translate("FormChinhSua", "Chức vụ : "))
        self.txtChucVu.setItemText(0, _translate("FormChinhSua", "Trưởng phòng"))
        self.txtChucVu.setItemText(1, _translate("FormChinhSua", "Phó phòng"))
        self.txtChucVu.setItemText(2, _translate("FormChinhSua", "Nhân viên "))
        self.label_8.setText(_translate("FormChinhSua", "Phòng ban : "))
        self.txtKinhDoanh.setItemText(0, _translate("FormChinhSua", "Kinh doanh"))
        self.txtKinhDoanh.setItemText(1, _translate("FormChinhSua", "IT"))
        self.txtKinhDoanh.setItemText(2, _translate("FormChinhSua", "Nhân sự"))
        self.txtKinhDoanh.setItemText(3, _translate("FormChinhSua", "Đối ngoại"))
        self.btnXoa.setText(_translate("FormChinhSua", "Xóa "))
        self.btnCapNhatKhuonMat.setText(_translate("FormChinhSua", "Cập nhật Khuôn mặt"))
        self.btnThoat.setText(_translate("FormChinhSua", "Thoát "))
        self.btnLuuLai.setText(_translate("FormChinhSua", "Lưu lại"))
        self.label_9.setText(_translate("FormChinhSua", "MaNV:"))
        self.LbID.setText(_translate("FormChinhSua", ""))
        self.DanhsachNhanVien.setTitle(_translate("FormChinhSua", "Bảng danh sách nhân viên trong Công Ty "))
        self.pushButton.setText(_translate("FormChinhSua", "Tải lại dữ liệu "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormChinhSua = QtWidgets.QWidget()
    ui = Ui_FormChinhSua()
    ui.setupUi(FormChinhSua)
    FormChinhSua.show()
    sys.exit(app.exec_())
