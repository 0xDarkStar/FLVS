'''
This is meant to help me find the diameter, radius, area, and circumference of a circle.
'''

import math

What = input("What do you need to find?\nA. Diameter + Radius\nB. Area\nC. Circumference\n\n  ")
A = ("a", "A", "Diameter", "diameter", "Radius", "radius")
B = ("b", "B", "Area", "area")
C = ("c", "C", "Circumference", "circumference")

#What did they choose?
if What in A:
    print("\nYou want to find the diameter and radius.")
    #Which one do they have?
    Which = input("Do you have the circumference or area? ")

    if Which in B:
        print("You have the area.")
        area = input("What is the area? ")
        radius = math.sqrt(float(area) / 3.14)
        print("The radius is " + str(radius) + " and the diameter is " + str(radius * 2))

    elif Which in C:
        print("You have the circumference.")
        circum = input("What is the circumference? ")
        diameter = float(circum) / 3.14
        print("The radius is " + str(diameter / 2) + " and the diameter is " + str(diameter))

    else:
        print("I didn't get that.")


elif What in B:
    print("You want to find the area.")
    #Which one do they have?
    Which = input("Do you have the radius, diameter, or circumference? ")

    if Which == "radius" or Which == "Radius":
        print("You have the radius")
        radius = input("What is the radius? ")
        area = 3.14 * pow(float(radius), 2)
        print("The area is " + str(area))

    elif Which == "diameter" or Which == "Diameter":
        print("You have the diameter.")
        diameter = input("What is the diameter? ")
        radius = float(diameter) / 2
        area = 3.14 * pow(float(radius), 2)
        print("The area is " + str(area))

    elif Which == "circumference" or Which == "Circumference":
        print("You have the circumference.")
        circum = input("What is the circumference? ")
        radius = (float(circum) / 3.14) / 2
        area = 3.14 * pow(float(radius), 2)
        print("The area is " + str(area))


elif What in C:
    print("You want to find the circumference.")
    #Which one do they have?
    Which = input("Do you have the radius, diameter, or area? ")

    if Which == "Radius" or Which == "radius":
        print("You have the radius.")
        radius = input("What is the radius? ")
        circum = (float(radius) * 2) * 3.14
        print("The circumference is " + str(circum))

    elif Which == "Diameter" or Which == "diameter":
        print("You have the diameter.")
        diameter = input("What is the diameter? ")
        circum = float(diameter) * 3.14
        print("The circumference is " + str(circum))

    elif Which == "area" or Which == "Area":
        print("You have the area.")
        area = input("What is the area? ")
        radius = math.sqrt(float(area) / 3.14)
        circum = (radius * 2) * 3.14
        print("The circumference is " + str(circum))

else:
    print("I didn't get that.")
