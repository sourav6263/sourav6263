import random
randNumber = random.randint(1, 100)
userguess = 0
guess = 0

while(userguess != randNumber):
    userguess = int(input("Enter your guess: "))
    if(userguess==randNumber):
        print("you guessed it right!")
    else:
        if(userguess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
           print("You guesed it wrong! Enter a larger number")



