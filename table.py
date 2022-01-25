# This is table programe
# Code Author: Khurram Shahzad
# Date : 25 jan, 2022
# use of for and while loop

count1 = 2 # Table Counter

while count1 < 5:
    count1 = count1 +1 #starting table of 3 at start
    inner1 = 1 # mutlyplayer 1 to 10
    print ("-------------------")
    print ("table of :", count1)
    print ("-------------------")
    while inner1 < 11:  # another loop to count multiplayer value from 1 to 10
        res = count1 * inner1   # Actual table 
        print (count1, " *", inner1, " =", res)
        inner1 = inner1 + 1
print ("salam")