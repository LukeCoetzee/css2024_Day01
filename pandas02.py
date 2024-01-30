# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:05:20 2024

@author: LCoetzee

Exercise
"""

import pandas

file = pandas.read_csv("insurance_data.csv", skiprows=5)

print(file)

print(file.info())

print(file.describe())