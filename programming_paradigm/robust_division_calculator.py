def safe_divide(numerator, denominator):
    try:
        x = float(numerator)
        y = float(denominator)
    except (TypeError, ValueError):
        return "Error: Please enter numeric values only."
    try:
        result = x / y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    return f"The result of the division is {result}"



