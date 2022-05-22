import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break
        
    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!!!")
        user_wins += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!!!")
        user_wins += 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!!!")
        user_wins += 1
    
    else:
        print("Oops! You lost!")
        computer_wins += 1
        
if user_wins > 1:
    print("You won", user_wins, "times.")
elif user_wins == 1:
    print("You won only", user_wins)
else:
    print("Sorry! You did not win any points.")
    
if computer_wins > 1:
    print("The computer won", computer_wins, "times.")
elif computer_wins == 1:
    print("The computer won only", computer_wins)
else:
    print("The computer did not win any points.")
    
print("Goodbye Champ!")