import threading

# global variable x
x = 0

# Viết hàm increment(), tăng giá trị biến toàn cục x
def increment():
    global x
    x += 1

# Hàm thread_task() thực hiện tác vụ luồng, thực hiện gọi hàm increment() 100000 lần.
def thread_task():
    for _ in range(100000):
        increment()

# Hàm main_task(): thực hiện nhiệm vụ chính của chương trình.
# Nó đặt giá trị của biến toàn cục x=0, tạo hai luồng (t1 và t2)
# để thực thi công việc trong thread_task().
def main_task():
    global x
    x = 0

    # creating threads
    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    # start threads
    t1.start()
    t2.start()

    # wait until threads finish their job
    t1.join()
    t2.join()

# Chương trình chạy vòng lặp 10 lần,
# trong mỗi lần lặp gọi main_task() để thực hiện công việc.
# Sau đó in giá trị x ở mỗi lần lặp ra màn hình.
for i in range(10):
    main_task()
    print("Lần lặp {0}: x = {1}".format(i, x))
