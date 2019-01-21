#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: Example_4_1_Page_152
Description: 
Category:
Given Elements:
Requested Elements:
Author: Luis Eduardo Correa Gallego
Created on: 16/01/2019
Last modification: 
Used IDE: PyCharm Professional Edition
"""
import matplotlib.pyplot as plt
import numpy

# Data
time = numpy.array([0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 10.0])  # min
C_C = numpy.array([0.000, 0.145, 0.270, 0.376, 0.467,
                   0.610, 0.715, 0.848, 0.957])  # kgmol/m3
C_A0 = 1  # kgmol/m3
y = numpy.log((C_A0 - C_C) / C_A0)
f = numpy.polyfit(time, y, 1)

# Plot
fig = plt.figure()
ax = fig.add_subplot(111)
fig.canvas.set_window_title('Example 4-1: Determining k from Batch Data')
ax.minorticks_on()
ax.plot(time, y, 'black', linewidth=0.7, marker='o')
ax.set_xlabel('$t \\ (min)$')
ax.set_ylabel('$ln \\left( \\frac{C_{A0} - C_C}{C_{A0}} \\right)$')
ax.grid(which='BOTH', ls=':')
ax.grid(True)
# Kinetic data
k = round(-1 * f[0], 4)  # min^{-1}
textString = '$k$ = ' + str(k) + '$\\ min^{-1}$'
position = (0.05, 0.45)
props = dict(boxstyle='round', facecolor='beige', alpha=1)
ax.text(position[0], position[1], textString,
        transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)
rateLaw = '$-r_A = $' + str(k) + '$min^{-1} \\ C_A$'
ax.text(position[0], 0.70 * position[1], rateLaw,
        transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)
fig.tight_layout()
plt.show()
