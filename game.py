# rock, paper, scissors game in python
import random
options=("rock","paper","scissors")
running=True
while running:
    player=None
    computer=random.choice(options)

    while player not in options:
        player=input("Enter a choice (rock,paper or scissors) : ")
    print(f"player   : {player}")
    print(f"computer : {computer}")
    if player==computer:
        print("Its a tie !")
    elif player=="rock" and computer=="paper":
        print("You won the game !")
    elif player=="paper" and computer=="rock":
        print("You won the game !")
    elif player=="scissors" and computer=="paper":
        print("You won the game !")
    else:
        print("You lose the game !")
    play_again=input("Play again ? (y/n) : ").lower()
    if play_again=="y":
        running
    elif play_again=="n":
        break
print("THANKS FOR PLAYING THE GAME DEAR NAZMUL HAQUE")
print("*********************************************")
