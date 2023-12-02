import numpy as np
import matplotlib.pyplot as plt


#создаем данные с норм. распределением
mu, sigma = 0, 0.1 #ср. значение и стандартное откл.
s = np.random.normal(mu, sigma, 1000)


#отрисовываем гистограмму распределенеия
count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu)**2 / (2 * sigma**2)), linewidth=2, color='y')
plt.show()
