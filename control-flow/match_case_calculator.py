# simple calculator script using match-case

# Prompt for the first number
num1 = float(input("Enter the first number: "))

# Prompt for the second number
num2 = float(input("Enter the second number: "))

# Prompt for the operator (make sure it matches exactly)
operator = input("Enter the operation (+, -, *, /): ")

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
        exit()  # Stop execution if the operator wasn’t one of the four

# Print the output message exactly once, after computing result
print(f"The result of {num1} {operator} {num2} is {result:.2f}")
