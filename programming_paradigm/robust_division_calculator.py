def safe_divide(numerator, denominator):
    try:
        x = float(numerator)
        y = float(denominator)
    except (TypeError, ValueError):
        print("Error: Please enter numeric values only.")
        return
    try:
        j = x / y
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return
    # Print the result in the required format
    print(f"The result of the division is {j}")



