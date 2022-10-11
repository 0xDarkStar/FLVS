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
def main():
#Products and their costs (from Amazon)
    global pCost1
    global pCost2
    global pCost3
    global pName1
    global pName2
    global pName3

    Test = namedtuple("Test", ["name", "cost"])
    a = 0

    Nothing = ("nothing", "Nothing", "NOTHING", "no")
    Nothing = Test(Nothing, "0.00")

    Jif = ("jif", "Jif", "JIF", "jif peanut butter", "Jif peanut butter", "JIF PEANUT BUTTER", "Jif Peanut Butter" "a", "A")
    Jif = Test(Jif, "23.00")

    Heinz = ("heinz", "Heinz", "HEINZ", "ketchup", "Ketchup", "KETCHUP", "b", "B")
    Heinz = Test(Heinz, "39.52")

    Asus = ("ASUS", "Asus", "asus", "Motherboard", "motherboard", "MOTHERBOARD", "Ryzen", "ryzen", "RYZEN", "c", "C")
    Asus = Test(Asus, "202.99")

    Windows = ("windows", "Windows", "WINDOWS", "os", "OS", "D", "d")
    Windows = Test(Windows, "109.98")

    Nike = ("nike", "Nike", "NIKE", "Air Force", "air force", "AIR FORCE", "E", "e")
    Nike = Test(Nike, "149.11")

    Blahaj = ("blahaj", "Blahaj", "BLAHAJ", "Ikea", "ikea", "IKEA", "F", "f")
    Blahaj = Test(Blahaj, "139.99")

    dugtrio = ("dugtrio", "dugtrio", "dugtrio", "buff dugtrio", "Buff dugtrio", "Buff dugtrio", "BUFF dugtrio", "G", "g")
    dugtrio = Test(dugtrio, "42.99")

    Pikachu = ("pikachu", "Pikachu", "PIKACHU", "buff pikachu", "Buff Pikachu", "Buff pikachu", "BUFF PIKACHU", "H", "h")
    Pikachu = Test(Pikachu, "35.99")

    Banana = ("Banana man", "Banana Man", "BANANA MAN", "banana man", "banana", "Banana", "BANANA", "helegeSONG", "helegesong", "HELEGESONG")
    Banana = Test(Banana, "15.99")

    Products = (Jif, Heinz, Asus, Windows, Nike, Blahaj, dugtrio, Pikachu, Banana, Nothing)

#look for the product name in a list to return price
    def pCost(product, list):
        if product in list.name:
            product = list.cost
            return product
        else:
            return False

#look for the product cost from all products to return name
    def pName(cost, list):
        if str(cost) in list.cost:
            cost = list.name[1]
            return cost
        else:
            return False

#List off products the user can choose from
    print("You can choose three products to keep. The products are: \n A. Jif Peanut Butter\n B. 1000 Heinz ketchup single serve packets\n C. ASUS AM4 TUF Gaming X570-Plus (Wi-Fi) AM4 Zen 3 Ryzen 5000 & 3rd Gen Ryzen ATX Motherboard with PCIe 4.0, Dual M.2, 12+2 with Dr. MOS Power Stage\n D. Windows 10 Home 64 Bit OS\n E. Nike Mens Air Force 1 Low Sneaker 8.5 M US\n F. Ikea Blahaj Soft Toy Shark (pack of 3, 39 1/4 inches)\n G. Buff dugtrio Figurine\n H. Buff Pikachu Figurine\n I. Banana Man")

#start asking what they want
#Product 1
#Get the cost
    product1 = input("What is the first product you want? ")
    while a <= 9:
        if pCost(product1, Products[a]) != False:
            if pCost(product1, Nothing) != False:
                pCost1 = 0.00
                print("You chose nothing")
                break
            pCost1 = float(pCost(product1, Products[a]))
            break
        else:
            a += 1
            if a == 10:
                print("You didn't choose anything on the list or didn't spell it write, try again")
                exit()

#Get the name
    a = 0
    if pCost1 > 0.00:
        while a <= 9:
            if pName(pCost1, Products[a]) != False:
                pName1 = pName(pCost1, Products[a])
                break
            else:
                a += 1
    else:
        pName1 = "Nothing"


#Product 2
#Get the cost
    product2 = input("What is the second product you want? ")
    a = 0
    while a <= 9:
        if pCost(product2, Products[a]) != False:
            if pCost(product2, Nothing) != False:
                pCost2 = 0.00
                print("You chose nothing")
                break
            pCost2 = float(pCost(product2, Products[a]))
            break
        elif pCost(product2, Products[a]) == False:
            a += 1
            if a == 10:
                print("You didn't choose anything on the list or didn't spell it write, try again")
                exit()

#Get the name
    a = 0
    if pCost2 > 0.00:
        while a <= 9:
            if pName(pCost2, Products[a]) != False:
                pName2 = pName(pCost2, Products[a])
                break
            else:
                a += 1
    else:
        pName2 = "Nothing"


#Product 3
#Get the cost
    product3 = input("What is the third product you want? ")
    a = 0
    while a <= 9:
        if pCost(product3, Products[a]) != False:
            if pCost(product3, Nothing) != False:
                pCost3 = 0.00
                print("You chose nothing")
                break
            pCost3 = float(pCost(product3, Products[a]))
            break
        elif pCost(product3, Products[a]) == False:
            a += 1
            if a == 10:
                print("You didn't choose anything on the list or didn't spell it write, try again")
                exit()

#Get the name
    a = 0
    if pCost3 > 0.00:
        while a <= 9:
            if pName(pCost3, Products[a]) != False:
                pName3 = pName(pCost3, Products[a])
                break
            else:
                a += 1
    else:
        pName3 = "Nothing"


    a = 0
    #add the costs of the products they chose
    Subtotal = float(pCost1) + float(pCost2) + float(pCost3)
    Subtotal=Subtotal*100
    Subtotal=Subtotal//1
    Subtotal=Subtotal/100
    if Subtotal > 0.00:
        Tax = Subtotal * .065
        Tax=Tax*100
        Tax=Tax//1
        Tax=Tax/100
        #add the 6.5% tax and $5.99 shipping cost
        Total = Tax + Subtotal + 5.99
        #this is to have only 2 digits after the "."
        Total=Total*100
        Total=Total//1
        Total=Total/100
        time.sleep(1)
        print("""
        Your Wishlist Results:

        Item                        Cost

        """ + pName1 + """                  $""" + str(pCost1) + """
        """ + pName2 + """                  $""" + str(pCost2) + """
        """ + pName3 + """                  $""" + str(pCost3) + """
        ------------------------------------------
            Subtotal:              $""" + str(Subtotal) + """
            Tax:                   $""" + str(Tax) + """
            Shipping:              $5.99
            Total:                 $""" + str(Total) + """

        I hope you enjoyed this service
        """)
        time.sleep(2)
        print("PLEASE GIVE ME A FIVE STAR REVIEW ON YELP! PLEASE! I BEG YOU!")
    #they chose "nothing" for all three products
    else:
        time.sleep(2)
        print("You really don't want any of them? Okay then, go have fun with your garbage! Not like I want people to try it....")
main()

"""
Should look like this

Item                        Cost

Product1                    $?.??
Product2                    $?.??
Product3                    $?.??
---------------------------------------
    Subtotal:              $??.??
    Tax:                    $?.??
    Shipping:               $5.99
    Total:                 $??.??
"""
