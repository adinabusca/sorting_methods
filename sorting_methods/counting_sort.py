import time
start_time = time.time()
import sys
sys.setrecursionlimit(10**5)

def countingsort(list):
    maxi = max(list)
    count = [0] * (maxi+1)
    
    for i in list:
        count[i] += 1
        
    for i in range(1,maxi+1):
        count[i] += count[i-1]
        
    output = [0] * len(list)
    
    for i in range(len(list)-1,-1,-1):
        output[count[list[i]]-1] = list[i]
        count[list[i]] -= 1
        
    return output





l = []#insert list here


print(countingsort(l))
print(time.time() - start_time)