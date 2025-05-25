# User monthly income calculator
# finance_calculator.py
mi = float(input("Enter your monthly income: "))
me = float(input("Enter your monthly expenses: "))
ms = mi - me

# project annual savings
ps = ms * 12 + (ms * 12 * 0.05)  # Assuming a 5% interest rate on savings   

print(f"Your monthly savings are: {ms}")
print("Projected savings after one year, with interest, is: {:.2f}".format(ps))
# Output: Your monthly savings are: 500.0
# Output: Projected savings after one year, with interest, is: 6300.00