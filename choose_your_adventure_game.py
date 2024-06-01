name = input("Type your name : ")
print("Welcome",name,"to this adventure :) ")

answer = input("You are on a dirt road and you have reached the end. Youc can go either left or right. Which way do you choose ? ").lower()

#left option
if (answer == "left"):
    answer = input("You chose the left way. Now you have reached an old bridge. Do you want to cross by the bridge (cross) or try jumping to other side (jump) ").lower()
    # 2 - cross or fly
    if ( answer == "cross"):
        print("Great choice. You crossed the bridge !")
        # 3 - swim or boat
        answer = input("You have reached a lake with crocodiles. Do you want to cross the river using a boat (boat) or swim through the lake (swim) ").lower()
        if ( answer == "boat"):
            print("Yess. You have crossed the river without getting eaten up by the crocodiles ")
            # 4 - fight or act
            answer = input("You have reached the last part of this adventure. There is a big bear. Do you want to act dead(act) or fight the bear(fight) ").lower()
            if ( answer == "act"):
                print("You are smart. The bear thought you were dead and walked away.") 
                print("Congratulations ! You were a good adventurer")
            elif( answer == "fight"):
                print("Oops ! You were killed by the bear. You lose !")
            else:
                print("Not a valid option.You lose. ")
        elif (answer == "swim"):
            print("You lose. Still, you were a great feast for the crocodiles ")
        else:
            print("Not a valid option.You lose. ")
    elif(answer == "jump"):
        print("OHH NOO. You fell. You lose. ")
    else:
        print("Not a valid option.You lose. ")

elif (answer == "right"):
    # 2 - boar ot swim
    answer = input("You have reached a lake with crocodiles. Do you want to cross the river using a boat (boat) or swim through the lake (swim) ").lower()
    if ( answer == "boat"):
            print("Yess. You have crossed the river without getting eaten up by the crocodiles ")
            answer = input("Now you have reached an old bridge. Do you want to cross by the bridge (cross) or try jumping to other side (jump) ").lower()
        # 3 - cross or jump
            if ( answer == "cross"):
                print("Great choice. You crossed the bridge !")
                # 4 - fight or act
                answer = input("You have reached the last part of this adventure. There is a big bear. Do you want to act dead(act) or fight the bear(fight) ").lower()
                if ( answer == "act"):
                    print("You are smart. The bear thought you were dead and walked away.") 
                    print("Congratulations ! You were a good adventurer")
                elif( answer == "fight"):
                    print("Oops ! You were killed by the bear. You lose !")
                else:
                    print("Not a valid option.You lose. ")
            elif(answer == "jump"):
                print("OHH NOO. You fell. You lose. ")
            else:
                print("Not a valid option.You lose. ")
    elif (answer == "swim"):
        print("You lose. Still, you were a great feast for the crocodiles ")
    else:
        print("Not a valid option.You lose. ")
        
            


else:
    print("Not a valid option.You lose. ")
