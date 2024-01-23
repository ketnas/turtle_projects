# 8-puzzle game
# By Kejkaew T.
# 2024/01/21

import turtle, os
import random,time

screen = turtle.Screen()
screen.title("8-Puzzle Game")
screen.setup(width = 320, height=320)
screen.tracer(0)

desired_height_in_pixels = 100
original_square_size = 20
stretch_factor = desired_height_in_pixels / original_square_size

# Register the shapes
cwd = os.getcwd()
dir = cwd + "/puzzle/assets"
num = [1,2,3,4,5,6,8,9]
shapes = ["image-"+str(i)+"-new.gif" for i in num]
for i in shapes:
    screen.register_shape(dir+"/"+i)

# Randomize the shapes
random.shuffle(shapes)
num.append(0)
shapes.append("")

turtles = []
pic_list = []

# Create the turtles and set their shapes
for i in range(len(shapes)):
    row = i // 3
    col = i % 3
    t = turtle.Turtle()
    t.penup()
    t.goto(-100+100*col, 100 - 100*row)
    t.shape("square")
    t.color("")
    t.pencolor("black")
    t.shapesize(stretch_wid=stretch_factor, stretch_len=stretch_factor,outline=2)
    turtles.append(t)
    pic = turtle.Turtle()
    pic.penup()
    pic.goto(-100+100*col, 100 - 100*row)
    if shapes[i] == "":
        pic.shape("square")
        pic.color("pink")
        pic.pencolor("black")
        pic.shapesize(stretch_wid=stretch_factor, stretch_len=stretch_factor,outline=2)
    else:
        pic.shape(dir+"/"+shapes[i])
    pic_list.append(pic)

# Function to check if the tile is clicked
def tile_click(x, y):
    for i, pic in enumerate(pic_list):
        pos = pic.pos()
        if pos[0] - 50 < x < pos[0] + 50 and pos[1] - 50 < y < pos[1] + 50:
            # ตรวจสอบว่าสามารถเลื่อนได้หรือไม่ (ต้องมีช่องว่างอยู่ข้างๆ)
            # if i == 0 and shapes[i+1] == '' or i == 1 and shapes[i+1] == '' or i == 3 and shapes[i+1] == '' or i == 4 and shapes[i+1] == '' or i == 6 and shapes[i+1] == '' or i == 7 and shapes[i+1] == '':
            if i in [0,1,3,4,6,7] and shapes[i+1] == '':
                pic.setpos(pos[0]+100,pos[1])
                pic_list[i+1].setpos(pos[0],pos[1])
                pic_list[i], pic_list[i+1] = pic_list[i+1], pic_list[i]
                shapes[i], shapes[i+1] = shapes[i+1], shapes[i]
                
            # elif i == 1 and shapes[i-1] == '' or i == 2 and shapes[i-1] == '' or i == 4 and shapes[i-1] == '' or i == 5 and shapes[i-1] == '' or i == 7 and shapes[i-1] == '' or i == 8 and shapes[i-1] == '':
            elif i in [1,2,4,5,7,8] and shapes[i-1] == '':
                pic.setpos(pos[0]-100,pos[1])
                pic_list[i-1].setpos(pos[0],pos[1])
                pic_list[i], pic_list[i-1] = pic_list[i-1], pic_list[i]
                shapes[i], shapes[i-1] = shapes[i-1], shapes[i]
            # elif i == 0 and shapes[i+3] == '' or i == 1 and shapes[i+3] == '' or i == 2 and shapes[i+3] == '' or i == 3 and shapes[i+3] == '' or i == 4 and shapes[i+3] == '' or i == 5 and shapes[i+3] == '':
            elif i in [0,1,2,3,4,5] and shapes[i+3] == '':
                pic.setpos(pos[0],pos[1]-100)
                pic_list[i+3].setpos(pos[0],pos[1])
                pic_list[i], pic_list[i+3] = pic_list[i+3], pic_list[i]
                shapes[i], shapes[i+3] = shapes[i+3], shapes[i]
            # elif i == 3 and shapes[i-3] == '' or i == 4 and shapes[i-3] == '' or i == 5 and shapes[i-3] == '' or i == 6 and shapes[i-3] == '' or i == 7 and shapes[i-3] == '' or i == 8 and shapes[i-3] == '':
            elif i in [3,4,5,6,7,8] and shapes[i-3] == '':
                pic.setpos(pos[0],pos[1]+100)
                pic_list[i-3].setpos(pos[0],pos[1])
                pic_list[i], pic_list[i-3] = pic_list[i-3], pic_list[i]
                shapes[i], shapes[i-3] = shapes[i-3], shapes[i]
            
            screen.update()
            if check_win():
                time.sleep(1)
                t = turtle.Turtle()
                t.hideturtle()
                t.color("black")
                t.write("You win", align="center", font=("Arial", 30, "normal"))
                screen.update()
            break

# check win?
complete_img = ['image-1-new.gif', 'image-2-new.gif', 'image-3-new.gif', 'image-4-new.gif', 'image-5-new.gif', 'image-6-new.gif', '', 'image-8-new.gif', 'image-9-new.gif']
def check_win():
    if shapes == complete_img:
        print("You win")
        return True
    else:
        return False
    
# # ตั้งค่าคลิกเมาส์
screen.onscreenclick(tile_click)

screen.update()
turtle.mainloop()
