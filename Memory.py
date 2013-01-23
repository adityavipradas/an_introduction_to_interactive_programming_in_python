# Implementation of card game - Memory
import simplegui
import random
global counter, m, index1, index2, choice1, choice2, state, val, position, exposed, numbers, CARD_WIDTH, CARD_LENGTH, HALF_CARD_WIDTH, HALF_CARD_LENGTH
numbers = []
exposed = []
position = [0]
val = range(16)
state = 0
choice1 = []
choice2 = []
index1 = []
index2 = []
m = 1
counter = 0
win = 0

def dimensions():
    global CARD_WIDTH, CARD_LENGTH, HALF_CARD_WIDTH, HALF_CARD_LENGTH
    CARD_WIDTH = 50
    HALF_CARD_WIDTH = CARD_WIDTH // 2
    CARD_LENGTH = 100
    HALF_CARD_LENGTH = CARD_LENGTH // 2


# helper function to initialize globals
def init():
    global val, choice1, choice2, index1, index2, m, counter, state, numbers, exposed, CARD_WIDTH, CARD_LENGTH, HALF_CARD_WIDTH, HALF_CARD_LENGTH
    dimensions()
    numbers = []
    exposed = []
    state = 0
    choice1 = []
    choice2 = []
    index1 = []
    index2 = []
    m = 1
    counter = 0
    l.set_text("Moves = 0")
    val = range(16)
    for i in range(16):
        if (i < 8):
            numbers.append(i)
            exposed.append(False)
            position.append(HALF_CARD_WIDTH + ((CARD_WIDTH//2)+1))
            HALF_CARD_WIDTH += CARD_WIDTH + 1
        else:
            numbers.append(i - 8)
            exposed.append(False)
            position.append(HALF_CARD_WIDTH + ((CARD_WIDTH//2)+1))
            HALF_CARD_WIDTH += CARD_WIDTH + 1
    random.shuffle(numbers)
                
# define event handlers
def mouseclick(pos):
    global counter, m, index1, index2, choice1, choice2, state, val, exposed
    if state == 0:
        for i in range(16):
            if (pos[0] > position[i]) and (pos[0] < position[i + 1]):
                val[i] = numbers[i]
                if exposed[i] == True:
                    state = 0
                elif exposed[i] == False:
                    compare()
                    choice1.append(val[i])
                    index1.append(i)
                    exposed[i] = True
                    state = 1
                    
    elif state == 1:
        for i in range(16):
            if (pos[0] > position[i]) and (pos[0] < position[i + 1]):
                val[i] = numbers[i]
                if exposed[i] == True:
                    state = 1
                elif exposed[i] == False:
                    choice2.append(val[i])
                    index2.append(i)
                    exposed[i] = True
                    state = 0
                    m += 1
                    counter += 1
                    l.set_text("Moves = " + str(counter))
    
def compare():
    global win, index1, index2, choice1, choice2
    if m > 1:
        for i in range(len(choice1)):
            if (choice1[i] == choice2[i]):
                exposed[index1[i]] = True
                exposed[index2[i]] = True
            else:
                exposed[index1[i]] = False
                exposed[index2[i]] = False
                                   
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global val, exposed, position, numbers, CARD_WIDTH, HALF_CARD_WIDTH, HALF_CARD_LENGTH
    for i in range(16):
        if (exposed[i] == True):
            display = str(val[i])
            canvas.draw_text(display, [position[i] + HALF_CARD_WIDTH/1.5, HALF_CARD_LENGTH], 15, "White")
        else:
            canvas.draw_line(((position[i] + HALF_CARD_WIDTH),0), ((position[i] + HALF_CARD_WIDTH),CARD_LENGTH), CARD_WIDTH, "White")
        win = 0
        for i in range(16):
            if (exposed[i] == True):
                win += 1
                if (win == 16):
                    l.set_text("You Won!!!!!")
        dimensions()

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 815, 100)
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
