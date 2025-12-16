import threading

# Khai báo biến toàn cục x và gán giá trị ban đầu là 0.
x = 0

# Viết hàm increment(), tăng giá trị biến toàn cục x
def increment():
    global x
    x += 1

# Hàm thread_task() thực hiện tác vụ luồng, trong task vụ này,
# luồng sẽ lặp lại 100000 lần.
def thread_task(lock):
    for _ in range(100000):
        lock.acquire()  # Yêu cầu lock bằng cách gọi phương thức lock.acquire
        increment()      # Tăng giá trị của x bằng cách gọi phương thức increment()
        lock.release()   # Giải phóng lock bằng cách gọi phương thức lock.release()

# Định nghĩa hàm main_task() là tác vụ chính của chương trình.
def main_task():
    global x
    x = 0  # Đặt biến toàn cục x=0.
    
    # creating a lock
    lock = threading.Lock()  # tạo ra một lock bằng cách gọi threading.Lock().
    
    # Tạo mới 2 luồng t1, t2 và chạy cùng một lúc, mỗi luồng gọi hàm thread_task() với
    # đối số lock.
    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    # start threads
    t1.start()
    t2.start()

    # Chờ cho đến khi các luồng kết thúc công việc
    t1.join()
    t2.join()

if __name__ == "__main__":
    # Kiểm tra module đang được chạy là module chính
    # hay không.
    for i in range(10):
        # Vòng lặp for chạy 10 lần
        main_task()  # Mỗi lần lặp main_task() được gọi
        print("Lần lặp {0}: x = {1}".format(i, x))
