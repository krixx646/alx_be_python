# User monthly income calculator
# finance_calculator.py

monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses

# project annual savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)  # Assuming a 5% interest rate on savings

print(f"Your monthly savings are: {monthly_savings}")
print("Projected savings after one year, with interest, is: {:.2f}".format(projected_savings))
