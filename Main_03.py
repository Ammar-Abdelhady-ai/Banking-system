from User_01 import User
from Bank_02 import Bank




def Main():
    global Name, Age, Gender, password, id
    
    # validation Name
    while True:
        
        print("Inter zero '0' to exit from system in any place ! ")

        Name = input("Please inter your Name : ")
        if Name == "0":
            exit()

        try:
            if len(Name) <=22:
                
                break
            else:
                print("Greater than 25 characters, Try again")
        except :
            print("Greater than 22 characters, Try again")


    #Validation Age
    while True:
        try:
            Age = int( input("Please inter your Age : "))
            if Age == 0:
                exit()
        except Exception as error_1:
            print(error_1)
        else:
            
            break
    
    #validation Gender
    while True:
        try:
            num = int(input("Please inter your Gender \n choise one '1' to Male \n choise two '2' to female : "))
            if num == 0:
                exit()

            if num == 1:
                Gender = "Male"
                
                break
            if num == 2 :
                Gender = "Female"
                
                break
            else :
                print("please inter 'One : 1' or 'Two : 1' ")
        except Exception as error_2:
            print(error_2)

    #validation of Password
    while True:
        password = input("Add your Own Password here : ")
        if password == 0:
            exit()

        try:
            if len(password) >= 8:
                break
            else:
                print("Smaller than 8 characters, Try again")
        except Exception as error_3:
            print(error_3)
    
    # validation of ID
    while True:
        try:
            id = int(input("Add your Own ID account here : "))
            if id == 0:
                exit()
        except Exception as error_4:
            print(error_4)

        else:
            break

        print("account created successfuly! \n")

Main()
User_1 = Bank(Name, Age, Gender)

while True:
    Password = input("inter your passwoed to Complete : ")
    if Password == password:   
        print("Inter 1 to show all details account")
        print("Inter 2 to show account balance")
        print("Inter 3 to withdraw")
        print("Inter 4 to deposit")
        print("Inter 5 If you want to Signout (not exit) then sign in with another account information .")
        print("Inter 0 to exit from the system")
        

        
        n = int(input("inter your choice : "))

        if n == 1:
            User_1.show_user_details() 
            print("\n")

        if n == 2:
            User_1.view_balance()
            print("\n") 

        if n == 3:
            s = int(input("Enter the amount to be withdrawn from the balance : "))
            User_1.withdraw(s)
            print("\n") 

        if n == 4:
            e = int(input("Enter the amount to be added to the balance : "))
            User_1.deposits(e)
            print("\n")

        if n == 5:
            Main()
        if n == 0:
            exit()

    if Password == "0":
        exit()

    else:
        print("inter your password agine or inter zero '0' to exit !")