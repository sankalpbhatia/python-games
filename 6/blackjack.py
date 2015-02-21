# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
outcome2="Hit or Stand?"

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.clist=[]	# create Hand object

    def __str__(self):
        s="Hand contains "
        for i in self.clist:
            s=s+str(i)+" "# return a string representation of a hand
        return s
    def add_card(self, card):
        self.clist.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        no=0
        value=0
        for i in self.clist:
            if i.rank=='A':
                no=no+1
            value=value+VALUES[i.rank]
        if no==0:
                return value
        else:
            if value+10<=21:
                    return value+10
            else:
                    return value
            
    def draw(self, canvas, pos):
        t=pos[0]
        for i in self.clist:
            
            #print t
            i.draw(canvas,[t,pos[1]])
            t=t+72# draw a hand on the canvas, use the draw method for cards
        

    
        
# define deck class 
class Deck:
    def __init__(self):
        self.cl=[]
        
        for i in SUITS:
            for j in RANKS:
                c1=Card(i,j)
                self.cl.append(c1)
            # create a Deck object

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cl)    # use random.shuffle()

    def deal_card(self):
        # deal a card object from the deck
        c1= self.cl[-1]
        self.cl.pop()
        return c1
    def __str__(self):
        s="Deck has "
        for i in self.cl:
            s=s+str(i)+" "
          
        return s# return a string representing the deck

deck=Deck()

dealer_hand=Hand()
player_hand=Hand()

#define event handlers for buttons
def deal():
    global outcome, in_play,deck,player_hand,dealer_hand,outcome2,score
    if in_play:
        score=score-1
    outcome=""
    outcome2="Hit or Stand?"
    deck=Deck()
    random.shuffle(deck.cl)
    player_hand=Hand()
    dealer_hand=Hand()
    c1=deck.deal_card()
    player_hand.add_card(c1)
    c2=deck.deal_card()
    player_hand.add_card(c2)
    
    c3=deck.deal_card()
    dealer_hand.add_card(c3)
    c4=deck.deal_card()
    dealer_hand.add_card(c4)
    
    
   # print "Player "+ str(player_hand)
   # print "Dealer "+str(dealer_hand)
    # your code goes here
    
    in_play = True

def hit():
    # replace with your code below
    global player_hand,deck,in_play,score,outcome,outcome2
    # if the hand is in play, hit the player
    if player_hand.get_value()<=21 and in_play==True:
        c=deck.deal_card()
        #print str(c)
        player_hand.add_card(c)
        #print player_hand.get_value()
        if player_hand.get_value()>21 and in_play==True:
            
            outcome="You have been Busted, YOU LOSE!!"
            outcome2="..New Deal??"
            in_play=False
            score=score-1
        
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    # replace with your code below
    global player_hand,in_play,dealer_hand,outcome,score,outcome2
    if player_hand.get_value()>21:
        outcome="You have already been busted!!"
        outcome2="..New Deal??"
        in_play=False
       # score=score-1
    while dealer_hand.get_value()<17 and in_play:
        c=deck.deal_card()
        dealer_hand.add_card(c)
    if dealer_hand.get_value()>21 and in_play:
        outcome="Dealer Busted, You win!!"
        outcome2="..New Deal??"
        in_play=False
        score=score+1
    if dealer_hand.get_value()>=player_hand.get_value() and in_play:
        outcome="Dealer wins!!"
        outcome2="..New Deal??"
        in_play=False
        score=score-1
    if dealer_hand.get_value()<player_hand.get_value() and in_play:
        outcome="You win!!"
        outcome2="..New Deal??"
        in_play=False
        score=score+1
        
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('BLACKJACK', (250, 60), 30, 'Cyan','monospace')
    canvas.draw_text(outcome, (180, 100), 20, 'Black','sans-serif')
    canvas.draw_text(outcome2, (200, 320), 22, 'Black','sans-serif')
    global player_hand,dealer_hand
    canvas.draw_text('Player', (100, 380), 22, 'Black')
    player_hand.draw(canvas, [100, 400])
    canvas.draw_text('Dealer', (100, 140), 22, 'Black')
    dealer_hand.draw(canvas, [100, 160])
    if in_play:
       canvas.draw_image(card_back,CARD_BACK_CENTER, CARD_BACK_SIZE, [136,208], CARD_SIZE)
    canvas.draw_text('Score', (500, 50), 25, 'Black')
    canvas.draw_text(str(score), (510, 80), 25, 'Black')
    
def rscore():
    global score  
    score=0


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.add_button("Reset score", rscore, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric