# sum of numbers from 1 to n using while loop

num = int(input("enter the N'th number: "))
x = 1
ans = 0

while x <= num :
    ans += x
    x+=1
    
print(f"Sum of numbers form 1 to {num}: {ans}")     
