import random

your_wins = 0
comp_wins = 0

options = ["rock", "paper", "scissor"]

while True:
    your_option = input("Enter your choosen from the options or q to quit: ")
    if your_option == "q":
        break

    if your_option not in options:
        continue
    comp_option = random.randint(0, 2)
    comp_pick = options[comp_option]
    

    if your_option == "rock" and comp_pick == "scissor":
        print("You won")
        your_wins += 1
        
    elif your_option == "paper" and comp_pick == "rock":
        print("You won")
        your_wins += 1
        
    elif your_option == "scissor" and comp_pick == "paper":
        print("You won")
        your_wins += 1
        
    else:
        print("You lost")
        comp_wins += 1

print("You won", your_wins, "times")
print("The computer won", comp_wins, "times.")
print("Goodbye!")

