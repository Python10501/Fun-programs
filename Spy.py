#Ask the user for their operation code (1,2,3)
import time

Opcode = int(input("Please enter your Op code (1,2,3): "))
int()

if Opcode == 1:

    spyName = len(input("What is your spy name?: "))
    if spyName >= 5 and spyName <= 10: # is name is 5 chars, mission aborted
        print ("Your mission has been aborted...")

    elif spyName >= 10 and spyName <= 15: # if name is 10 chars, their in danger
        print("You are in danger, move to your safe location!")

    elif spyName >=15 and spyName <= 30:
        print("This program will self-destruct in 3 seconds...")
        time.sleep(2)
        print("3")
        time.sleep(2)
        print("2")
        time.sleep(2)
        print("1")
        time.sleep(2)
        print("BOOM....")

#Ask the user for new spy name and two number
if Opcode == 2:
    newSpyName = input("What is your new spy name?: ")
    time.sleep(1)
    newName = int(input("Please enter a number: "))
    int()
    time.sleep(1)
    newName2 = int(input("Please enter another number: "))
    int()

    #add the sum of the two numbers
    sum = newName + newName2
    print ("Your new spy name is " + newSpyName + str(newName+newName2))

#Ask the user for their Date of Birth (DOB)

if Opcode == 3:
    DOB = int(input("What year were your born?: "))
    int()

    if DOB >= 1949 or DOB <= 2024:
        print("You are retired")

    elif DOB >= 1981 or DOB <= 2024:
        print("You should apply for a promotion")

    elif DOB >= 1991 or DOB <= 2024:
        print("Keep up the hard work")

    elif DOB >= 1992 or DOB <= 2024:
        print("Get some more real work experience before becoming a spy")
