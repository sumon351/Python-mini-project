# basic calculator in python
operator=input("Enter an operator (+ - * /) : ")
num1=float(input("enter 1st number : "))
num2=float(input("enter 2nd number : "))
if operator=="+":
    result=num1+num2
    print(result)
elif operator=="-":
    result=num1-num2
    print(result)
elif operator=="*":
    result=num1*num2
    print(result)
elif operator=="/":
    result=num1/num2
    print(result)
else :
    print(f"{operator} is a invalid operator")
    print("Please enter right operator")