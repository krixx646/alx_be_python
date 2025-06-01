# match_case_calculator.py

# Prompt for the first number
num1 = float(input("Enter the first number: "))

# Prompt for the second number
num2 = float(input("Enter the second number: "))

# Prompt for the operation (exact text the checker wants)
operator = input("Choose the operation (+, -, *, /): ")

match operator:
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

# Final print with “The result of … is …” format
print(f"The result of {num1} {operator} {num2} is {result:.2f}")
