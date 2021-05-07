import time

def bubbleSort(data, timer, drawData):
    size = len(data)
    for i in range(size-1):
        for j in range(size-1):
            if (data[j] > data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['yellow' if x == j or x == j+1 else 'red' for x in range(len(data))])
                time.sleep(timer)