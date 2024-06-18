# libraries
import time
import random

#User functions
def tellFortune(number):
    if number == 1:
        print ("Ask again later")
    elif number == 2:
        print ("It is decidedly so")
    elif number == 3:
        print ("My reply is no")
    elif number == 4:
        print ("Don't count on it")
    elif number == 5:
        print ("Yes")
    elif number == 6:
        print ("Concentrate and ask again")
    elif number == 7:
        print ("Better not tell you now")
    elif number == 8:
        print ("Outlook good")

#Ask the user if they want to play
print ("Welcome to the Magic 8 Ball!")
time.sleep(2)
answer = input ("Do you want to know your fortune?")

# if input is yes, start program
while answer == "y" or answer == "yes" or answer == "Y" or answer == "Yes":
    input ("What question do you want the answer for? ")
    print ("Shake")
    time.sleep(1)
    print ("Shake")
    time.sleep(1)
    print ("Shake")
    time.sleep(1)

    #creates a random number
    fortune = random.randint(1,8)

    tellFortune(fortune) #runs the number through the 8ball and tells fortune

    #ask if they want to play again
    answer = input ("Do you want to find another fortune? ")

if answer == "n" or answer == "no" or answer == "N" or answer == "No":
    print ("Ok, see you another time... bye bye")
    time.sleep(2)
    print ("program shutting down....")
    exit(0)
