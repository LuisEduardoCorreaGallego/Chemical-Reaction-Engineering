#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: Example_4_3_Page_171
Description: 
Category:
Given Elements:
Requested Elements:
Author: Luis Eduardo Correa Gallego
Created on: 18/01/2019
Last modification: 
Used IDE: PyCharm Professional Edition
"""
import numpy
import matplotlib.pyplot as plt

CA0 = 1 * 6 / (0.73 * 1980)  # lbmol/ft3
FA0 = 0.34 / 0.8
eps = 1
k = 0.072 * numpy.exp(82000 * (1100 - 1000)/(1.987*1000*1100))
X = numpy.linspace(0, 0.8, 500)
V = (FA0 / (k*CA0)) * ((1+eps)*numpy.log(1/(1-X))-eps*X)  # ft3
z = V / (0.0205*100)  # ft
C_A = CA0 * (1-X) / (1 + eps*X)
C_C = CA0 * X / (1 + eps*X)

# plot results
fig, ax = plt.subplots()
fig.canvas.set_window_title('Example 4-3: Producing 300 Million Pounds per ' +
                            'Year of Ethylene in a Plug-Flow Reactor: ' +
                            'Design of a Full-Scale Tubular Reactor')
ax.minorticks_on()
ax.plot(z, C_A, 'k', linewidth=1.1, label='$C_A$')
ax.plot(z, C_C, 'k-', linewidth=0.6, label='$C_C, C_B$')
ax.set_xlabel('$Distance\\ down\\ the\\ reactor\\ z(ft)$')
ax.set_ylabel('$Concentration \\ \\left( \\frac{lbmol}{ft^3} \\right)$')
ax.legend(loc='lower center', ncol=2)
ax.grid(which='BOTH', ls=':')
ax.grid(True)

ax1 = ax.twinx()
ax1.minorticks_on()
ax1.plot(z, X, 'k:', linewidth=1.5, label='$X$')
ax1.set_ylabel('$Conversion$')
ax1.legend(loc='upper center')

fig.tight_layout()

plt.show()
