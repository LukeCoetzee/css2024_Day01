# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:22 2024

@author: BBarsch

Purpose: Storing data in Python
1. Lists
2. Dictionaries
3. Data Frames
"""

import pandas
#import pandas as pd (shorthand)

file = pandas.read_csv("country_data.csv")

print(file)

"""
    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
"""

age1 = 30
age2 = 25
age3 = 29

age = [30,25,29,46,22]

print(age)

"""
[30, 25, 29, 46, 22]
"""

print(age[0])

print(max(age))
print(sum(age))
print(len(age))

average = sum(age) / len(age)

print(average)

g1 = "M"
g2 = "F"
g3 = "M"

gender = ["M", "F", "F"]

print(age[0:2]) # value/index "2", second "argument", is excluded
"""
[30, 25]

prints only two values, and not three
"""

age.append(100)

print(age)

"""
[30, 25, 29, 46, 22, 100]
"""

"""
Question: How to insert a value at index 0

age.insert(0,31)

"""

"""
Dictionaries - key:value pairs

cat: "a cute animal"

"""

mammals = {"cat":"a cute animal", "lion":"king of the jungle","elephant":"a gigantic herbivore"}

print(mammals["cat"])

"""
Data frames
"""

fruits = ["apple", "banana", "orange", "grape", "kiwi"]
size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

#dictionary
fruit_sizes = {
    'fruits': fruits,
    'sizes': size_nm
    }

"""
df = dataframe
"""
df = pandas.DataFrame(fruit_sizes)

print(df['fruits'])

print(df['sizes'])

print(df['sizes'].min())

print(df['sizes'].max())

print(df['sizes'].mean())

print(df.describe())

print(df[df['sizes'] > 10])

print("\n")

print(df[1:3])

"""
ADDING A NEW COLUMN
"""

prices = [10.00, 12.50, 16.00, 23.00, 7.00]

df['prices'] = prices

"""
REMOVING A COLUMN
"""

df.drop(columns=["sizes"], inplace=True)






