#!/usr/bin/env python
from sympy import *
import matplotlib.pyplot as plt
import numpy as np

index = 1
copyright = 'Copyright@Lin Yong Xiang 10612150'
def plotFigure(f, title, istart, iend, xy):
    x = np.linspace(istart, iend, 200)
    y = f(x)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('{}'.format(title))
    plt.text(xy[0], xy[1], copyright)
    global index
    plt.savefig('prob{}.png'.format(index))
    index += 1
    plt.clf()

x, C1, C2 = symbols('x C1 C2')
y = symbols('y', cls=Function)
subs = {C1: 1, C2:1}

def f1(x): return np.sin(x)/3 + np.sin(2*x) + np.cos(2*x)
def f2(x): return ((x + 1)*np.exp(x) + 1)*np.exp(x)
def f3(x): return x*(x**2 + 1)
def f4(x): return np.sin(x)**2/3 + np.sin(x) + np.cos(x) + 1/3
def f5(x): return x**2/6 + 1 + 1/x

plotFigure(f1, 'plotting 1 solve: sin(x)/3 + sin(2*x) + cos(2*x)', 0, 2 * np.pi, (0.2, -1.5))
plotFigure(f2, 'plotting 2 solve: ((x + 1)*exp(x) + 1)*exp(x)', 0, 1, (0.2, 2))
plotFigure(f3, 'plotting 3 solve: x*(x**2 + 1)', 0, 1, (0.2, 1))
plotFigure(f4, 'plotting 4 solve: sin(x)**2/3 + sin(x) + cos(x) + 1/3', 0, 2 * np.pi, (0.2, -0.75))
plotFigure(f5, 'plotting 5 solve: x**2/6 + 1 + 1/x', 0, 1, (0.2, 25))

# prob1
print("prob1")
diffeq = Eq(y(x).diff(x).diff(x) + 4 * y(x), sin(x))
solve = dsolve(diffeq, y(x)).subs(subs)
print(solve)

# prob2
print("prob2")
diffeq = Eq(y(x).diff(x).diff(x) - 3 * y(x).diff(x) + 2 * y(x), exp(2 * x))
solve = dsolve(diffeq, y(x)).subs(subs)
print(solve)

# prob3
print("prob3")
diffeq = Eq(x ** 2 * y(x).diff(x).diff(x) - 3 * x * y(x).diff(x) + 3 * y(x), 0)
solve = dsolve(diffeq, y(x)).subs(subs)
print(solve)

# prob4
print("prob4")
diffeq = Eq(y(x).diff(x).diff(x) + y(x), cos(x) ** 2)
solve = dsolve(diffeq, y(x)).subs(subs)
print(solve)

# prob5
print("prob5")
diffeq = Eq(x * y(x).diff(x).diff(x) + 2 * y(x).diff(x), x)
solve = dsolve(diffeq, y(x)).subs(subs)
print(solve)
