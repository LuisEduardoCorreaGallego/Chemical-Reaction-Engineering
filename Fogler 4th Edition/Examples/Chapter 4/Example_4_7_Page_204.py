#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: Fogler_Page206
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
    Model for a microreator
    :param F: Flows (A, B, C)
    :param V: Volume (dm3)
    :return: ODE system
    """
    Fa, Fb, Fc = F[0], F[1], F[2]
    T = 698
    Cto = 1641/8.314/T
    E = 24000
    Ft = Fa + Fb + Fc
    Ca = Cto * Fa / Ft
    k = 0.29*np.exp(E/1.987*(1/500-1/T))
    Fao = 0.0000226
    vo = Fao / Cto
    Tau = V/vo
    ra = -k*Ca**2
    X = 1-Fa/Fao
    rb = -ra
    rc = -ra/2
    rateA = -ra
    dFadV = ra
    dFbdV = rb
    dFcdV = rc
    return [dFadV, dFbdV, dFcdV]


# Initial condition for the flows
F0 = [0.0000226, 0, 0]

# Volume points
V = np.linspace(0, 1e-5, 100)

# Solve ODES
F = odeint(model, F0, V)

Fa = F[:, 0]
Fao = 0.0000226
X = 1 - Fa / Fao
Fb = F[:,  1]
Fc = F[:, 2]

# Plot ODE solution
fig = plt.figure()
ax = fig.add_subplot(111)
fig.canvas.set_window_title('Example 4-7: Gas-Phase Reaction in a Microreator' +
                            '- Molar Flow Rates')
ax.minorticks_on()
ax.plot(V, Fa * 1e6, 'r', linewidth=0.9, label='Fa')
ax.plot(V, Fb * 1e6, 'b', linewidth=0.9, label='Fb')
ax.plot(V, Fc * 1e6, 'g', linewidth=0.9, label='Fc')
ax.set_xlabel('$Volume \\ (dm^3)$')
ax.set_ylabel('$F_i \\ \\left( \\frac{\\mu mol}{s} \\right)$')
ax.grid(which='BOTH', ls=':')
ax.grid(True)
ax.legend(['Fa(t)', 'Fb(t)', 'Fc(t)'])
plt.show()
