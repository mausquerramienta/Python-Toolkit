# Hangman game 

import random

# Constant list of technical words
WORD_LIST = [
    "development", "keyboard", "loop", "algorithm",
    "interface", "function", "hangman", "screen",
    "variable", "server"
]

# Hangman ASCII Art states
HANGMAN_STAGES = [
    """
       -----
       |   |
       |   O
       |  /|\\
       |  / \\
       |
    --------
    """,
    """
       -----
       |   |
       |   O
       |  /|\\
       |  / 
       |
    --------
    """,
    """
       -----
       |   |
       |   O
       |  /|\\
       |  
       |
    --------
    """,
    """
       -----
       |   |
       |   O
       |  /|
       |  
       |
    --------
    """,
    """
       -----
       |   |
       |   O
       |   |
       |  
       |
    --------
    """,
    """
       -----
       |   |
       |   O
       |  
       |  
       |
    --------
    """,
    """
       -----
       |   |
       |   
       |  
       |  
       |
    --------
    """
]

def select_word(words):
    secret_word = random.choice(words).lower()
    unique_letters = set(secret_word)
    return secret_word, unique_letters

def ask_letter(used_letters):
    while True:
        chosen_letter = input("👉 Choose a letter: ").lower()
        if not chosen_letter.isalpha() or len(chosen_letter) != 1:
            print("Invalid input. Please enter a single letter.")
        elif chosen_letter in used_letters:
            print("You already chose that letter. Try a different one.")
        else:
            used_letters.append(chosen_letter)
            return chosen_letter

def validate_letter(letter, unique_letters, correct_list, incorrect_list, lives_left):
    if letter in unique_letters:
        correct_list.append(letter)
        return lives_left, True
    else:
        incorrect_list.append(letter)
        return lives_left - 1, False

def display_progress(secret_word, correct_list):
    display_list = [letter if letter in correct_list else "_" for letter in secret_word]
    print("\nWord: " + " ".join(display_list).upper())

def game_over(word):
    print(HANGMAN_STAGES[0])
    print("You ran out of lives!")
    print("The game is over.")
    print(f"The secret word was: {word.upper()}\n")

def start_game():
    print("=" * 50)
    print("Welcome to HANGMAN")
    print("=" * 50)
    print("You have 6 lives to guess the secret technical word.")
    print("Let's begin!\n")
    
    guessed_letters = []
    correct_letters = []
    incorrect_letters = []
    lives = 6
    
    secret_word, unique_letters = select_word(WORD_LIST)
    
    feedback_message = ""
    
    while lives > 0:
        if feedback_message != "":
            print("\n" + "=" * 50)
            print(feedback_message)
            
        print(HANGMAN_STAGES[lives])
        print("-" * 40)
        display_progress(secret_word, correct_letters)
        print(f"Wrong letters: {', '.join(incorrect_letters)}")
        print(f"Lives remaining: {lives}\n")
        
        current_letter = ask_letter(guessed_letters)
        lives, is_correct = validate_letter(current_letter, unique_letters, correct_letters, incorrect_letters, lives)
        
        if set(correct_letters) == unique_letters:
            print("\n" + "=" * 50)
            print(f"Awesome! The letter '{current_letter}' is in the word.")
            print(HANGMAN_STAGES[lives])
            print("-" * 40)
            display_progress(secret_word, correct_letters)
            print("\n🎉 CONGRATULATIONS! 🎉")
            print(f"You successfully guessed the word: {secret_word.upper()}!")
            print("=" * 50 + "\n")
            break
            
        if is_correct:
            feedback_message = f"Awesome! The letter '{current_letter}' is in the word."
        else:
            feedback_message = f"Oops! The letter '{current_letter}' is not in the word."

    if lives == 0:
        print("\n" + "=" * 50)
        print(feedback_message)
        game_over(secret_word)

start_game()
