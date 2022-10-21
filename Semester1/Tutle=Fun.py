#My first time messing with the turtle module

import turtle, time

def main():

	print("Artist Name: 0xDarkStar")
	print("Title: Bleeding Heart		(Boring, I know)")
	
	#draw the heart
	heart = turtle.Turtle()
	heart.pencolor("red")
	heart.left(45)
	heart.forward(50)
	#right curve
	for a in range(7):
		heart.left(25.7)
		heart.forward(10)
		a += 1
	heart.right(115)
	#left curve
	for a in range(7):
		heart.left(25.7)
		heart.forward(10)
		a += 1
	heart.left(29)
	heart.forward(54)
	heart.hideturtle()
	#heart is done, time to make an arrow
	
	arrow = turtle.Turtle()
	arrow.pencolor("red")
	arrow.left(45)
	arrow.forward(30)
	arrow.right(90)
	arrow.pencolor("black")
	#start stick of arrow
	arrow.forward(15)
	#right fin
	arrow.left(25)
	arrow.forward(10)
	arrow.right(25)
	arrow.forward(20)
	arrow.right(155)
	arrow.forward(10)
	arrow.right(25)
	arrow.forward(20)
	arrow.left(180)
	#back at the start of fin, time to make left fin
	arrow.right(25)
	arrow.forward(10)
	arrow.left(25)
	arrow.forward(20)
	arrow.left(155)
	arrow.forward(10)
	arrow.left(25)
	#left fin done, time to extend line further
	arrow.forward(60)
	#unsure on wether or not I should draw an arrow head
	
	blood = turtle.Turtle()
	blood.hideturtle()
	blood.pencolor("red") #passing through the heart
	blood.left(45)
	blood.forward(30)
	blood.pencolor("black") #reached the arrow
	blood.left(90)
	blood.forward(25)
	blood.showturtle()
	arrow.hideturtle()
	blood.pencolor("dark red") #starting to draw the blood
	blood.left(135)
	blood.forward(5)
	for a in range(9):
		blood.right(5)
		blood.forward(.5)
	for a in range(25):
		blood.left(5)
		blood.forward(.5)
	for a in range(12):
		blood.right(5)
		blood.forward(.3)
	for a in range(18):
		blood.left(10)
		blood.forward(1)
	blood.left(25)
	blood.forward(10)
	blood.hideturtle()
	time.sleep(2.5)
main()
