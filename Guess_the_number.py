
import random
import simplegui
import math

# initialize global variables used in your code
global secret, count, count100, count1000

#number of guesses restriction
count100 = math.log((100 - 0 + 1),2)
count100 = math.ceil(count100)
count1000 = math.log((1000 - 0 + 1),2)
count1000 = math.ceil(count1000)

# define event handlers for control panel
def range100():
    global secret, count, count100
    count = count100
    print "New game. Range is from 0 to 100"
    print "Number of guesses remaining: ",count
    print ""
    secret = random.randrange(0,100)
    
def range1000():
    global secret, count, count1000    
    count = count1000
    print "New game. Range is from 0 to 1000"
    print "Number of guesses remaining: ",count
    print ""
    secret = random.randrange(0,1000)
    
#decrement count after each guess
def decrement():
    global count
    count = count - 1
    print "Number of guesses remaining: ",count
    print ""
    

def get_input(guess):
    global secret, count, count100, count1000
        
    guess = int(guess)
    print "Guess was",guess
    if(secret < guess):
        print "Secret number is lower"
        decrement()
    elif(secret > guess):
        print "Secret number is higher"
        decrement()
    else:
        print "Correct guess. You Win!!"
        print ""
        print "Starting new game"
        range100()
            
    if (count < 1):
        print "You ran out of guesses. You lose!!"
        print "Number was",secret
        print ""
        range100()

#exit event handler
def stop_game():
    frame.stop()

#reveal the answer mid-way
def reveal():
    print "Number was", secret
    print "Starting new game"
    print ""
    range100()

#start with range from 0 - 100 
range100()

# create frame
frame = simplegui.create_frame("Guess the number",300,300)

# register event handlers for control elements
frame.add_button("Range [0,100)", range100, 200)
frame.add_button("Range [0,1000)", range1000, 200)
frame.add_input("Enter your guess", get_input, 100)
frame.add_button("Reveal secret number", reveal, 200)
frame.add_button("Exit game", stop_game, 200)

# start frame
frame.start()
