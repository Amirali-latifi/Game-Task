"""
this module is going to select random number
"""
import random


def guess():
    """
    this function start the game
    """
    while True:
        chances = 5
        number = random.randint(1, 10)  # Random number between 1 to 10
        print("My number is between 1 to 10")
        print(f"Chances: {chances * '❤'}")
        while chances > 0:  # checking if there is any chance
            try:  # make sure there is no value error
                user_guess = int(input("\nYour turn, guess my number: "))
            except ValueError:
                print("Please use integer.")
                continue

            if (user_guess < 1 or user_guess > 10):
                print("Warning! My number is between 1 to 10.")
            elif user_guess > number:
                print(f"My number is lower than '{user_guess}'")
                chances = chances - 1
                print(f"Chances: {chances * '❤'}")
            elif user_guess < number:
                print(f"My number is higher than '{user_guess}'")
                chances = chances - 1
                print(f"Chances: {chances * '❤'}")
            else:
                print("Oops, you did it! Well done.")
                break

        if chances == 0:
            print(f"Game over! My number was {number}.")
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Come back soon!")
            break


guess()
