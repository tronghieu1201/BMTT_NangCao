class SinhVien:
    def __init__(self, id, name, sex, major, diemTB):
        self._id = id
        self._name = name
        self._sex = sex
        self._major = major
        self._diemTB = diemTB
        self._hocLuc = ""

    def __str__(self):
        return f"ID: {self._id}, Tên: {self._name}, Giới tính: {self._sex}, Chuyên ngành: {self._major}, Điểm TB: {self._diemTB}, Học lực: {self._hocLuc}"
