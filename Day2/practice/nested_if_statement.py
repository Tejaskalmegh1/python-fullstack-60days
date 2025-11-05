# nested if statement 

num = 21

if num > 10:
    print("Number is greater than 10")
    if num > 20:
        print("Also greater than 20")
    else:
        print("But not greater than 20")
else:
    print("Number is less than 10")
