# SDA Assignment9

1946 UTC+8, 21 May, 2025

<mark>陈虹骏 2400011459</mark>

#### 7.1

##### (a)

$$
\chi^2 = \sum_{i = 1}^{N} \frac{(d_i - \alpha h_i)^2}{\sigma^2}
$$

要让chi_square最小，
$$
\frac{\mathrm{d} \chi^2}{\mathrm{d} \alpha} = 0
$$
得到
$$
\alpha = 1.663
$$

$$
\chi^2_1 = 662,\ p\ value \lt 0.00001
$$

使用第二个假设
$$
\chi^2 = \sum_{i = 1}^{N} \frac{(d_i - \alpha h_i - \beta h_i^2)^2}{\sigma^2}
$$

$$
\frac{\partial \chi^2}{\partial \alpha} = 0,\ \frac{\partial \chi^2}{\partial \beta} = 0
$$

得到
$$
\alpha = 2.793,\ \beta = -0.0014
$$

$$
\chi_2^2 = 64.7,\ p\ value \lt 0.00001
$$

都不好

##### (b)

$$
\chi^2 = \sum_{i = 1}^{N} \frac{(d_i - \alpha h_i^{\beta})^2}{\sigma^2}
$$

$$
\frac{\partial \chi^2}{\partial \alpha} = 0,\ \frac{\partial \chi^2}{\partial \beta} = 0
$$

$$
\alpha = 43.8,\ \beta = 0.511
$$

$$
\chi_3^2 = 3.756,\ p\ value = 0.29
$$

无法拒绝假设

##### (c)

这就是平抛运动
$$
\alpha = 47.09
$$

$$
\chi_4^2 = 4.208,\ p\ value = 0.38
$$

无法拒绝假设，并且比(b)的假设更好了

###### 代码

```python
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
```



#### 7.5

##### (a)

$$
\mathrm{cov} [y_1, y_2] = E[y_1 y_2] - E[y_1]E[y_2]
$$

由于
$$
E[x_i x_j] = \mu^2,\ E[x_ix_i] = \mu^2 + \sigma^2
$$
因此
$$
\mathrm{cov} [y_1, y_2] = \frac{c \sigma^2}{mn}
$$

##### (b)

$$
y = \frac{n - c}{m + n - 2c}y_1 + \frac{m - c}{m + n - 2c}y_2
$$

$$
V[y] = [\frac{1}{m} (\frac{n - c}{m + n - 2c})^2 + \frac{1}{n} (\frac{m - c}{m + n - 2c})^2 - \frac{2c}{mn}(\frac{n - c}{m + n - 2c})(\frac{m - c}{m + n - 2c})] \sigma^2
$$

#### 7.6

##### (a)

###### 线性的假设

$$
\alpha = 0.666,\ \chi^2 = 135,\ p\ value \lt 0.00001
$$

拒绝假设。

###### 二次假设

$$
\alpha = 0.825,\ \beta = 0.0025,\ \chi^2 = 3.1 \times 10^{-21},\ p\ value \approx 1
$$

这个数据是编的吧，这卡方也太小了

##### (b)

$$
r = 1.31,\ \chi^2 = 14.0,\ p\ value = 0.051
$$

刚好无法拒绝，虽然这个数据疑似是编造的

###### 代码

```python
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
```

