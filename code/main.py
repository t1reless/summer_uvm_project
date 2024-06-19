import csv
import pandas 
new_strings = 1
df = pandas.read_csv("negative.csv", index_col=False, header=0)
for column in df: 
    if new_strings == 1:
        present_column = df[column]
        print(present_column)
        print(type(present_column[:0]))
        new_strings += 1
    else: 
        break