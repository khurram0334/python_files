
# Client Name: Khurram, Kanwal, Aimun
# Code By : Khurram Shahzad
# Project Name: Health Management System


# define function to get time
def getdate():
    import datetime
    return datetime.datetime.now()

# define function to get data for exercise log and diet Log
def client_exer(c_data):

    if c_data == "khurram":
        type = str(input("Press e for exercise and d for Diet"))
        if type == "e":
            with open("khurram_e.txt", "a") as de:
                value = str(input())
                de.write(str([str(getdate())]) + ":::" + value)
                de.write("\n")
            print("Suceessfully written")

        elif type == "d":
            with open("khurram_d.txt", "a") as pe:
                value = str(input())
                pe.write(str([str(getdate())]) + ":::" + value)
                pe.write("\n")
            print("Successfully written")

        else:
            print("Wrong Input")

    if c_data == "kanwal":
        type = str(input("Press e for exercise and d for Diet"))
        if type == "e":
            with open("kanwal_e.txt", "a") as de:
                value = str(input())
                de.write(str([str(getdate())]) + ":::" + value)
                de.write("\n")
            print("Suceessfully written")

        elif type == "d":
            with open("kanwal_d.txt", "a") as pe:
                value = str(input())
                pe.write(str([str(getdate())]) + ":::" + value)
                pe.write("\n")
            print("Successfully written")

        else:
            print("Invalid Value")

    if c_data == "aimun":
        type = str(input("Press e for exercise and d for Diet"))
        if type == "e":
            with open("aimun_e.txt", "a") as de:
                value = str(input())
                de.write(str([str(getdate())]) + ":::" + value)
                de.write("\n")
            print("Suceessfully written")

        elif type == "d":
            with open("aimun_d.txt", "a") as pe:
                value = str(input())
                pe.write(str([str(getdate())]) + ":::" + value)
                pe.write("\n")
            print("Successfully written")

        else:
            print("Invalid Value")
# define function for retreival of clint data

def data_ret (r_data):
    if r_data == "khurram":
        with open("khurram_d.txt") as kr:
            for i in kr:
                print (i, end="")
        with open("khurram_e.txt") as kr:
            for i in kr:
                print (i, end="")
     
    elif r_data== "kanwal":
        with open("kanwal_e.txt") as kn:
            for i in kn:
                print (i, "\n")
        with open("kanwal_d.txt") as kn:
            for i in kn:
                print (i, "\n")
    elif r_data== "aimun":
        with open("aimun_e.txt") as am:
            for i in am:
                print (i, "\n")
        with open("aimun_d.txt") as am:
            for i in am:
                print (i, "\n")
    else: print ("Invalid Value")

        
# Main Code Starts from here Step 1
track = int(input("Press 1 for Entery and 2 for Retreival"))

# Condotion One
if track == 1: 
    c_one, c_two, c_three = "khurram", "kanwal", "aimun"
    c_list = [c_one, c_two, c_three]
    print("\n" "Select Name of Client to add Data \n", "\n", c_list, "\n")
    c_data = str(input("Enter Client Name: \n"))
    if c_data == "khurram":
        client_exer("khurram")
    elif c_data == "kanwal":
        client_exer("kanwal")
    elif c_data == "aimun":
        client_exer("aimun")
    else: print("invalid value")

    
# condition Two
elif track == 2:
    c_one, c_two, c_three = "khurram", "kanwal", "aimun"
    c_list = [c_one, c_two, c_three]
    print ("Select Name of Cleint to retreive data \n" , c_list, "\n")
    r_data = str(input("Enter Name of Clint: \n"))
    if r_data == "khurram":
        data_ret ("khurram")
    elif r_data == "kanwal":
        data_ret (r_data = "kanwal")
    elif r_data == "aimun":
        data_ret ("aimun")
    else: print ("Invalid Input")

