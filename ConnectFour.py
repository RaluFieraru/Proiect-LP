import turtle
import time

screen = turtle.Screen()
screen.setup(700, 700)
screen.setworldcoordinates(-450, -450, 450, 450)

turtle.speed(0)
turtle.hideturtle()
screen.tracer(0, 0)
score = turtle.Turtle()
score.up()
score.hideturtle()





def draw_circle(x,y,r,color):
    turtle.up()
    turtle.goto(x,y-r)
    turtle.seth(0)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r,360,150)
    turtle.end_fill()





def draw():
    draw_board()
    draw_pieces()
    screen.update()

def game_over_lastmove(bb,turn,r,c):
    # check horizontals
    cnt = 1
    i = c+1
    while i<COLS and bb[r][i]==turn: cnt, i = cnt+1, i+1
    i = c-1
    while i>=0 and bb[r][i]==turn: cnt, i = cnt+1, i-1
    if cnt>=4: return turn

    # check vertical
    if r>=3 and bb[r-1][c]==turn and bb[r-2][c]==turn and bb[r-3][c]==turn: return turn

    # check diag 2
    cnt = 1
    i = 1
    while r+i<ROWS and c+i<COLS and bb[r+i][c+i]==turn: cnt, i = cnt+1, i+1
    i = -1
    while r+i>=0 and c+i>=0 and bb[r+i][c+i]==turn: cnt, i = cnt+1, i-1
    if cnt>=4: return turn

    # check diag 1
    cnt = 1
    i = 1
    while r+i<ROWS and c-i>=0 and bb[r+i][c-i]==turn: cnt, i = cnt+1, i+1
    i = -1
    while r+i>=0 and c-i<COLS and bb[r+i][c-i]==turn: cnt, i = cnt+1, i-1
    if cnt>=4: return turn

    for i in range(COLS):
        if bb[ROWS-1][i] == 0:
            return -2
    return 0

# place piece in col for turn
def place_piece(bb,turn,col):
    for i in range(ROWS):
        if bb[i][col] == 0:
            bb[i][col] = turn
            return i

def init_board():
    global board
    for i in range(ROWS):
        row = []
        for j in range(COLS):
            row.append(0)
        board.append(row)





board = []
init_board()
draw_board()
draw_pieces()
turn = 1
working = False
screen.onclick(play)
screen.mainloop()
