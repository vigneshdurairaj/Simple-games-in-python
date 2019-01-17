import time
import random
#Getting Name of the Player
name = input("Tell us your Name?")
print("Hello---->"  "  " + name, "  ""<----Time to play HANGMAN!!")
print("-----------------------------\n --<Rules>--\n 1. You will be given a clue to guess the word. \n 2. You have 10 chances to guess.\n----------------------------")
time.sleep(1)
print("Start Guessing.....")
time.sleep(0.5)
#Word of the Game
words = ["google","github","facebook","twitter"]
wordt = random.choice(words)
word = wordt
print("-----<your>--<CLUE>------")
if wordt == "google":
    print("It is Initially called as Backrub")
elif wordt == "github":
    print("Gives Life for team Developement")
elif wordt == "facebook":
    print("Most used book")
elif wordt == "twitter":
    print("This Chippers")
print("-----------------------------")
time.sleep(2)

guess = ' '
#Initializing Number of Turns
turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in guess:
            print(char, end = " ")
        else:
            print("_", end =" ")
            failed +=1
    if failed == 0:
        print("You Won")
        print("-----<WINNER WINNER CHICKEN DINNER>------")
        break

    guesse = input("Guess the Character-->")
    guess += guesse

    if guesse not in word:
        turns -= 1

        print  ("Wrong")
        print("You Have", +turns,'more guess')

        if turns == 0:
            print("You loose")
            print("-----<BETTER LUCK NEXT TIME>------")






