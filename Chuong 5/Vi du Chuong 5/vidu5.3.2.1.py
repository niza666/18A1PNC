#code for update operation
import sqlite3

#Kết nối đến CSDL, tên CSDL được truyền như một tham số của connect
conn = sqlite3.connect('mydatabase.db')

#Cập nhật bản ghi nhân viên từ bảng users
conn.execute("UPDATE users SET 'Lương' = 45000000 where id = '1'")
conn.commit()

print("Tổng số dòng được cập nhật :",conn.total_changes)

cursor = conn.execute("SELECT *FROM users")
for row in cursor:
    print(row)
#Đóng kết nối sau khi hoàn thành công việc
conn.close()