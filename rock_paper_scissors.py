import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/ Paper/ Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Invaild entry. Try again!")
        continue
    
    random_number = random.randint(0,2)
    #0 is rock, 1 is paper, 2 is scissors
    computer_pick = options[random_number]
    print("The computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
       
    
    elif user_input == "paper" and computer_pick == "rock":
       print("You won!")
       user_wins += 1
       
    
    elif user_input == "scissors" and computer_pick == "paper":
       print("You won!")
       user_wins += 1

    elif user_input == computer_pick:
        print("DRAW")
       

    else:
        print("You lost")
        computer_wins += 1
        
       
    
print("You won", user_wins, "time(s).")
print("The computer won", computer_wins, "time(s).")
print("Bye for now")
