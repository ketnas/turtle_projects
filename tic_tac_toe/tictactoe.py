# Tic-Tac-Toe game
# By Kejkaew T.
# 2021/01/21
import turtle,random,time

# Set up the screen
screen = turtle.Screen()
screen.title("Tic-Tac-Toe")
screen.bgcolor("white")
screen.setup(width = 350, height=380)
screen.tracer(0)

# Create a turtle to draw the board
board_turtle = turtle.Turtle()
board_turtle.hideturtle()
board_turtle.penup()
board_turtle.speed(0)

# Create a turtle to write the text
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.goto(0, 150)
text_turtle.write("Player: X", align="center", font=("Arial", 22, "bold"))    

# Create cell positions
cell_x = [-150, -50, 50]*3
cell_y = [150]*3 + [50]*3 + [-50]*3
cell_size = 100

shapes = [""]*9
# Draw the Tic-Tac-Toe board
def draw_board():
    for i in range(9):
        board_turtle.goto(cell_x[i], cell_y[i])
        board_turtle.setheading(0)
        board_turtle.pendown()
        board_turtle.forward(cell_size)
        board_turtle.right(90)
        board_turtle.forward(cell_size)
        board_turtle.right(90)
        board_turtle.forward(cell_size)
        board_turtle.right(90)
        board_turtle.forward(cell_size)
        board_turtle.penup()

draw_board()
player = "X"

# Create a function to draw X
def draw_X(x, y):
    board_turtle.pencolor("red")
    board_turtle.goto(x, y)
    board_turtle.setheading(0)
    board_turtle.pendown()
    board_turtle.right(45)
    board_turtle.forward(80)
    board_turtle.penup()
    new_y = board_turtle.ycor()
    board_turtle.goto(x,new_y)
    board_turtle.setheading(0)
    board_turtle.pendown()
    board_turtle.left(45)
    board_turtle.forward(80)
    board_turtle.penup()

# Create a function to draw o
def draw_O(x, y):
    board_turtle.pencolor("blue")
    board_turtle.goto(x, y)
    board_turtle.setheading(180)

    board_turtle.pendown()
    board_turtle.circle(40)
    board_turtle.penup()

# Create a function to check if the click is in a cell
def click_in_cell(x, y):
    for i in range(9):
        if cell_x[i] < x < cell_x[i] + cell_size and cell_y[i] - cell_size < y < cell_y[i]:
            return i
    return -1

# Create a function to check if the game is over
def check_win():
    # Check row
    for i in range(3):
        if shapes[i*3] == shapes[i*3+1] == shapes[i*3+2] != '':
            return True
    # Check column
    for i in range(3):
        if shapes[i] == shapes[i+3] == shapes[i+6] != '':
            return True
    # Check diagonal
    if shapes[0] == shapes[4] == shapes[8] != '':
        return True
    if shapes[2] == shapes[4] == shapes[6] != '':
        return True
    return False

# Create a function to check if the game is draw
def check_draw():
    for shape in shapes:
        if shape == "":
            return False
    return True

# Create a function to draw X or O
def draw_OX(cell):
    global player

    x = cell_x[cell]
    y = cell_y[cell]
    if player == "X":
        draw_X(x+20, y-20)
        player = "O"
        
    else:
        draw_O(x+50, y-10)
        player = "X"
        screen.onscreenclick(cell_clicked)

    text_turtle.clear()
    text_turtle.write("Player: "+ player, align="center", font=("Arial", 22, "bold"))
    screen.update()
    shapes[cell] = player
    
# create a function to let computer play
def com_play():
    empty_cells = [i for i in range(9) if shapes[i] == ""]
    cell = random.choice(empty_cells)
    draw_OX(cell)
    
    if check_win():
        print("Computer Win")
        text_turtle.clear()
        text_turtle.write("Player O win", align="center", font=("Arial", 22, "bold"))
        screen.onclick(None)
    elif check_draw():
        print("Draw")
        text_turtle.clear()
        text_turtle.write("Draw!!", align="center", font=("Arial", 22, "bold"))
        screen.onclick(None)
    
# Create a function to handle click events
def cell_clicked(x, y):
    global player
    cell = click_in_cell(x, y)
    if cell == -1:
        return
    draw_OX(cell)
    
    if check_win():
        print("You Win")
        text_turtle.clear()
        text_turtle.write("Player X win", align="center", font=("Arial", 22, "bold"))
        screen.onclick(None)
    elif check_draw():
        print("Draw")
        text_turtle.clear()
        text_turtle.write("Draw!!", align="center", font=("Arial", 22, "bold"))
        screen.onclick(None)
    else:
        screen.onclick(None)
        time.sleep(2)
        com_play()
    
# Bind the click event
screen.onscreenclick(cell_clicked)
screen.update()
turtle.mainloop()