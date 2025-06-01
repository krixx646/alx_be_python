# multiplication_table.py

# Prompt for a number (exact text)
number = int(input("Enter a number to see its multiplication table: "))

# Loop from 1 to 10 (inclusive)
for x in range(1, 11):
    print(f"{number} * {x} = {number * x}")
