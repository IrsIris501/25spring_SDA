import math

d = [1500, 1340, 1328, 1172, 800]
h = [1000, 828, 800, 600, 300]
sigma = 15
left = 1
right = 3
mid = 2
def func(x):
    temp = 0
    for i in range(len(d)):
        temp += (d[i] - x * h[i]) * h[i]
    return temp

while abs(func(mid)) > float('1e-6'):
    if func(mid) > 0:
        left = mid
        mid = (left + right) / 2
    else:
        right = mid
        mid = (left + right) / 2
print(f'alpha = {mid}')

chi_square = 0
for i in range(len(d)):
    chi_square += ((d[i] - mid * h[i]) ** 2) / (sigma **2)
print(f'chi_square = {chi_square}')

def alpha(x):
    a = 0
    b = 0
    for i in range(len(d)):
        a += h[i] * d[i] - x * h[i] * h[i] * h[i]
        b += h[i] * h[i]
    return a / b

def func2(x):
    temp = 0
    for i in range(len(d)):
        temp += h[i] * h[i] * (d[i] - alpha(x) * h[i] - x * h[i] * h[i])
    return temp

left = -10
right = 10
mid = 5
while abs(func2(mid)) > float('1e-6'):
    if func2(mid) > 0:
        left = mid
        mid = (left + right) / 2
    else:
        right = mid
        mid = (left + right) / 2
print(f'alpha = {alpha(mid)}, beta = {mid}')

chi_square = 0
for i in range(len(d)):
    chi_square += ((d[i] - alpha(mid) * h[i] - mid * h[i] * h[i]) ** 2) / (sigma **2)
print(f'chi_square = {chi_square}')

def alpha3(x):
    a = 0
    b = 0
    for i in range(len(d)):
        a += d[i] * (h[i] ** x)
        b += h[i] ** (2*x)
    return a / b

def func3(x):
    temp = 0
    for i in range(len(d)):
        temp += (h[i] ** x) * (d[i] - alpha3(x) * (h[i] ** x)) * math.log(h[i])
    return temp

left = 0
right = 1
mid = 0.5
while abs(func3(mid)) > float('1e-6'):
    if func3(mid) > 0:
        left = mid
        mid = (left + right) / 2
    else:
        right = mid
        mid = (left + right) / 2
print(f'alpha3 = {alpha3(mid)}, beta3 = {mid}')

chi_square = 0
for i in range(len(d)):
    chi_square += ((d[i] - alpha3(mid) * (h[i] ** mid)) ** 2) / (sigma **2)
print(f'chi_square3 = {chi_square}')

left = 0
right = 100
mid = 50
def func4(x):
    temp = 0
    for i in range(len(d)):
        temp += (d[i] - x * math.sqrt(h[i])) * math.sqrt(h[i])
    return temp

while abs(func4(mid)) > float('1e-6'):
    if func4(mid) > 0:
        left = mid
        mid = (left + right) / 2
    else:
        right = mid
        mid = (left + right) / 2
print(f'alpha = {mid}')

chi_square = 0
for i in range(len(d)):
    chi_square += ((d[i] - mid * math.sqrt(h[i])) ** 2) / (sigma **2)
print(f'chi_square = {chi_square}')