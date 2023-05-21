import time, random, threading

def worker1(min, max):
    print("Worker1 started...", min, max)
    time.sleep(random.randint(min, max))
    print("Worker1 finished")

def worker2(min, max):
    print("Worker2 started...", min, max)
    time.sleep(random.randint(min, max))
    print("Worker2 finished")

def worker3(min, max):
    print("Worker3 started...", min, max)
    time.sleep(random.randint(min, max))
    print("Worker3 finished")

thread_1 = threading.Thread(target=worker1, args=[2, 6])
thread_2 = threading.Thread(target=worker2, args=[1, 3])
thread_3 = threading.Thread(target=worker3, args=[10, 20])

thread_1.start()
thread_2.start()
thread_3.start()