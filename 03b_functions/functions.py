import random
# FUNCTION -- a named piece of code that can be reused easily.
# FUNCTION SIGNATURE -- Syntax for creating a new function
def exampleFunctionA(): # NO PARAMETERS
    count = 0
    num = int(input("How many time do you want to wish a happy birthday?\n"))
    while count < num:
        print("Happy Birthday!\n")
        conut += 1

def exampleFunctionB(num, count): # PARAMETERS
    while count < num:
        print("Happy Birthday!\n")
        count += 1

# IF A FUNCTION REQUIRES PARAMETERS, YOUR CODE WILL CRASH WITHOUT THEM!

# RUNNING A FUNCTION IS KNOW AS CALLING THE FUNCTION
# exampleFunctionA()
# exampleFunctionB(5, 0)

def rollDice(numDice, sizeDice):
    numRolled = 0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        sum += roll
        print(f"Roll: {roll}\n")
        print(f"sum: {sum}\n")
        numRolled += 1

rollDice(4, 8)
# rollDice(1, 90)

strenthPlayer = rollDice(4, 8)
dexterityPlayer = rollDice(4, 8)
wisdomPlayer = rollDice(4, 8)

print(strenthPlayer)
print(dexterityPlayer)
print(wisdomPlayer)