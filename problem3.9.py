import math
import random

min_r=float(1e-8)
count=0
for i in range(10000000):
    x=(1-min_r)*random.random()+min_r
    fx=math.exp(-x)/math.sqrt(x)
    r=10000*random.random()
    if r<fx:
        count+=1
print(count/1000)
