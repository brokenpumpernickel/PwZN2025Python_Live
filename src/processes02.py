import multiprocessing
import os
import time

def worker(lst, val):
    lst.append(val)
    print(f'Process ID: {os.getpid()}, List: {lst}')

if __name__ == '__main__':
    lst = []

    processes = [multiprocessing.Process(target=worker, args=(lst, i)) for i in range(16)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(f'Main Process ID: {os.getpid()}, Final List: {lst}')