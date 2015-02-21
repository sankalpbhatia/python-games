# Rock-paper-scissors-lizard-Spock template

import random
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name=='rock':
        number=0
    if name=='Spock':
        number=1
    if name=='paper':
        number=2
    if name=='lizard':
        number=3
    if name=='scissors':
        number=4
    return number  

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number==0:
        name='rock'
    if number==1:
        name='Spock'
    if number==2:
        name='paper'
      
    if number==3:
        name='lizard'
        
    if number==4:
        name='scissors'
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    return name

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    print '\n'
    
    # print a blank line to separate consecutive games

    # print out the message for the player's choice
    print 'Player chooses ',player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_num=name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_num =random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice=number_to_name(comp_num)
    # print out the message for computer's choice
    print 'Computer chooses', comp_choice
    # compute difference of comp_number and player_number modulo five
    diff=(comp_num-player_num)%5
    # use if/elif/else to determine winner, print winner message
    if diff==3 or diff==4:
        print 'Player wins!'
    elif diff==1 or diff==2:
        print 'Computer wins!'
    else:
        print 'Player and Computer tie!'
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


