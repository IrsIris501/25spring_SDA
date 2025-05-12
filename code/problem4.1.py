import math
from scipy import integrate

def func(x):
    return math.exp(-x**2/2)
l=-3
r=-2
while r-l>float(1e-9):
    mid=(l+r)/2
    int1, err1 = integrate.quad(func, float('-inf'), mid)
    int2, err2 = integrate.quad(func, float('-inf'), mid-2)
    if int1/int2>1881:
        l=mid
    else:
        r=mid
print(l)