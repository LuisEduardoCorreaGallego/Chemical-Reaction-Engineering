#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: Example_3_5_Page_115
Description: 
Category:
Given Elements:
Requested Elements:
Author: Luis Eduardo Correa Gallego
Created on: 15/01/2019
Last modification: 
Used IDE: PyCharm Professional Edition
"""
import matplotlib.pyplot as plt
import numpy

# Data
epsilon = 0.28 * (1 - 1 - 1/2)
C_SO2_0 = 0.28 * 1495 / (8.314 * 500)
thetaB = 0.72 * 0.21 / 0.28
thetaI = 0.72 * 0.70 / 0.28
X = numpy.arange(0.0, 1.0, 0.01)
C_SO2 = C_SO2_0 * (1 - X)/(1 + epsilon*X)
C_O2 = C_SO2_0 * (thetaB - 0.5*X) / (1 + epsilon*X)
C_SO3 = C_SO2_0 * X / (1 + epsilon*X)
C_N2 = C_SO2_0 * thetaI / (1 + epsilon*X)

# Plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.minorticks_on()
fig.canvas.set_window_title('Example 3-5: Determining C_j = h_j(X) ' +
                            'for a Gas-Phase Reaction')
ax.set_xlabel('$Conversion, \\ X$')
ax.set_ylabel('$Concentration \\ \\left( \\frac{gmol}{dm^3} \\right)$')
ax.set_xlim(left=0.0, right=1.0)
concentrationsLabel = ('$C_{SO_2}$', '$C_{O_2}$', '$C_{SO_3}$', '$C_{N_2}$')
concentrationsData = (C_SO2, C_O2, C_SO3, C_N2)
for i in range(len(concentrationsLabel)):
    ax.plot(X, concentrationsData[i], label=concentrationsLabel[i])
ax.grid(which='BOTH', ls=':')
ax.grid(True)
ax.legend()
plt.show()
