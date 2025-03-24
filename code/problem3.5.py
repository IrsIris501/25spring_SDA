import random
import matplotlib.pyplot as plt
import math
import numpy

list_y=[]
while len(list_y)<1000000:
    x=numpy.random.normal(scale=100)
    r=random.random()
    t=-math.log(r)
    list_y.append(x+t)
plt.hist(list_y, histtype='step', bins=500, density=True)
plt.show()
