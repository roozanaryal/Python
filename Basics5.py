#functions in python
def hello():
    print("Hello World!")
hello()

def sum(num1 , num2):
    print( num1 + num2)

sum(5,10)

def add(num1=0 , num2=0): #passing deault argument
    if(type(num1) is not int or type(num2) is not int): #If anything that is not integer is passed then it reuturns none 
        return
    return num1 + num2

total=add(5,10)
print(total)

#Defining the function which has unknown number of parameter
def multiple_item(*args): #with double astrick ** we can input dictionary (also known as kwargs for **)
    print(args)
    print(type(args))

multiple_item(4,5,6)