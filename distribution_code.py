# this is code of distribution setup
# Code Author: khurram shahzad
# date: 25 jan, 2022

from itertools import count
from os import getppid
import statistics
from typing import Counter


directors = ("khurram shahzad", " Malik Majid")  # directors touple

salemen = ["Atif", "Mahboob", "Amir", "Sajid", "Pervaiz"] # list of salemen

salary = [20000, 16000, 15000, 17500, 20000] # list of salary of salemen
salemen_dic = dict (zip(salemen, salary)) # two list converted into dic but look at zip
loader = ["waqas" , "Ali", "liaqat", "usman", "zafar", "jalil khan"]



salemen_dic ["waheed"] = 25000

# calculate total salemen salaries and give average of it
total = sum(salary)
print (" salemen total salaries are : " , total )
c = statistics.mean(salary) # use statistical method
print (" average salary level of salemen : " , c)

print ("salam")
    
