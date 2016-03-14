# "Stopwatch: The Game"
# http://www.codeskulptor.org/#user41_RwgPLN8I3q_3.py
# define global variables
import simplegui

watch = 0
is_running = True
success = 0
attempt = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = str(t // 600)
    B = str(t // 100 % 6 )
    C = str(t % 100 / 10)
    D = str(t % 10)
    return A + ":" + B + C + "." + D
        
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global is_running
    timer.start()
    is_running = True

def stop_handler():
    global is_running, watch, success, attempt
    if is_running == True:
        timer.stop()
        attempt += 1
        is_running = False
        
    if watch % 10 == 0:
        success += 1
        
def reset_handler():
    global watch, is_running, success, attempt
    timer.stop()
    watch = 0
    is_running = False
    success = 0
    attempt = 0
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global watch
    if watch < 6000:
        watch += 1
    
# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(watch),(110,150),50,'Red')
    canvas.draw_text(str(success) + '/' + str(attempt),(240,30),30,'Green')
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 300)
frame.set_draw_handler(draw_handler)
frame.add_button('Start', start_handler)
frame.add_button('Stop', stop_handler)
frame.add_button('Reset', reset_handler)


# register event handlers

timer = simplegui.create_timer(100, timer_handler)
# start frame
frame.start()

# Please remember to review the grading rubric
