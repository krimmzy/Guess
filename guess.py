import random

def guessing_game():
    # The computer selects a random number between 1 and 100
    random_number = random.randint(1, 100)
    attempts = 0
    guessed_number = None

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while guessed_number != random_number:
        # Get the player's guess
        guessed_number = int(input("Make a guess: "))
        attempts += 1

        if guessed_number < random_number:
            print("Too low! Try again.")
        elif guessed_number > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")

# Run the game
guessing_game()
