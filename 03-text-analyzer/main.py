# Text Analyzer

print("=" * 50)
print("TEXT ANALYZER TOOL")
print("=" * 50)

# Input Section
text = input("Enter the text to analyze:\n> ")
text_lowercase = text.lower()
print("-" * 50)

# 1. Letter Frequency
print("Enter 3 letters to track frequency:")
x = input("  1st letter: ").lower()
y = input("  2nd letter: ").lower()
z = input("  3rd letter: ").lower()

letters = [x, y, z]
total_x = text_lowercase.count(letters[0])
total_y = text_lowercase.count(letters[1])
total_z = text_lowercase.count(letters[2])

print(f"Letter Frequency:")
print(f"   • '{letters[0]}': {total_x} times")
print(f"   • '{letters[1]}': {total_y} times")
print(f"   • '{letters[2]}': {total_z} times")
print("-" * 50)

# 2. Word Count
total_words = text.split()
print(f"Total Word Count: {len(total_words)} words")
print("-" * 50)

# 3. Structural Indexing
print(f"Character Position:")
print(f"   • First character: '{text[0]}'")
print(f"   • Last character:  '{text[-1]}'")
print("-" * 50)

# 4. String Reversal
inverted_text = " ".join(total_words[::-1])
print(f"Reversed Text (Word by Word):\n   \"{inverted_text}\"")
print("-" * 50)

# 5. Boolean Verification (Using Dictionary Mapping)
boolean_mapping = {True: "YES, 'Python' is present in the text.", False: "NO, 'Python' was not found."}
is_python_present = "python" in text_lowercase
print(f"Python Language Check:\n   {boolean_mapping[is_python_present]}")
print("=" * 50)