#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: Example_2_1_Page_42
Description: 
Category:
Given Elements:
Requested Elements:
Author: Luis Eduardo Correa Gallego
Created on: 13/01/2019
Last modification: 
Used IDE: PyCharm Professional Edition
"""


# Function definition
def Cao(yAo, Po, To, R=8.314):
    """
    Concentration for a ideal gas
    :param yAo: gas composition
    :param Po: initial pressure
    :param To: initial temperature
    :param R: universal constant, dm3*kPa / (gmol*K)
    :return: concentration
    """
    return yAo*Po / (R*To)


# Calculations for concentration and molar flow
Po = 830  # kPa == 8.2 atm
yAo = 1.0  # pure A
To = 500  # K, initial temperature
C_A0 = Cao(yAo=yAo, Po=Po, To=To)
print('C_A0 =', round(C_A0, 4), 'gmol/dm3')
F_A0 = C_A0 * 2
print('F_A0 =', round(F_A0, 4), 'gmol/s')
