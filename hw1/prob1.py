#!/usr/bin/env python
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import copyright

def xsinx(x):
    y = x * np.sin(x)
    return y

def genTaylor(time):
    x = symbols('x')
    y = 0
    for n in range(0, time):
        y += x ** (2 *(n + 1)) * (-1) ** n / np.math.factorial(2 * n + 1)
    print('gen')
    y.sort_key('rev-lex')
    print(y)
    print('check')
    e = x * sin(x)
    print(e.series(x, 0, 2 *(n + 1) + 1))
    return y

def plotBoth(f2, title, xy):
    x = np.linspace(-np.pi, np.pi, 100)
    y1 = xsinx(x)
    y2 = f2(x)
    plt.plot (x, y1, '-', x, y2, '--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('x*sin(x) & {}'.format(title))
    plt.text(xy[0], xy[1], copyright.copyright)
    plt.show()

# b
def taylorB(x):
    f = lambdify(symbols('x'), genTaylor(2), 'numpy')
    return f(x)

plotBoth(taylorB, 'x**2 - x**4/6', (-3, -6))

# c
def taylorC(x):
    f = lambdify(symbols('x'), genTaylor(3), 'numpy')
    return f(x)

plotBoth(taylorC, 'x**2 - x**4/6 + x**6/120', (-3, 0))

# d
def taylorD(x):
    f = lambdify(symbols('x'), genTaylor(4), 'numpy')
    return f(x)

plotBoth(taylorD, 'x**2 - x**4/6 + x**6/120 - x**8/5040', (-3, 0))
