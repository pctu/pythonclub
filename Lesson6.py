import random
for i in range(random.randint(1,1)):
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    computer_choice = random.choice(choices)
    user_choice = input("Enter one of rock, paper, scissor, lizard, or spock with correct spelling:").lower()

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "paper" or \
    user_choice == "rock" and computer_choice == "spock" or \
    user_choice == "paper" and computer_choice == "scissor" or \
    user_choice == "paper" and computer_choice == "lizard" or \
    user_choice == "scissor" and computer_choice == "rock" or \
    user_choice == "scissor" and computer_choice == "spock" or \
    user_choice == "lizard" and computer_choice == "rock" or \
    user_choice == "lizard" and computer_choice == "scissor" or \
    user_choice == "spock" and computer_choice == "paper" or \
    user_choice == "spock" and computer_choice == "lizard":
        print("You lose!")
    else: 
        print("You win")
# This is a "Rock, Paper, Scissors, Lizard, Spock" game.
# The user inputs their choice, and the computer randomly selects one.
# The program then compares the two choices and determines the winner.
# The game continues until the user decides to stop playing.
# The game is a simple implementation of the classic rock-paper-scissors game.