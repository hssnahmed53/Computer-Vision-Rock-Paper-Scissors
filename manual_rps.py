import random
import time


choice = ["rock","paper","scissors"]

def get_computer_choice():
    print("The Computer is thinking...")
    time.sleep(3)
    return choice[random.randint(0,2)];

def get_user_choice():
    while True:
        choice = input("Time to choose; rock, paper or scissors: ")
        try:
            if choice.lower() == "rock":
                return "rock"
            elif choice.lower() == "paper":
                return "paper"
            elif choice.lower() == "scissors":
                return "scissors"
            else:
                print("Invalid choice! Try again")
                continue
        except:
            print("Invalid choice! Try again")
            continue

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return "draw"
    else:
        if computer_choice == "rock":
            if user_choice == "paper":
                print(f"You Won, the computer chose: ",computer_choice)
            else:
                print(f"Looks like ya lost, the computer chose: ",computer_choice)    
        elif computer_choice == "paper":
            if user_choice == "scissors":
                print(f"Nice! you Won, the computer chose: ",computer_choice)
            else:
                print(f"Hmmm...you didn't win, the computer chose: ",computer_choice)
        elif computer_choice == "scissors":
            if user_choice == "rock":
                print(f"Good job! you Won, the computer chose: ",computer_choice)
            else:
                print(f"Sorry you didn't win, the computer chose: ",computer_choice)
        elif user_choice == "exit":
            return "exit"

def play():
    while True:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        winner = get_winner(computer_choice, user_choice)  

play()          
