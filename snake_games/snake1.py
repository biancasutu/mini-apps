import turtle
import time
import random

delay = 0.1

# Set up the screen
window = turtle.Screen()
window.title('Snake')
window.bgcolor('black')
window.setup(width=600, height=600)
window.tracer(0)  # turns off the animation on the screen



# Creating the Snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('red')
head.penup()
head.goto(0,0)  # the game starts from the center of the screen
head.direction = 'stop'  # so the player can choose the direction


# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,0)  # the game starts from the center of the screen

# Creating the snake body

segments = [] # we create a list

# Functions to make our snake move on the xOy axis
def move_up():
    head.direction = 'up'

def move_down():
    head.direction = 'down'

def move_right():
    head.direction = 'right'

def move_left():
    head.direction = 'left'

def move():
    if head.direction == 'up':
        y = head.ycor()  # used to return the snake's y coordinate of the current position of snake
        head.sety(y + 20)
    
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == 'right':
        x = head.xcor()  # used to return the snake's x coordinate of the current position of snake
        head.setx(x + 20)
    
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)


# Keyboard bindings - connects a keypress (w, a, s, d) with a specific function to show direction
window.listen()  # makes the window listen for clicks/keypresses
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_right, "d")
window.onkeypress(move_left, "a")


# Main game loop
while True:
    window.update()

    # check if the snake touches the food
    if head.distance(food) < 20:
        # move the food to a random position on screen
        # the screen has (500,500) px so 250px up, 250px down, 250px right, 250px left
        # the food will be positions randomly on screen with coordinates limits (290, 290) so it doesn't go off the screen
        x = random.randrange(-240, 240, 20)
        y = random.randrange(-240, 240, 20)
        food.goto(x, y)

        # add a segment in the body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('green')
        new_segment.penup()
        segments.append(new_segment)

    #Move the end segments first in reverse order
    # Adding each segment after the snake ate behind the head (beggining of the body/tale)
    # All the segments that are already in the snake's body will be moved with 1 position
    for i in range(len(segments)-1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    
    # Move segments 0 (first one after the head) to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)



    move()

    time.sleep(delay)

window.mainloop()  # keeps the window open



# Notes :
# the food's coordinates must be multiple of 20px
# the snake cannot move directly in the opposite direction because he would eat his tale
