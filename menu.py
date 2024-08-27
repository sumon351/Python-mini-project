# concession stand program
menu={
    "apple":3.35,
    "mango":2.22,
    "pizza":99.2,
    "burger":12.2,
    "pineapple":23.3,
    "banana":2.33

}
cart=[]
total=0
print("----------------------------")
for key , value in menu.items():
    print(f"{key:10}:{value:.2f}")
while True:
    food=input("select an item (q to quit) : ")
    if food.lower()=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("--------your order------")
for food in cart:
    print(food,end=" ")
    total+=menu.get(food)
print("")
print(f"Total cost is : ${total}")


