from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

a = b = 0.159
n = 5
k_a = stats.chi2.ppf(1-a, 2*n)
k_b = stats.chi2.ppf(b, 2*n)



# 定义函数
def f_a(x):
    return x * k_a
def f_b(x):
    return x * k_b

# 生成数据点
x = np.linspace(-5, 5, 100)  # 在[-5, 5]区间生成100个点
y = f_a(x)
z = f_b(x)

# 绘制图像
plt.plot(x, y, label="y = u_alpha", color="blue")
plt.plot(x, z, label="y = u_beta", color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot of upper and lower bound")
plt.grid(True)
plt.legend()
plt.show()

print(f'[{k_b}, {k_a}]')
