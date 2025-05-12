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