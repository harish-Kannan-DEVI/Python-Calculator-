def menu () :
    menu_input = input("Select : \n \t 1.Caluclator \n \t 2.Area Calculator")
    if menu_input in ["1"]:
        print("You have selected Calculator......")
        print("Proceed..")
        Calculator()
    elif menu_input in ["2"]:
        print("You have selected Area Calculator.......")
        print("Proceed..")
        Area_Calculator()
    else:
        print("Byee...")
def Calculator () :
    num1 = int(input("Enter a number :"))
    num2 = int(input("Enter a second number :"))
    operation = input("Enter an operation :")
    if operation in ["+"]:
        print("Sum :",round(num1+num2,2))
    elif operation in ["-"]:
        print("difference :",round(num1-num2,2))
    elif operation in ["*","x"]:
        print("Product :",round(num1*num2,2))
    elif operation in ["/"]:
        if num2 != 0:
            print("Quotion :",round(num1/num2,2))
        else :
            print("Cant dividde with zero ")


menu()