# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormMain.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
import numpy
from CreateForm import Ui_FormCreate
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox,QTableView


import sys
import sqlite3

class Ui_FormMain(object):
    def ClearForm(self):
        self.LbID.setText("")
        self.txtHoTen.setText("")
        self.txtTuoi.setValue(0)
        self.txtGioiTinh.setCurrentIndex(1)
        self.txtDiaChi.setText("")
        self.txtChucVu.setCurrentIndex(0)
        self.ComboPhongBan.setCurrentIndex(0)
        self.txtSoDienThoai.setText("")
        self.txtEmail.setText("")

    ############## Đặt câu hỏi có cập nhật khuôn mặt hay không #####################################3
    def ShowWarning(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText("Bạn đã cập nhật thành công thông tin.Bạn có muốn cập nhật lại khuôn mặt   ")
        self.msg.setWindowTitle("Cập nhật khuôn mặt  ")
        self.msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        self.msg.setDefaultButton(QMessageBox.Yes)
        #### Lấy giá trị click lưu vào ret #############################
        ret = self.msg.exec()
        print(str(ret))
        #### nếu ret =16384 hay click vào button yes thì in ra màn hình câu câu thông báo " click yes"
        if(ret == QMessageBox.Yes):
            import LoadCam
        #### nếu click vào no in ra câu thông báo " click no "
        if(ret == QMessageBox.No):
            print("Load Lại Form ")
            self.ClearForm()

    def create_connection(self,db_file):
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return None
    def delete_task(self,conn, id):

        sql = 'DELETE FROM NhanVien WHERE id=?'
        cur = conn.cursor()
        cur.execute(sql, (id,))
    def update_task(self,conn, task):

        sql = "UPDATE NhanVien SET HoTen = ? ,Tuoi = ? ,GioiTinh = ?,DiaChi=?, ChucVu=?,PhongBan=?, SoDienThoai=?,Email=?   WHERE id = ?"
        cur = conn.cursor()
        cur.execute(sql, task)

    def KiemTra(self):
        HoTen= self.txtHoTen.text()
        SoDienThoai=self.txtSoDienThoai.text()
        DiaChi=self.txtDiaChi.text()
        Email=self.txtEmail.text()

    def XoaNhanVien(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText(" Bạn có chắc muốn xóa thông tin này !!!")
        self.msg.setWindowTitle("Cảnh báo !")
        self.msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        self.msg.setDefaultButton(QMessageBox.No)
        #### Lấy giá trị click lưu vào ret #############################
        ret = self.msg.exec()
        print(str(ret))
        #### nếu ret =16384 hay click vào button yes thì in ra màn hình câu câu thông báo " click yes"
        if(ret == QMessageBox.Yes):
            Id=self.LbID.text()
            database = "DiemDanh.db"
            conn = self.create_connection(database)
            with conn:
                self.delete_task(conn, Id);
            self.LoadData()





    def CapNhat(self):
        Id=self.LbID.text()
        HoTen=self.txtHoTen.text()
        Tuoi=self.txtTuoi.text()
        GioiTinh=str(self.txtGioiTinh.currentText())
        ChucVu = str(self.txtChucVu.currentText())
        PhongBan= str(self.ComboPhongBan.currentText())
        DiaChi=self.txtDiaChi.text()
        SoDienThoai= self.txtSoDienThoai.text()
        Email= self.txtEmail.text()
        Task= (HoTen,Tuoi,GioiTinh,DiaChi,ChucVu,PhongBan,SoDienThoai,Email,Id)
        database = "DiemDanh.db"
        conn = self.create_connection(database)
        with conn:
            self.update_task(conn,Task)
        self.ShowWarning()
        self.LoadData()





    #### ánh xạ dữ liệu từ table lên textbox và combobox ##########################
    ##### index là vị trí con trỏ kích vào trong table #####################3
    def getData(self,index):
        #### tạo model lưu dữ liệu của dòng #############33333
        model = self.tableDanhSachNhanVien.model()
        data = []
        row= index.row()####### Index.row() lấy vị trí chuột theo số dòng
        #########################################3
        #test=model.index(2,2) thử lấy dữ liệu dòng 2 cột 2
        #dataa=test.data() lấy dữ liệu từ ô vừa chọn
        #print(dataa) in ra màn hình thử
        print(row)
        ##### đưa dư liệu từ table lên text box ######################
        MaNV=(model.index(row,0)).data()### MÃ nhân viên thuộc dòng Row/ lấy data tại vin trí index(row, số cột ) với số cột chạy từ đây đến cuối

        print("mã nhân viên "+ str(MaNV))
        self.LbID.setText(str(MaNV))
        HoTen=(model.index(row,1)).data()
        self.txtHoTen.setText(str(HoTen))
        Tuoi=(model.index(row,2)).data()
        self.txtTuoi.setValue(int(Tuoi))
        GioiTinh=(model.index(row,3)).data()
        if(GioiTinh == "Nữ"):
            self.txtGioiTinh.setCurrentIndex(1)
        else :
            self.txtGioiTinh.setCurrentIndex(0)

        DiaChi=(model.index(row,4)).data()
        self.txtDiaChi.setText(str(DiaChi))
        ChucVu=(model.index(row,5)).data()
        if(ChucVu == "Trưởng phòng"):
            self.txtChucVu.setCurrentIndex(0)
        else:
            if(ChucVu=="Phó phòng"):
                self.txtChucVu.setCurrentIndex(1)
            else :
                self.txtChucVu.setCurrentIndex(2)
        PhongBan=(model.index(row,6)).data()
        if(PhongBan=="Kinh doanh"):
            self.ComboPhongBan.setCurrentIndex(0)
        else:
            if(PhongBan=="IT"):
                self.ComboPhongBan.setCurrentIndex(1)
            else:
                if(PhongBan=="Nhân sự"):
                    self.ComboPhongBan.setCurrentIndex(2)
                else:
                    self.ComboPhongBan.setCurrentIndex(3)
        SoDienThoai=(model.index(row,7)).data()
        self.txtSoDienThoai.setText(str(SoDienThoai))
        Email=(model.index(row,8)).data()
        self.txtEmail.setText(str(Email))



       # for row in range(model.rowCount()):
          #  data.append([])
           # for column in range(model.columnCount()):
             #   index = model.index(row, column)
               # print(index)
    def SelectRow(self, index):
        print("current row is %d", index.row())
        pass
    def doubleClicked_table(self):
        index = self.tableDanhSachNhanVien.selectedIndexes()[0]
        id_us = int(self.tableDanhSachNhanVien.model().data(index).toString())
        print (" lấy  dữ liệu thành công")
    #############3 hàm load dữ liệu từ cơ sở dữ liệu / hiện thông tin lên tableView / sử dựng modelsqlite và tableview của PyQt
    def LoadData(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("DiemDanh.db")
        db.open()

        projectModel = QSqlQueryModel()
        projectModel.setQuery("select  id as [Mã Nhân Viên ],HoTen as [Họ và tên ], Tuoi as [Tuổi ],GioiTinh as[Giới tính], DiaChi as [Địa chỉ ], ChucVu as [Chức vụ], PhongBan as [Phòng ban],SoDienThoai as [Số điện thoại ], Email from NhanVien",db)
        self.tableDanhSachNhanVien.setModel(projectModel)
        self.tableDanhSachNhanVien.show()

    ######## Hiện form tạo mới nhân viên .####################################################################
    def ShowCreateForm(self) :
            self.CreateForm= QtWidgets.QMainWindow()
            self.ui= Ui_FormCreate()
            self.ui.setupUi(self.CreateForm)
            self.CreateForm.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 650)

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



        self.groupChucNang = QtWidgets.QGroupBox(Form)
        self.groupChucNang.setGeometry(QtCore.QRect(200, 10, 600, 600))
        self.groupChucNang.setObjectName("groupChucNang")
        self.groupBox_Parent = QtWidgets.QGroupBox(self.groupChucNang)
        self.groupBox_Parent.setGeometry(QtCore.QRect(10, 20, 531, 211))
        self.groupBox_Parent.setObjectName("groupBox_Parent")
        self.label = QtWidgets.QLabel(self.groupBox_Parent)
        self.label.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label.setObjectName("label")
        self.txtHoTen = QtWidgets.QLineEdit(self.groupBox_Parent)
        self.txtHoTen.setGeometry(QtCore.QRect(90, 20, 171, 20))
        self.txtHoTen.setObjectName("txtHoTen")
        self.txtTuoi = QtWidgets.QSpinBox(self.groupBox_Parent)
        self.txtTuoi.setGeometry(QtCore.QRect(470, 20, 42, 22))
        self.txtTuoi.setObjectName("txtTuoi")
        self.label_2 = QtWidgets.QLabel(self.groupBox_Parent)
        self.label_2.setGeometry(QtCore.QRect(430, 20, 47, 13))
        self.label_2.setObjectName("label_2")
        self.txtGioiTinh = QtWidgets.QComboBox(self.groupBox_Parent)
        self.txtGioiTinh.setGeometry(QtCore.QRect(90, 50, 69, 22))
        self.txtGioiTinh.setObjectName("txtGioiTinh")
        self.txtGioiTinh.addItem("")
        self.txtGioiTinh.addItem("")
        self.label_3 = QtWidgets.QLabel(self.groupBox_Parent)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_Parent)
        self.label_4.setGeometry(QtCore.QRect(280, 60, 71, 16))
        self.label_4.setObjectName("label_4")
        self.txtSoDienThoai = QtWidgets.QLineEdit(self.groupBox_Parent)
        self.txtSoDienThoai.setGeometry(QtCore.QRect(380, 60, 141, 20))
        self.txtSoDienThoai.setObjectName("txtSoDienThoai")
        self.label_5 = QtWidgets.QLabel(self.groupBox_Parent)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.label_5.setObjectName("label_5")
        self.txtDiaChi = QtWidgets.QLineEdit(self.groupBox_Parent)
        self.txtDiaChi.setGeometry(QtCore.QRect(90, 90, 171, 20))
        self.txtDiaChi.setObjectName("txtDiaChi")
        self.label_6 = QtWidgets.QLabel(self.groupBox_Parent)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 71, 16))
        self.label_6.setObjectName("label_6")
        self.txtEmail = QtWidgets.QLineEdit(self.groupBox_Parent)
        self.txtEmail.setGeometry(QtCore.QRect(90, 130, 171, 20))
        self.txtEmail.setObjectName("txtEmail")
        self.label_7 = QtWidgets.QLabel(self.groupBox_Parent)
        self.label_7.setGeometry(QtCore.QRect(300, 100, 47, 13))
        self.label_7.setObjectName("label_7")
        self.txtChucVu = QtWidgets.QComboBox(self.groupBox_Parent)
        self.txtChucVu.setGeometry(QtCore.QRect(380, 100, 131, 22))
        self.txtChucVu.setObjectName("txtChucVu")
        self.txtChucVu.addItem("")
        self.txtChucVu.addItem("")
        self.txtChucVu.addItem("")
        self.label_8 = QtWidgets.QLabel(self.groupBox_Parent)
        self.label_8.setGeometry(QtCore.QRect(290, 140, 61, 16))
        self.label_8.setObjectName("label_8")
        self.ComboPhongBan = QtWidgets.QComboBox(self.groupBox_Parent)
        self.ComboPhongBan.setGeometry(QtCore.QRect(380, 140, 131, 22))
        self.ComboPhongBan.setObjectName("ComboPhongBan")
        self.ComboPhongBan.addItem("")
        self.ComboPhongBan.addItem("")
        self.ComboPhongBan.addItem("")
        self.ComboPhongBan.addItem("")
        self.label_9 = QtWidgets.QLabel(self.groupBox_Parent)
        self.label_9.setGeometry(QtCore.QRect(300, 20, 41, 16))
        self.label_9.setObjectName("label_9")
        self.LbID = QtWidgets.QLabel(self.groupBox_Parent)
        self.LbID.setGeometry(QtCore.QRect(350, 20, 47, 13))
        self.LbID.setObjectName("LbID")



        self.btnXoa = QtWidgets.QPushButton(self.groupBox_Parent)
        self.btnXoa.setGeometry(QtCore.QRect(90, 170, 65, 23))
        self.btnXoa.setObjectName("btnXoa")
        self.btnXoa.clicked.connect(self.XoaNhanVien)
        self.btnCapNhatKhuonMat = QtWidgets.QPushButton(self.groupBox_Parent)
        self.btnCapNhatKhuonMat.setGeometry(QtCore.QRect(170, 170, 111, 23))
        self.btnCapNhatKhuonMat.setObjectName("btnCapNhatKhuonMat")
        self.btnThoat = QtWidgets.QPushButton(self.groupBox_Parent)
        self.btnThoat.setGeometry(QtCore.QRect(410, 170, 75, 23))
        self.btnThoat.setObjectName("btnThoat")
        self.btnLuuLai = QtWidgets.QPushButton(self.groupBox_Parent)
        self.btnLuuLai.setGeometry(QtCore.QRect(300, 170, 75, 23))
        self.btnLuuLai.setObjectName("btnLuuLai")
        ### chức năng cập nhật dữ liệu nhazan viên ###############3
        self.btnLuuLai.clicked.connect(self.CapNhat)


        self.DanhsachNhanVien = QtWidgets.QGroupBox(self.groupChucNang)
        self.DanhsachNhanVien.setGeometry(QtCore.QRect(10, 240, 531, 321))
        self.DanhsachNhanVien.setObjectName("DanhsachNhanVien")
        self.tableDanhSachNhanVien = QtWidgets.QTableView(self.DanhsachNhanVien)
        self.tableDanhSachNhanVien.setGeometry(QtCore.QRect(10, 30, 521, 291))
        self.tableDanhSachNhanVien.setObjectName("tableDanhSachNhanVien")
        #### mặc định chỉ cho chọn theo dòng trong table ######################################
        self.tableDanhSachNhanVien.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.tableDanhSachNhanVien.clicked.connect(self.getData)

        self.btnTaiLai = QtWidgets.QPushButton(self.groupChucNang)
        self.btnTaiLai.setGeometry(QtCore.QRect(230, 570, 91, 23))
        self.btnTaiLai.setObjectName("btnTaiLai")
        self.btnTaiLai.clicked.connect(self.LoadData)



    ##### Load dữ liệu từ database lên tableView ###############################################################################################
        self.LoadData()
