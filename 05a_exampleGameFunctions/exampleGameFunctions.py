# Example Game Functions Project, Kristopher Cooper v0.1
import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    user_choice = input("Enter your choice (rock/paper/si=cissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice, Please try again.:")
        play_game()

    print("Computer chose:", computer_choice)
    print("You chose:", user_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice =='scissors') or \
            (user_choice)