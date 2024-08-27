# temperature conversion in python
temp=float(input("Enter the temperature : "))
unit=input("Is temperature celcius or fahrenheit ? (C or F) : ")
if unit=="C".lower():
    Fahrenheit=temp*9/5 + 32
    print(f"the temperature of Fahrenheit is {Fahrenheit:.2f} degree Fahrenheit")
elif unit=="F".lower():
    Celcius=(temp-32)*5/9
    print(f"The temperature of Celcius is {Celcius:.2f} degree Celcius")
else :
    print(f"{unit} is not a valid unit")
    print("please enter the valid unit")