# Simple multiplication table
multiply = int(input("Enter a number to see its multiplication table: "))
jam = 0
for x in range(11):
    print(f"{multiply} * {x} = {multiply * x}")
    jam += (multiply * x)
print(f"the addition of all the product of the multiplication table of {multiply} is {jam}")
print("Done!")