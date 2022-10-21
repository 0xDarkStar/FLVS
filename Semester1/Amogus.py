'''
Draw Amogus for school

draw the background (the Y intersection at Mira HQ)
use randomness to choose who is the dead body and who is the killer
draw the dead body and draw the others
draw the knife in the killer's hand
if knife in dead body's hand, say it was a suicide and add shocked faces to others
'''

# TO DO: Draw knife, draw dead characters, draw background

import turtle, time, random

turtle.setup(850,850)

List = (1, 2, 3, 4) #list to choose who kills and who dies
#dead = random.choice(List) #choose who dies
#killer = random.choice(List) #choose who kills
dead = 5
killer = 5

def hide(turtle):
    turtle.penup()
    turtle.hideturtle()

def background():
    turtle.bgcolor("light blue")
    leftWall = turtle.Turtle() #draw the background (duh)
    middleWall = turtle.Turtle()
    rightWall = turtle.Turtle()
    floor = turtle.Turtle()
    hide(leftWall)
    hide(middleWall)
    hide(rightWall)
    hide(floor)

    def walls(turtle):
        turtle.pendown()
        turtle.showturtle()
        turtle.pencolor("black")
        if turtle == rightWall:
            turtle.left(130)
            turtle.forward(610)
            turtle.right(40)
            turtle.forward(500)
            turtle.hideturtle
        else:
            turtle.left(50)
            if turtle == middleWall:
                turtle.forward(570.71)
                turtle.right(100)
            else:
                turtle.forward(610)
                turtle.left(40)
            turtle.forward(570.71)
            turtle.hideturtle()

    leftWall.setpos(-450,-400)
    middleWall.setpos(-372,-455)
    rightWall.setpos(450,-400)
    floor.setpos(-399,-400)
    walls(leftWall)
    walls(middleWall)
    walls(rightWall)
    


def alive(turtle, color, num):
    turtle.pendown()
    turtle.showturtle()
    turtle.speed(0)
    turtle.forward(5)#draw the character in their respective color
    turtle.left(90)
    turtle.begin_fill()
    turtle.color("black", color)
    turtle.forward(10)
    for _ in range(10): #top of head
        turtle.left(18)
        turtle.forward(3)
    turtle.forward(17)
    for _ in range(5): #left foot
        turtle.left(36)
        turtle.forward(2.5)
    turtle.forward(2)
    turtle.right(90)
    turtle.forward(5.55)
    turtle.back(2)
    turtle.right(90)
    turtle.forward(5)
    for _ in range(5): #right foot
        turtle.left(36)
        turtle.forward(2.5)
    turtle.forward(18)
    turtle.end_fill() #go back up to start visor
    turtle.right(90)
    turtle.fillcolor("white")
    turtle.begin_fill() #starting visor
    for _ in range(10):
        turtle.right(18)
        turtle.forward(1)
    turtle.forward(4)
    for _ in range(10):
        turtle.right(18)
        turtle.forward(1)
    turtle.forward(4)
    turtle.end_fill() #ending visor
    turtle.left(90)
    turtle.penup()
    turtle.back(3)
    turtle.left(90)
    turtle.forward(18.94)
    turtle.pendown()
    turtle.begin_fill() #time to start the backpack
    turtle.fillcolor(color)
    turtle.forward(1)
    for _ in range(5):
        turtle.left(18)
        turtle.forward(1)
    turtle.forward(7)
    for _ in range(5):
        turtle.left(18)
        turtle.forward(1)
    turtle.end_fill() #backpack is done
    turtle.hideturtle() #character is done
    if killer == num:
        turtle.penup()
        turtle.goto(0,100)
  

def start():
    background()
    print(killer)
    print(dead)

    red = turtle.Turtle() #red amogus guy
    hide(red)
    red.pensize(3)
    red.setpos(0,100)
    if dead != 1:
        alive(red, "red", 1)
    if dead == 1: #he dead
        red.left(90)
        red.forward(100)

    blue = turtle.Turtle() #blue amogus guy
    hide(blue)
    blue.pensize(3)
    blue.setpos(125,-100)
    if dead != 2:
        alive(blue, "blue", 2)
    if dead == 2: #he dead
        blue.left(90)
        blue.forward(100)

    gray = turtle.Turtle() #gray amogus guy
    hide(gray)
    gray.pensize(3)
    if dead != 3:
        alive(gray, "gray", 3)
    if dead == 3: #he dead
        gray.left(90)
        gray.forward(100)

    green = turtle.Turtle() #green amogus guy
    hide(green)
    green.pensize(3)
    green.setpos(-125,-100)
    if dead != 4:
        alive(green, "green", 4)
    if dead == 4: #he dead
        green.left(50)
        green.forward(100)

start()
time.sleep(2)
