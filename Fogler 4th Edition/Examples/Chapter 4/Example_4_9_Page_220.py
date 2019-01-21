#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: Example_4_9_Page_220
Description: 
Category:
Given Elements:
Requested Elements:
Author: Luis Eduardo Correa Gallego
Created on: 16/01/2019
Last modification: 
Used IDE: PyCharm Professional Edition
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def model(C, t, k=2.2, vo=0.05, Cbo=0.025, Vo=5, Cao=0.05):
    """

    :param C:
    :param t:
    :param k:
    :param vo:
    :param Cbo:
    :param Vo:
    :param Cao:
    :return:
    """
    Ca, Cb, Cc, Cd = C[0], C[1], C[2], C[3]
    rate = k * Ca * Cb
    V = Vo + vo * t
    X = (Cao*Vo-Ca*V)/(Cao*Vo)
    dCadt = -k*Ca*Cb-vo*Ca/V
    dCbdt = -k*Ca*Cb+vo*(Cbo-Cb)/V
    dCcdt = k*Ca*Cb-vo*Cc/V
    dCddt = k*Ca*Cb-vo*Cd/V
    return [dCadt, dCbdt, dCcdt, dCddt]


# initial condition
C0 = [0.05, 0.025, 0, 0]

# Volume points
t = np.linspace(0, 500, 500)

# Solve ODES
C = odeint(model, C0, t)

Ca, Cb, Cc, Cd = C[:, 0], C[:, 1], C[:, 2], C[:, 3]
rate = 2.2 * Ca * Cb

# Plot ODE solution
fig = plt.figure()
ax = fig.add_subplot(111)
fig.canvas.set_window_title('Example 4-8: Membrane Reactor ' +
                            '(Concentration-time trajectories)')
ax.minorticks_on()
ax.plot(t, Ca, 'black', linewidth=0.7, label='$C_A$')
ax.plot(t, Cb, 'k:', linewidth=1.1, label='$C_B$')
ax.plot(t, Cc, 'k', linewidth=1.3, label='$C_C$')
# ax.plot(t, Cd, 'black', linewidth=0.7, label='$C_D$')
ax.set_xlabel('$t \\ (s)$')
ax.set_ylabel('$C_i \\ \\left( \\frac{gmol}{dm^3} \\right)$')
ax.grid(which='BOTH', ls=':')
ax.grid(True)
fig.tight_layout()
ax.legend()

fig2 = plt.figure()
ax1 = fig2.add_subplot(111)
fig2.canvas.set_window_title('Example 4-8: Membrane Reactor ' +
                             '(Reaction-time trajectory)')
ax1.minorticks_on()
ax1.plot(t, rate, 'black', linewidth=0.7)
ax1.set_xlabel('$t \\ (s)$')
ax1.set_ylabel('$Reaction \\ Rate \\ \\left( ' +
               '\\frac{gmol}{s\\times dm^3} \\right)$')
ax1.grid(which='BOTH', ls=':')
ax1.grid(True)
fig2.tight_layout()

plt.show()
