#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: Fogler_Page214
Description: 
Category:
Given Elements:
Requested Elements:
Author: Luis Eduardo Correa Gallego
Created on: 4/01/2019
Last modification: 
Used IDE: PyCharm Professional Edition
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def model(F, V):
    """
    Model for a membrane reactor
    :param F: Flows (A, B, C)
    :param V: Volume of reactor (dm3)
    :return: ODE system
    """
    Fa, Fb, Fc = F[0], F[1], F[2]
    kc = 0.2
    Cto = 0.2
    Ft = Fa + Fb + Fc
    k = 0.7
    Kc = 0.05
    ra = -k*Cto*((Fa/Ft)-Cto/Kc*(Fb/Ft)*(Fc/Ft))
    dFadV = ra
    dFbdV = -ra-kc*Cto*Fb/Ft
    dFcdV = -ra
    return [dFadV, dFbdV, dFcdV]


# initial condition
F0 = [10, 0, 0]

# Volume points
V = np.linspace(0, 500, 500)

# Solve ODES
F = odeint(model, F0, V)

Fa = F[:, 0]
Fb = F[:, 1]
Fc = F[:, 2]
print('Fa final = ', Fa[-1])

# Plot ODE solution
fig = plt.figure()
ax = fig.add_subplot(111)
fig.canvas.set_window_title('Example 4-8: Membrane Reactor')
ax.minorticks_on()
ax.plot(V, Fa, 'black', linewidth=0.7, label='Fa')
ax.plot(V, Fb, ':', linewidth=0.9, label='Fb')
ax.plot(V, Fc, 'black', linewidth=1.3, label='Fc')
ax.set_xlabel('$Volume \\ (dm^3)$')
ax.set_ylabel('$F_i \\ \\left( \\frac{\\mu mol}{s} \\right)$')
ax.grid(which='BOTH', ls=':')
ax.grid(True)
ax.legend(['Fa(t)', 'Fb(t)', 'Fc(t)'])
plt.show()
