import random


def guess_the_number():
    number = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to the guessing game! I have generated a number between 1 and 100.")
    print("Try to guess the number in as few attempts as possible. Good luck!\n")

    while guess != number:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("The number is higher. Try again!")
        elif guess > number:
            print("The number is lower. Try again!")
        else:
            print("You got it! The number was", number)
            print("It took you", attempts, "attempts to guess the number.")


guess_the_number()
