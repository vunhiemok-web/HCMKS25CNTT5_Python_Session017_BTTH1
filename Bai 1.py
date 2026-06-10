raw_logs = [] 
processed_logs = []

#Chức năng 1
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

#Chức năng 2    
def warning_raw_logs():
    global processed_logs
    global raw_logs
    count = 0
    if raw_logs == []:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
    else:
        for str in raw_logs:
            if "ERROR" in str or "CRITICAL" in str:
                processed_logs.append(str)
                count += 1
        print(f"Tìm thấy {count} cảnh báo nguy hiểm:")
        for pro_log in processed_logs:
            print(f"- {pro_log}")
        
#Hàm mã hóa ip        
def mask_ip(ip):
    if not ip or '.' not in ip:
        return ip
    parts = ip.split('.')
    if len(parts) == 4:
        return f"{parts[0]}.{parts[1]}.*.*"
    return ip        
        
#Chức năng 3
def encryption_ip():
    global processed_logs
    
    print("\n--- MÃ HÓA IP ---")
    
    if not processed_logs:
        print("Chưa có log nguy hiểm nào để mã hóa! Vui lòng chạy chức năng 2 trước.")
        return []
    
    masked_logs = []
    
    for log in processed_logs:
        words = log.split()
        masked_log = []
        
        for word in words:
            # Nếu từ chứa dấu chấm (có thể là IP)
            if '.' in word and word.replace('.', '').replace(':', '').isdigit() or \
               (word.count('.') == 3):
                masked_word = mask_ip(word)
                masked_log.append(masked_word)
            else:
                masked_log.append(word)
        
        masked_logs.append(" ".join(masked_log))
    
    # In báo cáo
    print("Báo cáo log an toàn:")
    for i, masked_log in enumerate(masked_logs, 1):
        print(f"{i}. {masked_log}")
    
    return masked_logs
        
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
            case 3:
                encryption_ip()
            case 4:
                print("Thoát chương trình!")
                break
           
if __name__ == "__main__":
    main()