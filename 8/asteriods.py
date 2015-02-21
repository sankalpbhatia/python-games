# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0.5
started=False

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(0.5)
ship_thrust_sound = simplegui.load_sound("https://dl.dropbox.com/s/rpnyczqnoha2a50/thrustmm.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    global a_missile
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
        
        
    def draw(self,canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "White", "White")
        canvas.draw_image(self.image,self.image_center,self.image_size,self.pos,self.image_size,self.angle);
        if self.thrust:
             center = [0,0]
             center[0] = self.image_center[0]+self.image_size[0]
             center[1] = self.image_center[1]
             canvas.draw_image(self.image, center, self.image_size, self.pos, self.image_size,self.angle)
            
    def update(self):
        self.pos[0]+=self.vel[0]
        self.pos[1]+=self.vel[1]
        self.angle+=self.angle_vel
        
        forward=angle_to_vector(self.angle)
        if self.thrust:
            self.vel[0]=self.vel[0]+0.5*forward[0]
            self.vel[1]=self.vel[1]+0.5*forward[1]
            
            
        self.pos[0] = self.pos[0]%WIDTH
        self.pos[1] = self.pos[1]%HEIGHT
        
        self.vel[0]*=0.98
        self.vel[1]*=0.98
       
    def angle_chp(self):
        self.angle_vel=0.05
    def angle_chn(self):
        self.angle_vel=-0.05
        
    def isOn(self):
        self.thrust=True
        ship_thrust_sound.play()
        
        
    def shoot(self):
        global missile_group
        forward=angle_to_vector(self.angle)
        #print forward
        velx=self.vel[0]+6*forward[0]
        vely=self.vel[1]+6*forward[1]
        posx=self.pos[0]+35*forward[0]
        posy=self.pos[1]+35*forward[1]
        a_missile=Sprite([posx,posy],[velx,vely],0,0,missile_image,missile_info,missile_sound)
        missile_group.add(a_missile)
    def get_radius(self):
        return self.radius
    
    def get_position(self):
        return self.pos

    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        canvas.draw_image(self.image,self.image_center,self.image_size,self.pos,self.image_size,self.angle)
    def update(self):
        
        self.pos[0]+=self.vel[0]
        self.pos[1]+=self.vel[1]
        self.angle+=self.angle_vel
        self.pos[0] = self.pos[0]%WIDTH
        self.pos[1] = self.pos[1]%HEIGHT
        
        self.age+=1
        if(self.age>self.lifespan):
            return True
        return False
    def get_radius(self):
        return self.radius
    
    def get_position(self):
        return self.pos
    
    def collide(self,other_object):
        or1=other_object.get_radius()
        op=other_object.get_position()
        sr=self.get_radius()
        sp=self.get_position()
        t=(sp[0]-op[0])**2 + (sp[1]-op[1])**2
        d=math.sqrt(t)
        
        if d<sr+or1:
            return True
            print hi
        else:
            return False
def group_collide(group,other_object):
    global number
    temp=set(group)
    
    for i in temp:
        if i.collide(other_object)==True:
            group.discard(i)
            number=number-1
            return True
            
    return False

def group_group_collide(g1,g2):
    global number
    t1=set(g1)
    t2=set(g2)
    num=0
    for i in t1:
        t=group_collide(g2,i)
        if t:
            num=num+1
            g1.remove(i)
         
    return num       
           
def draw(canvas):
    global time,lives,score,started,number,rock_group,missile_group
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_text('Lives',[30,20],20,'Cyan')
    canvas.draw_text('Score',[700,20],20,'Cyan')
    canvas.draw_text(str(lives),[30,45],20,'Cyan')
    canvas.draw_text(str(score),[730,45],20,'Cyan')
    
    # draw ship and sprites
    my_ship.draw(canvas)
 
   
    
    # update ship and sprites
    my_ship.update()
    
    
    
    process_sprite_group(rock_group,missile_group,canvas)
    
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
        
    if(group_collide(rock_group,my_ship)):
            lives=lives-1
    score =score+(group_group_collide(missile_group,rock_group))
     
    if lives==0:
        score=0
        missile_group=set([])
        rock_group=set([])
        started=False
        #soundtrack.rewind()
def process_sprite_group(grp,grp2,canvas):
    global started
    global number
    tg=set(grp)
    tg2=set(grp2)
    if  started:
        for i in tg:
            t=i.update()
            if(t):
                number=number-1
                grp.remove(i)
            i.draw(canvas)
        
        for j in tg2:
            tt=j.update()
            if(tt):
                number=number-1
                grp2.remove(j)
            j.draw(canvas)
    
    
    
    
def keydown(key):
    
   
    global started
    if key==simplegui.KEY_MAP["right"]:
        my_ship.angle_chp()
        
        
    if key==simplegui.KEY_MAP["left"]:
        my_ship.angle_chn()
   
         #print 4
    if key==simplegui.KEY_MAP["up"]:
       my_ship.isOn()
        
    if key==simplegui.KEY_MAP["space"] and started:
       my_ship.shoot()
   
def keyup(key):
    
    if key==simplegui.KEY_MAP["right"]:
       my_ship.angle_vel=0
        
    if key==simplegui.KEY_MAP["left"]:
       my_ship.angle_vel=0
    if key==simplegui.KEY_MAP["up"]:
       my_ship.thrust=False
       ship_thrust_sound.rewind()
def click(pos):
    global started,lives,score,number
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        lives=3
        number=0
        score=0
        soundtrack.rewind()
        soundtrack.play()

            
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group,number
    
    ang=0.5*random.randrange(0,2)
    angvel = random.random()*0.4 + -0.2
    velx=random.randrange(-3,3)
    vely=random.randrange(-3,3)
    
    posx=random.randrange(0,WIDTH)
    posy=random.randrange(0,HEIGHT)
    if number<12 and started:
        
        a_rock=Sprite([posx,posy],[velx,vely],ang,angvel,asteroid_image,asteroid_info)
        rock_group.add(a_rock)
        number=number+1;
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [1, 0], 0, ship_image, ship_info)
#a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, -1], 0, 0.1, asteroid_image, asteroid_info)
#a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)
rock_group=set([])
missile_group=set([])
number=0
# register handlers
frame.set_draw_handler(draw)

frame.set_keydown_handler(keydown)
frame.set_mouseclick_handler(click)
frame.set_keyup_handler(keyup)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
