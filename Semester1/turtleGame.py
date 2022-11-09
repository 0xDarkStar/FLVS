# Make a game to have the user move around as the turtle, draw boundaries to make sure the turtle doesn't hit anything
import turtle, keyboard
from os import system
from time import sleep

screen = turtle.Screen()
screen.setup(width = 550, height = 550)

# Lists
wallsL = [(225, 275, 225, 225), (225, 225, 175, 225)]
def search(xpos, ypos):
    item = [item for item in wallsL if xpos >= wallsL[0[0]] and xpos <= wallsL[0[1]]]
    print(item)
    if item != []:
        print("Found it in X")
        item1 = True
    else:
        item1 = False
    item = [item for item in wallsL if ypos >= wallsL[0[2]] and ypos <= wallsL[0[3]]]
    print(item)
    if item != []:
        print("Found it in Y")
        item2 = True
    else:
        item2 = False

    if item1 == True and item2 == True:
        item = True
        sleep(4)
        return item
    else:
        item = False
        sleep(4)
        return item

#Functions
def tunnel(turtle, lvl):
    a = 0
    while a == 0:
        if lvl == "lvl1":
            move = input("/------------------\ \n| frw = forward    |\n| r = right        |\n| l = left         |\n| exit = quit      |\n|                  |\n\------------------/\n")
            if move != "frw" and move != "r" and move != "l" and move != "exit" and move != "goto":
                system("cls")
            else:
                return move
        elif lvl == "lvl2":
            if turtle.xcor() in range(0, 50) and turtle.ycor() in range(0,50):
                move = input("/------------------\ \n| frw = forward    |\n| r = right        |\n| l = left         |\n| exit = quit      |\n| tp = teleport    |\n\------------------/\n")
                if move != "frw" and move != "r" and move != "l" and move != "exit" and move != "tp" and move != "goto":
                    system("cls")
                elif move == "tp":
                    turtle.speed(2)
                    turtle.penup()
                    turtle.goto("filler")
                    turtle.pendown()
                    turtle.speed(0)
                else:
                    return move
            else:
                move = input("/------------------\ \n| frw = forward    |\n| r = right        |\n| l = left         |\n| exit = quit      |\n|                  |\n\------------------/\n")
                if move != "frw" and move != "r" and move != "l" and move != "exit" and move != "goto":
                    system("cls")
                else:
                    return move

def maybe(turtle):
    xpos = turtle.xcor()
    ypos = turtle.ycor()
    crash = search(xpos, ypos)
    if crash == True:
        turtle.back(25)
    else:
        print("You didn't crash")
        

def wall(go1, go2, head, walls):
    walls.penup()
    walls.goto(go1, go2)
    walls.setheading(head)
    walls.pendown()
    walls.forward(50)

#Level 1
def lvl1():
    walls = turtle.Turtle()
    walls.speed(0)
    walls.penup()
    walls.goto(275, 275)
    walls.right(90)
    walls.hideturtle()
    walls.pendown()# Border
    walls.forward(550)
    walls.right(90)
    walls.forward(550)
    walls.right(90)
    walls.forward(550)
    walls.right(90)
    walls.forward(550) # Border done

    wall(225, 225, 0, walls) #line (225 - 275, 225)

    wall(225, 225, 270, walls) # line (225, 225 - 175)

    wall(225, 125, 0, walls) # line (225 - 275, 175)

    wall(225, 75, 270, walls)
    walls.forward(50) # line(225, 75 - -25)

    wall(225, -75, 180, walls)
    walls.forward(150) # line (225 - 25, -75)

    wall(25, -225, 90, walls)
    walls.forward(450) # line (25, 275 - -225 )

    wall(75, 275, 270, walls) # line (75, 225 - 275)

    wall(125, 275, 270, walls) # line (125, 275 - 225)
    walls.left(90)
    walls.forward(50) # line (125 - 175, 225)
    walls.right(90)
    walls.forward(100) # line (175, 225 - 125)
    walls.right(90)
    walls.forward(100) # line (175 - 75, 125)
    walls.right(90)
    walls.forward(50) # line (75, 125 - 175)
    walls.right(90)
    walls.forward(50) # line (75 - 125, 175)
    
    wall(225, 75, 180, walls) # line (225 - 175, 75)
    walls.left(90)
    walls.forward(150) # line (175, 75 - -75)

    wall(125, -75, 90, walls)
    walls.forward(100) # line (125, -75 - 75)
    walls.left(90)
    walls.forward(50) # line (125 - 75, 75)
    
    wall(75, 25, 180, walls) # line (75 - 25, 25)

    wall(75, -25, 0, walls) # line (75 - 125, -25)

    wall(275, -125, 180, walls)
    walls.forward(100) # line (275 - 125, -125)

    wall(75, -125, 270, walls) # line (75, -125 - -175)
    walls.left(90)
    walls.forward(150) # line (75 - 225, -175)
    walls.right(90)
    walls.forward(50) # line (225, -175 - -225)
    walls.right(90)
    walls.forward(200) # line (25 - 225, -225)

    wall(-25, -225, 180, walls)
    walls.forward(100) # line (-175 - -25, -225)

    wall(-25, -225, 90, walls)
    walls.forward(150) # line (-25, -225 - -25)
    
    wall(-225, -225, 90, walls) # line (-225, -225 - -175)
    walls.left(90)
    walls.forward(50) # line (-275 - -225, -175)

#start
def start():
    user = turtle.Turtle()
    user.pencolor("green")
    user.speed(0)
    user.penup()
    user.goto(250, 250) #true start
    #user.goto(-250, -200) #just to test
    user.setheading(180)
    user.pendown()
    lvl1()
    a = 0
    while a == 0:
        system("cls")
        move = tunnel(user, "lvl1")
        if move == "exit":
            system("cls")
            exit()
        elif move == "frw":
            user.forward(25)
            hmm = maybe(user)
            if hmm == True:
                user.back(25)

        elif move == "r":
            user.right(90)

        elif move == "l":
            user.left(90)

        elif move == "goto":
            x = int(input("First coordinate"))
            y = int(input("Second coord"))
            user.goto(x, y)


start()
