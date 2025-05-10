# Space Invaders Game
# By Kejkaew T.
# 2021/01/21
import turtle
import random,time

# Set up the screen
screen = turtle.Screen()
screen.setup(700, 400)
screen.bgcolor("black")
screen.tracer(0)  # Turn off auto screen updates

# Create a rocket
rocket = turtle.Turtle()
rocket.shape("turtle")
rocket.color("green")
rocket.penup()
rocket.goto(0, -150)
rocket.left(90)

bullets = []
bullets_x = []
aliens = []

# Create a function to move the rocket
def move_right():
    rocket.setx(rocket.xcor() + 10)

def move_left():
    rocket.setx(rocket.xcor() - 10)

# Create a function to create an alien
def create_alien():
    if len(aliens) < 10:
        a = turtle.Turtle()
        a.shape("circle")
        a.color("red")
        a.penup()
        a.goto(random.randint(-350, 350), 200)
        a.speed("fast")
        aliens.append(a)

# Create a function to move the aliens
def move_aliens():
    for a in aliens[:]:
        a.sety(a.ycor() - 10)
        if check_dead(a):
           return False 
        if a.ycor() < -200:
            a.hideturtle()
            aliens.remove(a)
    return True

# Create a function to shoot
def shoot():
    b = turtle.Turtle()
    b.shape("square")
    b.color("yellow")
    b.shapesize(stretch_wid=0.1, stretch_len=0.5)
    b.penup()
    b.goto(rocket.xcor(), rocket.ycor() + 10)
    b.setheading(90)
    bullets.append(b)

# Create a function to move the bullets
def move_bullets():
    for b in bullets[:]:
        b.sety(b.ycor() + 5)
        if b.ycor() > 200:
            b.hideturtle()
            bullets.remove(b)
        else:
            check_hits(b)

# check distance between bullet and alien
def check_hits(b):
    for a in aliens[:]:
        if a.distance(b) < 20 :
            print("hit")
            a.hideturtle()
            b.hideturtle()
            aliens.remove(a)
            if b in bullets:
                bullets.remove(b)

# check distance between rocket and alien
def check_dead(a):
    if a.distance(rocket) < 20:
        return True
    else:
        return False

screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(shoot, "space")
screen.listen()

# Main game loop
time_a = int(time.time())
second_a = 0
while True:
    if len(bullets) > 0:
        move_bullets()

    # if len(aliens) < 10:
    create_alien()

    time_b = int(time.time())
    second_b = time_b - time_a
    if second_a != second_b:
        # create_alien()
        playgame = move_aliens()
        second_a = second_b
        if not playgame:
            break

    screen.update()

turtle.mainloop()
