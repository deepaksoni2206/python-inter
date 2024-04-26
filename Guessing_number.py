import random

secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

# Run the game until the user guesses the correct number
while True:
    # Ask the user to guess the number
    guess = input("Enter your guess (between 1 and 100): ")
    
    # Check if the input is a valid number
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    # Convert the input to an integer
    guess = int(guess)
    
    # Compare the guess with the secret number
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {secret_number}!")
        break
