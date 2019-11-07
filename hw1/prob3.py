#!/usr/bin/env python
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import copyright

X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
x, y = np.meshgrid(X, Y)

def plotFigure(de, title):
    # DE
    dy = de 
    dx = 1

    # normal from
    norm = np.sqrt(dx * dx + dy * dy)
    dy = dy / norm
    dx = dx / norm

    # Plot
    plt.figure(1)
    q = plt.quiver(x, y, dx, dy)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Direction Field dy/dx = {}'.format(title))
    plt.grid()
    plt.text(-2, -4.8, copyright.copyright)

    plt.show()

#plotFigure(0.2 * x * y, '123')
plotFigure(x + y, 'x + y')
plotFigure(x - y, 'x - y')
plotFigure(x * y, 'x * y')
plotFigure(np.sin(x) * np.cos(y), 'sin(x) * cos(y)')

