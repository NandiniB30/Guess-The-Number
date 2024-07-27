"""
Instrutions - Have the user select a range.
Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses.
If user guesses higher than the actual number, the system will show "Try Again! You guessed too high".
If user guesses lower than the actual number, the system will show "Try Again! You guessed too small".
If the user guessed in a 7 number of guesses, the user gets a “Congratulations!” Output.
If the user didn’t guess the integer in the 7 number of guesses, user will get “Better Luck Next Time!” output.
"""

import random

while True:
    # fetch upper range
    uppRange = int(input("Enter the upper range:"))

    # fetch lower range
    lowRange = int(input("Enter the lower range:"))

    # generate a random number between the range of 1 and 100
    randNum = random.randint(lowRange, uppRange)

    print("You've got 7 chances to guess the number!")

    # Initialize number of guesses
    guessNo = 1
    isNumFound = False
    while guessNo <= 7:
        userGuess = int(input("Guess the number:"))
        if userGuess == randNum:
            print("Congratulations!You guessed the number correctly in", guessNo, "try")
            isNumFound = True
            break;
        elif userGuess > randNum:
            print("Try Again! You guessed too high.")
        else:
            print("Try Again! You guessed too small.")
        guessNo += 1

    if not isNumFound:
        print("Better Luck Next Time!")
    print("------GAME OVER--------")

    response = input("Do you want to restart ? Y or N:")
    if not (response == "Y" or response == "y"):
        break
