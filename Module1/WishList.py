"""
1. Make a list of items for the user to choose
2. Inform user that they are to choose 3 or more items from the list
3. Add up the prices and shipping costs of all the items they chose
4. Tell them the cost of everything they chose
all prices and shipping costs are coming from Amazon
"""

#imports
import time, math
from collections import namedtuple

#Products and their costs (from Amazon)
global cost1
global cost2
global cost3

Test = namedtuple('Test', ['name', 'cost'])
a = 0

Nothing = ("nothing", "Nothing", "NOTHING", "no")
Nothing = Test(Nothing, '0.00')

Jif = ("jif", "Jif", "JIF", "a", "A")
Jif = Test(Jif, '23.00')

Heinz = ("heinz", "Heinz", "HEINZ", "b", "B")
Heinz = Test(Heinz, '39.52')

Asus = ("ASUS", "Asus", "asus", "Motherboard", "motherboard", "MOTHERBOARD", "Ryzen", "ryzen", "RYZEN", "c", "C")
Asus = Test(Asus, '202.99')

Windows = ("windows", "Windows", "WINDOWS", "os", "OS", "D", "d")
Windows = Test(Windows, '109.98')

Nike = ("nike", "Nike", "NIKE", "Air Force", "air force", "AIR FORCE", "E", "e")
Nike = Test(Nike, '149.11')

Blahaj = ("blahaj", "Blahaj", "BLAHAJ", "Ikea", "ikea", "IKEA", "F", "f")
Blahaj = Test(Blahaj, '139.99')

Digtrio = ("digtrio", "Digtrio", "DIGTRIO", "G", "g")
Digtrio = Test(Digtrio, '42.99')

Pikachu = ("pikachu", "Pikachu", "PIKACHU", "H", "h")
Pikachu = Test(Pikachu, '35.99')

Banana = ("Banana man", "BANANA MAN", "Banana Man", "banana man", "banana", "Banana", "BANANA", "helegeSONG", "helegesong", "HELEGESONG", "I", "i")
Banana = Test(Banana, '15.99')

Products = (Jif, Heinz, Asus, Windows, Nike, Blahaj, Digtrio, Pikachu, Banana, Nothing)

#look for the product name in a list
def pCost(product, list):
    if product in list.name:
        product = list.cost
        return product
    else:
        return False

print("You can choose a few different products to keep. These products are: \n A. Jif Peanut Butter\n B. 1000 Heinz ketchup single serve packets\n C. ASUS AM4 TUF Gaming X570-Plus (Wi-Fi) AM4 Zen 3 Ryzen 5000 & 3rd Gen Ryzen ATX Motherboard with PCIe 4.0, Dual M.2, 12+2 with Dr. MOS Power Stage\n D. Windows 10 Home 64 Bit OS\n E. Nike Mens Air Force 1 Low Sneaker 8.5 M US\n F. Ikea Blahaj Soft Toy Shark (pack of 3, 39 1/4 inches)\n G. Buff Digtrio Figurine\n H. Buff Pikachu Figurine\n I. Banana Man")

product1 = input("What is the first product you want? ")
while a <= 9:
    if pCost(product1, Products[a]) != False:
        if pCost(product1, Nothing) != False:
            cost1 = 0.00
            print("You chose nothing")
            break
        cost1 = pCost(product1, Products[a]) #I had a print in the function before but it kept on getting ran twice so now it became...
        print("That will cost you $" + str(cost1)) #...this new print command, and the others I added....
        break
    elif pCost(product1, Products[a]) == False:
        a += 1
        if a == 10:
            print("You didn't choose anything on the list or didn't spell it write, try again")
            exit()

product2 = input("What is the second product you want? ")
a = 0
while a <= 9:
    if pCost(product2, Products[a]) != False:
        if pCost(product2, Nothing) != False:
            cost2 = 0.00
            print("You chose nothing")
            break
        cost2 = pCost(product2, Products[a])
        print("That will cost you $" + str(cost2))
        break
    elif pCost(product2, Products[a]) == False:
        a += 1
        if a == 10:
            print("You didn't choose anything on the list or didn't spell it write, try again")
            exit()

product3 = input("What is the third product you want? ")
a = 0
while a <= 9:
    if pCost(product3, Products[a]) != False:
        if pCost(product3, Nothing) != False:
            cost3 = 0.00
            print("You chose nothing")
            break
        cost3 = pCost(product3, Products[a])
        print("That will cost you $" + str(cost3))
        break
    elif pCost(product3, Products[a]) == False:
        a += 1
        if a == 10:
            print("You didn't choose anything on the list or didn't spell it write, try again")
            exit()

a = 0
totalProductCost = float(cost1) + float(cost2) + float(cost3)
#with taxes and shipping costs (and numbers past 2 digits behind the ".")
if totalProductCost > 0.00:
    totalProductCost = (totalProductCost * .065) + totalProductCost + 5.99
    #this is to have only 2 digits after the "."
    totalProductCost=totalProductCost*100
    totalProductCost=totalProductCost//1
    totalProductCost=totalProductCost/100
    time.sleep(2)
    print("\nI can't guarantee that they'd arrive at your home undamaged....")
    print("\nThe total cost of all those items are $" + str(totalProductCost) + ".")
    print("Now give me the money!")
else:
    time.sleep(2)
    print("You chose none of the products? Why? You could've gotten free stuff!")

print("\nThe total cost of all those items are $" + str(totalProductCost))
