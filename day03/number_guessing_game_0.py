import random

# Computer "thinks" of a number between 1 and 20
number_to_guess = random.randint(1, 20)

# Prompt the user for a guess
user_guess = int(input("Guess a number between 1 and 20: "))

# Check the user's guess
if user_guess < number_to_guess:
    print("Too low!")
elif user_guess > number_to_guess:
    print("Too high!")
else:
    print("Correct! You guessed the number.")