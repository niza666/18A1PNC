import sqlite3

# Kết nối đến cơ sở dữ liệu (hoặc tạo cơ sở dữ liệu mới nếu nó không tồn tại)
conn = sqlite3.connect('mydatabase.db')

# Tạo một đối tượng con trỏ (Cursor object) từ đối tượng kết nối
cursor = conn.cursor()

# Nhập dữ liệu từ người dùng
name = input("Nhập tên người dùng: ")
age = int(input("Nhập tuổi người dùng: "))

# Thực hiện câu lệnh INSERT để chèn dữ liệu từ người dùng vào cơ sở dữ liệu
cursor.execute('INSERT INTO users ("Tên", "Tuổi") VALUES (?, ?)', (name, age))

# Lưu các thay đổi vào cơ sở dữ liệu
conn.commit()

#In ra các dòng trong bảng sau khi cập nhật
cursor = conn.execute("SELECT * FROM users") 
for row in cursor: 
   print(row) 

# Đóng kết nối
conn.close()