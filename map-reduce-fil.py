

from contextlib import redirect_stderr
from functools import reduce
import imp


my_list = ["24", "12", "14", "3"]
# for i in range(len(my_list)):
#     my_list[i]= int(my_list[i])

# my_list [2] = my_list[2] + 4

# print (my_list[2])
    

    # we can use map function instead of above . map function apply function on any list/doc
a = list(map(int, my_list))
a [2] = a[2] + 2
print (a)

new = [2,4,6,8,10]

new_sq = list (map(lambda x: x*x, new))
print (new_sq)
even_n = list (map( lambda x:  x < 0,new_sq ))

print (even_n)

print ("@@@@@@@@@@@@@@@@@@@@")

def sq(a):
    return  a*a

def cub(a):
    return a*a*a

combine = [sq, cub]

for i in new:
    u_l = tuple(map( lambda x: x(i), combine))
    print (u_l)
    # with the help of lambda and map, we are applying lambda on both fucntion which is comibined
# map function return object

print ("____FILTER_____")

list_2 = [2,3,4,5,6,7,8,9]

greater_5 = list (filter(lambda x: x >5, list_2))
print (greater_5) 
# here catch is that x>5 return basicall bool value true false. but filert func gives actual value
# filer function return object
print ("______reduce______")
from functools import reduce

list3 = [5,5,5,5,5,5]
sum_a = reduce(lambda x,y: x+y, list3)
print (sum_a)

mul_a = reduce(lambda x,y: x*y, list3)
print (mul_a)
minus_a = reduce(lambda x,y: x-y, list3)
print (minus_a)
# reduce  function bassicaly reduce all in list