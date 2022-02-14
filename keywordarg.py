# what  are *args and **kwargs

def list_p (sec,*args, **kwargs):
    for i in args:
        print(i)
    for item, val in kwargs.items():
        print (item, val)
       
dr = ["dr israr", "farhat hasmi"]

# print(len(my_list))
normal = print ("i like these foods")
fruit = {"a":'apple',"b": "potato","c": "graps"}
list_p(normal,*dr, **fruit)

def arg_printer(a, b, *args):
    a= 100
    b = 200
    print(f'a is {a}')
    print(f'b is {b}')
    print(f'args are {args}')
c = (5,8,3)
arg_printer( *c)


print ("new prog/n")

import imp
import time
seconds = time.time()
print("Seconds since epoch =", ((((seconds/60)/60)/24)/365))

seconds = 1545925769.9618232
local_time = time.ctime(seconds)
print("Local time:", local_time)

t  = time.asctime()
print (t)


import csv
print(dir(csv))
