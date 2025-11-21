import threading
import time

cond = threading.Condition()

def notifier():
    print("Notifier: Preparing to notify...")
    time.sleep(5)  # Simulate some work
    print("Notifier: Notifying all waiting threads.")
    cond.acquire()
    cond.notify_all()
    cond.release()
    print("Notifier: Notification sent.")

def waiter(id):
    print(f"Waiter {id}: Waiting for notification...")
    cond.acquire()
    cond.wait()
    print(f"Waiter {id}: Received notification!")
    cond.release()

t1 = threading.Thread(target=notifier)

waiters = [threading.Thread(target=waiter, args=(i,)) for i in range(10)]

for w in waiters:
    w.start()

t1.start()

for w in waiters:
    w.join()