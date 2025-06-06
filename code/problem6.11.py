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
        a1 += n[i]
        b1 += math.exp(- A * z[i] / x)
    return a1 / b1

def func(x):
    temp = 0
    for i in range(N):
        temp += n[i] * A * z[i] * (10 ** 23) / (x ** 2) - nu(x) * math.exp(- A * z[i] / x) * A * z[i] * (10 ** 23) / (x ** 2)
    return temp

left = 1
right = 1.5
mid = (left + right) / 2
while abs(func(mid)) > float('1e3'):
    if func(mid) > 0:
        left = mid
        mid = (left + right) / 2
    else:
        right = mid
        mid = (left + right) / 2

print(mid, right - left)
print(nu(mid))

# get chi_square
nui = []
chi_square = 0
for i in range(N):
    nui.append(nu(mid) * math.exp(- A * z[i] / mid))
for i in range(N):
    chi_square += 2 * (n[i] * math.log(n[i] / nui[i]) + nui[i] - n[i])
print(f'chi_square = {chi_square}')