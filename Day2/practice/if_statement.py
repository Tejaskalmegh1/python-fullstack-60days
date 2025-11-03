# if statement

num1 = 100
num2 = 50
num3 = -15

# condition of if statement 
if num1 > num2:
    print("First number is greater!")


# AND operator: Returns True if both statements are true
if num1 and num2 > 0:
    print("Both Numbers are Possitive!")


# OR operator: Returns True if one of the statements is true
if num3 > 0 or num3 == 0:
    print("Number is Negative or zero!")


# NOT operator: Reverse the result, returns False if the result is true
if not( num3 < 10 and num3 > 20 ):
    print("False!")     

