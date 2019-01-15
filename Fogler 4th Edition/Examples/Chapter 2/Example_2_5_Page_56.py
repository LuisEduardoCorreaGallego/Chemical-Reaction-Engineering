#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: Example_2_5_Page_56
Description: 
Category:
Given Elements:
Requested Elements:
Author: Luis Eduardo Correa Gallego
Created on: 13/01/2019
Last modification: 
Used IDE: PyCharm Professional Edition
"""
import numpy
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Data
X = numpy.array([0.0, 0.1, 0.2, 0.4, 0.6, 0.7, 0.8])
Fao_rA = numpy.array([0.89, 1.09, 1.33, 2.05, 3.54, 5.06, 8.0])

# Plot
fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.minorticks_on()
fig1.canvas.set_window_title('Example 2-5: Comparing Volumes ' +
                             'for CSTRs in Series')
ax.set_xlabel('$Conversion, \\ X$')
ax.set_ylabel('$\\frac{F_{A0}}{-r_A} \\ \\left( m^3 \\right)$')
ax.plot(X, Fao_rA, 'k')
ax.grid(which='BOTH', ls=':')
ax.grid(True)
ax.add_patch(Rectangle(xy=(0.0, 0.0), width=0.4, height=2.05,
                       alpha=1, facecolor='lavender',
                       fill=True, edgecolor='blue', hatch="/"))
ax.add_patch(Rectangle(xy=(0.4, 0.0), width=0.4, height=8.0,
                       alpha=1, facecolor='moccasin',
                       fill=True, edgecolor='red', hatch="/"))
# Volume calculations
V_CSTR1 = 820.0
V_CSTR2 = 3200.0
textstr = '$V_{CSTR, 1}$ = ' + str(V_CSTR1) + '$\\ dm^3$\n' +\
          '$V_{CSTR, 2}$ = ' + str(V_CSTR2) + '$\\ dm^3$'
position = (0.15, 0.94)
props = dict(boxstyle='round', facecolor='lavender', alpha=1)
ax.text(position[0], position[1], textstr,
        transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)
plt.show()
