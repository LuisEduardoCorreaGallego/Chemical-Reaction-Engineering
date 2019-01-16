#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: Example_3_2_Page_105
Description: 
Category:
Given Elements:
Requested Elements:
Author: Luis Eduardo Correa Gallego
Created on: 15/01/2019
Last modification: 
Used IDE: PyCharm Professional Edition
"""
import numpy

C_A0 = 10  # gmol/dm3
C_B0 = 2  # gmol/dm3
thetaB = C_B0 / C_A0
conversions = numpy.array([20, 90]) / 100.0
C_D = C_A0 * conversions / 3
C_B = C_A0 * (thetaB - conversions / 3)
print('For 20% conversion of NaOH:')
print('\tC_D = ', round(C_D[0], 2), ' gmol/dm3')
print('\tC_B = ', round(C_B[0], 2), ' gmol/dm3')
print('For 90% conversion of NaOH:')
print('\tC_D = ', round(C_D[1], 2), ' gmol/dm3')
print('\tC_B = ', round(C_B[1], 2), ' gmol/dm3')
