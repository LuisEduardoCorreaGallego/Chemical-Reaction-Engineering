#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: Example_2_2_Page_48
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
from matplotlib.patches import Rectangle

# Data
X = np.array([0.0, 0.1, 0.2, 0.4, 0.6, 0.7, 0.8])
Fao_rA = np.array([0.89, 1.08, 1.33, 2.05, 3.54, 5.06, 8.0])

# Plot
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.minorticks_on()
fig1.canvas.set_window_title('Example 2-2: Sizing a CSTR')
ax1.set_xlabel('$Conversion, \\ X$')
ax1.set_ylabel('$\\frac{F_{A0}}{-r_A} \\ \\left( m^3 \\right)$')
ax1.set_title('Levenspiel PFR plot\n'
              + '$V_{CSTR} =$' + '6400 $dm^3$')
ax1.plot(X, Fao_rA, marker='o')
ax1.grid(which='BOTH', ls=':')
ax1.grid(True)
ax1.add_patch(Rectangle(xy=(0.0, 0.0), width=0.8, height=8.0,
                        alpha=1, facecolor='moccasin',
                        fill=True, edgecolor='peru', hatch="/"))
plt.show()
