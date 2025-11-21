import multiprocessing
import os
import time

def fibon(n):
    if n < 2:
        return n
    
    return fibon(n - 1) + fibon(n - 2)

def worker(n):
    result = fibon(n)
    print(f'Fibonacci({n}) = {result} from process {os.getpid()}.')

if __name__ == '__main__':
    start = time.time()
    for _ in range(16):
        worker(35)
    end = time.time()
    print(f'Single-threaded execution time: {end - start:.2f} seconds.')

    start = time.time()
    processes = [multiprocessing.Process(target=worker, args=(35,)) for _ in range(16)]
    for t in processes:
        t.start()
    for t in processes:
        t.join()
    end = time.time()
    print(f'Multi-processed execution time: {end - start:.2f} seconds.')