#!/usr/bin/env python
from sympy import *
from sympy.abc import t, s

print('prob a')
sol = laplace_transform(t ** 3 * exp(t), t, s)
print(sol)
# print(latex(sol))

print('prob b')
sol = laplace_transform(t * sin(2 * t), t, s)
print(sol)
# print(latex(sol))

print('prob c')
sol = laplace_transform(exp(2 * t) * cos(t), t, s)
print(sol)
# print(latex(sol))

print('prob d')
sol = inverse_laplace_transform(1 / (s ** 2 +  2 * s + 2), s, t)
print(sol)
# print(latex(sol))

print('prob e')
sol = inverse_laplace_transform(s / ((s - 2) * (s - 3) * (s - 6)), s, t)
print(sol)
# print(latex(sol))

print('prob f')
sol = inverse_laplace_transform(1 / (s ** 2 + 1) * exp(-pi * s), s, t)
print(sol)
# print(latex(sol))
