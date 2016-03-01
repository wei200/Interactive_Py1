# "Guess the number" mini-project for Week 2
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

low = 0
high = 100
secret_number = 0
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, n, low, high
    secret_number = random.randrange(low,high)
    n = int(math.ceil(math.log((high - low + 1), 2)))
    print "New game! Guess a number from", low, "to", high
    print "Number of remaining guesses is", n
    print ""
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
   
    global high
    high = 100
    secret_number = random.randrange(low,high)
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global high
    high = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global n
    n -= 1
    guess = int(guess)
    print "Guess was", guess
    print "Number of remaining guesses is", n
    if n == 0 and guess != secret_number:
        print "Ran out of guesses!"
        print "The answer is", secret_number
        new_game()
        print ""
    elif guess > secret_number:
        print "Higher"
        print ""
    elif guess < secret_number:
        print "Lower"
        print ""
    elif guess == secret_number:
        print "Correct"
        print ""
        new_game()
    

    
# create frame

frame = simplegui.create_frame("Guess the number!", 200, 200)
# register event handlers for control elements and start frame
#add buttons
button100 = frame.add_button("Range is [0, 100)", range100, 200) 
button1000 = frame.add_button("Range is [0, 1000)", range1000,200)
inp = frame.add_input("Your guess and press enter", input_guess, 50)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric