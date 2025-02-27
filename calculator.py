# Function to perform the arithmetic operation
def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation"

# Main program
print("Simple Calculator")
print("Available operations: add, subtract, multiply, divide")

# Prompt the user for input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()

    # Perform calculation and display the result
    result = calculate(num1, num2, operation)
    print(f"The result is: {result}")
except ValueError:
    print("Invalid input! Please enter numerical values.")
