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
    missionAssign = input("Enter your mission code word (Alpha, Bravo, Charlie): ")

    if missionAssign == "Alpha":
        print("Incoming Transmission...")
        time.sleep(3)
        print("A company has developed a new EMP weapon that is capable of disabling devices within a ten-mile radius...")
        time.sleep(3)
        print("A rival nation also has plans to steal the new weapon and use it for their own purposes....")
        time.sleep(3)
        print("Your task is to infiltrate the company, locate the weapon and destroy it before the rival nation gets their hands on it...")
        time.sleep(3)
        print("Good luck agent....")
        time.sleep(3)
        print("Transmission ended....")

    elif missionAssign == "Bravo":
        print("Incoming Transmission...")
        time.sleep(3)
        print("A high-ranking government official has been kidnapped by a notorious crime syndicate...")
        time.sleep(3)
        print("An informant on the inside states that the crime syndicate tends to interrogate the official about a top-secret government project...")
        time.sleep(3)
        print("Your mission is to infiltrate the compound at which the official is being held, and locate and rescue the official before any information about the project is compromised...")
        time.sleep(3)
        print("Once you rescue the official, a safe house 1 mile away will have a vehicle waiting to extract you and the official...")
        time.sleep(3)
        print("This is a stealth mission, only use lethal force if necessary...")
        time.sleep(3)
        print("Good luck agent...")
        time.sleep(3)
        print("Transmission ended...")

    elif missionAssign == "Charlie":
        print("Incoming Transmission...")
        time.sleep(3)
        print("A rogue scientist has created a biochemical weapon under the code name New Age...")
        time.sleep(3)
        print("The new biochemical weapon is capable of creating widespread damage of the likes that no one has even seen...")
        time.sleep(3)
        print("the scientist is hiding with is weapon in an abandon bunker in Europe...")
        time.sleep(3)
        print("Your mission is to infiltrate the abandon bunker, retrieve the formula to the biochemical weapon, neutralize the weapon, and if possible capture the rogue scientist...")
        time.sleep(3)
        print("We can not allow this weapon to fall into the wrong hands, failure is not an option...")
        time.sleep(3)
        print("Good luck agent...")
        time.sleep(3)
        print("Transmission ended...")