############### ###################################################################################################################################################################################
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
        self.groupChucNang.setTitle(_translate("Form", "Chức năng hệ thống"))
        self.groupBox_Parent.setTitle(_translate("Form", "Quản lý nhân viên "))
        self.label.setText(_translate("Form", "Họ Tên : "))
        self.label_2.setText(_translate("Form", "Tuổi : "))
        self.txtGioiTinh.setItemText(0, _translate("Form", "Nam"))
        self.txtGioiTinh.setItemText(1, _translate("Form", "Nữ"))

        self.label_3.setText(_translate("Form", "Giới tính : "))
        self.label_4.setText(_translate("Form", "Số điện thoại : "))
        self.label_5.setText(_translate("Form", "Địa chỉ : "))
        self.label_6.setText(_translate("Form", "Email : "))
        self.label_7.setText(_translate("Form", "Chức vụ : "))
        self.txtChucVu.setItemText(0, _translate("Form", "Trưởng phòng"))
        self.txtChucVu.setItemText(1, _translate("Form", "Phó phòng"))
        self.txtChucVu.setItemText(2, _translate("Form", "Nhân viên"))
        self.label_8.setText(_translate("Form", "Phòng ban : "))
        self.ComboPhongBan.setItemText(0, _translate("Form", "Kinh doanh"))
        self.ComboPhongBan.setItemText(1, _translate("Form", "IT"))
        self.ComboPhongBan.setItemText(2, _translate("Form", "Nhân sự"))
        self.ComboPhongBan.setItemText(3, _translate("Form", "Đối ngoại"))
        self.btnXoa.setText(_translate("Form", "Xóa "))
        self.btnCapNhatKhuonMat.setText(_translate("Form", "Cập nhật Khuôn mặt"))
        self.btnThoat.setText(_translate("Form", "Thoát "))
        self.btnLuuLai.setText(_translate("Form", "Lưu lại"))
        self.DanhsachNhanVien.setTitle(_translate("Form", "Bảng danh sách nhân viên trong Công Ty "))
        self.btnTaiLai.setText(_translate("FormChinhSua", "Tải lại dữ liệu "))
        self.label_9.setText(_translate("FormChinhSua", "MaNV:"))
       # self.LbID.setText(_translate("FormChinhSua", "abc"))


if __name__ == "__main__":
    import sys
    import cv2
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_FormMain()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())

