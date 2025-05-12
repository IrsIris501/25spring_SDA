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
