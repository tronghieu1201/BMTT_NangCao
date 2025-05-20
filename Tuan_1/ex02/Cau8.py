def chiahet(NhiPhan):
    try:
        so_thap_phan = int(NhiPhan, 2)  
        return so_thap_phan % 5 == 0     
    except ValueError:
        return False

chuoi_so_nhi_phan = input("Nhập chuỗi số nhị phân (cách nhau bởi dấu phẩy): ")
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
ket_qua = [so for so in so_nhi_phan_list if chiahet(so.strip())]

if ket_qua:
    print("Các số nhị phân chia hết cho 5 là:", ','.join(ket_qua))
else:
    print("Không có số nhị phân nào chia hết cho 5 trong chuỗi")