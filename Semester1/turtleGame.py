# Make a game to have the user move around as the turtle, draw boundaries to make sure the turtle doesn't hit anything
import turtle
from os import system
from time import sleep

screen = turtle.Screen()
screen.setup(width = 550, height = 550)

# Lists
moves = ["end"]

#Functions
def tunnel(turtle, lvl):
    a = 0
    while a == 0:
        if lvl == "lvl1":
            move = input("/------------------\ \n| frw = forward    |\n| r = right        |\n| l = left         |\n| exit = quit      |\n|                  |\n\------------------/\n")
            if move != "frw" and move != "r" and move != "l" and move != "exit":
                system("cls")
            else:
                return move
        elif lvl == "lvl2":
            if turtle.xcor() in range(0, 50) and turtle.ycor() in range(0,50):
                move = input("/------------------\ \n| frw = forward    |\n| r = right        |\n| l = left         |\n| exit = quit      |\n| tp = teleport    |\n\------------------/\n")
                if move != "frw" and move != "r" and move != "l" and move != "exit" and move != "tp":
                    system("cls")
                elif move == "tp":
                    turtle.speed(2)
                    turtle.penup()
                    turtle.goto(filler)
                    turtle.pendown()
                    turtle.speed(0)
                else:
                    return move
            else:
                move = input("/------------------\ \n| frw = forward    |\n| r = right        |\n| l = left         |\n| exit = quit      |\n|                  |\n\------------------/\n")
                if move != "frw" and move != "r" and move != "l" and move != "exit":
                    system("cls")
                else:
                    return move

def crashed(turtle, list):
    turtle.speed(2)
    crash = True
    moves.append(b)
    moves.append(c)
    print(moves)
    for _ in reversed(list):
        if _ == "end":
            print("You crashed. Try again.")
            sleep(2)

        elif _ == "frw":
            i = _

        elif _ == "l":
            i = _

        elif _ == "r":
            i = _

        elif i == "frw":
            turtle.back(_)

        elif i == "l":
            turtle.right(_)

        elif i == "r":
            turtle.left(_)

    turtle.clear()
    return crash

#for walls, if it runs into a line between two points, kill the user and make them restart
def frw(turtle, amount, lvl, list, cough):
    global moves, b, c
    b = 0
    c = "frw"
    crash = False
    for _ in range(amount):
        if crash == False:
            turtle.forward(1)
            b += 1
            if turtle.xcor() >= 275 or turtle.xcor() <= -275:
                crash = crashed(turtle, list)

            elif turtle.ycor() >= 275 or turtle.ycor() <=-275:
                crash = crashed(turtle, list)


            if lvl == "lvl1":
                if turtle.xcor() in range(225, 275) and turtle.ycor() == 225:
                    crash = crashed(turtle, list)               
                elif turtle.xcor() == 225 and turtle.ycor() in range(175, 225):
                    crash = crashed(turtle, list)
                elif turtle.xcor() in range (225,275) and turtle.ycor() == 125:
                    crash = crashed(turtle, list)             
                elif turtle.xcor() == 225 and turtle.ycor() in range(-25, 75):
                    crash = crashed(turtle, list)
                elif turtle.xcor() in range(25, 225) and turtle.ycor() == -75:
                    crash = crashed(turtle, list)
                elif turtle.xcor() == 25 and turtle.ycor() in range(-75, 275):
                    crash = crashed(turtle, list)
                elif turtle.xcor() in range(175, 225) and turtle.ycor() == 75:
                    crash = crashed(turtle, list)
                elif turtle.xcor() == 175 and turtle.ycor() in range(-75, 75):
                    crash = crashed(turtle, list)
                elif turtle.xcor() == 75 and turtle.ycor() in range(225, 275):
                    crash = crashed(turtle, list) 
                elif turtle.xcor() == 125 and turtle.ycor() in range(225, 275):
                    crash = crashed(turtle, list)
                elif turtle.xcor() in range(125, 175) and turtle.ycor() == 225:
                    crash = crashed(turtle, list)
                elif turtle.xcor() == 175 and turtle.ycor() in range(125, 225):
                    crash = crashed(turtle, list)
                elif turtle.xcor() in range(75, 175) and turtle.ycor() == 125:
                    crash = crashed(turtle, list)
                elif turtle.xcor() == 75 and turtle.ycor() in range(125, 175):
                    crash = crashed(turtle, list)                   
                elif turtle.xcor() in range(75, 125) and turtle.ycor() == 175:
                    crash = crashed(turtle, list)
                elif turtle.xcor() in range(75, 125) and turtle.ycor() == 75:
                    crash = crashed(turtle, list)
                elif turtle.xcor() == 125 and turtle.ycor() in range(-75, 75):
                    crash = crashed(turtle, list)
                elif turtle.xcor() in range(25, 75) and turtle.ycor() == 25:
                    crash = crashed(turtle, list)
                elif turtle.xcor() in range(75, 125) and turtle.ycor() == -25:
                    crash = crashed(turtle, list)
                elif turtle.xcor() in range(125, 275) and turtle.ycor() == -125:
                    crash = crashed(turtle, list)
                elif turtle.xcor() == 75 and turtle.ycor() in range(-175, -125):
                    crash = crashed(turtle, list)
                elif turtle.xcor() in range(75, 225) and turtle.ycor() == -175:
                    crash = crashed(turtle, list)
                elif turtle.xcor() == 225 and turtle.ycor() in range(-225, -175):
                    crash = crashed(turtle, list)
                elif turtle.xcor() in range(25, 225) and turtle.ycor() == -225:
                    crash = crashed(turtle, list)
                
    if crash == False: # James Blake - Life Is Not The Same (Official Lyric Video) 
        moves.append(b)
        moves.append(c)
        turtle.speed(0)
    elif crash == True:
        moves = ["end"]
        turtle.speed(0)
    return cough

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

    walls.right(90)
    walls.forward(350) # line (25, 275 - -75 )

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

#start
def start():
    user = turtle.Turtle()
    user.pencolor("green")
    user.speed(0)
    user.penup()
    user.goto(250, 250)
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
            amount = int(input("How far do you want to go? (only input a number) "))

            a = frw(user, amount, "lvl1", moves, a)
        elif move == "r":
            amount = int(input("How much do you want to turn. "))
            user.right(amount)
        elif move == "l":
            amount = int(input("How much do you want to turn. "))
            user.left(amount)
        if move != "frw":
            moves.append(amount)
            moves.append(move)


start()
