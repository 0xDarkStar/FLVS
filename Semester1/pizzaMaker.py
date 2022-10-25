global a
a = 0

import os

# Find the input in a list of lists
def find(input, listL):
    a = 0
    while a < 10:
        if input in listL[a]:
            return a
        else:
            a += 1

# Redefine the input to the 2nd one in the list that it's in
def redefine(input, listL):
    input = find(input, listL) # check line 7
    input = listL[input]
    input = input[2]
    return input

# WARNING!!!
# TONS OF LISTS AHEAD
# LOOKS TERRIBLE

def pizSize():
    small = ("a", "A", "small", "Small", "SMALL")
    medium = ("b", "B", "medium", "Medium", "MEDIUM")
    large = ("c", "C", "large", "Large", "LARGE")

    sizeL = (small, medium, large)

    size = input("What size pizza do you want? \nA. Small \nB. Medium \nC. Large\n   ") # Find out what size they want

    size = redefine(size, sizeL) # Check line 15
    return size

def pizCrust():
    stuff = ("a", "A", "stuffed crust", "Stuffed crust", "stuffed Crust", "Stuffed Crust", "STUFFED CRUST")
    cracker = ("b", "B", "cracker crust", "Cracker crust", "cracker Crust", "Cracker Crust", "CRACKER CRUST")
    flat = ("c", "C", "flat bread", "Flat bread", "flat Bread", "Flat Bread", "FLAT BREAD")
    # AAAAAA!!!! I'M SURROUNDED BY LISTS!!!
    thin = ("d", "D", "thin crust", "Thin crust", "thin Crust", "Thin Crust", "THIN CRUST")
    cheeseC = ("e", "E", "cheese crust", "Cheese crust", "cheese Crust", "Cheese Crust", "CHEESE CRUST")
    thick = ("f", "F", "thick crust", "Thick crust", "thick Crust", "Thick Crust", "THICK CRUST")

    crustL = (stuff, cracker, flat, thin, cheeseC, thick)

    # Eitherway, that one below me is to find what crust the user wants
    crust = input("\nWhat type of crust do you want? (If you don't know what any of these crusts are, I recommend googling it) \nA. Stuffed Crust \nB. Cracker Crust \nC. Flat Bread \nD. Thin Crust \nE. Cheese Crust \nF. Thick Crust \n   ")

    crust = redefine(crust, crustL) # Check line 15 if you don't know what this is
    return crust

def pizCheese():
    mozz = ("a", "A", "mozzarella", "Mozzarella", "MOZZARELLA")
    prov = ("b", "B", "provolone", "Provolone", "PROVOLONE")
    ched = ("c", "C", "cheddar", "Cheddar", "CHEDDAR")
    parm = ("d", "D", "parmesan", "Parmesan", "PARMESAN")
    # So many....
    goud = ("e", "E", "gouda", "Gouda", "GOUDA")
    goat = ("f", "F", "goat cheese", "Goat cheese", "goat Cheese", "Goat Cheese", "GOAT CHEESE")
    gruy = ("g", "G", "gruyere", "Gruyere", "GRUYERE")
    rico = ("h", "H", "ricotta", "Ricotta", "RICOTTA")

    cheeseL = (mozz, prov, ched, parm, goud, goat, gruy, rico)

    # Again, finding what the user wants. This time, it's cheese
    cheese = input("What type of cheese do you want? \nA. Mozzarella \nB. Provolone \nC. Cheddar \nD. Parmesan \nE. Gouda \nF. Goat Cheese \nG. Gruyere \nH. Ricotta \n   ")

    cheese = redefine(cheese, cheeseL)
    return cheese

