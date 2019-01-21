#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: Example_4_4_Page_183
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

P0 = 10  # atm
v0 = 104.4 / 0.413  # lbm/(h*ft3)
betha0 = 164.1 / (144 * 14.7)  # atm/ft
z_table = numpy.arange(0.0, 70.0, 10)  # ft
P_table = P0 * (1 - 2*betha0*z_table/P0) ** 0.5  # atm
v_table = v0 * P0 / P_table

# Table E4-4.1
print("_" * 33)
print('P AND v PROFILES'.center(33))
print("_" * 33)
print(" {:10} {:10} {:10} ".format("z (ft)", "P (atm)", "v (ft³/h)"))
print("_" * 33)
for i in range(len(z_table)):
    print(" {:10} {:10} {:10} ".format(round(z_table[i], 2),
                                       round(P_table[i], 2),
                                       round(v_table[i], 2)))
print("¯" * 33)

z = numpy.arange(0.0, 60.0, 0.1)  # ft
P = P0 * (1 - 2*betha0*z/P0) ** 0.5  # atm
v = v0 * P0 / P

# plot results
fig, ax = plt.subplots()
fig.canvas.set_window_title('Example 4-4: Calculating Pressure Drop in a' +
                            'Packed Bed (P profile)')
ax.minorticks_on()
ax.plot(z, P, 'k', linewidth=1.1)
ax.set_xlabel('$z(ft)$')
ax.set_ylabel('$P \\ \\left( atm \\right)$')
ax.grid(which='BOTH', ls=':')
ax.grid(True)

fig1, ax1 = plt.subplots()
fig1.canvas.set_window_title('Example 4-4: Calculating Pressure Drop in a' +
                             'Packed Bed (v profile)')
ax1.minorticks_on()
ax1.plot(z, v, 'k', linewidth=1.1)
ax1.set_xlabel('$z(ft)$')
ax1.set_ylabel('$v \\ \\left( \\frac{ft^3}{h} \\right)$')
ax1.grid(which='BOTH', ls=':')
ax1.grid(True)

fig.tight_layout()
plt.show()
