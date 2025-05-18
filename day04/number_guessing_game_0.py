import random

LOW = 1
HIGH = 20

def get_random_number():
    return random.randint(LOW, HIGH)

number = get_random_number()
guess = input(f"Guess the number ({LOW}-{HIGH}): ")
if guess.isdigit():
    guess = int(guess)
    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print("Correct!")
else:
    print("Invalid input.")