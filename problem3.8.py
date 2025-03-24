import random
import math

# 舍选法
ord_list=[]
while len(ord_list)<1000:
    r=random.random()
    r2=random.random()
    if r2<r:
        theta=2*math.pi*random.random()
        ord_list.append((r, theta))
