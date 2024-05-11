import time
start_time = time.time()
import sys
sys.setrecursionlimit(10**5)

l = [2,5,7,1,8,9,10]

for i in range (1, len(l)):
    aux = l[i]
    j = i - 1
    while j >= 0 and aux < l[j]:
        l[j+1] = l[j]
        j -= 1
    l[j+1] = aux
    
print(l)
print(time.time() - start_time)