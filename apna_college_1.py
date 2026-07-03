#MINI PROJECTS 
#1. GUESS THE NUMBER
import random
target=random.randint(1,100)

while True:
    userchoice=input("Guess the target or Quit:")
    if (userchoice=="Quit"):
        break
    userchoice=int(userchoice)
    if (userchoice==target):
        print("success:Correct Guess!!")
        break
    elif(userchoice<target):
        print("Your number is small, take a bigger guess..")
    else:
        print("Your number is bigger, take a smaller guess..")

print("--------GAME OVER----------")