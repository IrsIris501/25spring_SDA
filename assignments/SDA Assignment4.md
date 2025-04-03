# SDA第四周作业

陈虹骏 2400011459

Edited 1208 UTC+8, 23 March, 2025

### 习题3.3

##### (1)

累积函数
$$
F(x) = \int_{0}^{x} \frac{2x}{x_{max}^2} \mathrm{d}x=\frac{x^2}{x_{max}^2}
$$
变换函数
$$
x=F^{-1}(r)=x_{max}\sqrt{r}
$$
代码如下

```python
import random
import matplotlib.pyplot as plt
import math
list_x=[]
for i in range(1000000):
    r=random.random()
    list_x.append(math.sqrt(r))
plt.hist(list_x, bins=500, density=True, histtype="step")
plt.show()
```

得到

![](https://raw.githubusercontent.com/IrsIris501/img/main/Figure_1.png)

##### (2)

舍选法代码如下

```python
import random
import matplotlib.pyplot as plt
import math
list_x2=[]
while len(list_x2)<1000000:
    x=random.random()
    r2=random.random()
    if r2<=x:
        list_x2.append(x)
plt.hist(list_x2, bins=500, density=True, histtype="step")
plt.show()
```

得到

![](https://raw.githubusercontent.com/IrsIris501/img/main/Figure_1.1.png)

### 习题3.5

```python
import random
import matplotlib.pyplot as plt
import math
import numpy

list_y=[]
while len(list_y)<1000000:
    x=numpy.random.normal(scale=0.5)
    r=random.random()
    t=-math.log(r)
    list_y.append(x+t)
plt.hist(list_y, histtype='step', bins=500, density=True)
plt.show()

```

![](https://raw.githubusercontent.com/IrsIris501/img/main/Figure_3.5.1.png)

当
$$
\tau \gg \sigma
$$
时，设
$$
\tau=1, \sigma=0.005
$$
![](https://raw.githubusercontent.com/IrsIris501/img/main/Figure_3.5.2.png)

几乎接近于指数分布。当
$$
\tau \ll \sigma, \tau=1, \sigma=100
$$
时

![](https://raw.githubusercontent.com/IrsIris501/img/main/Figure_3.5.3.png)

接近于高斯分布。

### 习题3.6

##### (1)

$$
F(x) = \int_{-\infin}^{x} \frac{1}{\pi} \frac{1}{1+x^2} \mathrm{d}x= \frac{1}{\pi} \arctan x +\frac{1}{2} \\
x=F^{-1}(r)=\tan [\pi (r-\frac{1}{2})]
$$

```python
import random
import matplotlib.pyplot as plt
import math

list_x=[]
for i in range(10000):
    r=random.random()
    x=math.tan(math.pi*(r-0.5))
    list_x.append(x)
plt.hist(list_x, bins=100, histtype='step', density=True, range=(-10, 10)) #在-10和10截断，以免直方图比例太不协调
plt.show()
```

![](https://raw.githubusercontent.com/IrsIris501/img/main/Figure_3.6.1.png)

进行修改

```python
import random
import matplotlib.pyplot as plt
import math

list_x=[]
list_xbar=[]
for i in range(100000):
    list_temp=[]
    for j in range(10):
        r=random.random()
        x=math.tan(math.pi*(r-0.5))
        list_x.append(x)
        list_temp.append(x)
    list_xbar.append(sum(list_temp)/10)
plt.hist(list_x, bins=100, histtype='step', density=True, range=(-10, 10), label='x')
plt.hist(list_xbar, bins=100, histtype='step', density=True, range=(-10, 10), label='xbar')
plt.legend()
plt.show()
```

![](https://raw.githubusercontent.com/IrsIris501/img/main/Figure_3.6.2.png)

可见其实没什么区别

### 习题3.8

```python
import random
import math

# 舍选法
ord_list=[]
while len(ord_list)<1000:
    r=random.random()
    r2=random.random()
    if r2<r:
        theta=2*math.pi*random.random()
        ord_list.append((r, theta))

```

### 习题3.9

```python
import math
import random

min_r=float(1e-8)
count=0
for i in range(10000000):
    x=(1-min_r)*random.random()+min_r
    fx=math.exp(-x)/math.sqrt(x)
    r=10000*random.random()
    if r<fx:
        count+=1
print(count/1000)

# return 1.49
```

