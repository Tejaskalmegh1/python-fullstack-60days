def prime(num):
    if num <= 1:
       return False
    
    if num <= 3:
        return True
    
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 5
    while i * 2 <= num:  
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    
    return True 

print(prime(7))   
print(prime(12))  
print(prime(97))  

