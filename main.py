import pandas as pd
import os
import sys

master_filename = sys.argv[1]

present_filename = sys.argv[2]

name_data = pd.read_excel(os.path.join(master_filename), engine='openpyxl', usecols='A').values.tolist()
# print(name_data)

present_names = pd.read_excel(os.path.join(present_filename), engine='openpyxl', usecols='A').values.tolist()
# print(present_names)

master = name_data
# print(master)
persons = present_names
# print(persons)

for name in master:
    if name not in persons:
        print(name)