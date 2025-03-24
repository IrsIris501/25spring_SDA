import random
import matplotlib.pyplot as plt
import math

list_x=[]
list_xbar=[]
for i in range(100000):
    list_temp=[]
    for j in range(10):
        r=random.random()
        x=math.tan(math.pi*(r-0.5))
        list_x.append(x)
        list_temp.append(x)
    list_xbar.append(sum(list_temp)/10)
plt.hist(list_x, bins=100, histtype='step', density=True, range=(-10, 10), label='x')
plt.hist(list_xbar, bins=100, histtype='step', density=True, range=(-10, 10), label='xbar')
plt.legend()
plt.show()