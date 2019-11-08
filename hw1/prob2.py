#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random
import copyright

a = 2
b = 1
n = 20
x = np.linspace(0, 1, n)
noise = (random.rand(n) - 0.5)
y = a * x + b + noise

plt.plot(x, y, 'bo')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression with Noise')
plt.text(0.2, 1, copyright.copyright)

# xi sum
xi_sum = np.sum(x)
# xi^2 sum
xixi_sum = np.sum(x ** 2)
# yi sum
yi_sum = np.sum(y)
# xi * yi sum
xiyi_sum = np.sum(x * y)

delta = np.linalg.det([[xixi_sum, xi_sum], [xi_sum, n]])
solve_a = np.linalg.det([[xiyi_sum, xi_sum], [yi_sum, n]]) / delta
solve_b = np.linalg.det([[xixi_sum, xiyi_sum], [xi_sum, yi_sum]]) / delta

print('a = {}, b = {}'.format(solve_a, solve_b))
plt.text(0.4, 1.2, 'a = {}'.format(solve_a))
plt.text(0.4, 1.4, 'b = {}'.format(solve_b))
plt.plot([0, 1], [solve_a * 0 + solve_b, solve_a * 1 + solve_b])
plt.show()


