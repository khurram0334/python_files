



def print_m_n (my_name):

    return f"my name is :  {my_name}"

def add(a,b):
    return a+b-2


print("Imported From :", __name__) # this will show in the main2.py

    # main and name condition is used when u don't want to get these code run into another program
    # and main progrma starts from here.    
if __name__ =="__main__":
    print (print_m_n("khurram"))
    print (add(2,2))

