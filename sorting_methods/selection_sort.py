import time
start_time = time.time()
import sys
sys.setrecursionlimit(10**5)

l = []#insert list here

for i in range(len(l)-1):
    k = i
    for j in range (i+1, len(l)):
        if l[k] > l[j]:
            k = j
    if k != i:
        l[i], l[k] = l[k], l[i]
print(l)
print(time.time() - start_time)