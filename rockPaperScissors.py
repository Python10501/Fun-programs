import random
import time

#Game description

print("Welcome to Rock Paper Scissors!")
time.sleep(2)
print("The game is very simple, you have 3 choices either Rock, Paper, or Scissors.")
time.sleep(2)
print("You will play 3 rounds, after the game ends, you can chose to play again")
time.sleep(2)
print("If you select an action that defeats the computer, you win!")
time.sleep(2)

#if yes, start game
answer = input("Would you like to play?: ")
while answer == "y" or answer == "yes" or answer == "Y" or answer == "Yes":
    rounds = 0
    for rounds in range(3):
        if rounds <= 3:

            humanAction = input("Choose an option (rock,paper,scissors): ")
            playableAction = ["rock","paper","scissors"]
            computerAction = random.choice(playableAction)

            print(f"\nPlayer chooses {humanAction}, Computer chooses {computerAction}. \n")

            if humanAction == computerAction:
                print(f"Both players chose {humanAction}. Tie!")
                time.sleep(2)

            elif humanAction == "rock":
                if computerAction == "scissors":
                    print("Rock smashes scissors!, Player wins")
                    time.sleep(2)
                else:
                    print("Paper covers rock!, Computer wins")
                    time.sleep(2)

            elif humanAction == "paper":
                if computerAction == "rock":
                    print("Paper covers rock!, Player wins")
                    time.sleep(2)
                else:
                    print("Scissors cuts paper!, Computer wins")
                    time.sleep(2)

            elif humanAction == "scissors":
                if computerAction == "paper":
                    print("Scissors cuts paper!, Player wins")
                    time.sleep(2)
                else:
                    print("Rock smashes scissors!, Computer wins")
                    time.sleep(2)

    answer = input ("Would you like to play again?: ")
    if answer == "n" or answer == "no" or answer == "N" or answer == "No":
        print("Goodbye, see you next time")
        exit(0)
