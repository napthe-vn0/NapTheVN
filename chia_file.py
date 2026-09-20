# Đổi 'index.html' thành tên chính xác của file 27k dòng trên máy bạn
file_goc = "index.html"
so_dong_moi_phan = 3000
tong_so_phan = 9

try:
    with open(file_goc, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total_lines = len(lines)
    print(f"Tổng số dòng thực tế trong file của bạn là: {total_lines}")

    for i in range(tong_so_phan):
        start = i * so_dong_moi_phan
        end = min((i + 1) * so_dong_moi_phan, total_lines)
        
        # Nếu đã hết dòng thì dừng lại
        if start >= total_lines:
            break

        chunk_lines = lines[start:end]
        output_filename = f"phan_{i+1}.html"
        
        with open(output_filename, "w", encoding="utf-8") as f_out:
            f_out.writelines(chunk_lines)
            
        print(f"Đã tạo xong: {output_filename} (Từ dòng {start+1} đến {end})")

    print("Hoàn tất! Đã chia file thành công.")

except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
