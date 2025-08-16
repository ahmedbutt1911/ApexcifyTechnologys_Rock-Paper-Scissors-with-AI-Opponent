                                                        #AHMED ASAD
                                                        #TASK 1: Rock-Paper-Scissors with AI Opponent

import random


options = ['Rock', 'Paper', 'Scissor']


user_score = 0
computer_score = 0
draws = 0
user_moves = {0: 0, 1: 0, 2: 0}


def get_user_choice():
    
    choice = input("Your choice (0=Rock, 1=Paper, 2=Scissor, -1=Quit): ")
    return int(choice)


def ai_choice():
    """AI opponent that predicts user moves based on history."""
    if sum(user_moves.values()) <= 1:  # First round or no data
        return random.randint(0, 2)
    predicted_user_move = max(user_moves, key=user_moves.get)
    return (predicted_user_move + 1) % 3  # Counter move


def determine_winner(user_choice, computer_choice):
    
    global user_score, computer_score, draws

    if user_choice == computer_choice:
        draws += 1
        return "DRAW!"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        user_score += 1
        return "YOU WIN!"
    else:
        computer_score += 1
        return "COMPUTER WINS!"


def print_scoreboard():
    
    print(f"Score -> You: {user_score}, Computer: {computer_score}, Draws: {draws}")
    print("-" * 30)



print("Welcome to Rock-Paper-Scissors with AI Opponent ")
print("Type 0 for Rock, 1 for Paper, 2 for Scissor, or -1 to quit.")

while True:
    user_choice = get_user_choice()

    if user_choice is None:
        print("Invalid input. Please enter 0, 1, 2, or -1.")
        continue

    if user_choice == -1:
        print("\nGame Over!")
        print(f"Final Score -> You: {user_score}, Computer: {computer_score}, Draws: {draws}")
        print("Thanks for playing!")
        break

    if user_choice not in [0, 1, 2]:
        print("Invalid input. Please enter 0, 1, 2, or -1.")
        continue

    user_moves[user_choice] += 1


    computer_choice = ai_choice()


    print(f"You chose: {options[user_choice]}")
    print(f"Computer chose: {options[computer_choice]}")


    result = determine_winner(user_choice, computer_choice)
    print(result)

    print_scoreboard()
