import operator

operations = {
    "add": operator.add,
    "sub": operator.sub,
    "mult": operator.mul,
    "div": lambda x, y: x / y if y != 0 else "Error: Division by zero"
}

a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
operation = input("Choose operation (add/sub/mult/div): ")

# get the function or None if invalid
func = operations.get(operation)

if func:
    print("Result:", func(a, b))
else:
    print("Invalid operation")