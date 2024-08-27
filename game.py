import random
lowest_num=1
highest_num=10
answer=random.randint(lowest_num,highest_num)

guesses=0
print("Number guessing game in python ")
print(f"select a number between {lowest_num} and {highest_num}")
while True :
    guess=input("enter guess the number : ")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess < lowest_num or guess > highest_num :
            print("The number is out of range ")
            print(f"please select a number between {lowest_num} and {highest_num}")
        elif guess < answer :
            print("too low ! try again ")
        elif guess > answer:
            print("too high ! try again")
        else:
            print(f"Correct ! . The number was {answer}")
            print(f"The number was guesses {guesses}")
    else:
        print("invalid guess")
        print(f"please select a number between {lowest_num} and {highest_num}")
    
        
    