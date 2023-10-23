# Select the secret number from a given range.
# Player must guess the number.
# Compare guess to the secret number.
# What happens if the guess is wrong?
    # Tell them te guess is wrong.
    # Tell them the number of guesses left.
    # Tell them if too high/ too low.
# What happens if the guess us right?
    # Tell them the guess is correct.
    # Award a point.
# What happens if the player runs out of guesses?
    # Tell player round has been lost.
    # Award point to CPU.
# Check to see if player or CPU has >= 3 points, of so they win.

import random # Import the random module to our code.

# DECLARATIONS
secretNumber = -1
playerGuess = -1
playerScore = 0
cpuScore = 0
numGuesses = 0
playerName = ""
difficult = ""
rangeMin = -1
rangeMax = -1
numAttempts = -1

print("""
      *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
      |                                  |
      |         Guess a Number           |
      |        Kristopher Cooper         |
      |              2023                |
      *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
           """)

# CPU SECRET NUMBER GENERATION

# GAME LOOP
print("You need to guess a number from 0 to 30 and you have four gusses.\nIf you guess it right, you get a point.\nIf you can't guess it in four guesses, the CPU gets a point\n")
print("Easy max range 20 num attempts 5, Normal max range 25 num attempts 4, Hard max range 30 num attempts 3.")
difficult = input("Choose difficult\n")
# In your instructions, you typed Easy \ Normal \ Hard but the code you check for easy \ normal \ hard.
# Your code should match your instructions! 
if difficult == "easy":
    rangeMin = 0
    rangeMax = 20
    numAttempts = 5
elif difficult == "normal":
    rangeMin = 0
    rangeMax = 25
    numAttempts = 4
elif difficult == "hard":
    rangeMin = 0
    rangeMax = 30
    numAttempts = 3
else:
    # Add 'default values' for rangeMin, rangeMax, and numAttempts if player does not select difficulty correctly.
    # Without them, your code loops infinitely when difficulty is not typed correctly. 
    print("Wrong! Try again.")
# ADD CODE HERE TO CHANGE DIFFICULTY BETWEEN EACH MATCH.
# print() an explanation of your three difficulty levels.
# Use imput() to store difficulty in difficulty variable.
# assign values to numAttempts, rangeMin, rangeMax based on choice.

while playerScore != 3 and cpuScore != 3:
    #pass -- Tells Python to skip this block of code
    print(f"Player Score: {playerScore}\nCPU Score: {cpuScore}.\n")
    secretNumber = random.randint(rangeMin, rangeMax)
    #print(secretNumber)
    # ADD CODE HERE TO CHANGE DIFFICULTY BETWEEN EACH ROUND.
    numGuesses = 0
    for guessed in range(numAttempts):
        print(f"You have {numAttempts - numGuesses} guesses remaining.\n")
        playerGuess = int(input(f"Type a number from {rangeMin} to {rangeMax} and push ENTER.\n"))
        # input() saves all data as a STRING by default. 
        # int() will convert to a INTEGER
        # float() will convert to a FLOAT
        print(f"You have chosen {playerGuess}. Let's see if you're right!\n")
        if playerGuess == secretNumber:
            print("Whoa dude, what a guess! You got it!\n")
            playerScore += 1
            break # IMMEDIATELY EXIT ANY LOOP YOU ARE IN
        else:
            print("You did not guess correctly.\n")
            if playerGuess > secretNumber:
                print("Your guess is too high.\n")
            else:
                print("Your guess is too low.\n")
        numGuesses += 1
    if playerGuess != secretNumber:
        cpuScore += 1
        print("The CPU wins a point since you ran out of guesses.\n")

if playerScore >= 3:
    print("Winner, Winner, chicken dinner! You scored 3 points frist!\n")
else:
    print("Yo, you losy to a computer. You are a scrub.\n")