def pizTopping():
    pep = ("a", "A", "pepperoni", "Pepperoni", "PEPPERONI")
    mus = ("b", "B", "mushroom", "Mushroom", "MUSHROOM")
    che = ("c", "C", "extra cheese", "Extra cheese", "extra Cheese", "Extra Cheese", "EXTRA CHEESE")
    sau = ("d", "D", "sausage", "Sausage", "SAUSAGE")
    oni = ("e", "E", "onion", "Onion", "ONION")
    # This function has the most lists out of them all
    bla = ("f", "F", "black olives", "Black olives", "black Olives", "Black Olives", "BLACK OLIVES")
    gre = ("g", "G", "green pepper", "Green pepper", "green Pepper", "Green Pepper", "GREEN PEPPER")
    frG = ("h", "H", "fresh garlic", "Fresh garlic", "fresh Garlic", "Fresh Garlic", "FRESH GARLIC")
    tom = ("i", "I", "tomato", "Tomato", "TOMATO")
    frB = ("j", "J", "fresh basil", "Fresh basil", "fresh Basil", "Fresh Basil", "FRESH BASIL")

    toppingL = (pep, mus, che, sau, oni, bla, gre, frG, tom, frB)

    amount = int(input("How many toppings do you want? (most you can choose is 10) "))

    # WARNING!!!
    # REALLY REPETETIVE CODE UP AHEAD
    # SKIP TO LINE 241 IF YOU DON'T WANT TO SEE IT

    if amount > 1:
        print("Okay, I will have multiple prompts for you to input the topping you want. Don't put them all in one promp please.")

    # It begins
    if amount == 1:
        topping1 = input("What toppings do you want? \nA. Pepperoni\nB. Mushroom\nC. Extra Cheese\nD. Sausage\nE. Onion\nF. Black Olives\nG. Green Pepper\nH. Fresh Garlic\nI. Tomato\nJ. Fresh Basil\n   ")
        topping1 = redefine(topping1, toppingL)
        return topping1
    elif amount == 2:
        topping1 = input("What toppings do you want? \nA. Pepperoni\nB. Mushroom\nC. Extra Cheese\nD. Sausage\nE. Onion\nF. Black Olives\nG. Green Pepper\nH. Fresh Garlic\nI. Tomato\nJ. Fresh Basil\n   ")
        topping1 = redefine(topping1, toppingL)
        topping2 = input("   ")
        topping2 = redefine(topping2, toppingL)
        topping = topping1 + " and " + topping2
        return topping
    elif amount == 3:
        topping1 = input("What toppings do you want? \nA. Pepperoni\nB. Mushroom\nC. Extra Cheese\nD. Sausage\nE. Onion\nF. Black Olives\nG. Green Pepper\nH. Fresh Garlic\nI. Tomato\nJ. Fresh Basil\n   ")
        topping1 = redefine(topping1, toppingL)
        topping2 = input("   ")
        topping2 = redefine(topping2, toppingL)
        topping3 = input("   ")
        topping3 = redefine(topping3, toppingL)
        topping = topping1 + ", " + topping2 + ", and " + topping3
        return topping
    elif amount == 4:
        topping1 = input("What toppings do you want? \nA. Pepperoni\nB. Mushroom\nC. Extra Cheese\nD. Sausage\nE. Onion\nF. Black Olives\nG. Green Pepper\nH. Fresh Garlic\nI. Tomato\nJ. Fresh Basil\n   ")
        topping1 = redefine(topping1, toppingL)
        topping2 = input("   ")
        topping2 = redefine(topping2, toppingL)
        topping3 = input("   ")
        topping3 = redefine(topping3, toppingL)
        topping4 = input("   ")
        topping4 = redefine(topping4, toppingL)
        topping = topping1 + ", " + topping2 + ", " + topping3 + ", and " + topping4
        return topping
    elif amount == 5:
        topping1 = input("What toppings do you want? \nA. Pepperoni\nB. Mushroom\nC. Extra Cheese\nD. Sausage\nE. Onion\nF. Black Olives\nG. Green Pepper\nH. Fresh Garlic\nI. Tomato\nJ. Fresh Basil\n   ")
        topping1 = redefine(topping1, toppingL)
        topping2 = input("   ")
        topping2 = redefine(topping2, toppingL)
        topping3 = input("   ")
        topping3 = redefine(topping3, toppingL)
        topping4 = input("   ")
        topping4 = redefine(topping4, toppingL)
        topping5 = input("   ")
        topping5 = redefine(topping5, toppingL)
        topping = topping1 + ", " + topping2 + ", " + topping3 + ", " + topping4 + ", and " + topping5
        return topping
    elif amount == 6:
        topping1 = input("What toppings do you want? \nA. Pepperoni\nB. Mushroom\nC. Extra Cheese\nD. Sausage\nE. Onion\nF. Black Olives\nG. Green Pepper\nH. Fresh Garlic\nI. Tomato\nJ. Fresh Basil\n   ")
        topping1 = redefine(topping1, toppingL)
        topping2 = input("   ")
        topping2 = redefine(topping2, toppingL)
        topping3 = input("   ")
        topping3 = redefine(topping3, toppingL)
        topping4 = input("   ")
        topping4 = redefine(topping4, toppingL)
        topping5 = input("   ")
        topping5 = redefine(topping5, toppingL)
        topping6 = input("   ")
        topping6 = redefine(topping6, toppingL)
        topping = topping1 + ", " + topping2 + ", " + topping3 + ", " + topping4 + ", " + topping5 + ", and " + topping6
        return topping
    elif amount == 7:
        topping1 = input("What toppings do you want? \nA. Pepperoni\nB. Mushroom\nC. Extra Cheese\nD. Sausage\nE. Onion\nF. Black Olives\nG. Green Pepper\nH. Fresh Garlic\nI. Tomato\nJ. Fresh Basil\n   ")
        topping1 = redefine(topping1, toppingL)
        topping2 = input("   ")
        topping2 = redefine(topping2, toppingL)
        topping3 = input("   ")
        topping3 = redefine(topping3, toppingL)
        topping4 = input("   ")
        topping4 = redefine(topping4, toppingL)
        topping5 = input("   ")
        topping5 = redefine(topping5, toppingL)
        topping6 = input("   ")
        topping6 = redefine(topping6, toppingL)
        topping7 = input("   ")
        topping7 = redefine(topping7, toppingL)
        topping = topping1 + ", " + topping2 + ", " + topping3 + ", " + topping4 + ", " + topping5 + ", " + topping6 + ", and " + topping7
        return topping
    elif amount == 8:
        topping1 = input("What toppings do you want? \nA. Pepperoni\nB. Mushroom\nC. Extra Cheese\nD. Sausage\nE. Onion\nF. Black Olives\nG. Green Pepper\nH. Fresh Garlic\nI. Tomato\nJ. Fresh Basil\n   ")
        topping1 = redefine(topping1, toppingL)
        topping2 = input("   ")
        topping2 = redefine(topping2, toppingL)
        topping3 = input("   ")
        topping3 = redefine(topping3, toppingL)
        topping4 = input("   ")
        topping4 = redefine(topping4, toppingL)
        topping5 = input("   ")
        topping5 = redefine(topping5, toppingL)
        topping6 = input("   ")
        topping6 = redefine(topping6, toppingL)
        topping7 = input("   ")
        topping7 = redefine(topping7, toppingL)
        topping8 = input("   ")
        topping8 = redefine(topping8, toppingL)
        topping = topping1 + ", " + topping2 + ", " + topping3 + ", " + topping4 + ", " + topping5 + ", " + topping6 + ", " + topping7 + ", and " + topping8
        return topping
    elif amount == 9:
        topping1 = input("What toppings do you want? \nA. Pepperoni\nB. Mushroom\nC. Extra Cheese\nD. Sausage\nE. Onion\nF. Black Olives\nG. Green Pepper\nH. Fresh Garlic\nI. Tomato\nJ. Fresh Basil\n   ")
        topping1 = redefine(topping1, toppingL)
        topping2 = input("   ")
        topping2 = redefine(topping2, toppingL)
        topping3 = input("   ")
        topping3 = redefine(topping3, toppingL)
        topping4 = input("   ")
        topping4 = redefine(topping4, toppingL)
        topping5 = input("   ")
        topping5 = redefine(topping5, toppingL)
        topping6 = input("   ")
        topping6 = redefine(topping6, toppingL)
        topping7 = input("   ")
        topping7 = redefine(topping7, toppingL)
        topping8 = input("   ")
        topping8 = redefine(topping8, toppingL)
        topping9 = input("   ")
        topping9 = redefine(topping9, toppingL)
        topping = topping1 + ", " + topping2 + ", " + topping3 + ", " + topping4 + ", " + topping5 + ", " + topping6 + ", " + topping7 + ", " + topping8 + ", and " + topping9
        return topping
    elif amount == 10:
        topping1 = input("What toppings do you want? \nA. Pepperoni\nB. Mushroom\nC. Extra Cheese\nD. Sausage\nE. Onion\nF. Black Olives\nG. Green Pepper\nH. Fresh Garlic\nI. Tomato\nJ. Fresh Basil\n   ")
        topping1 = redefine(topping1, toppingL)
        topping2 = input("   ")
        topping2 = redefine(topping2, toppingL)
        topping3 = input("   ")
        topping3 = redefine(topping3, toppingL)
        topping4 = input("   ")
        topping4 = redefine(topping4, toppingL)
        topping5 = input("   ")
        topping5 = redefine(topping5, toppingL)
        # ;-;
        topping6 = input("   ")
        topping6 = redefine(topping6, toppingL)
        topping7 = input("   ")
        topping7 = redefine(topping7, toppingL)
        topping8 = input("   ")
        topping8 = redefine(topping8, toppingL)
        topping9 = input("   ")
        topping9 = redefine(topping9, toppingL)
        topping10 = input("   ")
        topping10 = redefine(topping10, toppingL)
        topping = topping1 + ", " + topping2 + ", " + topping3 + ", " + topping4 + ", " + topping5 + ", " + topping6 + ", " + topping7 + ", " + topping8 + ", " + topping9 + ", and " + topping10
        return topping
    elif amount == 0:
        print("You want no toppings? Got it!")
        topping == "nothing"
        return topping
# That's all the lists done

def program():
    # Storing the return values as variables to use in the print
    size = pizSize() # Go to line 26 if you want to check it
    crust = pizCrust() # Go to line 38 if you want to check it
    cheese = pizCheese() # Go to line 55 if you want to check it
    topping = pizTopping() # Go to line 74 if you want to check it

    # Just so you know, the pizTopping function ends at line 242
    # 168 LINES LATER!
    # That's how repetetive it is....

    os.system("cls") # Get rid of the terrible mess from before

    # And now we tell them what they chose in a clean print statement.
    print("You want your pizza to be a " + size + " with " + crust + ".\n You want the on your pizza cheese to be " + cheese + ". You also want " + topping + " on top.")
# And it's done
# All that's left is...

program()# To run it all!
