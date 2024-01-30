# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:13:01 2024

@author: 23676469
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)

print(file.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Age      11 non-null     int64 
 1   Gender   11 non-null     object
 2   Country  11 non-null     object
dtypes: int64(1), object(2)
memory usage: 396.0+ bytes
None
"""

print(file.describe())

"""
             Age
count  11.000000
mean   33.363636
std     9.233339
min    22.000000
25%    27.000000
50%    30.000000
75%    39.500000
max    49.000000
"""