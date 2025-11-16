#  Function with arguments & parameters

def FunWithArgu(name):                     # "name" is parameter
    print(name+" is my email address.")

FunWithArgu("er.tejaskalmegh@gmail.com")   # "er.tejaskalmegh@gmail.com" is argument


#  Function with numbers of arguments

def FunWithArgu2(fname,lname):
    print(fname + " " + lname)

FunWithArgu2("Tejas","Kalmegh")


#  Function with default parameter values
#  You can assign default values to parameters. If the function is called 
#  without an argument, it uses the default value

def functiondemo(country = "India"):
    print("I am from " + country)

functiondemo("Japan")
functiondemo()
functiondemo("Russia")


#  Function with keyword arguments
#  You can send arguments with the key = value syntax

def functiondemo2(myname,animal):
    print("I am " + myname)
    print("I love " + animal + "'s")

functiondemo2(myname = "Tejas",animal = "Cat")

# This way with keyword arguments, the order of the arguments does not matter

def functiondemo3(animal,myname):
    print("I am " + myname)
    print("I love " + animal + "'s")

functiondemo3(animal = "Cat",myname = "Tejas")


#  Functional with positional arguments
#  When you call a function with arguments without using keywords,
#  they are called positional arguments
#  Positional arguments must be in the correct order

def functiondemo4(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

functiondemo4("dog", "Buddy")

#  The order matters with positional arguments

def functiondemo5(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

functiondemo5("Buddy", "dog")
