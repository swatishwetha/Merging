import random

secret = random.randint(1, 20)
guess = 0

while guess != secret:
    guess = int(input("Guess a number between 1 and 20: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print("Correct! You guessed the number!.")
import random

secret = random.randint(1, 20)
guess = 0

while guess != secret:
    guess = int(input("Guess a number between 1 and 20: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print("Correct! You guessed the number!.")


