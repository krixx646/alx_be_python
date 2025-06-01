#Pattern printer
pattern_num = int(input("Enter the size of the pattern: "))

x = 0
while x < pattern_num:
    for y in range(pattern_num):
        print("*", end="")
    print()
    x = x + 1
print("Done!")