import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2 ** x

# Функция для построения ступенчатых фигур, соответствующих суммам Дарбу
def plot_darboux_sums(f, interval, n):
    x_sub = np.linspace(interval[0], interval[1], n+1)  # массив точек равномерного разбиения исходного интервала на n подынтервалов
    delta_x = (interval[1] - interval[0]) / n  # ширина интервалов

    m_i = f(x_sub[:-1])  # минимальные значения функции на подынтервалах для нижней суммы Дарбу
    M_i = f(x_sub[1:])  # максимальные значения функции на подынтервалах для верхней суммы Дарбу

    # Построение графика функции
    x_smooth = np.linspace(interval[0], interval[1], 1000)  # создаём массив значений
    plt.figure(figsize=(12, 8))  # создание графика размера 12 x 8 дюйм
    plt.plot(x_smooth, f(x_smooth), label='f(x)=$2^x$', color='black', linewidth=1.5)  # построение f(x)

    # Построение сумм Дарбу
    plt.bar(x_sub[:-1], m_i, width=delta_x, align='edge', edgecolor='black', linewidth=0.75, \
            color='blue', alpha=0.3, label='Нижние суммы Дарбу')  # нижние суммы Дарбу
    plt.bar(x_sub[:-1], M_i, width=delta_x, align='edge', edgecolor='black', linewidth=0.75, \
            color='green', alpha=0.3, label='Верхние суммы Дарбу')  # верхние суммы Дарбу

    # Настройки графика
    plt.title(f'Функция f(x)=$2^x$\nCтупенчатые фигуры, соответсвующие суммам Дарбу, n={n}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(False)
    plt.show()

n_input = int(input('Введите число точек разбиения n: '))
plot_darboux_sums(f, interval=[0, 1], n=n_input)

