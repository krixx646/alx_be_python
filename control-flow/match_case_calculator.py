# match_case_calculator.py

# Prompt for the first number
num1 = float(input("Enter the first number: "))

# Prompt for the second number
num2 = float(input("Enter the second number: "))

# Prompt for the operation (must match the checker’s regex)
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        result = num1 / num2
    case _:
        print("Invalid operator")
        exit()

# Print starting with “The result is …”
print(f"The result is {result:.2f}")
