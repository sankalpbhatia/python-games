# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 15
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos=[300,200]
ball_vel=[1,1]
paddle1_pos=HEIGHT/2
paddle2_pos=HEIGHT/2

paddle1_vel=0
paddle2_vel=0
score1=0
score2=0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[300,200]
    if direction==False:
        ball_vel[0]=random.randrange(-5,-2)
        ball_vel[1]=random.randrange(-6,-2)
    elif direction==True:
        ball_vel[0]=random.randrange(3, 5)
        ball_vel[1]=random.randrange(-4,-1)

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2 # these are ints
    score1=0
    score2=0
    spawn_ball(True)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel,paddle2_vel
 
    canvas.draw_text(str(score2),[130,30],24,"Red") 
    canvas.draw_text(str(score1),[430,30],24,"Red")
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0]+=ball_vel[0]
    
    ball_pos[1]+=ball_vel[1]
    
    if ball_pos[1]<=BALL_RADIUS or ball_pos[1]>=HEIGHT-BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
    if ball_pos[0]<=(BALL_RADIUS+PAD_WIDTH):
        if ball_pos[1]<=paddle1_pos+40 and ball_pos[1]>=paddle1_pos-40:
            ball_vel[0]=-ball_vel[0]
            ball_vel[0]=1.1*ball_vel[0]
            ball_vel[1]=1.1*ball_vel[1]
        else:
            spawn_ball(RIGHT)
            score1+=1
            canvas.draw_text(str(score1),[430,30],24,"Red")
    if score1==3:
        canvas.draw_text("Player 2 Wins!!!",[200,100],36,"BLUE");
        ball_vel[0]=0
        ball_vel[1]=0
            
    if ball_pos[0]>=(600-(BALL_RADIUS+PAD_WIDTH)):
        if ball_pos[1]<=paddle2_pos+40 and ball_pos[1]>=paddle2_pos-40:
            ball_vel[0]=-ball_vel[0]
            ball_vel[0]=1.1*ball_vel[0]
            ball_vel[1]=1.1*ball_vel[1]
        else:
            spawn_ball(LEFT)
            score2+=1
            canvas.draw_text(str(score2),[130,30],24,"Red")
    if score2==3:
        canvas.draw_text("Player 1 Wins!!!",[200,100],36,"BLUE");
        ball_vel[0]=0
        ball_vel[1]=0
   
        
    
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,0.5,"Red","Red")
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos<=40 and paddle1_vel==-5:
        paddle1_vel=0
    if paddle1_pos>=360 and paddle1_vel==5:
        paddle1_vel=0
    paddle1_pos+=paddle1_vel
    if paddle2_pos<=40 and paddle2_vel==-5:
        paddle2_vel=0
    if paddle2_pos>=360 and paddle2_vel==5:
        paddle2_vel=0
    paddle2_pos+=paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([[0,paddle1_pos-40],[0,paddle1_pos+40],[8,paddle1_pos+40],[8,paddle1_pos-40]],2,"White","White")
    canvas.draw_polygon([[600,paddle2_pos-40],[600,paddle2_pos+40],[592,paddle2_pos+40],[592,paddle2_pos-40]],2,"White","White")
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel,paddle1_pos,paddle2_pos
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel=-5
        
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel=5
    if key==simplegui.KEY_MAP["w"]:
         paddle1_vel=-5
    if key==simplegui.KEY_MAP["s"]:
         paddle1_vel=5
         #print 4
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel,paddle1_pos,paddle2_pos
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel=0
        
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel=0
    if key==simplegui.KEY_MAP["w"]:
         paddle1_vel=0
    if key==simplegui.KEY_MAP["s"]:
         paddle1_vel=0
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",new_game)
frame.add_label("P-1:Up- 'w' Down- 's' key")
frame.add_label("P-2:Up- 'Up' Down- 'Down' key")


# start frame
new_game()
frame.start()
