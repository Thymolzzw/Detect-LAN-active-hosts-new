from multiprocessing import Process
import time

def worker_1(interval):
    print("worker_1")
    time.sleep(interval)
    print("end worker_1")


if __name__ == "__main__":
    p1 = Process(target=worker_1, args=(6,))
    p2 = Process(target=worker_1, args=(4,))
    p3 = Process(target=worker_1, args=(2,))
    p1.start()
    p2.start()
    p3.start()
