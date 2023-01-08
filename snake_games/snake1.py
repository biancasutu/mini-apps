import turtle
import time
import random

delay = 0.1

# Count Score
score = 0
high_score = 0


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

# Pen - for scoring and writing
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Score: 0  High Score: 0', align='center', font=('Courier', 24, 'normal'))


# Functions to make our snake move on the xOy axis
def move_up():
    if head.direction != 'down':
        head.direction = 'up'

def move_down():
    if head.direction != 'up':
        head.direction = 'down'

def move_right():
    if head.direction != 'left':
        head.direction = 'right'

def move_left():
    if head.direction != 'right':
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

    # check for collision with the borders of screen
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'

        # hide existing segments (body of snake) after colliding with the border
        for segment in segments:
            segment.goto(1000, 1000)

        # clear the segments (start again with no body)
        segments.clear()

        # Reset the score
        score = 0
        pen.clear()
        pen.write(f'Score: {score}  High Score: {high_score}', align="center", font=("Courier", 24, "normal"))
        
        # reset the delay
        delay = 0.1

    # check if the snake touches the food
    if head.distance(food) < 20:
        # move the food to a random position on screen
        # the screen has (500,500) px so 250px up, 250px down, 250px right, 250px left
        # the food will be positions randomly on screen with coordinates limits (290, 290) so it doesn't go off the screen
        x = random.randrange(-240, 240, 20)
        y = random.randrange(-240, 240, 20)
        food.goto(x, y)

        # add a segment in the body after the snake eats
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('green')
        new_segment.penup()
        segments.append(new_segment)

        # shorten the delay as the snake eats (because Turtle slows down when the
        #  nr of items on the screen is increased )
        delay -= 0.001

        # Increase the score
        score += 10 # adds 10 points to score after eating 

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write(f'Score: {score}  High Score: {high_score}', align="center", font=("Courier", 24, "normal"))

    

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

    # Check if snake eats itself (head touches the body)
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'
        
            # hide existing segments (body of snake) after colliding with the border
            for segment in segments:
                segment.goto(1000, 1000)

            # clear the segments (start again with no body)
            segments.clear()

            score = 0
            pen.clear()
            pen.write(f'Score: {score}  High Score: {high_score}', align="center", font=("Courier", 24, "normal"))
            
            # reset the delay
            delay = 0.1

    time.sleep(delay)

window.mainloop()  # keeps the window open



# Notes :
# the food's coordinates must be multiple of 20px
# the snake cannot move directly in the opposite direction because he would eat his tale
# the food should appear randomly on the empty screen (not where the snake is)
