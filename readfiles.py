
from asyncore import write
from re import M


f = open ("test.txt", "a")
f.write("\nthis is the new line added")
f.write("\nmake new line")
f.close()


file = open("test.txt", "r")
print (file.readable())

if file.readable() == True:
    for x in file:
        print (x)

else:
        print ("file not readable")
file.close()


ok = open("write.txt", "w")
ok.write("created with write command, /n this is added file")
ok.close()

kk = open("write.txt", "r")
print(kk.read())
kk.close()

import os 
if os.path.exists("import.py.txt"):
    os.remove("import.py")
else:
    print ("ok")
    
print ("file does not exist")


os.mkdir("Directory")

n1 = open("Directory/test.txt","w")
n1.write("this is test file in the new dir")
n1.close()

m1= open("Directory/test.txt","r")
print (m1.read())
m1.close()
