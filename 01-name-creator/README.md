# Name Creator 🍻

A concise, interactive command-line script that dynamically generates a brand name based on user input. 

This project demonstrates the fundamental concepts of standard input/output operations and string manipulation in Python, executing the entire logic flow within a single, nested statement.

## 🧠 Core Concepts Applied

### `input()`
*   **Functionality:** Halts program execution to read a line from the standard input (the keyboard), stripping the trailing newline.
*   **Return Type:** Always evaluates and returns the captured data as a `String` object.
*   **Implementation:** Used here to display a prompt and dynamically capture the user's city and color preferences in real-time.

### `print()`
*   **Functionality:** Evaluates expressions and writes the resulting output to the standard output console.
*   **Implementation:** Functions as the outer wrapper of this script. It waits for the nested `input()` functions to resolve, concatenates the returned strings using the `+` operator, and applies an escape character (`\n`) to format the final output onto a new line.

## 🚀 How to Run

1. Open your terminal.
2. Navigate to the project directory.
3. Execute the script using Python:

```bash
python main.py