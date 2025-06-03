# SDA Assignment10

Updated 1006 UTC+8, 29 May, 2025

<mark>陈虹骏 物理学院</mark>

#### 7.7

##### (a)

$$
\chi^2 = \sum_{i = 1}^{N} \frac{(n_i - \theta a(x_i))^2}{\theta a(x_i)}
$$

要
$$
\frac{\partial \chi^2}{\partial \theta} = \sum (-\frac{n_i^2}{\theta^2 a(x_i)} + a(x_i)) = 0
$$
得
$$
\hat{\theta} = (\frac{\sum \frac{n_i^2}{a(x_i)}}{\sum a(x_i)})^{\frac{1}{2}}
$$
展开的0阶项
$$
\hat{\theta_0} = \theta
$$
1阶项一定是0，2阶项中交叉项也是0
$$
\hat{\theta_2} = \sum \frac{\frac{\sum \frac{n_i^2}{a(x_i)}}{a(x_j)} - \frac{n_j^2}{a(x_j)^2}}{2(\sum \frac{n_i^2}{a(x_i)})^{\frac{3}{2}}(\sum a(x_i))^{\frac{1}{2}}} \nu_j
$$
带入
$$
\nu_i = \theta a(x_i)
$$
得到
$$
b = \frac{N-1}{2\sum a(x_i)} + O(E[(n_i - \nu_i)^3])
$$

##### (b)

$$
\chi^2 = \sum_{i = 1}^{N} \frac{(n_i - \theta a(x_i))^2}{n_i}
$$

得到
$$
\frac{\partial \chi^2}{\partial \theta} = \sum (-2a(x_i) + 2 \theta a(x_i)^2 / n_i) = 0
$$
得
$$
\hat{\theta} = \frac{\sum a(x_i)}{\sum \frac{a(x_i)^2}{n_i}}
$$
二阶项中的非交叉项

设
$$
A = \sum a (x_i)
$$

$$
\hat{\theta_2} = \sum - \frac{A - a(x_i)}{A^2} = - \frac{N-1}{A}
$$
故
$$
b = -\frac{N-1}{A} + O(E[(n_i - \nu_i)^3])
$$

##### (c)

对于(a)中
$$
V[\hat{\theta}] = \sqrt{\frac{\theta}{A}}
$$
(b)也是
$$
V[\hat{\theta}] = \sqrt{\frac{\theta}{A}}
$$

#### 7.8

##### (a)

由 7.7 可得
$$
\hat{\nu_0} = (\frac{\sum n_i^2 e^{B z_i / k}}{\sum e^{- B z_i / k}})^{1/2}
$$


得到
$$
k = 1.199 \times 10^{-23},\ \nu_0 = 1846
$$
代码

```python
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

```



##### (b)

$$
\hat{\nu_0} = \frac{ \sum e^{- B z_i / k}}{\sum e^{-2 B z_i / k} / n_i}
$$

$$
k = 1.197 \times 10^{-23},\ \nu_0 = 1844
$$

基本上差不多

代码

```python
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
        a1 += math.exp(- A * z[i] / x)
        b1 += math.exp(- 2 * A * z[i] / x) / n[i]
    return a1 / b1

def func(x):
    temp = 0
    for i in range(N):
        temp += (1 - nu(x) * math.exp(- A * z[i] / x) / n[i]) * z[i] * math.exp(- A * z[i] / x)
    return temp

left = 1
right = 1.5
mid = (left + right) / 2
while abs(func(mid)) > float('1e-10'):

    if func(mid) > 0:
        left = mid
        mid = (left + right) / 2
    else:
        right = mid
        mid = (left + right) / 2

print(mid, right - left)
print(nu(mid))

```

