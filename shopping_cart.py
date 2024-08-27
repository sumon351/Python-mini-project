# create shopping cart in python
foods=[]
prices=[]
total=0
while True :
    food=input("Enter a food to by (q to quit) : ")
    if food.lower()=="q":
        break
    else :
        price=float(input(f"Enter price of a {food} $"))
        foods.append(food)
        prices.append(price)
print("----------your cart---------")
for food in foods:
    print(food,end=" ")
for price in prices:
    total+=price 
print()

print(f"Total amount of ${total:.2f}")   


