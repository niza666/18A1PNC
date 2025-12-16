import threading
def my_function(arg):
 # Công việc của luồng
 print("Đối số là: ",arg)
 print("Đây là luồng đang chạy!!")
my_thread = threading.Thread(target=my_function, args=(10,)) 
my_thread.start()