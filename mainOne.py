import math
from scipy import integrate
import matplotlib.pyplot as plt

def function(x):
    """Исходная функция"""
    return 8*( 7 * math.pow(2,2)+34 * 2 * x - 5* math.pow(2,2))/(27* math.pow(2,2)+33 * 2 * x + 10* math.pow(x,2))



val_b = [-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] #значения верхнего предела
                                                                                                  #нижний передел фиксированный а = -1

def sympson(f, n, val_b):
    """ Метод вычисления интегралов методом Симпсона(парабол).

    На вход подается необходимая функция(f), число проходов(n) и список значений верхнего предела(val_b).
    Нижний предел фиксированный и равен -1
    """
    a = -1
    sympson_val = dict()
    for b in val_b:

        h = (b - a) / (2 * n)
        tmp_sum = float(f(a)) + float(f(b))

        for step in range(1, 2 * n):
            if step % 2 != 0:
                tmp_sum += 4 * float(f(a + step * h))
            else:
                tmp_sum += 2 * float(f(a + step * h))

        result = tmp_sum * h / 3
        sympson_val[b] = result

    return sympson_val


def rect(f, n, val_b):
    """ Метод вычисления интегралов методом прямоугольников.

    На вход подается необходимая функция(f), число проходов(n) и список значений верхнего предела(val_b).
    Нижний предел фиксированный и равен -1
    """
    a = -1
    rect_val = dict()

    for b in val_b:
        h = (b - a) / float(n)
        total = sum([f((a + (k * h))) for k in range(0, n)])
        result = h * total
        rect_val[b] = result

    return rect_val


def trap(f, n, val_b):
    """ Метод вычисления интегралов методом трапеций.

    На вход подается необходимая функция(f), число проходов(n) и список значений верхнего предела(val_b).
    Нижний предел фиксированный и равен -1
    """
    a = -1
    trap_val = dict()

    for b in val_b:
        delx = (b - a) / n
        ind = a + delx
        sumfpod = 0

        while (ind < b):
            sumfpod += 2 * f(ind)
            ind += delx

        sumfpod = (sumfpod + f(a) + f(b)) * delx / 2
        trap_val[b] = sumfpod

    return trap_val

NL = dict()
for b in val_b: # истинные значения
    NL[b] = integrate.quad(function, -1, b)[0]

plt.figure(figsize=(12, 7))
q = 1
for i in [1, 5, 10, 100]: # количество проходов
    plt.subplot(2, 2, q)
    plt.grid(True)
    q += 1
    plt.plot(NL.keys(), NL.values(), label = 'true')
    plt.plot(sympson(function, i, val_b).keys(), sympson(function, i, val_b).values(), label = 'sympson')
    plt.plot(rect(function, i, val_b).keys(), rect(function, i, val_b).values(), label = 'rect')
    plt.plot(trap(function, i, val_b).keys(), trap(function, i, val_b).values(), label = 'trap')
    plt.title('Количество проходов {}'.format(i), fontsize = 10)
    plt.legend()
plt.show()