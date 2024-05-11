import time
start_time = time.time()
import sys
sys.setrecursionlimit(10**5)

l = []#insert list here#

ok = True
while ok == True:
    ok = False
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            ok = True
print(l)
print(time.time() - start_time)