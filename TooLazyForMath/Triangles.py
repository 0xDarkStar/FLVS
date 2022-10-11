#I hate having to find the side of a triangle by looking at the hypotenuse or legs or a hypotenuse and a leg to find the other sides

import math

#Variables for the sides. If you don't have the measurment for that side, leave a "?". Also, don't add "inches", "in.", "cm", "centimeters", etc.

Leg1 =5
Leg2 = 10
Hypot = 14

#Make sure that the program doesn't run with only one measurement since it won't work with only one (duh). It would also work if all three are "?"
if Leg1 == "?" and Leg2 == "?" or Leg2 == "?" and Hypot == "?" or Leg1 == "?" and Hypot == "?":
    print("I need two measurements to work, please come back when you have two.")
    exit()

#Now that we know the user has 2 or more variables filled in then we can start doing the math
#Let's start with finding the hypotenuse
if Leg1 != "?" and Leg2 != "?"  and Hypot == "?":
    print("\nI am looking for the hypotenuse")
    print("Leg 1 is '" + str(Leg1) + "' and Leg 2 is '" + str(Leg2) + "'.")
    Hypot = math.sqrt(float(Leg1) ** 2 + float(Leg2) ** 2)
    print("\nThe hypotenuse is " + str(Hypot))
    print("\nI hope this helped!")

#If they had the hypotenuse then we'll look using that
elif Hypot != "?" and Leg1 != "?" and Leg2 == "?" or Hypot != "?" and Leg2 != "?" and Leg1 == "?":
    if Leg1 == "?":
        print("\nI will look for Leg 1")
        print("Leg 2 is '" + str(Leg2) + "' and the hypotenuse is '" + str(Hypot) + "'.")
        Leg1 = math.sqrt(float(Hypot) ** 2 - float(Leg2) ** 2)
        print("\nLeg 1 is '" + str(Leg1) + "'.")
        print("\nI hope this helped!")
    else:
        print("\nI will look for Leg 2")
        print("Leg 1 is '" + str(Leg1) + "' and the hypotenuse is '" + str(Hypot) + "'.")
        Leg2 = math.sqrt(float(Hypot) ** 2 - float(Leg1) ** 2)
        print("\nLeg 2 is '" + str(Leg2) + "'.")
        print("\nI hope this helped!")

#If they have all the measurements then we can check if they are correct or not
elif Leg1 != "?" and Leg2 != "?" and Hypot != "?":
    print("\nI will check if that can be a triangle")
    print("Leg 1 is '" + str(Leg1) + "', leg 2 is '" + str(Leg2) + "', and the hypotenuse is '" + str(Hypot) + "'.")
    x = math.sqrt(float(Leg1) ** 2 + float(Leg2) ** 2)
    y = round(x, 2) #Nobody would want to type an extremely long number as their answer right? You'd want to round to the hundredths place most of the time.
    print(x)
    print(y)
    if y == Hypot or int(y) == Hypot or x == Hypot:
        print("\nThat can be a triangle.")
        print("\nI hope this helped!")
    else:
        print("\nIt can't be a triangle.")
        print("\nI hope this helped!")