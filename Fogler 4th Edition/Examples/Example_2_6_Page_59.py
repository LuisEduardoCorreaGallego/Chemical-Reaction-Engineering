#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: Example_2_6_Page_59
Description: 
Category:
Given Elements:
Requested Elements:
Author: Luis Eduardo Correa Gallego
Created on: 14/01/2019
Last modification: 
Used IDE: PyCharm Professional Edition
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

X = np.array([0.0, 0.1, 0.2, 0.4, 0.6, 0.7, 0.8])
Fao_rA = np.array([0.89, 1.08, 1.33, 2.05, 3.54, 5.06, 8.0])

# Calculations for areas under curve
# Using composite Simpson's rule
area = simps(y=Fao_rA, x=X, dx=0.00001)

# Delimiter for shaded area
y0 = np.zeros(len(Fao_rA))

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.minorticks_on()
fig1.canvas.set_window_title('Example 2-6: Sizing Plug-Flow Reactors in Series')
ax1.set_xlabel('$Conversion, \\ X$')
ax1.set_ylabel('$\\frac{F_{A0}}{-r_A} \\ \\left( m^3 \\right)$')
ax1.plot(X, Fao_rA, marker='o')
ax1.fill_between(X[:4], y0[:4], Fao_rA[:4], where=Fao_rA[:4] > y0[:4],
                 facecolor='gray', edgecolor='red', alpha=1, hatch='/')
ax1.fill_between(X[3:], y0[3:], Fao_rA[3:], where=Fao_rA[3:] > y0[3:],
                 facecolor='peru', edgecolor='royalblue', alpha=1, hatch='/')
ax1.grid(which='BOTH', ls=':')
ax1.grid(True)

V_PFR1 = round(simps(x=X[:4], y=Fao_rA[:4], dx=0.00001) * 1000.0, 2)
V_PFR2 = round(simps(x=X[3:], y=Fao_rA[3:], dx=0.00001) * 1000.0, 2)
textstr = '$V_{PFR, 1}$ = ' + str(V_PFR1) + '$\\ dm^3$\n' +\
          '$V_{PFR, 2}$ = ' + str(V_PFR2) + '$\\ dm^3$'
position = (0.15, 0.94)
props = dict(boxstyle='round', facecolor='lavender', alpha=1)
ax1.text(position[0], position[1], textstr,
         transform=ax1.transAxes, fontsize=10,
         verticalalignment='top', bbox=props)

plt.show()
