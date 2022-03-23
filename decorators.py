#what are decoratros, with decoratros we can integrate different functions into one function or


def city (func):
    def street ():
        print ("Maghi Road")
        func()
        print ("address")
 
    return street()
@city  # it is actuallay sum() = func()
def sum():

    print(2+2)
@city #it is actuallay  mul() = func()
def mul():
    print (3*2)

@city # it is catually vill() = func()
def vill():
    print ("Chattal")

