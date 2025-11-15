#  Function with no return value

def functiondemo():
    print("Welcome to demo function!")

functiondemo()
functiondemo()
functiondemo()


#  Function with return value 

def functiondemo2():
    return "This is return value string"

message = functiondemo2()
print(message)


#  Function with pass statement
# Function definitions cannot be empty. we need to create a function 
# placeholder without any code, use the pass statement

def functiondemo3():
    pass

