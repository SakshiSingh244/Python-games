import random 

# 0 -> rock
# 1 -> paper
# 2 -> scissors

c = 0
h = 0

outcomes = ["rock","paper","scissors"]

while True:
    human = input("type rock/paper/scissors to play or q to quit ").lower()

    if (human == "q"):
        break

    if ( human not in ["rock","paper","scissors"]):
        continue

    computer = random.randint(0,2)

    print("Compuer picked",outcomes[computer])

    if ( human == outcomes[computer]):
        print(" Match is draw. Points are computer : human-",c,":",h)
        print()

    if (human == "rock") and (computer == 1):
        c+=1
        print(" Match is won by computer. Points are computer : human-",c,":",h)
        print()
    
    if (human == "rock") and (computer == 2):
        h+=1
        print(" Match is won by human. Points are computer : human-",c,":",h)
        print()

    if (human == "scissors") and (computer == 0):
        c+=1
        print(" Match is won by computer. Points are computer : human-",c,":",h)
        print()

    if (human == "scissors") and (computer == 1):
        h+=1
        print(" Match is won by human. Points are computer : human-",c,":",h)
        print()

    if (human == "paper") and (computer == 0):
        h+=1
        print(" Match is won by human. Points are computer : human-",c,":",h)
        print()

    if (human == "paper") and (computer == 2):
        c+=1
        print(" Match is won by computer. Points are computer : human-",c,":",h)
        print()
    
print("good bye. total score you scored",h,"and the computer scored",c)
