num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
oper = input("Choose operation (+,-,*,/): ").strip()

 
 #addition
if ( oper=="+" ):
    print(f"Result : {num1 + num2}")

elif ( oper=="-" ):
    print(f"Result : {num1 - num2}")

elif ( oper=="*" ):
    print(f"Multiplication : {num1*num2}")

elif ( oper=="/" ):
    if num2==0:
        print("Cannot divide by zero!")

    else:
        print(f"Division : {num1/num2}")

else:
    print("enter a valid operation")