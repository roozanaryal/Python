#Loops in Python
value=1
while value<=10:
    print(value)
    # if value==6: #It goes till 6 if this is not commented
    #     break
    value+=1
print("")
v=1
while v<10:
    v+=1
    if v==6: #It skips 6
        continue
    print(v)
else:
    print("Value is equal to "+ str(v)) #we typecast it to string as only string can be concatinated 
    #and also this else is outside the while loop

#For Loop
name=["Rojan","Yunish","Aashish"]
for x in name: #this is to print every name in list
    print(x)
print("")

for x in "Rojan": #this is to print individual letters in name rojan
    print(x)

print("")
for x in name:#this is to print only rojan
    if x=="Yunish":
        break
    print(x)

#for loop to print range of numbers
for i in range(4): #print the range of number form 0 to 3
    print(i)
print("")
for i in range(3,7): #prints the range of numbers from 3 to 6 as 7 is not included
    print(i)
print("")
#to print table of 5 in Python
for i in range(5,51,5): #the last column which has number 5 means that number should be incremented by 5 
    print(i)
else:
    print("Glad that\'s over") #the backward slash is to ignore that ( ' ). 

names=["Rojan"]
action=["Codes","Eates","Travel","Sleeps"]
for n in names:
    for a in action:
        print(n + " " + a)