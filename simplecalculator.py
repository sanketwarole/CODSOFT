#Addition function
def addition(a,b):
    print("The addition is: ",(a+b))

#Subtraction function
def subtraction(a,b):
    print("The subtraction is: ",(a-b))

#Multiplication function
def multiplication(a,b):
    print("The multiplication is: ",(a*b))

#Division function
def division(a,b):
    print("The division is: ",(a/b))

#---------------Main Code--------------------
print("<<<<<<<<<<<<<<< SIMPLE CALCULATOR >>>>>>>>>>>>>>>>>\n")

a=int(input("Enter the 1st number: \n"))
b=int(input("Enter the 2nd number: \n"))

print("----Operations----------\n")
print("1->Addition\n")
print("2->Subtraction\n")
print("3->Multiplication\n")
print("4->Division\n")
print("5->Exit\n")




while True:
    choice=int(input("Enter the Choice:\n"))

    if(choice==1):
        addition(a,b)
    elif(choice==2):
        subtraction(a,b)
    elif(choice==3):
        multiplication(a,b)
    elif(choice==4):
        division(a,b)
    elif(choice==5):
        print("Exiting")
        break
    else:
        print("Invalid Choice")