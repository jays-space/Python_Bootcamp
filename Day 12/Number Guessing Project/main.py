from art import logo
import random

def print_header():
    """ Prints the header """
    print(logo)
    print("Welcome to Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

def print_lives_remaining(lives):
    """ Prints the number of lives remaining """
    if lives > 0:
        print("Guess again.")
        print(f"You have {lives} attempts remaining to guess the number.")


# TODO: Initialise a global variable by generating a random_number between 1 and 100. (DONE)
# TODO: Prompt user to choose difficulty: easy or hard. 'Easy' = 10 guess attempts (10 lives), 'hard' = 5 (5 lives). Initialise variable (lives) with this (DONE)
# TODO: While lives > 0, run the following:
# TODO: Prompt user to make a guess: if guess > random_number, print("Too high"). If guess < random_number, print ("Too low").
# TODO: Each time the user guesses wrong, deprecate lives by 1
# TODO: If lives == 0, print("GAME OVER!)", else it means the user guessed right, print("You got it! The answer was 39")

def main():
    print_header()
    random_number = random.randint(1, 100)
    # print(f"Number: {random_number}")
    difficulty = input("Choose a difficulty level. type 'easy' or 'hard': ").lower()
    lives = 10 if difficulty == 'easy' else 5 if difficulty == 'hard' else None
    if not lives:
        print("That is not a valid difficulty level! Try again.")

    while lives > 0:
        guess = int(input("Make a guess: "))
        if guess > random_number:
            lives -= 1
            print("Too high!")
            print_lives_remaining(lives)
        elif guess < random_number:
            lives -= 1
            print("Too low!")
            print_lives_remaining(lives)

        else:
            print("You got it! The number was", random_number)
            break

    if lives == 0:
        print(f"You lose! The number was {random_number}")
        print("GAME OVER!")
main()