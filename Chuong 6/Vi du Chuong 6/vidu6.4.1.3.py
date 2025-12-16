import threading

class ATM:
    def __init__(self):
        self.semaphore = threading.Semaphore(1)

    def withdraw(self, amount):
        self.semaphore.acquire()
        # Thực hiện giao dịch rút tiền
        print(f"Đã rút {amount} ngàn từ máy ATM")
        self.semaphore.release()

def main():
    atm = ATM()

    # Tạo 10 luồng
    for i in range(10):
        threading.Thread(target=atm.withdraw, args=(100,)).start()

if __name__ == "__main__":
    main()
