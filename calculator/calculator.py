# Calculator
# By Kejkaew T.
# 2024/01/21

import turtle

# Create the screen
screen = turtle.Screen()
screen.title("Calculator")
screen.setup(width=300, height=530)
screen.tracer(0)

# Create a turtle to draw buttons
drawer = turtle.Turtle()
drawer.penup()
drawer.hideturtle()

# Function to draw a button
def draw_button(x, y, text):
    drawer.goto(x, y)
    drawer.pendown()
    drawer.setheading(0)
    drawer.pencolor("black")
    drawer.pensize(2)
    drawer.begin_fill()
    drawer.fillcolor("grey")
    for _ in range(4):
        drawer.forward(75)
        drawer.right(90)
    drawer.end_fill()
    drawer.penup()
    drawer.goto(x+37.5, y-50)
    drawer.write(text, align="center", font=("Arial", 30, "normal"))
    

max_height = 530/2
# set up layout
layout = [(-150,max_height),(-150,max_height-75)]
button_start = max_height-150
buttons = [('AC',-150),('CE',-75),('%',0),('/',75),
           ('7',-150),('8',-75),('9',0),('x',75),
           ('4',-150),('5',-75),('6',0),('-',75),
           ('1',-150),('2',-75),('3',0),('+',75),
           ('0',-150),('',-75),('.',0),('=',75)]

# Draw layout
for (x, y) in layout:
    drawer.goto(x, y)
    drawer.pendown()
    drawer.setheading(0)
    drawer.pencolor("black")
    drawer.pensize(2)
    drawer.forward(300)
    drawer.right(90)
    drawer.forward(75)
    drawer.right(90)
    drawer.forward(300)
    drawer.right(90)
    drawer.forward(75)

# Draw buttons
i = 0
for (text, x) in buttons:
    y = button_start - 75*int(i/4)
    draw_button(x, y, text)
    i += 1

screen.update()

# Calculator display
display = turtle.Turtle()
display.hideturtle()
display.penup()
display.goto(120, max_height-130)
display.write("0", align="right", font=("Arial", 40, "normal"))

# Calculator history display
hist = turtle.Turtle()
hist.hideturtle()
hist.penup()
hist.goto(-130, max_height-60)

# Update display
def update_display(message):
    display.clear()
    display.write(message, align="right", font=("Arial", 40, "normal"))

def update_history(message):
    global display_hist,history
    display_hist += message
    if message == "x":
        history += "*"
    elif message == "%":
        history += "/100"
    else:
        history += message
    hist.clear()
    hist.write(display_hist, align="left", font=("Arial", 40, "normal"))

current_number = ""
history = ""
display_hist = ""
# click on number or operator
def on_number_click(x, y):
    global current_number
    global display_hist,history
    i = 0
    for (text, btn_x) in buttons:
        btn_y = button_start - 75*int(i/4)
        if btn_x < x < btn_x + 75 and btn_y-75 < y < btn_y :
            if text.isdigit():
                current_number += text
                update_display(current_number)
                update_history(text)
            elif text == '+' or text == '-' or text == 'x' or text == '/' or text == '%':
                if current_number:
                    current_number = ""
                    operator = text
                    update_history(operator)
            
            elif text == '=':
                result = eval(history)
                current_number = ""
                update_display(str(result))
            elif text == 'AC':
                current_number = ""
                history = ""
                display_hist = ""
                update_display("0")
                hist.clear()
            elif text == 'CE':
                current_number = ""
                update_display("0")
            elif text == '.':
                if current_number:
                    current_number += text
                    update_display(current_number)
                    update_history(text)
            return
        i += 1

# Press on keyboard
def keys(object):
    global current_number
    if object.isdigit() or object == '.':
        current_number += object
        update_display(current_number)
        update_history(object)
    elif object == '+' or object == '-' or object == 'x' or object == '/' or object == '%':
        if current_number:
            current_number = ""
            update_history(object)
    elif object == '=':
        result = eval(history)
        current_number = ""
        update_display(str(result))
            
def setup_keypress():
    for num in range(10):  # For numbers 0-9
        screen.onkeypress(lambda num=num: keys(str(num)), f"KP_{num}")
    print("Keys setup")
    screen.onkeypress(lambda: keys("."), "KP_Decimal")
    screen.onkeypress(lambda: keys("+"), "KP_Add")
    screen.onkeypress(lambda: keys("-"), "KP_Subtract")
    screen.onkeypress(lambda: keys("*"), "KP_Multiply")
    screen.onkeypress(lambda: keys("/"), "KP_Divide")
    screen.onkeypress(lambda: keys("="), "KP_Enter")

screen.listen()

setup_keypress()

screen.onscreenclick(on_number_click)

screen.update()
turtle.mainloop()