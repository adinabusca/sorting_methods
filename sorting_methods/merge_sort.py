import time
start_time = time.time()
import sys
sys.setrecursionlimit(10**5)

def mergesort(list):
    if len(list) == 0 or len(list) == 1:
        return
    if len(list) > 1:
        m = len(list) // 2
        l1 = list[:m]
        mergesort(l1)
        l2 = list[m:]
        mergesort(l2)
        k = 0
        i = 0
        j = 0
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                list[k] = l1[i]
                i += 1
                k += 1
            elif l1[i] > l2[j]:
                list[k] = l2[j]
                j += 1
                k += 1
            elif l1[i] == l2[j]:
                list[k] = l1[i]
                i += 1
                k += 1
                list[k] = l2[j]
                j += 1
                k += 1
        if i < len(l1):
            while i < len(l1):
                list[k] = l1[i]
                i += 1
                k += 1
        if j < len(l2):
            while j < len(l2):
                list[k] = l2[j]
                j += 1
                k += 1
        
       
l = []#insert list here

mergesort(l)
print(l)
print(time.time() - start_time)