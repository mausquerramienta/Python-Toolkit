# Day 4 Project
# Guess the number
from random import randint

print("=" * 45)
print("🎲 GUESS THE SECRET NUMBER 🎲")
print("=" * 45)

name = input("Enter your name: ")
print("-" * 45)
print(f"👋 Hello, {name}!")
print("I am thinking of a number between 1 and 100.")
print("You have 8 attempts to guess it.")
print("-" * 45)

number = randint(1, 100)
attempts = 8

while attempts > 0:
    print(f"\n▶ Attempts remaining: {attempts}")
    guess = int(input("Enter your guess: "))

    if guess > 100 or guess < 1:
        print("⚠️ Invalid input. Please choose between 1 and 100.")
    elif guess > number:
        print("📉 Incorrect. Try a SMALLER number.")
        attempts -= 1
    elif guess < number:
        print("📈 Incorrect. Try a LARGER number.")
        attempts -= 1
    else:
        print("\n" + "=" * 45)
        print("🎉 CONGRATULATIONS! 🎉")
        print(f"The correct number was {number}.")
        print(f"🏆 You guessed it in {8 - attempts} attempts!")
        print("=" * 45)
        break

if attempts == 0:
    print("\n" + "=" * 45)
    print("GAME OVER")
    print("You ran out of attempts.")
    print(f"The secret number was {number}.")
    print("=" * 45)
