# Hangman Game 🎯

A fully functional, command-line version of the classic Hangman game, themed around software development terminology.

This project was built to practice core Python mechanics such as state management, input validation loops, and separating logic into single-responsibility functions. It features a clean CLI interface complete with dynamic ASCII art to track the player's remaining lives.

## 🧠 Core Concepts Applied

* **Single-Responsibility Functions:** The game logic is modularized into specific functions (`select_word`, `ask_letter`, `validate_letter`, `display_progress`), making the code highly readable and easy to maintain.
* **Sets for Logical Comparison:** Utilizing Python `set()` structures to extract unique letters from the secret word. This makes checking the win condition (`set(correct_letters) == unique_letters`) highly efficient without needing complex loops.
* **List Comprehensions:** Used to dynamically generate the hidden word display (e.g., `_ E _ _ O _ _ D`) in a single, elegant line of code.
* **Robust Input Validation:** Using string methods like `.isalpha()` and `len()` inside a `while True` loop to ensure the program doesn't crash when users input numbers, special characters, or multiple letters at once.

## 🚀 How to Run

1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd 05-hangman-game
