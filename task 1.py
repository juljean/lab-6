import numpy as np
import array
n= int(input("Enter n:"))
arr=list(np.random.randint(-10000,10000,n))
print(arr)
countpos=0
countneg=0
for i in arr:
    if i>0:
        countpos+=1
    elif i<0:
        countneg+=1
if countneg>countpos:
    arr.extend(np.random.randint(0,100000,(countneg-countpos)))
if countneg<countpos:
    arr.extend(np.random.randint(-100000, 0, (countpos-countneg)))
print(arr)