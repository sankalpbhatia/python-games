# implementation of card game - Memory

import simplegui
import random
list_num=range(0,8)+range(0,8)
random.shuffle(list_num)
com1=[0,0]
com2=[0,0]
score=0
exposed=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

# helper function to initialize globals
def new_game():
    global state
    global score
    global exposed
    state=0
    score=0
    exposed=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

     
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state
    global score
    global exposed
    global com1,com2
    
    j=pos[0]/50+1
    if state == 0:
        state = 1
        exposed[j-1]=True
        com1[0]=list_num[j-1]
        com1[1]=j-1
        score=score+1
    elif state == 1:
        state = 2
        exposed[j-1]=True
        com2[0]=list_num[j-1]
        com2[1]=j-1
        #score=score+1
    else:
        state = 1
        exposed[j-1]=True
        if com1[0]!=com2[0]:
            exposed[com1[1]]=False
            exposed[com2[1]]=False
            
        com1[0]=list_num[j-1]
        com1[1]=j-1  
        score=score+1
   # label = frame.add_label("Turns = "+ str(score))      
    #print state
   # print score 
    label.set_text("Turns = "+ str(score))
    #print exposed[j-1]
 
    
    
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    i=0
    j=100
    k=100
    global exposed 
    global score
    global list_num
    num=0
    l=0
    for num in list_num:
        
        
        if exposed[l]:
             canvas.draw_text(str(num),(i,j),100,"White")
        elif not exposed[l]:
             canvas.draw_polygon([(i,100),(i,0),(i+50,0),(i+50,100)],2,"Black","Green")
       
        i=i+50
        l=l+1
       
        


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = "+ str(score))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric