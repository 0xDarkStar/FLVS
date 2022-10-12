'''
I hate having to find a side of a right triangle for school or just work that I'm doing....
Now I won't have to though (and neither do you) since the code would do it for you!
All you have to do is fill in the variables with what you know and it tell you the answer!
(You need two or more variables filled in)
'''

import math, time

#Variables for the sides. If you don't have the measurment for that side, leave a "?". Also, don't add "inches", "in.", "cm", "centimeters", etc.

print("I will ask you for the sizes of both legs and the hypotenuse, if you don't have it, just put '?'. \nAlso! Don't include stuff like inches or cm, you would break the code.") 
time.sleep(2)
Leg1 = input("\nWhat is the size of leg 1? ")
Leg2 = input("What is the size of leg 2? ")
Hypot = input("What is the size of the hypotenuse? ")

#Make sure that the program doesn't run with only one measurement since it won't work with only one (duh). It would also work if all three are "?"
if Leg1 == "?" and Leg2 == "?" or Leg2 == "?" and Hypot == "?" or Leg1 == "?" and Hypot == "?":
    print("I need two measurements to work, please come back when you have two.")
    exit()

#Now that we know the user has 2 or more variables filled in then we can start doing the math
#If the have both legs, it'll tell them the hypotenuse
if Leg1 != "?" and Leg2 != "?":
    print("\nI will check if that can be a right triangle. If it isn't, I'll tell you the correct hypotenuse.")
    print("Leg 1 is '" + str(Leg1) + "' and leg 2 is '" + str(Leg2) + "'.")
    x = math.sqrt(float(Leg1) ** 2 + float(Leg2) ** 2)
    y = round(x, 2) #Nobody would want to type an extremely long number as their answer right? You'd want to round to the hundredths place most of the time.
    if y == Hypot or int(y) == Hypot or x == Hypot:
        print("\nThat is a right triangle.")
        print("\nI hope this helped!")
    elif Hypot == "?" or Hypot == "":
        print("The hypotenuse would be '" + str(x) + "'.")
        print("\nI hope this helped!")
    else:
        print("\nIt isn't a right triangle.")
        print("The hypotenuse is '" + str(x) + "'.")
        print("\nI hope this helped!")

#If they have a hypotenuse and one leg we'll look for the missing leg
elif Hypot != "?" and Leg1 != "?" and Leg2 == "?" or Hypot != "?" and Leg2 != "?" and Leg1 == "?":
    if Leg1 == "?": #Leg 1 is missing
        print("\nI will look for Leg 1")
        print("Leg 2 is '" + str(Leg2) + "' and the hypotenuse is '" + str(Hypot) + "'.")
        Leg1 = math.sqrt(float(Hypot) ** 2 - float(Leg2) ** 2)
        print("\nLeg 1 is '" + str(Leg1) + "'.")
        print("\nI hope this helped!")
    else: #Leg 2 is missing
        print("\nI will look for Leg 2")
        print("Leg 1 is '" + str(Leg1) + "' and the hypotenuse is '" + str(Hypot) + "'.")
        Leg2 = math.sqrt(float(Hypot) ** 2 - float(Leg1) ** 2)
        print("\nLeg 2 is '" + str(Leg2) + "'.")
        print("\nI hope this helped!")