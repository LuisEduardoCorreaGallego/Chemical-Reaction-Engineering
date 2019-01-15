#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: Example_2_3_SizingAPFR
Description: 
Category:
Given Elements:
Requested Elements:
Author: Luis Eduardo Correa Gallego
Created on: 7/01/2019
Last modification: 
Used IDE: PyCharm Professional Edition
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

# Data
X = np.array([0.0, 0.1, 0.2, 0.4, 0.6, 0.7, 0.8])
Fao_rA = np.array([0.89, 1.08, 1.33, 2.05, 3.54, 5.06, 8.0])

# Calculations for areas under curve
# Using composite Simpson's rule
area = simps(y=Fao_rA, x=X, dx=0.00001)

# Delimiter for shaded area
y0 = np.zeros(len(Fao_rA))

# Calculating volume with conversion data
V = []
for i in range(1, len(X) + 1):
    V_i = simps(x=X[:i], y=Fao_rA[:i], dx=0.00001)
    V.append(round(V_i, 4) * 1000)

# Calculation for -rA
Fao = 0.4  # gmol/s
rA = Fao / Fao_rA

# Plots
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.minorticks_on()
fig1.canvas.set_window_title('Example 2-3: Sizing a PFR, point a')
ax1.set_xlabel('$Conversion, \\ X$')
ax1.set_ylabel('$\\frac{F_{A0}}{-r_A} \\ \\left( m^3 \\right)$')
ax1.set_title('Levenspiel PFR plot\n'
              + '$V_{PFR} =$' + str(round(area, 4) * 1000) + ' $dm^3$')
ax1.plot(X, Fao_rA, marker='o')
ax1.fill_between(X, y0, Fao_rA, where=Fao_rA > y0,
                 facecolor='royalblue', alpha=0.7)
ax1.grid(which='BOTH', ls=':')
ax1.grid(True)

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.minorticks_on()
fig2.canvas.set_window_title('Example 2-3: Sizing a PFR, point b, part 1')
ax2.set_ylabel('$Conversion, \\ X$')
ax2.set_xlabel('$V \\ \\left( dm^3 \\right)$')
ax2.set_title('Conversion profile')
ax2.plot(V, X, 'r', marker='o')
ax2.grid(which='BOTH', ls=':')
ax2.grid(True)

fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
ax3.minorticks_on()
fig3.canvas.set_window_title('Example 3-3: Sizing a PFR, point b, part 2')
ax3.set_ylabel('$-r_A \\ \\left( \\frac{mol}{m^3 \\times s} \\right)$')
ax3.set_xlabel('$V \\ \\left( dm^3 \\right)$')
ax3.set_title('Reaction rate profile')
ax3.plot(V, rA, 'black', marker='o')
ax3.grid(which='BOTH', ls=':')
ax3.grid(True)

plt.show()
