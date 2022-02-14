
# Touples
my_t = ("khurram","shahzad", 1977, 2005)
print (my_t [-3]) # printing specific value in touple
print(len(my_t)) #printing length of touple
# strings
name = "khurram_shahzad"
print (name [:]) #printing complete length of string
print (type (my_t)) #printing the type of objec
#list
my_l = ["khurram", "shahzad", 1977, 255, "gujrat"]
print (len(my_l))

#dictionaries (Key:valuse)
my_dic = {"Father": ("Khurram_Shahzad", 2005, "feb", "gujrat"), 
"Daughter" : ("Areesha_sahzad", 2007, "march", "gujrat")} # touple can also be added  as values
my_dic ["Mother"] = "Kanwal Shahzad" # type key and get value of key
my_dic ["Father"] = "Khurram Shahzad"
print (my_dic["Daughter"])
print (my_dic.keys()) # to get only keys
my_dic ["Grand Father"] = "Manzoor Hussain" 
print (my_dic)
my_dic.pop("Mother") # to remove any key,value from dictionary

print (my_dic)


# For loop
my_list = []

for i in range (4,8):
    my_list.append(i) # for adding value in list  
    
print (my_list)

# List Comprehension 
n_list = [i for i in range (4,8)]
print (n_list, "\n____________")


# Python 3: List comprehensions
fruits = ['Banana', 'Apple', 'Lime']
loud_fruits = [fruit.upper() for fruit in fruits]
print(loud_fruits)


# List and the enumerate function , it gives number to values in list
print (list(enumerate(fruits)))
print (type(fruits))

my_h = ["cricket", "reading", "joggint"]
n_list = [i.upper() for i in my_h] # to convert initial list into upper case
print (n_list)


list(enumerate(my_h))
print (my_h)

results = {n: n ** 2 for n in range(10)} # to make list that multiply with 2
print (results)

my_dd = {j : j+3 for j in range (10)} # to make list that added 3 in each jth value
print (my_dd.values())


a = [2, 4, 8, 10]

for i in a:
    if i/2 == 1:
        print ('ok')
    else:
        break

# list comprehension

a_list = [i for i in a if i/2 ==1 ]
print (a_list)
print (list(range(1,10,2))) # to print list with interval of 2.