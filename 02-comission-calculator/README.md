# Commission Calculator 💰

A command-line utility designed to dynamically process user inputs, perform mathematical operations, and return formatted financial data.

This project highlights core Python mechanics, specifically focusing on data type conversion (casting), variable allocation, arithmetic processing, and modern string interpolation.

## 🧠 Core Concepts Applied

### Variables & Data Types
*   **Variables:** Used as memory containers (`name`, `sales`, `commission`) to store, update, and retrieve data dynamically during runtime.
*   **Strings:** Sequential text data captured natively through the user prompt.
*   **Floats:** Floating-point numbers utilized to handle currency, allowing for precise decimal representation necessary in financial calculations.

### Type Casting (Data Conversion)
*   **Implementation:** The script captures data via `input()`, which natively returns a String. To perform mathematical operations, the `float()` function is applied immediately to wrap and cast the string into a numeric floating-point value.

### Arithmetic Operations & `round()`
*   **Operators:** Utilizes standard multiplication (`*`) and division (`/`) to calculate percentage-based yields.
*   **`round()` Function:** Applied to the final calculation to strictly limit the floating-point result to two decimal places, preventing memory overflow from infinite fractions and maintaining standard currency formatting.

### String Formatting (f-strings)
*   **Implementation:** Leverages literal string interpolation (`f"..."`) to seamlessly inject evaluated variables and expressions directly into the output string. This modern approach eliminates the need for manual string concatenation, ensuring cleaner and more readable code.

## 🚀 How to Run

1. Open your terminal.
2. Navigate to the project directory.
3. Execute the script using Python:

```bash
python main.py