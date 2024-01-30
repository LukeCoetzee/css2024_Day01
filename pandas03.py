# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:07:52 2024

@author: LCoetzee

Exercise
"""

import pandas

# NOTE: Delimiter change possible using sep (in case of text files)
# file = pandas.read_csv("data.csv", sep=";")

file = pandas.read_csv("housing_data.csv")

print(file)

print(file.info())

print(file.describe())

"""
Problem: Dirty data, no column names
"""
column_names = ["A", "B", "C",...]

file = pandas.read_csv("housing_data.csv", names = column_names)

print(file)

print(file.info())

print(file.describe())