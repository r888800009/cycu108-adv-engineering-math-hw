#!/usr/bin/env python
from sympy import *
import matplotlib.pyplot as plt
import numpy as np

copyright = 'Copyright@Lin Yong Xiang 10612150'
def plotFigure(f, title, istart, iend):
    x = np.linspace(istart, iend, 100)
    y = f(x)
    plt.plot (x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('{}'.format(title))
    plt.text(0, 0, copyright)
    plt.show()

def fa(x): return (x - 1) / x
def fb(x): return np.sin((x ** 2) / 2)
def fc(x): return -x * np.cos(x) + x
def fd(x): return np.cos(x) * np.sin(x) + np.cos(x)
def fe(x): return np.tan(x) - x - 1

plotFigure(fa, 'IVP A solve: (x - 1) / x', 0, 1)
plotFigure(fb, 'IVP A solve: sin((x ** 2) / 2)', 0, 2 * np.pi)
plotFigure(fc, 'IVP A solve: -x * cos(x) + x', 0, 8 * np.pi)
plotFigure(fd, 'IVP A solve: cos(x) * sin(x) + cos(x)', 0, 4 * np.pi)
plotFigure(fe, 'IVP A solve: tan(x) - x - 1', 0, 4 * np.pi)

print('checks')
x = symbols('x')
y = symbols('y', cls=Function)

print('check a')
diffeq = Eq(y(x).diff(x), (y(x) - 1) ** 2)
print(dsolve(diffeq, y(x), ics={y(1): 0}))

print('check b')
diffeq = Eq(y(x).diff(x), x * sqrt(1 - y(x) ** 2))
print(dsolve(diffeq, y(x)))

print('check c')
diffeq = Eq(x * y(x).diff(x) - y(x), (x ** 2) * sin(x))
print(dsolve(diffeq, y(x)))
print(dsolve(diffeq, y(x), ics={y(2 * pi): 0}))

print('check d')
diffeq = Eq(y(x).diff(x) + tan(x) * y(x), cos(x) ** 2)
print(dsolve(diffeq, y(x)))
print(dsolve(diffeq, y(x), ics={y(0): 1}))

print('check e')
diffeq = Eq(y(x).diff(x), (x + y(x) + 1) ** 2)
print(dsolve(diffeq, y(x), hint="best"))
print(dsolve(diffeq, y(x), ics={y(0): -1}, hint="best"))
