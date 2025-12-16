import threading
import os

def task1():
    print("Gắn tác vụ 1 đến luồng: {}".format(threading.current_thread().name))
    print("ID của tiến trình chạy task 1: {}".format(os.getpid()))

def task2():
    print("Gắn tác vụ 2 đến luồng: {}".format(threading.current_thread().name))
    print("ID của tiến trình chạy task 2: {}".format(os.getpid()))

if __name__ == "__main__":
    # In ra ID của luồng hiện thời
    print("ID của luồng đang thực thi trong chương trình chính: {}".format(os.getpid()))

    # in ra tên luồng chính
    print("Tên của luồng chính: {}".format(threading.current_thread().name))

    # Tạo các luồng
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    # Bắt đầu các luồng:
    t1.start()
    t2.start()

    # Chờ cho đến khi các luồng kết thúc:
    t1.join()
    t2.join()
