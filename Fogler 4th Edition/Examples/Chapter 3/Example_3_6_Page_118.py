#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: Example_3_6_Page_118
Description: 
Category:
Given Elements:
Requested Elements:
Author: Luis Eduardo Correa Gallego
Created on: 14/01/2019
Last modification: 
Used IDE: PyCharm Professional Edition
"""
import numpy
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


# Part a
def equations(variables):
    """
    Set of non-linear equations
    :param variables: parameters
    :return: set of equations
    """
    Xeb, Xef = variables
    Kc = 0.1
    Cao = 0.07174
    eps = 1
    return Xeb - (Kc * (1 - Xeb) / (4 * Cao)) ** 0.5, Xef - (
                Kc * (1 - Xef) * (1 + eps * Xef) / (4 * Cao)) ** 0.5


K_c = 0.1
C_A0 = 0.07174
epsilon = 1
initialGuess = numpy.array([0.5, 0.5])

X_eb, X_ef = fsolve(equations, initialGuess)

print('\tXeb = ', X_eb)
print('\t\tf(Xeb) = ', X_eb - (K_c * (1 - X_eb) / (4 * C_A0)) ** 0.5)
print('\tXef = ', X_ef)
print('\t\tf(Xef) = ',
      X_ef - (K_c * (1 - X_ef) * (1 + epsilon * X_ef) / (4 * C_A0)) ** 0.5)

# Part c
X = numpy.arange(0.0, 0.5, 0.01)
rA = 0.0036 * ((1 - X)/(1 + X) - ((2.88*X**2)/((1 + X)**2)))

fig = plt.figure()
ax = fig.add_subplot(111)
fig.canvas.set_window_title('Example 3-6: Calculating the ' +
                            'Equilibrium Conversion')
ax.minorticks_on()
ax.plot(X, 1/rA, 'black', linewidth=1)
ax.vlines(x=0.5, ymin=-11000, ymax=15000, color='red')
ax.set_xlabel('Conversion, X')
ax.set_ylabel('$-r_A \\ \\left( \\frac{dm^3 \\times min}{gmol} \\right)$')
ax.grid(which='BOTH', ls=':')
ax.grid(True)
ax.set_ylim(bottom=0, top=10000)
plt.show()

# Part d
X = 0.4
rA = 0.0036 * ((1 - X)/(1 + X) - ((2.88*X**2)/((1 + X)**2)))
Fao = 3  # gmol/min
V_CSTR = round(Fao*X/rA, 2)
print('\n\tV_CSTR = ', V_CSTR, ' dm3')
