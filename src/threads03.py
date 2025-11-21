import threading

# counter = 0

# def worker():
#     global counter
#     for _ in range(1000000):
#         counter += int(1)

# threads = [threading.Thread(target=worker) for _ in range(10)]

# for t in threads:
#     t.start()
# for t in threads:
#     t.join()

# print(f'Final counter value: {counter}')
# print(f'Expected counter value: {len(threads) * 1000000}')
# print(f'Is equal: {counter == len(threads) * 1000000}')

### Locks

# counter = 0
# lock = threading.RLock()

# def worker():
#     global counter
#     for _ in range(1000000):
#         lock.acquire()
#         counter += int(1)
#         lock.release()

# threads = [threading.Thread(target=worker) for _ in range(10)]

# for t in threads:
#     t.start()
# for t in threads:
#     t.join()

# print(f'Final counter value: {counter}')
# print(f'Expected counter value: {len(threads) * 1000000}')
# print(f'Is equal: {counter == len(threads) * 1000000}')

### With

counter = 0
lock = threading.RLock()

def worker():
    global counter
    for _ in range(1000000):
        with lock:
            counter += int(1)

threads = [threading.Thread(target=worker) for _ in range(10)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f'Final counter value: {counter}')
print(f'Expected counter value: {len(threads) * 1000000}')
print(f'Is equal: {counter == len(threads) * 1000000}')