#quiz game in python
questions=(
    "Who is the most famous person in the whole world ? ",
    "What is the capital of Bangladesh ? ",
    "How many bones of the human body ? ",
    "What's the name of largest sea beach ?"
)
options=(("A. Hz Mohammad(sa) ","B. Dalton ","C. Newton ","D. Sumon "),
         ("A. dhaka ","B. faridpur ","C. khulna ","D. Panchagarh "),
         ("A. 222 ","B. 206 ","C. 205 ","D. 209 "),
         ("A. cox's bazar ","B. kuakata ","C. sant martin ","D. gonga "))
         
answers=("A","A","B","A")
guesses=[]
score=0
question_num=0
for question in questions:
    print("--------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Enter guess (A, B, C, D) : ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("Correct !")
    else:
        print("Incorrect !")
        print(f"{answers[question_num]} is the correct answer")



    
    question_num+=1
print("--------------------")
print("       Result       ")
print("--------------------")
print("answers:",end=" ")
for answer in answers:
    print(answer, end=" ")
print()
print("guesses:",end=" ")
for guess in guesses:
    print(guess, end=" ")
print()
score=int(score/len(questions)*100)
print(f"total score is {score}%")


