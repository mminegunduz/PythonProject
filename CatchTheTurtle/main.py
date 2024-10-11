import turtle
import random


turtle_board = turtle.Screen()

turtle_board.bgcolor("light blue")
turtle_board.title("Catch The Turtle")
FONT=('monaco',20,'bold')
game_over= False

#turtle list
turtle_list = []

scoreTurtle = turtle.Turtle()

timer_turtle= turtle.Turtle()
scor=0
def setup_turtle():
    scoreTurtle.hideturtle()
    scoreTurtle.color("purple")
    scoreTurtle.penup()

    top_height = turtle_board.window_height() / 2  # en yüksek nokta
    y = top_height * 0.8

    scoreTurtle.setpos(0, y)
    scoreTurtle.write("Scor:0", False, font=FONT, align="center")




grid_size=10
def make_turtle(x,y):
    se = turtle.Turtle()

    def handle_click(x,y):
        global scor
        scor +=1
        scoreTurtle.clear()
        scoreTurtle.write(f"Scor: {scor}", False, font=FONT, align="center")

        # print(x,y)

    se.onclick(handle_click)
    se.penup()
    se.shape("turtle")
    se.shapesize(2,2)
    se.color("green")
    se.setposition(x * grid_size, y*grid_size)
    turtle_list.append(se)

x_coordinates=[-20,-10,0,10,20]
y_coordinates=[20,10,0,-10]


def coordinates():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)



def hideTurtles():
    for se in turtle_list:
        se.hideturtle()


#recursive
def show_turtle():
    if not game_over:
     hideTurtles()
     random.choice(turtle_list).showturtle()
     turtle_board.ontimer(show_turtle, 500)

def timer(time):
    global game_over
    timer_turtle.hideturtle()
    timer_turtle.penup()

    top_height = turtle_board.window_height() / 2  # en yüksek nokta
    y = top_height * 0.8
    timer_turtle.setpos(0, y-30)
    timer_turtle.clear()

    if time>0:
        timer_turtle.clear()
        timer_turtle.write(f"Time:{time}", False, font=FONT, align="center")
        turtle_board.ontimer(lambda: timer(time -1 ),1000)
    else:
        game_over= True
        timer_turtle.clear()
        hideTurtles()
        timer_turtle.write("Game Over!!!", False, font=FONT, align="center")


def start_game():
    turtle.tracer(0)
    coordinates()
    setup_turtle()
    timer(10)
    hideTurtles()
    show_turtle()
    turtle.tracer(1)


start_game()
turtle.done()
