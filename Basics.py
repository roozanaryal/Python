import math

print("Python First Program")

greeting='Hello World'        #Assigning Values in Variable(String)
print(greeting)

line01="*********"    # comment
line02="*Welcome*"

print(line01)
print(line02)
print(line01)

print(" ")

#IF Else Statement In Python

meaning=20

if meaning<10:
    print("Not Today")
else:
    print("This is Fucked Up")


#Ternary Operator
print("Right On!") if meaning < 10 else print("Hacker Hai Vai!")

#Checking The Type of Variable
a_var='Car'
print(type(a_var))
print(isinstance(a_var,str))    #Checking if this is string

#literal Assigning
pizza=str("Pepperoni")

#string concatination
decade=str(1980)
statement="I like Rock music form the " + decade + "'s."
print(statement)

#multiline
a='''
Hey?        
How
    are 
        You?
'''
print(a)

#Escaping special character
print('I\'m Back \n Hehe!')

#String Methods
name="Roozan"
print(name)
print(name.lower())
print(name.upper())

print(a.title())
print(a.replace("How","Why"))
print(len(a))
print(len(a.strip()))

print("")

#Justifying Techniques
x="Menu".upper()
print(x.center(20,"="))
# print("Coffee".ljust(16,".") + "1$"rjust(4))
# print("Cheese Cake".ljust(16,".") + "6$"rjust(4))

#Letter Extraction form String
print(x[0])
print(x[-1])
print(x[0:2]) #goes to 0 index to 2
print(x[2:]) #Goes to 2 index to end 
print(x.startswith("M"))
print(x.endswith("U")) #false as U is in capital

#Using Math Module

gpa=3.28
print(math.ceil(gpa))
print(math.sqrt(64))

#Casting a string to integer
zip_code="1111101"
zip_value=int(zip_code)

