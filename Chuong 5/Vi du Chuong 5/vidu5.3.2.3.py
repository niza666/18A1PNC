# code thực hiện xóa bản ghi 
import sqlite3 
  
# Kết nối đến cơ sở dữ liệu,  
conn = sqlite3.connect('mydatabase.db') 
  
# xóa bản ghi của bảng users từ database mydatabase.db
conn.execute("DELETE from users where id=7") 
conn.commit() 
print("Tổng số bản ghi được xóa :", conn.total_changes )
  
cursor = conn.execute("SELECT * FROM users") 
for row in cursor: 
   print(row) 

# Đóng kết nối sau khi hoàn tất công việc 
 
conn.close() 