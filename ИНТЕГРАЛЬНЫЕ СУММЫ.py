import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2 ** x

# Функция для построения интегральных сумм и расчёта значения интеграла Римана
def plot_and_calculate_riemann_sum(f, interval, n, method):
    x_sub = np.linspace(interval[0], interval[1], n+1)  # массив точек равномерного разбиения исходного интервала на n подынтервалов
    delta_x = (interval[1] - interval[0]) / n  # ширина интервалов

    if method == 'левые':  # левые концы интервалов
        x_riemann = x_sub[:-1]
    elif method == 'правые':  # правые концы интервалов
        x_riemann = x_sub[1:]
    elif method == 'средние':  # середины интервалов
        x_riemann = (x_sub[:-1] + x_sub[1:]) / 2
    elif method == 'случайные':  # случайные точки внутри интервалов
        x_riemann = x_sub[:-1] + np.random.rand(n) * delta_x

    y_riemann = f(x_riemann)
    riemann_sum = np.sum(y_riemann * delta_x)

    # Построение графика функции
    x_smooth = np.linspace(interval[0], interval[1], 1000)  # создаём массив значений
    plt.figure(figsize=(12, 8))  # создание графика размера 12 x 8 дюйм
    plt.plot(x_smooth, f(x_smooth), label='f(x)=$2^x$', color='black', linewidth=1.5)  # построение f(x)

    # Построение интегральных сумм
    plt.bar(x_sub[:-1], y_riemann, width=delta_x, align='edge', edgecolor='black', linewidth=1.5, \
            color='darkorchid', alpha=0.7, label='Интегральные суммы')

    # Настройки графика
    plt.title(f'Функция f(x)=$2^x$\nИнтегральные суммы, n={n}, способ выбора оснащения:{method}, значение={riemann_sum:.4f}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(False)
    plt.show()

    return riemann_sum

n_input = int(input('Введите число точек разбиения n: '))
method_input = input('Введите способ выбора оснащения (левые, правые, средние, случайные): ')
riemann_sum = plot_and_calculate_riemann_sum(f, interval=[0, 1], n=n_input, method=method_input)
print(f'Интегральные суммы: {riemann_sum}')
