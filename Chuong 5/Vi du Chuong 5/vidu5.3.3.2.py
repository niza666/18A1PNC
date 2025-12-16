import sqlite3
import matplotlib.pyplot as plt

# Kết nối đến cơ sở dữ liệu
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# Truy vấn dữ liệu từ cơ sở dữ liệu
cursor.execute("SELECT year, revenue FROM sales")
rows = cursor.fetchall()

# Tách dữ liệu thành hai danh sách riêng biệt cho năm và doanh thu
years = [row[0] for row in rows]
revenues = [row[1] for row in rows]

# Đóng kết nối
conn.close()

# Vẽ biểu đồ Line Chart
plt.plot(years, revenues, marker='o', linestyle='-')
plt.xlabel('Các năm')
plt.ylabel('Doanh thu (đơn vị: tỷ đồng)')
plt.title('Biểu đồ biểu diễn doanh thu theo năm')

plt.legend(['Doanh thu theo năm'])  # Thêm chú thích vào biểu đồ
plt.grid(True)  # Thêm lưới trên biểu đồ
plt.show()