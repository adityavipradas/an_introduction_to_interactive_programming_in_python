# Rock-Paper-Scissors-Lizard-Spock
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

#assign name to given number
def number_to_name(number):
    if (number == 0):
        name = "rock"
    elif (number == 1):
        name = "spock"
    elif (number == 2):
        name = "paper"
    elif (number == 3):
        name = "lizard"
    elif (number == 4):
        name = "scissors"
    else:
        name = "null"
    return name                

#assign number to given name
def name_to_number(name):
    if (name == "rock"):
        num = 0
    elif (name == "spock"):
        num = 1
    elif (name == "paper"):
        num = 2
    elif (name == "lizard"):
        num = 3
    elif (name == "scissors"):
        num = 4
    else:
        num = 5
    return num

#decide winner
def rpsls(guess):
    
    player_number = name_to_number(guess)
    
    #Print player's choice
    
    print "Player chooses",guess
    
    #Select random computer's choice
    
    comp_number = random.randrange(0,5)
    
    #Convert computer's choice to name
    
    comp_name = number_to_name(comp_number)
    
    #Print computer's choice
    
    print "Computer chooses",comp_name 
    
    subtract = player_number - comp_number
    
    rem = subtract % 5
    
    if (rem == 1 or rem == 2):
        print "Player wins!\n"
    elif (rem == 3 or rem == 4):
        print "Computer wins!\n"
    else:
        print "Player and computer tie!\n"
    
    return 0


rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
