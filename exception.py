
try:
    a = int(input("Enter First Number: "))
    
    b = int(input("Enter Seconed Numeber: "))
    
    print ("Resulted Values is :","\n",round(a/b,2)) # round() is used to handle 
    #decimal values
  
    
except ValueError:
    print("Invalid Values")
except NameError:
    print ("some thin wrong in the code")
except ZeroDivisionError:
    print ("You can not divide by zero")
except SyntaxError:
    print ("There is problem in syntax....")

except Exception as e:
    print ("Unknown Error", e)

finally:
    print ("Code Completed")





