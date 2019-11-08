#!/usr/bin/env python
from sympy import *
from sympy.abc import n
import numpy as np

def genTaylor():
    x= symbols('x')
    f = x ** (2 *n + 2) * (-1) ** n / factorial(2 * n + 1)
    sigma = Sum(f, (n, 0 ,oo))
    print('gen')
    print(sigma)
    print(sigma.doit())

    print("========")
    print('T(10)')
    eq = x * sin(x)
    sigma = Sum(f, (n, 0 ,4))
    print(eq.series(x, 0, 10))
    print(sigma.doit())

genTaylor()
# a

