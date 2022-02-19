

list = ["mango", "banana", "potato", "chilli", "garlic"]
i = 1
for item in list:
    if i%2 != 0:
        print (item)
    i = i +1

# above code will return even item

# same code can be wirtten with the help of enuerator function
# enumerate function can retur indes value as well
list = ["atif", "amjad", "ali", "waqas", "noor"]

for index, item in enumerate( list):
    if index%2==0:
        print (index,item)
        print(type(index))
        # print (len(index))