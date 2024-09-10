import random

def guess_the_number():
    number = random.randint(1, 100)
    print("Welcome to the Guess It!")
    print("I have picked a number between 1 and 100. Can you guess it?")
    
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
guess_the_number()