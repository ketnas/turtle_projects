# Breakout game
# By Kejkaew T.
# 2024/01/21

import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=600, height=500)
screen.tracer(0)

# Create a paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("blue")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -200)

# Paddle movement
def paddle_right():
    x = paddle.xcor()
    if x < 300:
        paddle.setx(x + 20)

def paddle_left():
    x = paddle.xcor()
    if x > -300:
        paddle.setx(x - 20)

screen.listen()
screen.onkeypress(paddle_right, "Right")
screen.onkeypress(paddle_left, "Left")

# Create a ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = -0.5

# Create bricks
bricks = []
color = ["red", "orange", "yellow", "green"]

def create_bricks():
    y_positions = [220, 180, 140, 100]  # Y positions for bricks
    for y in y_positions:
        for x in range(-280, 280, 50):  # Arrange bricks horizontally
            brick = turtle.Turtle()
            brick.shape("square")
            brick.color(color[y_positions.index(y)])
            brick.shapesize(stretch_wid=1, stretch_len=2)
            brick.penup()
            brick.goto(x, y)
            bricks.append(brick)

create_bricks()

# Create text for start
text = turtle.Turtle()
text.color("purple")
text.hideturtle()
text.penup()
text.goto(0, -50)
text.write("Press space to start", align="center", font=("Arial", 30, "normal"))

# Play the game
def play_game():
    text.clear()
    while True:
        screen.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.xcor() > 300 or ball.xcor() < -300:
            ball.dx *= -1
        if ball.ycor() > 250:
            ball.dy *= -1
        if ball.ycor() < -250:
            ball.goto(0, 0)  # Reset the ball
            ball.dy *= -1

        # Paddle and ball collision
        if (-200 < ball.ycor() < -190 ) and (paddle.xcor() - 30 < ball.xcor() < paddle.xcor() + 30):
            ball.sety(-190)
            ball.dy *= -1
            print("Hit! 1")
        elif (-200 < ball.ycor() < -190 ) and ((paddle.xcor() - 50 < ball.xcor() <= paddle.xcor() - 30) or (paddle.xcor() + 30 <= ball.xcor() < paddle.xcor() +50)):
            ball.sety(-190)
            ball.dy *= -1
            ball.dx *= -1
            print("Hit! 2")

        # Ball and brick collision
        for brick in bricks:
            if brick.distance(ball) < 30:
                ball.dy *= -1
                brick.hideturtle()
                bricks.remove(brick)

screen.onkeypress(play_game, "space")

screen.update()
turtle.mainloop()