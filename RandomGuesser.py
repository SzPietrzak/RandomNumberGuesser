#Program to guess pseudo randomly generated number (maximum value is 99)

import random
genRandom = random.randrange(100)


userGuess = int(input("Please input your guess: "))

while (userGuess != genRandom):
    if (userGuess > genRandom):
        print("Your guess is to high.")
    else:
        print("Your guess is to low.")

    userGuess = int(input("Please input your guess: "))

print("Congratulations! Your guess", userGuess, "is the same as computer random", genRandom)
