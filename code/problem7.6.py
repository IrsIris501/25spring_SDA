import math

d = [8, 15.5, 22.5, 29, 35, 40.5, 45.5, 50]
h = [10, 20, 30, 40, 50, 60, 70, 80]
sigma = 0.5


left = 0
right = 100
mid = 50

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

def rad(x):
    return x * math.pi / 180
def func3(x):
    temp = 0
    for i in range(len(d)):
        temp += (rad(d[i]) - math.asin(math.sin(rad(h[i])) / x)) * math.sin(rad(h[i])) / math.sqrt(1 - (math.sin(math.sin(rad(h[i])) / x)) ** 2)
    return temp

left = 1
right = 2
mid = 1.5
while abs(func3(mid)) > float('1e-6'):
    if func3(mid) < 0:
        left = mid
        mid = (left + right) / 2
    else:
        right = mid
        mid = (left + right) / 2
print(f'r = {mid}')

chi_square = 0
for i in range(len(d)):
    chi_square += ((rad(d[i]) - math.asin(math.sin(rad(h[i])) / mid)) ** 2) / (rad(sigma) **2)
print(f'chi_square = {chi_square}')