
# my_val = ("snake", "water", "gun")
# import random
# print (random.choices(my_val))

# print (my_val[0])
import random




def snake():
    result = random.choice(c_choice) #random function was used and value stored in to result for comuter value
    my_choice = "snake"
    print ("you selected = " + my_choice + " & computer selected = " + result)
    #first probability
    if my_choice == "snake" and result == "snake":
        final_result = "Draw"
        print (final_result)
        total.append(final_result)
        
    # seconded probability
    elif my_choice == "snake" and result == "water":
        final_result = "Won"
        print(final_result)
        total.append(final_result)
    #third probability
    elif my_choice == "snake" and result == "gun":
        final_result = "Lose"
        print(final_result)
        total.append(final_result)
    else: print ("invalid input-a")

def water(): # please refer to snake() function for same documentation
    result = random.choice(c_choice)
    
    my_choice = "water"
    print ("you selected = " + my_choice + " & computer selected = " + result)
    
    if my_choice == "water" and result == "water":
        
        final_result = "Draw"
        print (final_result)
        total.append(final_result)
                
    elif my_choice == "water" and result == "gun":
        final_result = "Won"
        print(final_result)
        total.append(final_result)
        
    elif my_choice == "water" and result == "snake":
        final_result = "Lose"
        print(final_result)
        total.append(final_result)
    else: print ("invalid input-b")


def gun():
    result = random.choice(c_choice)
  
    my_choice = "gun"
    print ("you selected = " + my_choice + " & computer selected = " + result)
    if my_choice == "gun" and result == "gun":
        final_result = "Draw"
        print (final_result)
        total.append(final_result)
        
    elif my_choice == "gun" and result == "snake":
        final_result = "Won"
        print(final_result)
        total.append(final_result)
    elif my_choice == "gun" and result == "water":
        final_result = "Lose"
        print(final_result)
        total.append(final_result)
    else: print("invalid input -c")

def my_game():
    ur_choice = int(input("Enter 1 for snake, 2 for water, 3 for gun : "))

    

    if ur_choice == 1:
        snake() #if u select snake then there are three probablaties
        
    elif ur_choice == 2:
        water()#if u select water then there are three probablaties
        
        
    elif ur_choice == 3:
        gun() #if u select gun then there are three probablaties
    else: print ("invalid input")

# Main program starts from here
total_tries = int(input("Number of Tries = ")) # asking numbr of tries to play
i = 0 # for while loop till number of tries
total = [] # to add all final results into empty list
c_choice = ["snake", "water", "gun"] #list of choices
 #while loop started
while i != total_tries:
    my_game() # main function to ask input from you and leading to further nested functions
    i = i +1 



d = total.count("Draw")
w = total.count("Won")
l = total.count("Lose")

print ("You Won for " , w, " times.")
print ("You losed for " , l, " times.")
print ("Game draw for " , d , " times.")

