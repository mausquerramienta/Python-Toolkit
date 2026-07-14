# Bank Account Manager 🏦

A terminal-based banking simulator demonstrating the core principles of Object-Oriented Programming (OOP) in Python. 

This interactive command-line application allows a user to register a bank account and perform standard financial transactions, securely tracking the monetary balance through instance methods and encapsulated state changes.

## 🧠 Core Concepts Applied

* **Object-Oriented Programming (OOP):** Implementation of custom structures (`Person` and `Client`) to model real-world entities, establishing a clear separation of data and behavior.
* **Inheritance:** The `Client` class inherits attributes from the `Person` base class using the `super()` function, promoting code reusability and demonstrating structural hierarchy.
* **State Encapsulation:** The account balance is managed safely within the instance environment. It cannot be modified directly via the console; it strictly relies on internal class methods (`deposit` and `withdraw`) to validate and execute mutations.
* **Dunder Methods (Magic Methods):** Utilization of the `__str__` method to override the default object memory address response, providing a clean, human-readable string representation of the account details.
* **Data Formatting:** Application of string interpolation and float formatting (`${amount:,.2f}`) to display financial data correctly with decimal constraints and comma separators.

## 🚀 How to Run

1. Open your terminal.
2. Navigate to the project directory:
   ```bash
   cd 07-bank-account