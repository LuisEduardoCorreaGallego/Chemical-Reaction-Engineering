#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: Example_3_4_Page_114
Description: 
Category:
Given Elements:
Requested Elements:
Author: Luis Eduardo Correa Gallego
Created on: 15/01/2019
Last modification: 
Used IDE: PyCharm Professional Edition
"""
import sympy

a = sympy.var('a')
b = sympy.var('b')
C_A = sympy.var('C_A')
C_A0 = sympy.var('C_A0')
C_B = sympy.var('C_B')
epsilon = sympy.var('epsilon')
F_A0 = sympy.var('F_A0')
F_B = sympy.var('F_B')
P = sympy.var('P')
P_0 = sympy.var('P_0')
T = sympy.var('T')
T_0 = sympy.var('T_0')
thetaB = sympy.var('thetaB')
v = sympy.var('v')
v_0 = sympy.var('v_0')
X = sympy.var('X')

C_B = F_B / v
F_B = F_A0 * (thetaB - (b/a)*X)
v = v_0 * (1 + epsilon*X) * (P_0 / P) * (T / T_0)
C_A0 = F_A0 / v_0
C_B = F_A0 * (thetaB - (b/a)*X) / v

sympy.pprint(C_B)
