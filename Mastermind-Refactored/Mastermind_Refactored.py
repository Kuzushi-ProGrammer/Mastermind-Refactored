#Remake mastermind but better

#Take input                         check
#Check nums                         
#Sort based on colour
#If all wrong print one red
#If all right win game

from distutils.command.config import config
from math import fabs
import random
import colorama
from colorama import Fore, Back, Style

num_list = []
player_input_list = []
config_list = []
input_active = True
n = 0

for x in range(3):
    num =  random.randint(0, 9)
    num_list.append(num)

print(num_list)
# --------------------------------------------------------- # Input system #
while input_active == True:

    player_input = input("num here: ")
    
    try:
        int(player_input)
        
        if len(player_input) <= 3:
                print(player_input)
                input_active = False

        elif len(player_input) >= 3:
            print("Too many characters, try again.")

    except:
        print("Invalid Character(s), please try again.")

# --------------------------------------------------------- #

for x in player_input:
    player_input_list.append(int(x))

print(player_input_list)

for x in num_list:
    if player_input_list[n] in num_list:        #Two of the same number can register as yellow (e.g ans = 123 input = 333 output = GYY)
        print("yes in list")
        if player_input_list[n] == x:
            print("same spot too")
            config_list.insert(0, "Green")
        else:
            print("not same spot")
            config_list.append("Yellow")

    else:
        print("not in list")
        
    n+=1

try:
    if config_list[0] == None:
        pass
except:
        config_list.append("Red")
        print("no elements")

print(config_list)

input("- Press any Button to Exit -")


