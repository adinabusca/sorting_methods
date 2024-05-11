import time
start_time = time.time()
import sys
sys.setrecursionlimit(10**5)


def partition (list, left, right):
    pivot = list[right]
    i = left - 1
    for j in range (left, right+1):
        if list[j] < pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i+1], list[right] = list[right], list[i+1]
    return i+1
def quicksort (list, left, right):
    if left < right:
        p = partition (list, left, right)
        quicksort (list, left, p-1)
        quicksort (list, p+1, right)

l = []#insert list here


quicksort (l,0, len(l)-1)
print(l)
print(time.time() - start_time)