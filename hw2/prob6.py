#!/usr/bin/env python
from sympy import *
import matplotlib.pyplot as plt
import numpy as np

index = 1
copyright = 'Copyright@Lin Yong Xiang 10612150'
def plotFigure(f, title,ylabel, istart, iend, xy):
    x = np.linspace(istart, iend, 200)
    y = f(x)
    plt.plot(x, y)
    plt.xlabel('t')
    plt.ylabel(ylabel)
    plt.title('{}'.format(title))
    plt.text(xy[0], xy[1], copyright)
    global index
    plt.savefig('prob6-{}.png'.format(index))
    index += 1
    plt.clf()

def q(t): return -12 / 25 * np.exp(-5 * t) -12 / 5 * t * np.exp(-5 * t)
def i(t): return 12 * t *np.exp(-5 * t)

plotFigure(q, 'plotting q(t)', 'q(t)', 0, 2, (0.2, -0.4))
plotFigure(i, 'plotting i(t)', 'i(t)', 0, 2, (0.2, 0.4))
