from QuanLySinhVien import QuanLySinhVien

def main():
    qlsv = QuanLySinhVien()

    while True:
        print("\n===== QUẢN LÝ SINH VIÊN =====")
        print("1. Nhập sinh viên")
        print("2. Cập nhật sinh viên theo ID")
        print("3. Hiển thị danh sách sinh viên")
        print("0. Thoát")
        choice = input("Chọn chức năng: ")

        if choice == '1':
            qlsv.nhapSinhVien()
        elif choice == '2':
            try:
                ID = int(input("Nhập ID sinh viên cần cập nhật: "))
                qlsv.updateSinhVien(ID)
            except ValueError:
                print("ID không hợp lệ.")
        elif choice == '3':
            qlsv.showSinhVien()
        elif choice == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Chức năng không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
