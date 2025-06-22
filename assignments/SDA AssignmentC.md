# SDA AssignmentC

Updated 1640 UTC+8, 22 Jun, 2025

<mark>陈虹骏 2400011459</mark>

#### 9.2

##### (a)

$$
\alpha = \int_{u_\alpha}^{\infin} g(\hat{\xi};\xi) \mathrm{d} \xi = \int_{u_\alpha}^{\infin} \frac{n^n}{(n-1)!} \frac{\hat{\xi}^{n-1}}{\xi^n} e^{-n\hat{\xi} / \xi} \mathrm{d} \hat{\xi} \\
1-\alpha = \int^{u_\alpha}_{0} \frac{n^n}{(n-1)!} \frac{\hat{\xi}^{n-1}}{\xi^n} e^{-n\hat{\xi} / \xi} \mathrm{d} \hat{\xi}
$$

令
$$
x = 2n \hat{\xi}/\xi \\
1-\alpha = \int^{x_\alpha}_{0} \frac{n^n}{(n-1)!} \frac{\hat{\xi}^{n-1}}{\xi^n} e^{-n\hat{\xi} / \xi} \mathrm{d} \hat{\xi} \\
1-\alpha = \int_{0}^{x_{\alpha}} f_{\chi^2}(x; 2n) \mathrm{d}x \\
u_\alpha = \frac{\xi}{2n} F_{\chi^2}^{-1} (1-\alpha ; 2n)
$$
同理
$$
u_\beta = \frac{\xi}{2n} F_{\chi^2}^{-1} (\beta ; 2n)
$$
![](https://raw.githubusercontent.com/IrsIris501/img/main/problem9.2a.png)

##### (b)

$$
[a, b] = [\frac{\hat{\xi}}{2n} F_{\chi^2}^{-1} (\beta ; 2n), \frac{\hat{\xi}}{2n} F_{\chi^2}^{-1} (1-\alpha ; 2n)]
$$

就是上图中x = 1 处

代入得
$$
[5.68, 14.32]
$$

#### 9.3

##### (a)

利用题给关系，得到
$$
\alpha = \sum_{k=0}^{n-1} \frac{N!}{k!(N-k)!} p^k (1-p)^{N-k} = F_F [\frac{(N-n+1)p_{lo}}{n(1-p_{lo})}; 2n, 2(N-n+1)] \\
1-\beta = \sum_{k=0}^{n} \frac{N!}{k!(N-k)!} p^k (1-p)^{N-k} = F_F [\frac{(N-n)p_{up}}{(n+1)(1-p_{up})}; 2(n+1), 2(N-n)]
$$
解得
$$
p_{lo} = \frac{n F_F^{-1}[\alpha; 2n, 2(N-n+1)]}{N-n+1+nF_F^{-1}[1-\beta; 2n, 2(N-n+1)]} \\
p_{up} = \frac{(n+1) F_F^{-1}[\alpha; 2(n+1), 2(N-n)]}{N-n+ (n+1)F_F^{-1}[1-\beta; 2(n+1), 2(N-n)]}
$$


