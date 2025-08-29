# Program to print only alphabets from a string

s = input("Enter a string: ")

result = ""
for ch in s:
    if ch.isalpha():   # check if character is an alphabet
        result += ch

print("Alphabets in the string:", result)
