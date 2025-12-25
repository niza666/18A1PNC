import sqlite3
import matplotlib.pyplot as plt

# Kết nối đến cơ sở dữ liệu hoặc tạo CSDL mới nếu nó chưa tồn tại
conn = sqlite3.connect('ct_giadinh.db')
cursor = conn.cursor()     #Tạo đối tượng con trỏ cursor từ đối tượng kết nối conn

# Truy vấn dữ liệu từ bảng 'khoan_chi'
cursor.execute("SELECT * FROM khoan_chi")
rows = cursor.fetchall()

# Lấy thông tin về các tên cột
column_names = [d[0] for d in cursor.description][1:]

# Tách dữ liệu thành hai danh sách riêng biệt cho loại chi tiêu và tổng số tiền
loai_chi = column_names
tien_chi = rows[0][1:]

# Đóng kết nối
conn.close()

# Vẽ biểu đồ Pie Chart
plt.pie(tien_chi, labels=loai_chi, autopct='%1.2f%%')
plt.title('Biểu đồ tỉ lệ mức chi tiêu một hộ gia đình')
plt.axis('equal')  # Để đảm bảo hình tròn
plt.show()