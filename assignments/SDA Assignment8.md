# SDA Assignment8

1554 UTC+8, 21 May, 2025

<mark>陈虹骏 2400011459</mark>

#### 5.2, 5.4, 6.1, 6.5

![](https://raw.githubusercontent.com/IrsIris501/img/main/ebef653184e5e595b983517a946da5f.jpg)

![](https://raw.githubusercontent.com/IrsIris501/img/main/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250521192456.jpg)

![](https://raw.githubusercontent.com/IrsIris501/img/main/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250521192533.jpg)

#### 6.11

##### (a)

$$
\ln L(\nu_0, k) = \sum_{i = 1}^{4} (n_i \ln \nu_0 - n_i \frac{4 \pi r^3 \Delta \rho g z_i}{3 k T} - \nu_0 e^{-\frac{4 \pi r^3 \Delta \rho g z_i}{3 k T}})
$$

有
$$
\frac{\mathrm{d} \ln L(\nu_0, k)}{\mathrm{d} \nu_0} = 0 \\
\frac{\mathrm{d} \ln L(\nu_0, k)}{\mathrm{d} k} = 0
$$

得到
$$
k = 1.199 \times 10^{-23} J/mol K, \nu_0 = 1845
$$

##### (b)

$$
N_A = 6.94 \times 10^{23} / mol
$$

##### (c)

$$
\chi_p^2 和 \ln L(\nu_0, k) 同时取到最值，因此直接带入
$$

$$
\chi_p^2= 4.587
$$

服从自由度为4 - 2 = 2的卡方分布
$$
p\ value = 0.10
$$
一般般吧，不过N确实有点太小了

系统误差可以来源于：

1. 观测时可能未达到平衡态

2. 颗粒并非都是完美的球形

3. 颗粒密度可能在吸了水之后发生变化

   等...

###### 代码

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
```

