import threading
import multiprocessing
import concurrent.futures
import numpy as np
import matplotlib.pyplot as plt
import time

def bnw_image(file_name):
    image = plt.imread(file_name)

    height, width, _ = image.shape
    for i in range(height):
        for j in range(width):
            image[i, j, :] = np.sum(image[i, j, :]) / 3

    plt.imsave(file_name + '_bnw.png', image)

# bnw_image('src/images/img0.png')

if __name__ == '__main__':
    start = time.time()
    for i in range(10):
        bnw_image(f'src/images/img{i}.png')
    end = time.time()
    print(f'Serial processing time: {end - start} seconds')

    start = time.time()
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=16)
    futures = [executor.submit(bnw_image, f'src/images/img{i}.png') for i in range(10)]
    #results = [future.result() for future in futures]  
    concurrent.futures.wait(futures)
    end = time.time()
    print(f'Threaded processing time: {end - start} seconds')
    executor.shutdown(wait=True)

    start = time.time()
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=16)
    futures = [executor.submit(bnw_image, f'src/images/img{i}.png') for i in range(10)]
    #results = [future.result() for future in futures]  
    concurrent.futures.wait(futures)
    end = time.time()
    print(f'Process-based processing time: {end - start} seconds')
    executor.shutdown(wait=True)    