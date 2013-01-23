#KINDLY RELOAD THE CODE 3-4 TIMES IF THINGS DO NOT LOAD UP IN FIRST GO
#.....................................................................
#APOLOGY FOR THE INCONVENIENCE........................................
#.....................................................................
# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
width = 800
height = 600
score = 0
lives = 3
time = 0

def incr():
    my_ship.increment()
    
def decr():
    my_ship.decrement()
    
def acc():
    ship_thrust_sound.play()
    ship_thrust_sound.set_volume(1)
    my_ship.thrust = True
    my_ship.thrusters()

def bullet():
    missile_sound.play()
    missile_sound.set_volume(1)
    a_missile.pos[0] = my_ship.pos[0] + (my_ship.image_size[0]/2)*angle_to_vector(my_ship.angle)[0]
    a_missile.pos[1] = my_ship.pos[1] + (my_ship.image_size[1]/2)*angle_to_vector(my_ship.angle)[1]
    a_missile.vel[0] = 15*(angle_to_vector(my_ship.angle)[0])
    a_missile.vel[1] = 15*(angle_to_vector(my_ship.angle)[1])

def misc():
    my_ship.thrust = False
    my_ship.decel = True
    
press = {"right": incr, "left": decr, "up": acc, "space": bullet}
release = {"right": decr, "left": incr, "up": misc}

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
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.png")

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
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)

# Ship class
class Ship:
    def __init__(self, pos, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.thrust = False
        self.decel = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.boost = 1
        self.orient = angle
        
    def draw(self,canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "White", "White")
        if (self.thrust == False):
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle) 
        elif (self.thrust == True):
            canvas.draw_image(self.image, [130, 45], self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self): 
        self.angle += self.angle_vel
        if (self.pos[1] < -20):
            self.pos[1] = height
        elif (self.pos[1] > 620):
            self.pos[1] = 0
        elif (self.pos[0] < -20):
            self.pos[0] = width
        elif (self.pos[0] > 820):
            self.pos[0] = 0
        else:
            #Cruise
            if (self.thrust == False and self.decel == False):
                self.pos[0] += self.boost*(angle_to_vector(self.orient)[0])
                self.pos[1] += self.boost*(angle_to_vector(self.orient)[1])
            #Accelerate
            if (self.thrust == True):
                self.orient = self.angle
                self.pos[0] += self.boost*(angle_to_vector(self.angle)[0])
                self.pos[1] += self.boost*(angle_to_vector(self.angle)[1])
            #Decelerate
            elif (self.thrust == False and self.decel == True):
                    self.boost -= 0.05
                    self.pos[0] += self.boost*(angle_to_vector(self.orient)[0])
                    self.pos[1] += self.boost*(angle_to_vector(self.orient)[1])
                    if (self.boost < 1):
                        self.boost = 1
                        self.decel = False
    
    def increment(self):
        self.angle_vel += 0.1
    
    def decrement(self):
        self.angle_vel -= 0.1
        
    def thrusters(self):   
        self.boost = 7
            
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
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.angle += self.angle_vel
           
def draw(canvas):
    global time, lives, score
    
    # animiate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [width/2, height/2], [width, height])
    canvas.draw_image(debris_image, [center[0]-wtime, center[1]], [size[0]-2*wtime, size[1]], 
                                [width/2+1.25*wtime, height/2], [width-2.5*wtime, height])
    canvas.draw_image(debris_image, [size[0]-wtime, center[1]], [2*wtime, size[1]], 
                                [1.25*wtime, height/2], [2.5*wtime, height])

    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    a_missile.update()
    
    canvas.draw_text('LIVES LEFT : ' + str(lives), (20, 30), 10, "White")
    canvas.draw_text('SCORE : ' + str(score), (680, 30), 10, "White")       

def keyd(key):
    for i in press:
        if (key == simplegui.KEY_MAP[i]):
            press[i]()
            
def keyu(key):
    for i in release:
        if (key == simplegui.KEY_MAP[i]):
            release[i]()
        
# timer handler that spawns a rock    
def rock_spawner():
    a_rock.vel[0] = random.randrange(-5, 5)
    a_rock.vel[1] = random.randrange(-5, 5)
    a_rock.angle_vel = random.randrange(1, 5)
    a_rock.pos[0] = random.randrange(0, 800)
    a_rock.pos[1] = random.randrange(0, 600)
    
# initialize frame
frame = simplegui.create_frame("Asteroids", width, height)

# initialize ship and two sprites
my_ship = Ship([width / 2, height / 2], 0, ship_image, ship_info)
a_rock = Sprite([width / 3, height / 3], [random.random(), random.random()], 0, random.random(), asteroid_image, asteroid_info)
a_missile = Sprite([-10, -10], [0, 0], my_ship.angle, 0, missile_image, missile_info, missile_sound)    

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keyd)
frame.set_keyup_handler(keyu)
timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
