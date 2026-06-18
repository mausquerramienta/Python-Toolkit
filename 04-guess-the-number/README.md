# Guess The Number 🎲

An interactive, logic-based terminal game that challenges the user to guess a dynamically generated secret number within a limited set of attempts.

This project showcases fundamental algorithm design, specifically highlighting state management through loops, standard input/output parsing, and progressive condition validation.

## 🧠 Core Concepts Applied

### Control Flow & Comparison Operators
* **`if`, `elif`, `else`:** Evaluates user input sequentially. The structure first sanitizes out-of-bounds inputs, then utilizes comparison operators (`>` and `<`) to provide mathematical hints, reducing the problem space dynamically.
* **State Verification:** A final `if` statement checks the remaining attempts variable outside the loop to accurately determine the win/loss state of the application.

### Loops & Execution Control
* **`while` Loop:** Establishes an active game session that continues to execute as long as the conditional condition (`attempts > 0`) evaluates to `True`.
* **`break` Statement:** Implemented to immediately terminate the loop execution upon a successful guess, preventing unnecessary processing and securely exiting the game state.

### The `random` Library
* **`randint(a, b)`:** Imports specific functionality from Python's standard `random` module to securely generate a pseudo-random integer inclusive of the defined constraints (1 to 100), ensuring replayability.

### Standard I/O Operations
* **`input()`:** Halts execution to capture real-time keyboard inputs, which are immediately wrapped in type-casting functions (`int()`) to enable arithmetic comparisons.
* **`print()`:** Evaluates and pushes string expressions to the standard console. Utilized heavily alongside *f-strings* to inject variable states directly into the user interface.

## 🚀 How to Run

1. Open your terminal.
2. Navigate to the project directory.
3. Execute the script using Python:

```bash
python main.py