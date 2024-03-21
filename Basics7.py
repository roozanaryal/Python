name="Rojan"#Global varible

def greeting():
    colour="red"
    print(name)
greeting()
# print(colour) #This is wrong as colour is in local scope of the function
#We can also make nested function


n="Raj"
count=1

def nf():
    col="Pink"
    global count
    count+=1
    print(count)

    def af():
        nonlocal col
        col="Red"
        print(col)
    af()#calling in the nf function

nf()
# af() #we cannot call nested function outside the finction