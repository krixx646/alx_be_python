# simple calculator script using a match case
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
oprator = input("choose your operator (+,-,*,/): ")

match oprator:
    case "+":
        num = num1 + num2
    case "/":
        num = num1 / num2
    case "*":
        num = num1 * num2
    case _ :
        num = num1 - num2
print(f"the result of {num1} and {num2} is {num:.2f}")