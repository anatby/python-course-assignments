import random

LOW = 1
HIGH = 20

def get_random_number():
    return random.randint(LOW, HIGH)

debug_mode = False
move_mode = False

def play_game():
    global debug_mode, move_mode
    number = get_random_number()
    while True:
        if debug_mode:
            print(f"(Debug) The number is: {number}")
        guess = input(f"Guess ({LOW}-{HIGH}), 's'=show, 'x'=exit, 'd'=debug, 'm'=move, 'n'=new game: ")
        if guess == 'x':
            print("Exiting the game.")
            return False
        elif guess == 's':
            print(f"(Cheat) The number is: {number}")
        elif guess == 'd':
            debug_mode = not debug_mode
        elif guess == 'm':
            move_mode = not move_mode
        elif guess == 'n':
            print("Starting new game...")
            return True
        elif guess.isdigit():
            guess = int(guess)
            if guess < number:
                print("Too low.")
            elif guess > number:
                print("Too high.")
            else:
                print("Correct!")
                return True
        else:
            print("Invalid input.")

        if move_mode:
            number += random.choice([-2, -1, 0, 1, 2])
            number = max(LOW, min(HIGH, number))

while True:
    if not play_game():
        break