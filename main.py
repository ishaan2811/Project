print("             MINI CALCULATOR")
num1=float(input("Enter 1st number "))
num2=float(input("Enter 2nd number "))

print("press 1 for addition\n"
      "press 2 for subtraction\n"
      "press 3 for multiplication\n"
      "press 4 for division")
choice = int(input("Enter your choice from 1-4"))
if(choice==1):
    a=num1+num2
    print(a)
elif(choice==2):
    a=num1-num2
    print(a)
elif(choice==3):
    a=num1*num2
    print(a)
elif(choice==4):
    a=num1/num2
    print(a)
else:
    print("Invalid Input")