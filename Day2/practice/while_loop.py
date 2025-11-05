# while loop

num = int(input("enter a number between 1 to 10: "))

while num < 1 or num > 10:
    print(f"{num} this number is not valid!")
    num = int(input("enter a number between 1 to 10: "))

print(f"your number is {num}")    

# while loop execute some code while some condirion remain true