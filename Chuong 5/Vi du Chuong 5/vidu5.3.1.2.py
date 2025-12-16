import sqlite3

# Kết nối đến cơ sở dữ liệu (hoặc tạo cơ sở dữ liệu mới nếu nó không tồn tại)
conn = sqlite3.connect('mydatabase.db')

# Tạo một đối tượng con trỏ (Cursor object) từ đối tượng kết nối
cursor = conn.cursor()

# Thực thi câu lệnh SQL và truy xuất dữ liệu được đặt trong cặp dấu '''...'''
cursor.execute('''
               CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY, 
               "Tên" TEXT, 
               "Tuổi" INTEGER,
               "Lương" REAL)
               ''')
cursor.execute('''
               INSERT INTO users ("Tên", "Tuổi", "Lương") 
               VALUES ("Nguyễn Văn A", 30, 15000000)
               ''')

# Lưu các thay đổi vào cơ sở dữ liệu (nếu cần)
conn.commit()

# Truy xuất dữ liệu từ bảng users
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# In kết quả
for row in rows:
    print(row)

# Đóng con trỏ (Cursor object) và đóng kết nối
cursor.close()
conn.close()