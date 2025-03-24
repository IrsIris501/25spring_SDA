import random
import matplotlib.pyplot as plt
import math
list_x=[]

for i in range(1000000):
    r=random.random()
    list_x.append(math.sqrt(r))
plt.hist(list_x, bins=500, density=True, histtype="step")
plt.show()

list_x2=[]
while len(list_x2)<1000000:
    x=random.random()
    r2=random.random()
    if r2<=x:
        list_x2.append(x)
plt.hist(list_x2, bins=500, density=True, histtype="step")
plt.show()
