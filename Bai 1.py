raw_logs = [] 
processed_logs = []

def input_raw_data():
    global raw_logs
    str_input = input("Nhập chuỗi log thô (cách nhau bởi dấu ;): ")
    table = str_input.maketrans(
        "","","!@#$"
    )
    str_input = str_input.translate(table)
    new_list = str_input.split(";")
    raw_logs.extend(new_list)
    print(f"Đã làm sạch và lưu {len(new_list)} dòng log vào hệ thống.")
    
def warning_raw_logs():
    global processed_logs
    global raw_logs
    count = 0
    for str in raw_logs:
        if "ERROR" in str or "CRITICAL" in str:
            processed_logs.append(str)
            count += 1
    print(f"Tìm thấy {count} cảnh báo nguy hiểm:")
    for pro_log in processed_logs:
        print(f"- {pro_log}")
def main():
    while True:
        print(f"============= SECURITY LOG ANALYZER =============\n"
              f"1. Nhập và làm sạch dữ liệu Log thô\n"
              f"2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)\n"
              f"3. Mã hóa địa chỉ IP (Masking)\n"
              f"4. Đóng hệ thống\n"
              f"=================================================")
        while True:
            try:
                choice = int(input("Chọn chức năng (1-4): "))
                
                if 1 <= choice <= 4:
                    break
                
                print("Vui lòng chỉ nhập từ 1 - 4")
            except ValueError:
                print("Vui lòng chỉ nhập từ 1 - 4")
                
        match choice:
            case 1:
               input_raw_data() 
            case 2:
                warning_raw_logs()
            case 4:
                print("Thoát chương trình!")
                break
            
if __name__ == "__main__":
    main()