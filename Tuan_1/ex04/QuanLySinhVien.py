from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def ganerateID(self):
        maxID = 1
        if self.soLuongSinhVien() > 0:
            maxID = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if maxID < sv._id:
                    maxID = sv._id
            maxID += 1
        return maxID

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svId = self.ganerateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành sinh viên: ")
        diemTB = float(input("Nhập điểm trung bình sinh viên: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính sinh viên: ")
            major = input("Nhập chuyên ngành sinh viên: ")
            diemTB = float(input("Nhập điểm của sinh viên: "))

            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Không tìm thấy sinh viên với ID này.")

    def xepLoaiHocLuc(self, sv: SinhVien):
        if sv._diemTB >= 8:
            sv._hocLuc = "Giỏi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Khá"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung Bình"
        else:
            sv._hocLuc = "Yếu"

    def findByID(self, ID):
        for sv in self.listSinhVien:
            if sv._id == ID:
                return sv
        return None

    def showSinhVien(self):
        if self.soLuongSinhVien() == 0:
            print("Không có sinh viên nào.")
        else:
            for sv in self.listSinhVien:
                print(sv)
