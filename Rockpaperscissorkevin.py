import random
for i in range(random.randint(1,3)):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    user_choice = input("Enter one of rock, paper, or scissor with correct spelling:").lower()

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "paper" or \
    user_choice == "paper" and computer_choice == "rock" or \
    user_choice == "scissor" and computer_choice == "rock":
        print("You lose!")
    else: 
        print("You win!")
