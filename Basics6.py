import sys
import random
from enum import Enum

def rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSOR =3

        # #Taking Input form User
        # value=input('Please Input a Value \t')
        # print("\t"+value)



    print("")
    playerchoice=input("Enter.....\n 1 for Rock\n 2 for Paper \n 3 for Scissor\n\t")
    if playerchoice not in ["1","2","3"]:
        print("Invalid Input")
        return rps()
    
    player=int(playerchoice)
    computerchoice=random.choice("123")
    computer=int(computerchoice)
    print("")
    print("You Chose" + str(RPS(player)).replace("RPS.","") + ".")
    print("Python Chose" + str(RPS(computer)).replace("RPS.","") + ".") #If we donot use replace answer will come like RPS. Paper.....* 
    print("")

    if player==1 and computer==3:
        print("You Win!")
    elif player==2 and computer==1:
        print("You Win!")
    elif player==3 and computer==2:
        print("You Win!")
    elif player==computer:
        print("Tie Game")
    else:
        print("Python Wins!")

    playagain=input("\n Wanna Play Again?\n Press Y to Continue and N to Quit!")
    if playagain.lower() == "y":
        continue
    else:
        print("Thank you for Playing")
        playagain=False
sys.exit()