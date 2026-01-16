# A counter
import time

def count(end, start=0):
    for x in range(start, end+1):
        print(x, end=" ")
        time.sleep(1)
    print("Donee!")

count(10)
