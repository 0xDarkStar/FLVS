'''
Draw Amogus for school

draw the background (the Y intersection at Mira HQ)
use randomness to choose who is the dead body and who is the killer
draw the dead body and draw the others
draw the knife in the killer's hand
if knife in dead body's hand, say it was a suicide and add shocked faces to others
'''

# TO DO: Draw knife, draw characters, draw background

import turtle, time, random

turtle.setup(850,850)

def hidden(turtle):
    if turtle.isvisible() == False: #was ran again (possibly), delete what was drawn before 
        turtle.showturtle()
        turtle.clear()
    else:
        turtle.hideturtle() #hide the turtle


def background():
    leftWall = turtle.Turtle() #draw the background (duh)
    middleWall = turtle.Turtle()
    rightWall = turtle.Turtle()
    floor = turtle.Turtle()
    hidden(leftWall)
    hidden(middleWall)
    hidden(rightWall)
    hidden(floor)
    leftWall.setpos(-400,-400)
    middleWall.setpos(-350,-400)
    rightWall.setpos(400,-400)
    floor.setpos(-399,-400)
    hidden(leftWall)
    hidden(middleWall)
    hidden(rightWall)
    hidden(floor)


def amogus(color):
    color.forward(50) #draw the character in their respective color


background()
List = (1, 2, 3, 4) #list to choose who kills and who dies
dead = random.choice(List) #choose who dies
killer = random.choice(List) #choose who kills
print(killer)
print(dead)

red = turtle.Turtle()
hidden(red)
red.pensize(10)
red.pencolor("red")
red.forward(60)
if killer == 1:
    hidden(red)
    red.right(90)
    red.forward(100)
if dead == 1:
    red.left(90)
    red.forward(100)
    red.goto(350,0)

blue = turtle.Turtle()
blue.pensize(10)
blue.pencolor("blue")
blue.left(90)
blue.forward(60)
if killer == 2:
    blue.right(90)
    blue.forward(100)
if dead == 2:
    blue.left(90)
    blue.forward(100)

black = turtle.Turtle()
black.pensize(10)
black.right(90)
black.forward(60)
if killer == 3:
    black.right(90)
    black.forward(100)
if dead == 3:
    black.left(90)
    black.forward(100)

green = turtle.Turtle()
green.pensize(10)
green.pencolor("green")
green.left(180)
green.forward(60)
if killer == 4:
    green.right(90)
    green.forward(100)
if dead == 4:
    green.left(90)
    green.forward(100)

time.sleep(2)
