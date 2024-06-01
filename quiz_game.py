print("Welcome to the quiz")

playing = input(" Do you want to play this game ? y/n ")
if  (playing.lower() != "y"):
    quit()

print(" Okay! Let's play :) ")

score = 0 

answer = input(" What does ROM stands for ? ")
if ( answer.lower() == "read only memory"):
    print(" Answer is correct. ")
    score+=1
else:
    print("Incorrect Answer ")

answer = input(" Which programming language has the name of a reptile ? ")
if ( answer.lower() == "python"):
    print(" Answer is correct. ")
    score+=1
else:
    print("Incorrect Answer ")

answer = input(" Which part of computer is the brain of computer  ? ")
if ( answer.lower() == "cpu"):
    print(" Answer is correct. ")
    score+=1
else:
    print("Incorrect Answer ")

answer = input(" What does RAM stands for ? ")
if ( answer.lower() == "random access memory"):
    print(" Answer is correct. ")
    score+=1
else:
    print("Incorrect Answer ")

answer = input(" GPU stands for ? ")
if ( answer.lower() == "graphics processing unit"):
    print(" Answer is correct. ")
    score+=1
else:
    print("Incorrect Answer ")

print("Your score is",score,"/ 5")