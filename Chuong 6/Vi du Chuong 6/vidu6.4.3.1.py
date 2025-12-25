import queue
import threading
import time

thread_exit_Flag = 0

class SampleThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("Initializing " + self.name)
        process_data(self.name, self.q)
        print("Exiting " + self.name)

# Helper function to process data
def process_data(threadName, q):
    while not thread_exit_Flag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
            time.sleep(1)

thread_list = ["Thread-1", "Thread-2", "Thread-3"]
name_list = ["A", "B", "C", "D", "E"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []

# Create and start new threads
for threadID, threadName in enumerate(thread_list):
    thread = SampleThread(threadID, threadName, workQueue)
    thread.start()
    threads.append(thread)

# Fill the queue with data
queueLock.acquire()
for word in name_list:
    workQueue.put(word)
queueLock.release()

# Wait for the queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
thread_exit_Flag = 1

# Wait for all threads to complete
for t in threads:
    t.join()

print("Exit Main Thread")
