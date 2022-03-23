#Topic= List comprehension



karachi = ["imran khan", "babar azam", "farhad", "rizwan"]

num_a = [ len(n) for n in karachi ]
print (num_a)
lahore = ["misbah", "Noor", "dhani", "mustafa", "Afridi"]
print (zip(karachi,lahore))
com_list = [ i.upper() for i in karachi+lahore if i.startswith("m") ]
print (com_list)

my_dic = {key:value for key ,value in zip(karachi  ,lahore)}
print (my_dic)
# n_dic = { value: key for key,value in zip (karachi,lahore)}
# print (n_dic)







# squares = [n for n in range (1,11) if n % 5 == 0]
# print (squares)

# remin5 = [n%5 for n in range (1,20) ]
# set_n = set(remin5)

# print (set_n)


s_list = [("atif", 20000), ("kamran", 15000), ("jamshid", 20000),("waqas", 25000)]
sal = [salmen for (salmen, salary) in s_list if salary >= 15000]
sal_d = [salary for (salmen, salary) in s_list if salary >= 15000]
print (sal, sal_d)

print (type(s_list))
for r in s_list:
    for c in r:
        print (c)

# vet = {2, 4, 5}
# sq = {n**2 for n in vet}
# print (sq)

# set1 = {2,4,8}
# set2 = {10,12,24}

# set3 = {(i,j) for i in set1  for j in set2}
# print (set3)
# n_list = list(set3)
# print (n_list[2])

# pair = [(num,letter) for num in range (1,6) for letter in "abcdef"]
# print (pair)

alnafi= "The Propotius"
print (alnafi [0:2])


