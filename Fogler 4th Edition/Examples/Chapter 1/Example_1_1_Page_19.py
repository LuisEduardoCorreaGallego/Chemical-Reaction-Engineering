#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: Example_1_1_Page_19
Description: 
Category:
Given Elements:
Requested Elements:
Author: Luis Eduardo Correa Gallego
Created on: 19/01/2019
Last modification: 
Used IDE: PyCharm Professional Edition
"""
import numpy

vo = 10  # dm3/min
k = 0.23  # min^-1
V = round((vo/k) * numpy.log(1 / 0.1), 4)
print('V = ', V, ' dm3')
print('V = ', V / 1000, ' m3')
