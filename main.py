import pandas as pd
import os
import sys
import xlsxwriter
import colorama
from colorama import Fore, Back, Style

colorama.init()

master_filename = sys.argv[1]

present_filename = sys.argv[2]

name_data = pd.read_excel(os.path.join(master_filename), engine='openpyxl', usecols='A').values.tolist()
# print(name_data)

present_names = pd.read_excel(os.path.join(present_filename), engine='openpyxl', usecols='A').values.tolist()

master = name_data

persons = present_names

def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele     
    return str1  

for name in master:
    if name not in persons:
        strname = listToString(name)
        print(f" {Back.BLACK + Fore.GREEN + strname}")


