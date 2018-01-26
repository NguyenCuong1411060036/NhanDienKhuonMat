import sqlite3
def InsertOrUpdate (self):
        HoTen=self.txtHoTen.text()
        Tuoi=self.txtTuoi.text()
        GioiTinh=str(self.ComboChucVu.currentText())
        ChucVu = str(self.ComboGioiTinh.currentText())
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
