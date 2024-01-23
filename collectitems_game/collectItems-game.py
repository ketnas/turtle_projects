# collect items game
# By Kejkaew T.
# 2024-1-21
import turtle,random,time,pygame
from PIL import Image
import os

# Initialize pygame mixer
pygame.mixer.init()

screen = turtle.Screen()
screen.setup(800, 400)

# set path for image files
cwd = os.getcwd()
rabbit = cwd+"/collectitems_game/assets/rabbit-new.gif"
carrot = cwd+"/collectitems_game/assets/carrot-new.gif"
bg = cwd+"/collectitems_game/assets/bg-park.gif"

# Load the image
screen.bgpic(bg)
screen.register_shape(rabbit)
screen.register_shape(carrot)
screen.tracer(0)

# function for playing sound
def play_sound(x, y):
    pygame.mixer.Sound("example.wav").play()

# Define functions for movement
def move_forward():
    t.forward(20)

def move_backward():
    t.backward(20)

def createCarrot():
    tc = turtle.Turtle()
    tc.penup()
    tc.speed(0)
    tc.goto(random.randint(-390,390),random.randint(200,300))
    tc.shape(carrot)
    return tc

t = turtle.Turtle()
t.penup()
t.goto(0,-100)
t.shape(rabbit)

t_score = turtle.Turtle()
t_score.penup()
t_score.hideturtle()
t_score.speed(0)
t_score.goto(300, 160)  # Position turtle in the center of the screen

timer = turtle.Turtle()
timer.penup()
timer.hideturtle()
timer.speed(0)
timer.goto(-330, 160)

screen.listen()
screen.onkeypress(move_forward, "Right")    # Arrow Up key
screen.onkeypress(move_backward, "Left")  # Arrow Down key

# score and timer
score = 0
t_score.write("score: "+str(score), align="center", font=("Arial", 30, "bold"))
second = 60
timer.write("Time: "+str(second), align="center", font=("Arial", 30, "bold"))

carrot_list = [createCarrot() for i in range(5)]

speed_list = [random.randint(1,10) for i in range(5)]

def addCarrot():
    new_c = createCarrot()
    carrot_list.append(new_c)

time_a = int(time.time())

# Main game loop
while True:
    
    for index, item in enumerate(carrot_list):
        # Move the object downwards
        y_position = item.ycor()  # get the current y-coordinate
        y_position -= speed_list[index]  # decrease the y-coordinate to move downwards
        item.sety(y_position)  # update the turtle's y-coordinate
        
        # Stop when the object reaches the bottom of the screen
        if item.distance(t) < 45:
            item.hideturtle()
            pygame.mixer.Sound(cwd+"/collectitems_game/assets/sound-item.mp3").play()
            # item.clear()
            carrot_list.pop(index)
            speed_list.pop(index)
            score += 1
            t_score.clear()
            t_score.write("score: "+str(score), align="center", font=("Arial", 30, "bold"))
        elif item.ycor() < -200:
            item.hideturtle()
            # item.clear()
            carrot_list.pop(index)
            speed_list.pop(index)


    if len(carrot_list) < 5:
        addCarrot()
        speed_list.append(random.randint(4,10))
    
    time_b = int(time.time())
    if time_b - time_a >0:
        second -= time_b-time_a
        timer.clear()
        timer.write("Time: "+str(second), align="center", font=("Arial", 30, "bold"))
        time_a = time_b
    if second <= 0:
        break
    # Update the screen
    screen.update()

turtle.mainloop()


