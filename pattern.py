

from re import M


rows = int(input("Enter Number of rows to be printed : "))
logo = "*"
design = int(input("Enter (1) for straight printing and (0) for revese printing : " ))
m = 1
if design == True:
    while m <= rows:
        print (logo * m)
        m = m +1

elif design == False:
    n = (rows)
    while m <= rows:
        print (logo * n)
        m = m + 1
        n = n -1



        

