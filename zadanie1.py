import numpy as np
import matplotlib.pyplot as plt
import scipy.signal


#создаем сам прямоугольный сигнал
t = np.linspace(0, 1, 500, endpoint=False)
square_wave = scipy.signal.square(2 * np.pi * 5 * t)


#отрисовываем сигнал
plt.plot(t, square_wave)
plt.title('Прямоугольный сигнал')
plt.xlabel('Время')
plt.ylabel('Амплитудда')
plt.show()