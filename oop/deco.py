#1.Create only with function

#Add two function
def addtwo(a,b):
     return a+b

#Add three function by using add two
def addthree(a,b,c):
     result = addtwo(a,b)+c
     print(f"Addition of three number is : {result}")

#function calling
addthree(2,3,4)

#2.Create with decorator

#a.First create the decorator
def decorate_add_three(func):
    
    def wrapper(a,b,c):
        result = func(a,b)+c
        print(f"adiition of three number is : {result}")
    return wrapper
     
#apply decorator    
@decorate_add_three
def addtwo(a,b):
    return a+b

addtwo(2,3,4)

#2.first create original funcyion that you want decorate

#addtwo function
def addtwo(a,b):
    return a+b

#Decorator
def decorate_add_three(func):
    def wrapper(a,b,c):
        result = func(a,b)
        total = result + c
        print(f"addition of three number is : {total}")
    return wrapper

#Apply the decorator on original function
@decorate_add_three
def addtwo(a,b):
    return a+b

#Call the function
addtwo(2,4,3)

#4.Without using @decorator
#add two function
def addtwo(a,b):
    return a+b

#decorator
def decorator_add_three(func):
    def wrapper(a,b,c):
        result = func(a,b)
        total = result+c
        print(f"addition of three number is : {total}")
    return wrapper

#Applying decorator
addtwo = decorate_add_three(addtwo)

addtwo(2,4,3)