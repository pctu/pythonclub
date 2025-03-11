# Function definitions for calculator operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b

# Main calculator function
def calculator():
    while True:  # Loop to allow multiple calculations
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Choose operation (+, -, *, /) or 'q' to quit: ")

            if operation == 'q':
                print("Exiting calculator. Goodbye!")
                break
            
            if operation == "+":
                result = add(num1, num2)
            elif operation == "-":
                result = subtract(num1, num2)
            elif operation == "*":
                result = multiply(num1, num2)
            elif operation == "/":
                result = divide(num1, num2)
            else:
                result = "Invalid operation"

            print(f"Result: {result}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
