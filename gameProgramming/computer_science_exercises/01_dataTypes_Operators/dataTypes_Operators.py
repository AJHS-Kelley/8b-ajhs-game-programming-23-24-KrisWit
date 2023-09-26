# Data Types and Operators, Kristopher Cooper, v0.5

# Variable Rules
# CANNOT START WITH A NUMBER!!!!!!!!!!!!
# CANNOT USE BULIT-IN KEYWORDS AS VARIABLES.
# VARIABLES NAME SHOULD DESCRIBE THE DATA BEING STORED.
# snake_case variables use _ to separate words, all lower case.
# Camelcase variables do not use spaces, 1st word lower, rest upper.

# String Literal Examples
playerName = "Chad Gamerson"
emptyString = ""
spaceString = " "
weapon = "sword"

# Integer Data Types
health = 100
extralife = 5
temperature = -17
speed = 50

# Floating Point Data Types
pi = 3.1215678
laptime = 3.5
velocity = -2.0
brakes = 5.0

# Boolean Data Types
isFireTyp = False
weaponequipped = True
pvpEnabled = False
Damaged = False

# Arithmetic Operators
# PEMDAS APPLIES JUST LIKE IN MATH CLASS!
print(4 + 5) # Addition
print(5 - 50) # Subtraction
print(10 * 11) # Multiplicatiom
print(100 / 15) # Division
print(30 ** 2) # Expomemts
print(150 % 20) # Modulus -- Divides, then returns remainder, most commonly used to deternine even/odd

# Comparison Operators
# Evalute the expression then return True or Flase
print(5 > 3) # Greater Than
print(7 >= -1) # Greater Than or Equal to
print(-1 < -2) # Less Than
print(0 <= 0) # Less Than or Equal to
print(5 == 3) # Is Equal to
print(-99 != 99) # Not Equal to

# Assignment Operators
myVariable = "myValue" # Assign variable on left the value on the right, throw out any current value
myOtherVariable = (10 + 5)

# Addition assignment -- Add the value on the right, keep any current value
myWallet= 0
myWallet += 1
myWallet += 5
print(myWallet)

# Same Effect
x = 0
x += 10
x = x + 10

# Logical Operators
print(3 > 5 and 4 < 3) # AND requires ALL Epression to be True
print(3 > 2 and 4< 3)
print(3 > 2 and 4 != 3)
print(3 > 2 and 4 != 3 and favColor == "Green" and temp == -5)
# When writing adn expression, put the value most likely to be False first!

# Logical OR -- Requires ONE expression to be True.
print(5 > 2 or 2 < -2)
print(3 != 3 or 5 == 5)

# AND OR Combined
print("Line 81")
print(3 > 2 and 4 < 3 and 5 != 7)
# print(True and False or True)

# NOT Logical Operator
print(not ( 3 > 2))
print(not (not (not ( 5 != 3))))

