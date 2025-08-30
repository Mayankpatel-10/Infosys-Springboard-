text = "Python is a powerful programming language"

# Default split (splits by spaces)
words = text.split()
print("Split by spaces:", words)

# Split by a specific character
csv_data = "apple,banana,grape,orange"
fruits = csv_data.split(",")
print("Split by comma:", fruits)

# Split by a specific word/character
sentence = "one-two-three-four"
numbers = sentence.split("-")
print("Split by dash:", numbers)

# Limiting number of splits
data = "A:B:C:D"
limited = data.split(":", 2)  # only 2 splits
print("Split with limit:", limited)
