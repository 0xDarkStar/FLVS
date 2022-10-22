'''
Draw Amogus for school

draw the background (the Y intersection at Mira HQ)
use randomness to choose who is the dead body and who is the killer
draw the dead body and draw the others
draw the knife in the killer's hand
if knife in dead body's hand, say it was a suicide
'''

# TO DO: nothing

from collections import namedtuple
import turtle, time, random


List = (1, 2, 3, 4) #list to choose who kills and who dies
dead = random.choice(List) #choose who dies
killer = random.choice(List) #choose who kills

def knife(turtle):
    turtle.speed(0)
    turtle.pendown()
    turtle.begin_fill() # handle is being made
    turtle.fillcolor("black")
    turtle.forward(6)
    turtle.left(90)
    turtle.forward(2)
    turtle.right(90)
    turtle.forward(1)
    turtle.right(90)
    turtle.forward(3)
    turtle.forward(3)
    turtle.right(90)
    turtle.forward(1)
    turtle.right(90)
    turtle.forward(2)
    turtle.left(90)
    turtle.forward(6)
    turtle.right(90)
    turtle.forward(2)
    turtle.end_fill() # handle has been made
    turtle.penup()
    turtle.right(90)
    turtle.forward(7)
    turtle.pendown()
    turtle.pensize(1)
    turtle.begin_fill() # blade is being made
    turtle.fillcolor("gray")
    turtle.forward(10)
    turtle.right(135)
    turtle.forward(2.8)
    turtle.right(45)
    turtle.forward(8)
    turtle.end_fill() # blade is made

def hide(turtle):
    turtle.penup()
    turtle.hideturtle()

def background():
    turtle.bgcolor("light blue")
    leftWall = turtle.Turtle() #draw the walls
    middleWall = turtle.Turtle()
    rightWall = turtle.Turtle()
    hide(leftWall)
    hide(middleWall)
    hide(rightWall)

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
    walls(leftWall)
    walls(middleWall)
    walls(rightWall)
    

def alive(turtle, color, num):
    turtle.pendown()
    turtle.showturtle()
    turtle.speed(0)
    sPos = turtle.pos()
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
    if killer == num:
        turtle.penup()
        turtle.forward(8)
        turtle.left(90)
        turtle.forward(2)
        turtle.right(60)
        knife(turtle)
    turtle.hideturtle() #character is done

def Dead(turtle, color, num):
    turtle.speed(0)
    sPos = turtle.pos()
    turtle.pendown()
    turtle.showturtle()
    print( color + " is dead")
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(11):
        turtle.left(36)
        turtle.forward(5)
    turtle.end_fill()
    turtle.begin_fill()
    turtle.forward(9)
    for _ in range(5):
        turtle.left(36)
        turtle.forward(2)
    turtle.left(180)
    turtle.forward(2)
    turtle.left(15)
    turtle.end_fill()
    turtle.begin_fill()
    for _ in range(5):
        turtle.left(18)
        turtle.forward(1)
    for _ in range(3):
        turtle.left(8)
        turtle.forward(2)
    for _ in range(5):
        turtle.left(17)
        turtle.forward(2)
    turtle.forward(1)
    turtle.left(177)
    for _ in range(3):
        turtle.right(36)
        turtle.forward(5)
    turtle.end_fill()
    turtle.setheading(90)
    hide(turtle)
    turtle.goto(sPos)
    turtle.forward(7)
    turtle.pendown()
    turtle.left(125)
    turtle.pensize(1)
    turtle.begin_fill()
    turtle.fillcolor("white")
    turtle.forward(3)
    turtle.left(115)
    for _ in range(10):
        turtle.right(27)
        turtle.forward(1)
    turtle.left(180)
    for _ in range(10):
        turtle.right(27)
        turtle.forward(1)
    turtle.forward(1)
    turtle.left(90)
    turtle.forward(3)
    turtle.end_fill()
    turtle.penup()
    if killer == num:
        print("I guess " + color + " killed themselves....")
        turtle.setheading(315)
        turtle.forward(15)
        turtle.left(60)
        knife(turtle)
    hide(turtle)


        

def start():
    background()

    red = turtle.Turtle() #red amogus guy
    hide(red)
    red.pensize(3)
    red.setpos(0,100)
    if dead != 1:
        alive(red, "red", 1)
    if dead == 1: #he dead
        Dead(red, "red", 1)

    blue = turtle.Turtle() #blue amogus guy
    hide(blue)
    blue.pensize(3)
    blue.setpos(125,-100)
    if dead != 2:
        alive(blue, "blue", 2)
    if dead == 2: #he dead
        Dead(blue, "blue", 2)

    gray = turtle.Turtle() #gray amogus guy
    hide(gray)
    gray.pensize(3)
    if dead != 3:
        alive(gray, "gray", 3)
    if dead == 3: #he dead
        Dead(gray, "gray", 3)

    green = turtle.Turtle() #green amogus guy
    hide(green)
    green.pensize(3)
    green.setpos(-125,-100)
    if dead != 4:
        alive(green, "green", 4)
    if dead == 4: #he dead
        Dead(green, "green", 4)
        
    if killer == 1:
        if dead == 2:
            print("Red killed Blue")
        elif dead == 3:
            print("Red killed Gray")
        elif dead == 4:
            print("Red killed Green")
    
    elif killer == 2:
        if dead == 1:
            print("Blue killed Red")
        elif dead == 3:
            print("Blue killed Gray")
        elif dead == 4:
            print("Blue killed Green")
    
    elif killer == 3:
        if dead == 1:
            print("Gray killed Red")
        elif dead == 2:
            print("Gray killed Blue")
        elif dead == 4:
            print("Gray killed Green")
    
    elif killer == 4:
        if dead == 1:
            print("Green killed Red")
        elif dead == 2:
            print("Green killed Blue")
        elif dead == 3:
            print("Green killed Gray")

start()
time.sleep(3)
