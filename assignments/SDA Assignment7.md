# SDA Assignment7

Updated 1201 UTC+8, 9 May, 2025

<mark>陈虹骏 物理学院 2400011459</mark>

#### 期中考前的作业

![](https://raw.githubusercontent.com/IrsIris501/img/main/23f5d18e84f199333601151e55353c3.jpg)

![](https://raw.githubusercontent.com/IrsIris501/img/main/6a7cd1af6fd40fde91d4b9df2f22be7.jpg)

![](https://raw.githubusercontent.com/IrsIris501/img/main/1de5575ba5e1e73fb793c6ced06f574.jpg)

#### 4.4

##### (a)

直方图

![](https://raw.githubusercontent.com/IrsIris501/img/main/p4.4a.png)
$$
\chi^2_{theory1} = 15.82, \chi^2_{theory2} = 35.97
$$
代码

```python
import numpy as np
import matplotlib.pyplot as plt

N=20
# 定义区间及频数
intervals = []
for i in range(N):
    intervals.append((i*0.5, (i+1)*0.5))
counts=list(map(float, input().split()))
counts1=list(map(float, input().split()))
counts2=list(map(float, input().split()))
chi2_1=0
chi2_2=0
for i in range(len(counts)):
    chi2_1+=(counts[i]-counts1[i])**2/counts1[i]
    chi2_2+=(counts[i]-counts2[i])**2/counts2[i]
print(chi2_1, chi2_2)
# 生成每个区间内的模拟数据
data = []
for (low, high), count in zip(intervals, counts):
    # 生成对应频数的随机样本（这里乘以100为了方便转成整数）
    sample_size = int(count * 100)
    samples = np.random.uniform(low, high, sample_size)
    data.extend(samples)

data1 = []
for (low, high), count in zip(intervals, counts1):
    # 生成对应频数的随机样本（这里乘以100为了方便转成整数）
    sample_size = int(count * 100)
    samples = np.random.uniform(low, high, sample_size)
    data1.extend(samples)

data2 = []
for (low, high), count in zip(intervals, counts2):
    # 生成对应频数的随机样本（这里乘以100为了方便转成整数）
    sample_size = int(count * 100)
    samples = np.random.uniform(low, high, sample_size)
    data2.extend(samples)
# 画直方图
plt.hist(data, bins=20, rwidth=0.8, histtype="step", label='data', weights=[0.01]*len(data))
plt.hist(data1, bins=20, rwidth=0.8, histtype="step", label='theory1', weights=[0.01]*len(data1))
plt.hist(data2, bins=20, rwidth=0.8, histtype="step", label='theory2', weights=[0.01]*len(data2))
plt.legend()


plt.title('problem 4.4(a)')
plt.show()
```

##### (b)

采用第n组的权重为n-1，加权平均计算泊松分布的v值得到
$$
\nu_1=7.837, \nu_2=10.059
$$
使用Monte Carlo法模拟得到的卡方统计量的分布为

![](https://raw.githubusercontent.com/IrsIris501/img/main/p4.5b1.png)

![](https://raw.githubusercontent.com/IrsIris501/img/main/p4.5b2.png)

根据mc法得到的卡方统计量分布计算p值
$$
p_1=0.776, p_2=0.059
$$
用正常的卡方分布计算是
$$
p_1=0.727, p_2=0.015
$$
代码

```python
import numpy as np
import matplotlib.pyplot as plt
import math

N=20
# 定义区间及频数
intervals = []
for i in range(N):
    intervals.append((i*0.5, (i+1)*0.5))
counts=list(map(float, input().split()))
counts1=list(map(float, input().split()))
counts2=list(map(float, input().split()))

'''
# 生成每个区间内的模拟数据
data = []
for (low, high), count in zip(intervals, counts):
    # 生成对应频数的随机样本（这里乘以100为了方便转成整数）
    sample_size = int(count * 100)
    samples = np.random.uniform(low, high, sample_size)
    data.extend(samples)

data1 = []
for (low, high), count in zip(intervals, counts1):
    # 生成对应频数的随机样本（这里乘以100为了方便转成整数）
    sample_size = int(count * 100)
    samples = np.random.uniform(low, high, sample_size)
    data1.extend(samples)

data2 = []
for (low, high), count in zip(intervals, counts2):
    # 生成对应频数的随机样本（这里乘以100为了方便转成整数）
    sample_size = int(count * 100)
    samples = np.random.uniform(low, high, sample_size)
    data2.extend(samples)
# 画直方图
plt.hist(data, bins=20, rwidth=0.8, histtype="step", label='data', weights=[0.01]*len(data))
plt.hist(data1, bins=20, rwidth=0.8, histtype="step", label='theory1', weights=[0.01]*len(data1))
plt.hist(data2, bins=20, rwidth=0.8, histtype="step", label='theory2', weights=[0.01]*len(data2))
plt.legend()


plt.title('problem 4.4(a)')
plt.show()
'''

chi2_1=0
chi2_2=0
for i in range(len(counts)):
    chi2_1+=(counts[i]-counts1[i])**2/counts1[i]
    chi2_2+=(counts[i]-counts2[i])**2/counts2[i]
print(f'chi2_1 = {chi2_1}, chi2_2 = {chi2_2}')


v1=0
v2=0
for i in range(len(counts)):
    v1+=(counts1[i])*i
    v2+=(counts2[i])*i

v1/=sum(counts1)
v2/=sum(counts2)
print(f'v1={v1}, v2={v2}')

# monte carlo
n_tot=sum(counts)
chi2_list1=[]
chi2_list2=[]
for i in range(5000):
    m1_dis=[0 for k in range(20)]
    while sum(m1_dis)<n_tot:
        j = np.random.poisson(lam=v1)
        if 0<=j<20:
            m1_dis[j]+=1
    m2_dis = [0 for k in range(20)]
    while sum(m2_dis) < n_tot:
        j = np.random.poisson(lam=v2)
        if 0 <= j < 20:
            m2_dis[j] += 1
    chi2_mc1=0
    chi2_mc2=0
    for j in range(len(m1_dis)):
        chi2_mc1+=(m1_dis[j]-counts1[j])**2/counts1[j]
        chi2_mc2 += (m2_dis[j] - counts2[j]) ** 2 / counts2[j]
    chi2_list1.append(chi2_mc1)
    chi2_list2.append(chi2_mc2)

plt.hist(chi2_list1, bins=20, rwidth=0.8, histtype="step", label='chi2_mc1')
plt.title('chi square for theory 1')
plt.show()
plt.hist(chi2_list2, bins=20, rwidth=0.8, histtype="step", label='chi2_mc1')
plt.title('chi square for theory 2')
plt.show()
cnt1=0
cnt2=0
for i in range(5000):
    if chi2_list1[i]>chi2_1:
        cnt1+=1
    if chi2_list2[i] > chi2_2:
        cnt2 += 1
print(f'p value for theory 1 is {cnt1/5000}, p value for theory 2 is {cnt2/5000}')
'''
data_mc = []
for (low, high), count in zip(intervals, m1_dis):
    # 生成对应频数的随机样本（这里乘以100为了方便转成整数）
    sample_size = int(count * 100)
    samples = np.random.uniform(low, high, sample_size)
    data_mc.extend(samples)
plt.hist(data_mc, bins=20, rwidth=0.8, histtype="step", label='data', weights=[0.01]*len(data_mc), range=(0, 10))
plt.show()
'''
```



#### 4.5

##### (a)

$$
\overline{m}=3.87, s^2=3.70, t=0.955
$$

$$
(n_{tot}-1)t=2488.9, n_{tot}-1=2607, 
$$

##### (b)

使用高斯分布的近似计算得
$$
p\ value=0.051
$$
应该是t大表示相符

##### (c)

t的直方图（共1000个t）

![](https://raw.githubusercontent.com/IrsIris501/img/main/p4.5c.png)

计算得到
$$
p\ value =0.058
$$
比(a)中的p值更大

代码

```python
import math
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt


n_m=list(map(int, input().split()))
n_tot=sum(n_m)
m_bar=0
s2=0
for i in range(15):
    m_bar+=i*n_m[i]

m_bar/=n_tot
for i in range(15):
    s2+=((i-m_bar)**2)*n_m[i]
s2/=(n_tot-1)
t=s2/m_bar
print(m_bar, s2, t, t*(n_tot-1))

mu=2607
sigma=math.sqrt(2*2607)
# 定义被积函数
def integrand(x):
    return math.exp(-((x-mu)**2)/(2*(sigma**2)))/math.sqrt(2*math.pi*sigma**2)

a =float('-inf')
b =t*(n_tot-1)
result, error = quad(integrand, a, b)

print(f"定积分的结果为：{result}, 误差为：{error}")

t_list=[]
for i in range(1000):
    m_list=np.random.poisson(lam=m_bar, size=n_tot)
    s2_mc=0
    for j in m_list:
        s2_mc+=(j-m_bar)**2
    s2_mc/=(n_tot-1)
    t_mc=s2_mc/m_bar
    t_list.append(t_mc)

cnt=0
for i in range(1000):
    if t_list[i]<t:
        cnt+=1
print(f'p value is {cnt/1000}')
plt.hist(t_list, bins=20)
plt.show()

```

#### 4.9

泊松分布，次数
$$
n=10\pm 1
$$
观察到5次是-5sigma，大于alpha=0.05 对应的1.96sigma，确实不是幸运年

#### 4.10

##### 原因：

1. **独立性假设**：虽然每个检验是独立的，但p值的乘积并不直接反映总的显著性水平。p值的乘积实际上表示的是在所有检验中同时观察到这些极端结果的概率，这并不等同于总的显著性水平。
2. **多重检验问题**：进行多个显著性检验会增加犯第一类错误（即错误地拒绝原假设）的概率。例如，如果进行n个独立的显著性检验，每个检验的显著性水平为α，那么至少犯一次第一类错误的概率是1 - (1 - α)^n，这通常会比单个检验的显著性水平α大得多。因此，简单地将p值相乘会低估总的显著性水平。
3. **p值的定义**：p值本身并不是概率的乘积，而是每个检验在原假设下的极端性度量。p值的乘积并不具有直接的统计意义，不能用来直接推断总的显著性水平。

##### 证明：

设
$$
Y=-2\ln X, g(Y)\mathrm{d}Y=\mathrm{d}X
$$
则
$$
g(Y)=|\frac{\mathrm{d}X}{\mathrm{d}Y}|=\frac{1}{2} \exp (-\frac{Y}{2})
$$
是自由度为2的卡方分布

##### 计算p值：

选择统计量
$$
t=\sum -2\ln P_i
$$
由于
$$
-2\ln P_i \sim \chi^2(2)
$$
因此
$$
t \sim \chi^2(2n)
$$
合并后的p值
$$
p_{combined} = P(\chi^2(2n)>t)
$$
代入数据计算得
$$
p=0.076
$$
