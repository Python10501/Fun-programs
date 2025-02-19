#libraries
import time
import random



#user functions
def findWinner(winsPlayer1, winsPlayer2):
    if winsPlayer1 > winsPlayer2: # if p1 is bigger than p2 they win
        print ("Player 1 wins!!")
    elif winsPlayer1 < winsPlayer2: # if p2 is bigger than p1 they win
        print ("Player 2 wins!!")
    elif winsPlayer1 == winsPlayer2: # if value is the same, its a tie
        print ("Tie!!")

#Game description

print("Welcome to the Game Of War!")
time.sleep(2)
print("In this game, 4 rounds will be played.")
time.sleep(2)
print("The player with the highest card will win the round.")
time.sleep(2)
print("At the end of the game, the players will total how many wins to determine the real winner of the game.")
time.sleep(2)

#If yes, games starts

answer = input("Would you like to play the Game of War?:")
while answer == "y" or answer == "yes" or answer == "Y" or answer == "Yes":
    rounds = 0
    for rounds in range(4):
        if rounds <= 4:
            print ("Attack launching in")
            time.sleep(2)
            print("3")
            time.sleep(2)
            print("2")
            time.sleep(2)
            print("1")
            time.sleep(2)

            winsPlayer1 = random.randint(0,10) #gives a random card number 0 through 10
            winsPlayer2 = random.randint(0,10)
            findWinner(winsPlayer1, winsPlayer2)
            print("Player 1 draws " + str(winsPlayer1))
            print("Player 2 draws " + str(winsPlayer2))
            #p1score = 1
            #p2score = 1

            time.sleep(2) # two seconds between rounds

    answer = input ("Would you like to play again?") # asks the user if they want to play again

    if answer == "n" or answer == "no" or answer == "N" or answer == "No":
        print("Thank you for playing the Game Of War...")
        exit(0)
