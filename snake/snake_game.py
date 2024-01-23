# Snake game
# By Kejkaew T.
# 2024/01/21
import turtle
import time
import random

# Set up UI screen
def screen_setup(): 
    screen = turtle.Screen()
    screen.title("Snake Game")
    screen.bgcolor("black")
    screen.setup(width=420, height=420)
    screen.tracer(0)  # Turns off the screen updates
    return screen

# Set up button for start game
def button_setup(wid, length):
    button = turtle.Turtle("square")
    button.color("")
    button.shapesize(stretch_wid=wid, stretch_len=length,outline=2)
    button.pencolor("green")
    return button

# function for adding text
def text_setup(message,size,pos_y):
    text = turtle.Turtle()
    text.penup()
    text.goto(0, pos_y)
    text.color("green")
    text.hideturtle()
    text.write(message, align="center", font=("Arial", size, "normal"))
    return text

# Start game
def startgame():
    # Set up the screen
    screen = screen_setup()

    # Create a snake body
    snake = []
    for i in range(3):
        segment = turtle.Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(-20 * i, 0)
        snake.append(segment)

    # Create snake food
    food = turtle.Turtle("circle")
    food.color("red")
    food.penup()
    food.goto(random.randint(-190, 190), random.randint(-190, 190))

    # Control the snake
    def go_up():
        if snake[0].heading() != 270:
            snake[0].setheading(90)

    def go_down():
        if snake[0].heading() != 90:
            snake[0].setheading(270)

    def go_left():
        if snake[0].heading() != 0:
            snake[0].setheading(180)

    def go_right():
        if snake[0].heading() != 180:
            snake[0].setheading(0)

    screen.listen()
    screen.onkey(go_up, "Up")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")
    screen.onkey(go_right, "Right")
    score = 0
    # Main game loop
    while True:
        score += 1
        screen.update()
        time.sleep(0.2)

        # Move the end segments first in reverse order
        for i in range(len(snake) - 1, 0, -1):
            x = snake[i - 1].xcor()
            y = snake[i - 1].ycor()
            snake[i].goto(x, y)

        # Move segment 0 to where the head is facing
        snake[0].forward(20)

        # Check for collision with food
        if snake[0].distance(food) < 20:
            # Move the food to a random position
            food.goto(random.randint(-190, 190), random.randint(-190, 190))

            # Add a new segment
            new_segment = turtle.Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            snake.append(new_segment)
            score += 5

        # Check for collision with the wall
        if abs(snake[0].xcor()) > 200 or abs(snake[0].ycor()) > 200:
            print("wall")
            time.sleep(1)
            for segment in snake:
            
                # segment.goto(1000, 1000)  # Move segments out of the screen
                segment.hideturtle()
            snake.clear()
            food.hideturtle()
            # break
            return True

        # Check for collision with self
        for segment in snake[1:]:
            if snake[0].distance(segment) < 19:
                print("self")
                print(snake[0].distance(segment))
                time.sleep(1)
                for segment in snake:
                    # segment.goto(1000, 1000)
                    segment.hideturtle()
                snake.clear()
                food.hideturtle()

                # break
                return True
    turtle.mainloop()

window = screen_setup()
button = button_setup(3,6)
text = text_setup("Start",40,-25)

def pressbutton(x, y):
    global window, button, text
    if -100 < x < 100 and -50 < y < 50:
        button.hideturtle()
        text.clear()
        window.onscreenclick(None)
        # window.bye()
        end = startgame()
        
        if end:
            window = screen_setup()
            button = button_setup(2.5,7.5)
            text = text_setup("Gameover",30,-20)
            window.update()
            time.sleep(2)
            text.clear()
            button.hideturtle()
            button = button_setup(3,6)
            text.write("Start", align="center", font=("Arial", 40, "normal"))   
            window.onscreenclick(pressbutton)
            window.update()

window.listen()
window.onscreenclick(pressbutton)

window.update()
turtle.mainloop()
