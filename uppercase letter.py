s = input("Enter a string: ")

result = ""
for ch in s:
    if ch.isupper():  
        result += ch

print("Uppercase letters in the string:", result)

