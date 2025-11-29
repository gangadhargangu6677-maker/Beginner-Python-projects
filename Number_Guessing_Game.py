import random

print("Number Guessing Game")
print("I am thinking of a number between 1 and 50")

secret_number = random.randint(1, 50)
attempts = 0

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too low, try again")
    elif guess > secret_number:
        print("Too high, try again")
    else:
        print(f"Correct. You guessed it in {attempts} attempts")
        break
