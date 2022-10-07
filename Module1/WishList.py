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

Jif = ("jif", "Jif", "JIF", "peanut", "Peanut", "PEANUT", "butter", "Butter", "BUTTER", "a", "A")
Jif = Test(Jif, '23.00')

Heinz = ("heinz", "Heinz", "HEINZ", "tomato", "Tomato", "TOMATO", "ketchup", "Ketchup", "KETCHUP", "b", "B")
Heinz = Test(Heinz, '5.87')

Asus = ("ASUS", "Asus", "asus", "Motherboard", "motherboard", "MOTHERBOARD", "c", "C")
Asus = Test(Asus, '202.99')

Products = (Jif, Heinz, Asus, )

#look for the product name in a list
def pCost(product, list):
    if product in list.name:
        product = list.cost
        return product
    else:
        return False

product1 = input("What is the first product you want? ")
while a <= 7:
    if pCost(product1, Products[a]) != False:
        cost1 = pCost(product1, Products[a])
        print("That will cost you $" + str(cost1))
        break
    else:
        a += 1

product2 = input("What is the second product you want? ")
a = 0
while a <= 7:
    if pCost(product2, Products[a]) != False:
        cost2 = pCost(product2, Products[a])
        print("That will cost you $" + str(cost2))
        break
    else:
        a += 1

product3 = input("What is the third product you want? ")
a = 0
while a <= 7:
    if pCost(product3, Products[a]) != False:
        cost3 = pCost(product3, Products[a])
        print("That will cost you $" + str(cost3))
        break
    else:
        a += 1

a = 0
totalProductCost = float(cost1) + float(cost2) + float(cost3)
#with taxes and shipping costs (and numbers past 2 digits behind the ".")
totalProductCost = (totalProductCost * .065) + totalProductCost + 5.99
#this is to have only 2 digits after the "."
totalProductCost=totalProductCost*100
totalProductCost=totalProductCost//1
totalProductCost=totalProductCost/100

print("\nThe total cost of all those items are $" + str(totalProductCost))
