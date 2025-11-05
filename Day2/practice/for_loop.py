# for loop 


for x in range(1, 11):
    print(x)


# break statement 

for y in range(21, 31):
    if y == 27:
        break
    else:
        print(y)

# continue statement

for z in range(51, 61):
    if z == 57:
        continue
    else:
        print(z)

# pass statement

for a in range(31, 41):
    pass

# if for some reason have a for loop with no content,
# so put the pass statement to avoid getting an error