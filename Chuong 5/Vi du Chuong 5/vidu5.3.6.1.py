import psycopg2

try:
    connection = psycopg2.connect(
        dbname="my_database",
        user="postgres",
        password="uneti",
        host="localhost",
        port="5432"
    )
    print("Đã kết nối đến cơ sở dữ liệu PostgreSQL.")
except Exception as e:
    print("Không thể kết nối đến PostgreSQL:", e)

#Thực thi truy vấn SQL
cursor = connection.cursor()
cursor.execute("SELECT * FROM employees;")
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.close()