# multiplication table using for

num = int(input("Enter a number to generate table: "))

for x in range(1, 11):
    print(f"{num} * {x} = {num*x}")
