# Control Flow, Kristopher Cooper, v0.3
# DECLARATIONS

favColor = "Green"
luckyNumber = 77
myGPA = 4.0
myAge = 16
pineappleOnPizza = False

# if Statements - Check for a condition to be True/False, do something if true
if favColor == "Green":
    print("I like Turtles.")

if myAge == 16:
    print("I like Cookies.")

if luckyNumber > 500:
    print("Big numbers for a big winner!")

# if-else Statement -- Check for a condition, do something for True or False
if myGPA >= 3.0:
    print("Congratulations on making the honor roll!")
else:
    print("Better luck next year. Try to study more!")

if myAge <= 16:
    print("Not old enough.")
else:
    print("Congratulation!")

# if - elif - else Statement -- Checks for multiple conditions
if myAge > 65:
    print("Congratulation on retiring!")
elif myAge > 50:
    print("Congratulation, you have earned a bouns of $1000!")
else:
    print("You are not old enough for a bonus")
# 1 if, 1 else, any number of elif allowed.

# Nested if - elif - else Statements
if myAge > 15:
    print(" You are eligible for a license!")
    if myGPA >= 3.5:
        print("You qualify for a new car!")
    elif myGPA > 2.0:
        print("You qualify for $500 off a car!")
    else:
        print(" You get nothing!")
else:
    print("You are not yet old enough to drive.")

# When doing if - elif - else Statemenents, check for the highest values first!!!!
if myGPA > 1.5:
    print("You are in danger of failing for the year.")
elif myGPA > 2.0:
    print("You are on track to graduate.")
elif myGPA > 3.0:
    print("You qualify for some scholarship money!")
elif myGPA > 3.99:
    print("You qualify for Bright Futures 100 percent scholarship!")
else:
    print("GPA was not calculated. Please try again.")

# while Loop -- Think "MUSICAL CHAIRS" -- Used when you do NOT know how many interations you need.
# iteration = one complete trip through a loop
x = 0
while x < 100:
    print(f"X is currentily equal to {x}")
    x += 15

while x >= 0:
     print(f"X is currentily equal to {x}")
     x -= 1

# for Loop -- Think 'Go Fish', used when you knoq number of interations needed
print("FOR LOOP STARTS HERE")
for i in range(10): # i = iterable variable
    print(i)

print("EVEN OR ODD LOOP!")
for i in range(101):
    print(i)
    if i % 2 == 0:
        print("That number is even!")
    else:
        print("That number is odd!")