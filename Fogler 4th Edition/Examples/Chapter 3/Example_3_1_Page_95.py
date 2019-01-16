#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: Example_3_1_Page_95
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

# Data
T = numpy.array([313.0, 319.0, 323.0, 328.0, 333.0])
k = numpy.array([0.00043, 0.00103, 0.00180, 0.00355, 0.00717])
inv_T = 1 / T
lnk = numpy.log(k)

# Linear regression
straightLine = numpy.polyfit(inv_T, lnk, 1)
normalLine = numpy.polyval(straightLine, inv_T)

# Semilog plot
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.minorticks_on()
fig1.canvas.set_window_title('Example 3-1: Determination of ' +
                             'the Activation Energy, semilog plot')
ax1.set_xlabel('$\\frac{1}{T}, \\ (K^{-1})$')
ax1.set_ylabel('$k \\ {s^{-1}}$')
ax1.plot(inv_T, k, marker='o', linewidth=0)
ax1.plot(inv_T, numpy.exp(normalLine), 'r', linewidth=1)
ax1.set_yscale('log')
ax1.grid(which='BOTH', ls=':')
ax1.grid(True)
# Kinetic parameters
E_A = round(-8.314 * straightLine[0] / 1000, 2)
A = round(numpy.exp(straightLine[1]), 2)
ax1.text(0.00308, 0.005,
         '$k  \\ = ' + str(A) +
         '\\times e^{\\frac{' +
         str(round(straightLine[1], 4)) + '}{T}}$',
         {'color': 'red', 'fontsize': 12})
plt.xticks(rotation='horizontal', fontsize=7)

# Normal plot
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.minorticks_on()
fig2.canvas.set_window_title('Example 3-1: Determination of ' +
                             'the Activation Energy, normal plot')
ax2.set_xlabel('$\\frac{1}{T}, \\ (K^{-1})$')
ax2.set_ylabel('$ln(k)$')
ax2.plot(inv_T, lnk, marker='o', linewidth=0)
ax2.plot(inv_T, normalLine, 'r', linewidth=0.7)
ax2.grid(which='BOTH', ls=':')
ax2.grid(True)
ax2.text(0.00308, -5.5,
         '$ln(k) \\ = \\ \\frac{' +
         str(round(straightLine[0], 4)) +
         '1}{T} + ' +
         str(round(straightLine[1], 4)) +
         '$',
         {'color': 'red', 'fontsize': 12})
textString = '$E_A$ = ' + str(E_A) + '$\\ \\frac{kJ}{gmol}$' +\
             '\nA = ' + str(A) + '$\\ s^{-1}$'
position = (0.08, 0.25)
props = dict(boxstyle='round', facecolor='lavender', alpha=1)
ax2.text(position[0], position[1], textString,
         transform=ax2.transAxes, fontsize=10,
         verticalalignment='top', bbox=props)
plt.xticks(rotation='horizontal', fontsize=7)
plt.show()
