import time
start_time = time.time()
import sys
sys.setrecursionlimit(10**5)

def shellsort(list):
    gap = len(list) // 2
    
    while gap > 0:
        j = gap
        while j < len(list):
            i = j-gap
            while i >= 0:
                if list[i+gap] > list[i]:
                   break
                else:
                    list[i+gap],list[i] = list[i],list[i+gap]
                i = i- gap
            j += 1
        gap //= 2


l = []#insert list here

shellsort(l)
print(l)
print(time.time() - start_time)