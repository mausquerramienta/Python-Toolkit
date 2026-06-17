# Text Analyzer 🔍

A robust string processing utility that analyzes text structures, evaluates substring frequencies, implements sequence reversal, and performs boolean lookups without relying on conditional statements or loops.

This project demonstrates a comprehensive understanding of Python's built-in data collections, sequence slicing, and memory manipulation methodologies.

## 🧠 Core Concepts Applied

### String Methods & Manipulation
* **`.lower()`:** Standardizes inputs to lowercase, enabling case-insensitive comparisons and ensuring data integrity during analysis.
* **`.count()`:** Scans the target string to evaluate the absolute frequency of specified substrings.
* **`.split()`:** Tokenizes the string based on whitespace delimiters, converting a contiguous string block into a dynamic `List` of individual words.
* **`.join()`:** Concatenates an iterable sequence of strings back into a single string using a designated separator string.

### Sequencing & Indexing (Substrings)
* **Zero-Based Indexing:** Accesses individual characters directly from memory. `text[0]` retrieves the leading element, while negative indexing (`text[-1]`) targets the terminating element.
* **Sequence Slicing (`[::-1]`):** Evaluates a sequence structure with a negative stride step (`-1`), performing an efficient word-by-word inversion across the string array.

### Built-in Data Collections
* **Lists (`[]`):** Mutable, ordered sequences utilized to store and index user-defined characters dynamically.
* **Dictionaries (`{}`):** Hash-map structures storing key-value pairs. Used here to establish a deterministic mapping for boolean states (`True`/`False`), substituting standard procedural control flow (`if/else`) with an explicit O(1) memory lookup.

### Booleans & Logical Operators
* **`in` Operator:** Performs a containment check over sequences, returning a primitive `Boolean` evaluation (`True` or `False`) based on substring existence.

## 🚀 How to Run

1. Open your terminal.
2. Navigate to the project directory.
3. Execute the script using Python:

```bash
python main.py