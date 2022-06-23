import random

print("welcome to my guessing game")

number=random.randint(1,9)

chances = 3

print("guess a number between 1-9")

while chances>0:
    guess=int(input("enter your guess:"))
    if(guess==number):
        print("congrats you're not dumb")
        break
    elif(guess>number):
        print("bruh too high, guess lower")
    else:
        print("bruh too low, guess higher")
    chances=chances-1
    if(chances==0):
        print("boi you have negative IQ, the number was",number)
