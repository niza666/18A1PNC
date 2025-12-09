import sqlite3

# Kết nối đến cơ sở dữ liệu (hoặc tạo cơ sở dữ liệu mới nếu nó không tồn tại)
conn = sqlite3.connect('sinhvien.db')
c = conn.cursor()

# Tạo bảng và thêm dữ liệu 
def tao_bang():
    c.execute('CREATE TABLE IF NOT EXISTS bang_diem (diem REAL, ten TEXT)')

def nhap_diem():
    diem = 8.5
    ten = 'Nguyễn Văn A'
    c.execute("INSERT INTO bang_diem (diem, ten) VALUES(?, ?)", (diem, ten))
    conn.commit()

tao_bang()
nhap_diem()

# In ra các dòng trong bảng sau khi cập nhật
cours = conn.execute("SELECT * FROM bang_diem")
for row in cours:
    print(row)

c.close()
conn.close()