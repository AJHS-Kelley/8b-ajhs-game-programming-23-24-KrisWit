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
exampleFunctionA()
exampleFunctionB(5, 0)