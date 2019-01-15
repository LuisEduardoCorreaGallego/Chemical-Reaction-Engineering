#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: Example_2_4_Page_53
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
from matplotlib.patches import Rectangle
from scipy.integrate import simps

# Data
X = numpy.array([0.0, 0.1, 0.2, 0.4, 0.6, 0.7, 0.8])
Fao_rA = numpy.array([0.89, 1.08, 1.33, 2.05, 3.54, 5.06, 8.0])

# Delimiter for shaded area
y0 = numpy.zeros(len(Fao_rA))
y1 = 8.0 * numpy.ones(len(Fao_rA))

# Plot
fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.minorticks_on()
fig1.canvas.set_window_title('Example 2-4: Comparing CSTR and PFR Sizes')
ax.set_xlabel('$Conversion, \\ X$')
ax.set_ylabel('$\\frac{F_{A0}}{-r_A} \\ \\left( m^3 \\right)$')
ax.plot(X, Fao_rA, 'k', linewidth=1.3)
ax.grid(which='BOTH', ls=':')
ax.grid(True)
ax.fill_between(X, y1, Fao_rA, where=y1 > X,
                facecolor='gainsboro', edgecolor='red', alpha=1, hatch='\\')
ax.fill_between(X, y0, Fao_rA, where=Fao_rA > y0,
                facecolor='khaki', edgecolor='magenta', alpha=1, hatch='/')

# Volume calculations
V_PFR = round(simps(x=X, y=Fao_rA, dx=0.00001) * 1000.0, 2)  # dm3
V_CSTR = round(0.8 * 8 * 1000, 2)  # dm3
textstr = '$V_{CSTR}$ = ' + str(V_CSTR) + '$\\ dm^3$\n' +\
          '$V_{PFR}$   = ' + str(V_PFR) + '$\\ dm^3$\n' +\
          'Difference between CSTR and PFR = ' + str(V_CSTR - V_PFR) +\
          '$\\ dm^3$'
position = (0.1, 0.84)
props = dict(boxstyle='round', facecolor='beige', alpha=1)
ax.text(position[0], position[1], textstr,
        transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)
plt.show()
