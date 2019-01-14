#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: Fogler_Page355
Description: 
FAtegory:
Given Elements:
Requested Elements:
Author: Luis Eduardo Correa Gallego
Created on: 4/01/2019
Last modification: 
Used IDE: PyCharm Professional Edition
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def model(F, V):
    """
    Model for NH3 oxidation in a PFR
    :param F: Flows (A, B, C, D, E, F)
    :param V: Volume of PFR (dm3)
    :return: ODE system
    """
    FA, FB, FC, FD, FE, FF = F[0], F[1], F[2], F[3], F[4], F[5]
    Ft = FA + FB + FC + FD + FE + FF
    r1A = -5 * 8 * (FA / Ft) * (FB / Ft) ** 2
    r2A = -2 * 4 * (FA / Ft) * (FB / Ft)
    r4C = -5 * 3.175 * (FC / Ft) * (FA / Ft) ** (2 / 3)
    r3B = -10 * 8 * (FC / Ft) ** 2 * (FB / Ft)
    CA = 2 * FA / Ft
    rA = r1A + r2A + 2 * r4C / 3
    rB = 1.25 * r1A + 0.75 * r2A + r3B
    rC = -r1A + 2 * r3B + r4C
    rD = -1.5 * r1A - 1.5 * r2A - r4C
    rE = -0.5 * r2A - 5 * r4C / 6
    rF = -2 * r3B
    dFAdV, dFBdV, dFCdV, dFDdV, dFEdV, dFFdV = rA, rB, rC, rD, rE, rF
    return [dFAdV, dFBdV, dFCdV, dFDdV, dFEdV, dFFdV]


# Flow units
flowUnits = 'gmol/min'
volumeUnits = 'dm^3'
components = 'A', 'B', 'C', 'D', 'E', 'F'

# initial condition
F0 = [10, 10, 0, 0, 0, 0]

# Volume points
finalVolume = 10.0  # dm3
V = np.linspace(0, finalVolume, 333)

# Solve ODES
F = odeint(model, F0, V)

# Printing final values
print('Final flows:')
for i in range(len(components)):
    print('\t F' + components[i] + ' =', F[-1][i], flowUnits)

print('Final total flow')
finalFt = F[-1][0] + F[-1][1] + F[-1][2] + F[-1][3] + F[-1][4] + F[-1][5]
print('\t Ft =', finalFt, flowUnits)

print('Final reaction rates')
finalFA, finalFB, finalFC = F[-1][0], F[-1][1], F[-1][2]
finalFD, finalFE, finalFF = F[-1][3], F[-1][4], F[-1][5]
r1A = -5 * 8 * (finalFA / finalFt) * (finalFB / finalFt) ** 2
r2A = -2 * 4 * (finalFA / finalFt) * (finalFB / finalFt)
r4C = -5 * 3.175 * (finalFC / finalFt) * (finalFA / finalFt) ** (2 / 3)
r3B = -10 * 8 * (finalFC / finalFt) ** 2 * (finalFB / finalFt)
CA = 2 * finalFA / finalFt
final_rA = r1A + r2A + 2 * r4C / 3
final_rB = 1.25 * r1A + 0.75 * r2A + r3B
final_rC = -r1A + 2 * r3B + r4C
final_rD = -1.5 * r1A - 1.5 * r2A - r4C
final_rE = -0.5 * r2A - 5 * r4C / 6
final_rF = -2 * r3B
reactionRates = ('rA', 'rB', 'rC', 'rD', 'rE', 'rF')
r_s = (final_rA, final_rB, final_rC, final_rD, final_rE, final_rF)
for i in range(len(reactionRates)):
    print('\t ' + reactionRates[i] + ' =', r_s[i])

# Plot ODE solution
fig = plt.figure()
ax = fig.add_subplot(111)
fig.canvas.set_window_title('Example 6-10: Calculating Concentrations as' +
                            'Functions of Position for NH3 Oxidation in a PFR')
ax.minorticks_on()
for j in range(len(components)):
    ax.plot(V, F[:, j], linewidth=1.1, label='$F_' + components[j] + '$')
ax.set_xlabel('$Volume \\ (dm^3)$')
ax.set_ylabel('$F_j \\ \\left( \\frac{gmol}{min} \\right)$')
ax.grid(which='BOTH', ls=':')
ax.grid(True)
ax.legend()
plt.show()
