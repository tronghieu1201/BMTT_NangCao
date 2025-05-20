SoGio = float(input("Nhập số giờ: "))
LuongGio = float(input("Nhập lương giờ: "))
SoGioChuan = 44
SoGioLamThem = max(0, SoGio - SoGioChuan)
SoGioThuong = min(SoGio, SoGioChuan)
ThucLinh = SoGioThuong * LuongGio + SoGioLamThem * LuongGio * 1.5
print(f"Số tiền thực lĩnh của nhân viên: {ThucLinh}")