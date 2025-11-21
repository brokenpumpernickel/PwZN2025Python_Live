import threading

def fibon(n):
    if n < 2:
        return n
    
    return fibon(n - 1) + fibon(n - 2)

class MyThread(threading.Thread):
    def __init__(self, n):
        threading.Thread.__init__(self)
        self.n = n

    def run(self):
        result = fibon(self.n)
        print(f'Fibonacci({self.n}) = {result} from thread {threading.get_ident()}.')

def worker(n):
    result = fibon(n)
    print(f'Fibonacci({n}) = {result} from thread {threading.get_ident()}.')

t1 = MyThread(35)
t1.start()
t1.join()

t2 = threading.Thread(target=worker, args=(35,))
t2.start()
t2.join()