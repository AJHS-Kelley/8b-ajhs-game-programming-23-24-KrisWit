# Example Game Functions Project, Kristopher Cooper v2
import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    user_choice = input("Enter your choice (rock/paper/scissors):\n").lower()

    if user_choice not in choices:
        print("Invalid choice, Please try again.:")
        play_game()

    print("Computer chose:", computer_choice)
    print("You chose:", user_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice =='scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == "scissors" and computer_choice == 'paper'):
        print("You win!")
        global user_score
        user_score += 1
    else:
        print("Computer wins")
        global computer_score
        computer_score += 1

    print("Score: You", user_score, "- Computer", computer_score)    
user_score = 0
computer_score = 0

while True:
    play_game()

    play_again = input("Do you want to play again? (yes/no):\n").lower()
    if play_again != 'yes':
        break

print("Thanks for playing!")
print('Final score: You', user_score, "-Computer", computer_score)