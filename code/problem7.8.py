import math


N = 4
n = [1880, 940, 530, 305]
z = [0, 0.000006, 0.000012, 0.000018]
A = (4 * math.pi * (0.00000052**3) * 63 * 9.8 * (10**23) / (3 * 293))


# get nu and k
def nu(x):
    a1 = 0
    b1 = 0
    for i in range(N):
        a1 += n[i] * n[i] * math.exp(A * z[i] / x)
        b1 += math.exp(- A * z[i] / x)
    return math.sqrt(a1 / b1)

def func(x):
    temp = 0
    for i in range(N):
        temp += (1 - n[i] * n[i] / (nu(x) * nu(x) * math.exp(- 2 * A * z[i] / x))) * z[i] * math.exp(- A * z[i] / x)
    return temp

left = 1
right = 1.5
mid = (left + right) / 2
while abs(func(mid)) > float('1e-12'):

    if func(mid) < 0:
        left = mid
        mid = (left + right) / 2
    else:
        right = mid
        mid = (left + right) / 2

print(mid, right - left)
print(nu(mid))
