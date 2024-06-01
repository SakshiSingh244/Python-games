import random

print(" Type -1 whenever you want to quit")
num = int(input("guess the number ? Hint : Number is positive "))
a = num
r_num = random.randint(0,num)
tries = 1


while (num != r_num) and (num != -1):
    if num < 0:
        nums = int(input("Nope.Try a positive number "))
    elif num > a:
        nums = int(input("Nope. You are above the number"))
    else:
        num = int(input("Ohh no. Try Again "))
        tries+=1


if ( num == -1):
    quit()


print("Yes you guessed it right. It was",num,"You guessed it in",tries,"try" )