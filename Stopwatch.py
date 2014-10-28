import simplegui

# define global variables
global count, min, sec, x, y
count = 0
sec = 0
min = 0
x = 0
y = 0
n1 = 0
n2 = 0

# counting tenths of seconds into formatted string A:BC.D
def format(t):
    global count, sec, min
    t = count
    if (t == 10):
        sec = sec + 1
        count = 0
        
    if (sec == 60):
        min = min + 1
        sec = 0
        
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    global n1, n2
    if ((n1-n2) == 0):
        n1 = n1 + 1
        timer.start()

def stop_timer():
    global x, y, n1, n2
    if ((n1-n2) == 1):
        n2 = n2 + 1
        timer.stop()
        y = y + 1
        if (count == 0):
            x = x + 1
    
def reset_timer():
    global count, sec, min, x, y
    timer.stop()
    count = 0
    sec = 0
    min = 0
    x = 0
    y = 0

def exit_timer():
    frame.stop()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global count
    count = count + 1
    
def draw_handler(canvas):
    global count, sec, min, x, y
    format(count)
    if (sec < 10):
        canvas.draw_text(str(min)+":"+str(0)+str(sec)+"."+str(count),(70,110),20,"White")
    else:
        canvas.draw_text(str(min)+":"+str(sec)+"."+str(count),(70,110),20,"White")
    canvas.draw_text(str(x)+"/"+str(y), (10,30), 20, "Red")

# create frame
frame = simplegui.create_frame("Stopwatch:The Game",200,200)

# register event handlers
timer = simplegui.create_timer(100,timer_handler)
frame.add_button("Start",start_timer,100)
frame.add_button("Stop",stop_timer,100)
frame.add_button("Reset",reset_timer,100)
frame.set_draw_handler(draw_handler)
frame.add_button("Exit Game",exit_timer,100)

# start timer and frame
frame.start()
