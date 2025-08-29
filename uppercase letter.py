# Program to print only uppercase letters from a string

s = input("Enter a string: ")

result = ""
for ch in s:
    if ch.isupper():   # check if character is uppercase
        result += ch

print("Uppercase letters in the string:", result)
