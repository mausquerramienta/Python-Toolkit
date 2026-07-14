# Digital Recipe Book 📖

A fully functional, command-line recipe manager designed to securely handle external file interactions. 

This project demonstrates advanced interaction with the host operating system, specifically focusing on directory creation, file reading/writing, and safe deletion protocols using Python's modern object-oriented file system paths.

## 🧠 Core Concepts Applied

* **Object-Oriented Pathing (`pathlib.Path`):** Bypasses `os.path` strings in favor of modern `Path` objects. This allows for dynamic directory referencing (`Path(__file__).parent`), ensuring the code is executable on any machine (Windows, macOS, Linux) without hardcoding absolute paths.
* **Cross-Platform Compatibility:** Implements environmental checks (`os.name == "nt"`) to dynamically trigger the correct terminal clearing commands (`cls` vs `clear`), providing a seamless UX regardless of the user's OS.
* **Safe File Manipulation:** Utilizes `.read_text()` and `.write_text(encoding="utf-8")` to handle file I/O safely without explicitly requiring `open()` and `close()` context managers, preventing memory leaks and encoding errors.
* **Structural Pattern Matching (`match-case`):** Leverages Python control flow architecture to cleanly manage the interactive CLI menu state instead of relying on heavily nested `if/elif` statements.
* **Data Validation & Error Handling:** Validates all user inputs using string methods (`.isnumeric()`) and prevents the deletion of non-empty directory structures to maintain data integrity.

## 🚀 How to Run

1. Open your terminal.
2. Navigate to the project directory:
   ```bash
   cd 06-recipe-book
