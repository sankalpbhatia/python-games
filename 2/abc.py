import simplegui
import random
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

secret_number=0
rem=7
temp=rem

rang=100

# helper function to start and restart the game
def new_game():
    global rang
    global secret_number
    secret_number=random.randrange(0,rang)
    # initialize global variables used in your code here
    print "New game. Range is from 0 to",rang
    print "No. of remaining guesses is",rem
    # remove this when you add your code    
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global rang
    rang=100
    global rem 
    global temp
    temp=7
    rem=7
   
    # remove this when you add your code'
    new_game()    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
     global rang
     global rem
     global temp
     rem=10
     temp=10
     rang=1000
     
     new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    num=int(guess)
    print "Guess was",num  
    global rem
    global temp
    rem=rem-1
    print "No. of remaining guesses is",rem
    
        
    if num<secret_number:
         print "Higher!"
    elif num>secret_number:
         print "Lower!"
    else :
        print "Correct!"
        rem=temp
        new_game()
    if rem==0:
        rem=temp
        new_game()
    # remove this when you add your code
    

    
# create frame
f=simplegui.create_frame("Guess the Number",200,200)

# register event handlers for control elements and start frame
f.add_button("Range is [0-100]",range100,200)
f.add_button("Range is [0-1000]",range1000,200)
f.add_input("Enter a guess",input_guess,200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
