import random

def number_guessing_game():
    """
    A simple number guessing game where the player tries to guess a random number.
    """

    # 1. Random Number Generation
    lower_bound = 1  # You can change the lower bound
    upper_bound = 100 # You can change the upper bound
    secret_number = random.randint(lower_bound, upper_bound)

    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

    # 2. User Guesses
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # 3. Feedback
        if guess < secret_number:
            print("Too low! Try guessing higher.")
        elif guess > secret_number:
            print("Too high! Try guessing lower.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "_main_":
    number_guessing_game()