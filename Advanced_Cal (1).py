import math
def menu () :
    menu_input = input("Select : \n \t 1.Calculator \n \t 2.Area Calculator \n \t 3.Perimeter Calculator")
    if menu_input in ["1"]:
        print("You have selected Calculator......")
        print("Proceed..")
        Calculator()
    elif menu_input in ["2"]:
        print("You have selected Area Calculator.......")
        print("Proceed..")
        Area_Calculator()
    elif menu_input in ["3"]:
        print("you have selected perimeter......")
        print("Proceed.....")
        Prerimeter_Calculator()
    else:
        print("Byee...")
def Calculator () :
    import math 
    num1 = int(input("Enter a number :"))
    num2 = int(input("Enter a second number :"))
    operation = input("Enter an operation : \n \t \t \t + -Addition \n \t \t \t - -Subtraction \n \t \t \t x -multiplication \n \t \t \t / -Division\n \t \t \t 5 -Square root\n \t \t \t 6 -Power")
    if operation in ["+","1"]:
        print("Sum :",round(num1+num2,2))
    elif operation in ["-","2"]:
        print("difference :",round(num1-num2,2))
    elif operation in ["*","x","3"]:
        print("Product :",round(num1*num2,2))
    elif operation in ["/","4"]:
        if num2 != 0:
            print("Quotient :",round(num1/num2,2))
        else :
            print("Cant dividde with zero ")
    elif operation in ["5"]:
        print("Square root : ",round(math.sqrt(num1)))
    elif operation in ["6"]:
        print("Exponent :",math.pow(num1,num2))
    else:
        print("Invalid operation .........")
    back_src()
def Area_Calculator () :
    operation=input("Enter a shape : \n \t 1.Triangle \n \t 2.Rectangle \n \t 3.Square \n \t 4.Circle")
    if operation in ["triangle","1"]:
        b=int(input("Enter Width :"))
        h=int(input("Enter height :"))
        print("Area of triangle :",0.5*b*h)
    elif operation in ["rectangle","2"]:
        l=int(input("Enter length :"))
        b=int(input("Enter Width :"))
        print("Area of rectangle :",l*b)
    elif operation in ["square","3"]:
        l=int(input("Enter length :"))
        print('Area of square :',l**2)
    elif operation in ["circle","4"]:
        r=int(input("Enter radius :"))
        print("Area of circle :",3.14*r**2)
    else :
        print("no shape is selected........")
    back_src()
def Prerimeter_Calculator() :
    operation=input("Enter a shape : \n \t 1.Triangle \n \t 2.Rectangle \n \t 3.Square \n \t 4.Circle")
    if operation in ["1","triangle"]:
        l=int(input("Enter length :"))
        b=int(input("Enter Width :"))
        h=int(input("Enter heigth :"))
        print("Perimeter : ",l+b+h)
    elif operation in ["2","rectangle"]:
        l=int(input("Enter length :"))
        b=int(input("Enter width : "))
        print("Perimeter :",2(l+b))
    elif operation in ["3","square"]:
        l=int(input("Enter length :"))
        print("Perimeter :",4*l)
    elif operation in ["4","circle"]:
        r=int(input("Enter radius :"))
        print("Perimeter :",2*3.14*r)
    else:
        print("no shape is selected ......")
    back_src()
def again () :
    again = input("Would you like to continue :")
    if again in ["y","yes"]:
        Calculator()
    else :
        print("byee....")
def again_1 () :
    again_1 = input("Would you like to continue ? ")
    if again_1 in ["y","yes"]:
        Area_Calculator()
    else:
        print("byee.....")                
def back_src () :
    back_src = input("")
    if back_src in ["/b","back"]:
        menu()
    elif back_src in ["/q","quit"]:
        quit ()
    else :
        again()
def quit () :
    print("bye.....")
    return
menu ()
