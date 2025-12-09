import mysql.connector

def mysqlconnect():
    # Thử kết nối đến cơ sở dữ liệu MySQL
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="uneti",
            database="mySQLdb"
        )
    # Nếu connection không thành công 
    except mysql.connector.Error as err:
        print("Không thể kết nối đến database mySQLdb:", err)
        return 0

    # Nếu kết nối thành công
    print("Đã kết nối đến Database.")

    # Tạo đối tượng con trỏ để thực thi truy vấn
    cursor = db_connection.cursor()

    # Thực thi truy vấn
    cursor.execute("SELECT CURDATE();")

    # Lấy dữ liệu (một dòng đầu tiên) từ kết quả truy vấn
    m = cursor.fetchone()

    # In kết quả
    print("Hôm nay là ngày :", m[0])

    # Đóng kết nối cơ sở dữ liệu
    db_connection.close()

# Gọi hàm kết nối
mysqlconnect()