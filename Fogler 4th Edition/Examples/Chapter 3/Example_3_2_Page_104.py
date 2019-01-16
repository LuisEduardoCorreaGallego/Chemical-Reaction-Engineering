#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: Example_3_2_Page_104
Description: 
Category:
Given Elements:
Requested Elements:
Author: Luis Eduardo Correa Gallego
Created on: 15/01/2019
Last modification: 
Used IDE: PyCharm Professional Edition
"""

reaction = {'A': ('NaOH', '-1'), 'B': ('(C₁₇H₃₅COO)₃C₃H₅', '-⅓'),
            'C': ('C₁₇H₃₅COONa', '+1'), 'D': ('C₃H₅(OH)₃', '+⅓'),
            'I': ('H₂O', '+0')}
symbols = tuple(reaction.keys())
initially = ['N_' + symbols[i] + '0' for i in range(len(symbols))]
initially[-1] = 'N_I0'
initiallyNA = 'N_A0'
symbols_and_coeff = tuple(reaction.values())
species = [symbols_and_coeff[i][0] for i in range(len(symbols))]
coefficients = [symbols_and_coeff[i][1] for i in range(len(symbols))]
change = [coefficients[i] + ' ' + initiallyNA + ' X' for i in range(len(coefficients))]
change[-1] = '-'
remaining = [initiallyNA + '(Θ_' + symbols[i] + coefficients[i] + 'X)' for i in range(len(symbols))]
remaining[-1] = 'N_I0'
initiallyCA = 'C_A0'
concentration = [initiallyCA + '(Θ_' + symbols[i] + coefficients[i] + 'X)' for i in range(len(symbols))]
concentration[-1] = 'C_I0'

# Stoichiometric table
print("_" * 121)
print('STOICHIOMETRIC TABLE FOR LIQUID-PHASE SOAP REACTION'.center(121))
print("_" * 121)
print(" {:19} {:19} {:19} {:19} {:19} {:19} ".format("Species", "Symbol", "Initially", "Change", "Remaining", "Concentration"))
print("_" * 121)
for i in range(len(species)):
    print(" {:19} {:19} {:19} {:19} {:19} {:19} ".format(species[i], symbols[i], initially[i], change[i], remaining[i], concentration[i]))
print("¯" * 121)
