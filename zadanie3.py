import csv
import matplotlib.pyplot as plt


passenger_data = []
with open('passengers.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        passenger_data.append(int(row[1]))


#построение линейного графика
plt.figure(1)
plt.plot(passenger_data)
plt.title('Зависимость количества пассажиров от времени')
plt.xlabel('Месяцы')
plt.ylabel('Число пассажиров')


#распределение пассажиров по месяцам в 1951-1955
plt.figure(2)
plt.hist(passenger_data, bins=12)
plt.title('Распределение по месяцам')
plt.xlabel('Число пассажиров')
plt.ylabel('Частота')
plt.show()
