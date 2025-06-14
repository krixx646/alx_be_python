# try and catch error handling

def safe_divide(numerator, denominator):
    try:
       x = float(numerator)
       y = float(denominator)
    except (TypeError, ValueError) as e:
        print(f'one or both of the input is not a float or not decimal', e)
        return
    try:
        j = x / y
    except ZeroDivisionError:
        # Exactly match the required message:
        print("Error: Cannot divide by zero.")
        return
    return j


