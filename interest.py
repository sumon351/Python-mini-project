# compound interest program in python
principle=0
rate=0
time=0
while principle <= 0:
    principle=float(input("Enter your principle amount : "))
    if principle <= 0:
        print("Principle cannot less than or equal zero ")
while rate <= 0:
    rate=float(input("enter your rate : "))
    if rate <= 0:
        print("rate cannot less than or equal zero ")
while time <=0:
    time=float(input("enter time : "))
    if time <=0 :
        print("Time cannot be less than or equal zero ")
final_amount=principle*(1 + rate/100)**time
print(f"your total balance is : {final_amount:.3f} in {time} year/s")
