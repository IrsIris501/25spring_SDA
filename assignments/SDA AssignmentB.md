# SDA AssignmentB

Last update 1527 UTC+8, 6 Jun, 2025

<mark>陈虹骏 2400011459</mark>

#### 8.1

$$
E[a_1 (x)] = \mu,\ E[a_2 (x)] = \mu^2 + \sigma^2
$$

$$
\hat{e_1} = \frac{\sum x_i}{n},\ \hat{e_2} = \frac{\sum x_i^2}{n}
$$

得到
$$
\hat{\mu} = \frac{\sum x_i}{n},\ \hat{\sigma^2} = \frac{\sum x_i^2}{n} - (\frac{\sum x_i}{n})^2
$$

###### 计算期待值

$$
E[\hat{\mu}] = \mu,\ E[\hat{\sigma^2}] = \frac{n-1}{n} \sigma^2
$$

在n趋于无穷大时几乎是无偏的

#### 8.2

$$
E[\cos^2 \theta] = \frac{1}{3} + \frac{4}{15} \eta
$$

$$
\hat{\eta} = \frac{4}{15} (\frac{\sum \cos^2 \theta_i}{n} - \frac{1}{3})
$$

如果用a=x 的话那E[a]就是0，没有\eta 了

###### 计算期待值

$$
E[\hat{\eta}] = \eta
$$

###### 计算方差

$$
V[\hat{e}] = \frac{1}{n(n-1)} \sum (\cos \theta_i - \frac{\sum \cos \theta_i}{n})^2
$$

$$
V[\hat{\eta}] = \frac{16}{225} V[\hat{e}] = \frac{16}{225 n (n-1)} \sum (\cos \theta_i - \frac{\sum \cos \theta_i}{n})^2
$$

#### 9.1

###### (a)

![](https://raw.githubusercontent.com/IrsIris501/img/main/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250606152149.jpg)

###### (b)

此时
$$
\alpha = \beta = \frac{\gamma}{2}
$$
由于
$$
\alpha = P(\hat{\theta} > u_\alpha (\theta))
$$
因此下界为
$$
\hat{\theta } - \sigma_\hat{\theta} \phi^{-1}(1 - \gamma / 2)
$$
同样的，上界
$$
\hat{\theta } + \sigma_\hat{\theta} \phi^{-1}(1 - \gamma / 2)
$$
