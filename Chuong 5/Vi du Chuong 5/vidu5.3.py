import sqlite3
conn = sqlite3.connect('nhan_vien.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY, 
"Tên" TEXT, 
"Tuổi" INTEGER
)
''')
cursor.execute('''
INSERT INTO users ("Tên", "Tuổi") 
VALUES ("Nguyễn Văn A", 30)
''')
conn.commit()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
conn.close()
 #Hồ Thị Minh Hằng