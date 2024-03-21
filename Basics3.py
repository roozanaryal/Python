#Dictionaries
dict1 ={
    "vocals":"plant",
    "guitar":"page"
}
dict2=dict(vocals="plant",guitar="page")

print(dict1)
print(dict2)
print(len(dict2))

#Accessing Item in Dictionary
print(dict2["vocals"])
print(dict2.get("guitar"))
#list all keys
print(dict1.keys())
#list all values
print(dict2.values())
#list of key value pair as tuples
print(dict1.items())
#verify if key exist in dictionary
print("guitar" in dict1)

#changing values in dictionary
dict1["vocals"]="tatti"
dict1.update({"bass":"JPJ"})
#remove item
print(dict1.pop("bass"))#.popitem will delete and not print the last element
del dict1["vocals"]
del dict2
dict2=dict1 #this is not a copy but a refrence
dict3=dict1.copy()#correct method
dict4=dict(dict1)

#Nested dictionaries
mem1={
    "name":"rojan",
    "sirname":"aryal"
}
mem2={
    "name":"ram",
    "sirname":"aryal"
}
mem3={
    "this":mem1,
    "shit":mem2
}
print(mem3)
print(mem3["this"]["name"])


#Sets
nums={1,2,3,4}
nums2=set((1,2,3,4))
#sets ignore dublicate data
nums.add(8)#to add
addnums={5,6,7}
nums.update(addnums)

one={1,2,3,4,5}
two={5,6,7}
unoset=one.union(two)
print(unoset)
