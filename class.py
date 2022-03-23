from ctypes import addressof
from email.headerregistry import Address


class Family:
    address = 'Sabowal Road-Gujrat'  # address would be shared by all objects,
                                        # Note  if we creat separate instacne with the name of address of aimun outside the class then it would be the instance of aimun not class
    #now we create mathod
    def detail(self):
        return f"Name of the daughter of Khurram is {self.name} and age is {self.age} and gender is {self.gender}"


# aimun is oject of the class family and age, gender are the instance of aimun.

aimun = Family()
areesha = Family()
aimun.name = "Aimun Khurram Shahzad"
aimun.age = 15
aimun.gender = 'femail'

print(aimun.__dict__)
print(aimun.detail())
