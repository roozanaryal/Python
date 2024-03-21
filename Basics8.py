#closure is a function having accesss to the scope of its parents
#function after the parent function has returned
def parent_fun():
    coins=3
    def child_fun():# this is closure function
        nonlocal coins
        coins-=1

#f_string in python 
person="Rojan"
paisa=5
message="{} has {} Rs with him.".format(person,paisa)
print(message)

person="Rojan"
paisa=5
message="{1} has {0} Rs with him.".format(paisa,person)
print(message)

player={'name':'Rojan','cash':150}
mess="{name} has {cash} Rupees.".format(**player)
print(mess)

mess=f"{person.lower()} has {paisa} Rupees." #fstring method
print(mess)

mess=f"{player['name']} has {15*10} Rupees."
print(mess)