# Matching Game
# By Kejkaew T.
# 2024/01/21
import turtle,time,os
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Matching Game")
screen.setup(width=420, height=320)
screen.tracer(0)
desired_height_in_pixels = 100
original_square_size = 20
stretch_factor = desired_height_in_pixels / original_square_size

# Register the shapes
cwd = os.getcwd()
dir = cwd+"/matching_game/assets"
shapes = ["pic"+str(i)+".gif" for i in range(1, 7)]
for i in shapes:
    screen.register_shape(dir+"/"+i)

# Create a list of picture names
shapes = shapes * 2
random.shuffle(shapes)

# Create an empty list to store the turtles
turtles = []
pic_list = []

# Create the turtles and set their shapes
for i in range(len(shapes)):
    row = i // 4
    col = i % 4
    t = turtle.Turtle()
    t.penup()
    t.goto(-150+100*col, 100 - 100*row)
    t.shape("square")
    t.color("blue")
    t.pencolor("black")
    t.shapesize(stretch_wid=stretch_factor, stretch_len=stretch_factor,outline=2)
    turtles.append(t)
    pic = turtle.Turtle()
    pic.penup()
    pic.goto(-150+100*col, 100 - 100*row)
    pic.shape(dir+"/"+shapes[i])
    pic_list.append(pic)

# Create a list to store the flipped turtles
flipped = []

# Create a variable to keep track of matches
matches = 0

# number of flips
flips = 0

# Create check click a square area
def check_click(x, y,square_num):
    square_area = turtles[square_num].pos()
    if square_area[0] - 50 <= x <= square_area[0] + 50 and square_area[1] - 50 <= y <= square_area[1] + 50:
        return True
    else:
        return False

# Function to flip a turtle
def flip(x, y):
    for i in range(len(turtles)):
        if not turtles[i] is None:
            if check_click(x,y,i):
                turtles[i].hideturtle()
                global flips
                flips += 1
                flipped.append(i)
                if len(flipped) == 2:
                    screen.update()
                    time.sleep(1)
                    # turtle.time.sleep(1)
                    if shapes[flipped[0]] == shapes[flipped[1]]:
                        turtles[flipped[0]].hideturtle()
                        turtles[flipped[1]].hideturtle()
                        global matches
                        matches += 1
                        turtles[flipped[0]] = None
                        turtles[flipped[1]] = None
                        if matches == 6:
                            print("You won!")
                            # return True
                    else:
                        
                        print("Not match")
                        turtles[flipped[0]].showturtle()
                        turtles[flipped[1]].showturtle()
                    flipped.clear()
                    # break
                screen.update()

# Listen for a click
screen.onscreenclick(flip)
screen.update()
# Keep the window open
turtle.mainloop()