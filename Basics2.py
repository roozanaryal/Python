user=['Rojan','Yunish']
list_=['Rojan',1,True]
emptylist=[]

print("Rojan",in user) #output is ture as Rojan is in user list
print("Rojan",in emptylist)
print(user[0])
print(list_[-2])
print(user.index('Yunish'))
print(list_[1:2])
print(len(list_)) #returns 3 as there are 3 data, doesnt starts counting form 0
list_.append('Kushal')
user += ['Aashish'] #Another way to appent user in list
list_.extend(['Aakash','Kedar'])
list_.extend(user) #We can even add whole list in here
user.insert(0,'Ram') #We add Ram to the first index
user[2:2]=['Bharat','Shyam'] #adding two from two
user.remove('Bharat')
del user[0] #deleting user at zero index
user.sort() #sort data in array in alphabetical order Capital then samll
user.sort(key=str.lower)
nums=[1,2,4,5,3]
nums.reverse() #prints the list in reverse order
nums.sort(reverse=True) #arranging in reverse order
print(sorted(nums,reverse=True)) #only prints but donot change list order

#Methods to create copy of lists
n=nums.copy()
mynums=list(nums)
copy=nums[:]
m=list(['Ram',1])#another way to create list

#Tuples
mytuple=tuple(('Ram',1,True))
anothertuple=('Shyam',2,3,4)
newlist=list(mytuple)#so that we can manupulate the date in it 
#the again we convert it to tuple like so
(one,two,*three)=anothertuple #the * hold the remaining value #if * is in second then it will hold the all middle value
print(one)
print(two)
print(three)
print(anothertuple.count('Shyam')) #Will count the occurance of shyam in tuple




