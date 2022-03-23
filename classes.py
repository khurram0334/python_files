class Cleint: # creating class and start class name with capital as it is class naming convention
    def __init__(self, name, address, package, bill): #__init__ is constructer used to pass values in Client Class
        self.name = name   # these are the instance refered to object outside class.
        self.address =address
        self.package = package
        self.bill=bill

    #Following is the method created inside the class
    def c_p_detail(self):
        return f'''Name of the Cleint is {self.name}. Address is {self.address}. Package selected is {self.package} Mbps
        .Monthly bill is Rs : {self.bill}'''

zubair = Cleint('Zubair', 'Dhako Road', 10, 1600 )


print (zubair.c_p_detail())


class Car: #we created class with tha name of car
    
    def __init__(self,make, varient, model, color): # we created constructer 
        self.make = make
        self.varient = varient
        self.model = model
        self.color = color
        
    def price(self): #we created method inside the class
        if self.varient == 'city':
            price_city = 2000000
            return f'Price of the {self.make}- {self.varient}- {self.model}- {self.color} is :', price_city
            
        else:
            return "Error"
             
honda = Car('Honda', 'city', 2022, 'black') #object that belongs to car class

print (honda.price())
print (honda.__dict__)