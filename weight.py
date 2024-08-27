# weight converter in python
weight=float(input("enter your weight : "))
unit=input("enter kilograms or pounds (K or L) : ")
if unit=="K".lower():
    weight = weight * 2.205
    unit = "Lbs"
    print(f"your weight is : {weight}{unit}")
elif unit=="L".lower():
    weight = weight/2.205
    unit = "Kgs"
    print(f"Your weight is : {weight}{unit}")
else : 
    print(f"{unit} is a invalid unit ")