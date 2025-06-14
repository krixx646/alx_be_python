# try and catch error handling

def safe_divide(numerator, denominator):
    try:
       x = float(numerator)
       y = float(denominator)
    except Exception as e:
        print(f'one or both of the input is not a float or not decimal', e)
        return
    try:
        j = x / y
    except ZeroDivisionError as e:
        print(f"{e}, we have talked about this, use your brain")
        return
    return j


