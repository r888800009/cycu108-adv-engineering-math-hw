#!/usr/bin/env python
from sympy import *
from sympy.abc import t, s
import matplotlib.pyplot as plt
import numpy as np

index = 1
copyright = 'Copyright@Lin Yong Xiang 10612150'
def plotFigure(f, title, istart, iend, xy):
    x = np.linspace(istart, iend, 200)
    y = f(x)
    plt.plot(x, y)
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.title('{}'.format(title))
    plt.text(xy[0], xy[1], copyright)
    global index
    plt.savefig('prob8-{}.png'.format(index))
    index += 1
    plt.clf()

def u_t(x): return np.heaviside(x, 0)

def f1(t): return np.sin(2 * t) * u_t(t - np.pi)
def f2(t): return np.exp(-t) * np.sin(4 * t) * u_t(t - np.pi / 2)

plotFigure(f1, 'plotting a: f(t) = sin(2 * t) * u(t - pi)', 0, 4 * np.pi, (0.2, 0.1))
plotFigure(f2, 'plotting b: f(t) = exp(-t) * sin(4 * t) * u(t - pi / 2)', 0, 4 * np.pi, (0.2, 0.1))
