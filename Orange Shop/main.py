import os
from apple import Apple
from orange import Orange
from shelf import Shelf

shelf = Shelf()
containerOranges = 0
containerApples = 0
totalApples = 0
totalOranges = 0
oranges = 0
apples = 0 

def main():
    global containerOranges, containerApples, oranges, apples, totalApples, totalOranges
    print(""" 
    --- Remember to buy merchandise before opening the store ---
        1. Buy Oranges 
        2. Apple order
        3. Open the store
    """)
    ans = input("Select an option: ")

    if ans == "1":
        print("The purchase price of oranges is $2")
        print("The selling price in the market for oranges is $4")
        containerOranges = int(input(" Enter the number of containers you want to buy: "))
        oranges = int(input(" Enter the number of oranges you want to buy in each container: "))
        totalOranges = containerOranges * oranges
        for i in range(totalOranges):
            addOranges()
        print("The amount of oranges you bought are: " + str(totalOranges)) 
        os.system("Pause")
        main()

    if ans == "2":
        print(" --- This order of apples will arrive at the store when we have no more oranges ---")
        print("The purchase price of apples is $3")
        print("The selling price in the market for apples is $5")
        containerApples = int(input(" Enter the number of containers you want to buy:"))
        apples = int(input(" Enter the number of apple you want to buy in each container: "))
        totalApples = containerApples * apples
        print("The amount of apples you preordered are: " + str(totalApples))
        os.system("Pause")
        main()
        
    if ans == "3":
        print("\n The number of oranges on the shelf is: " + str(shelf.size())+ "\n")
        flag = True
        while flag:
            if(shelf.size() == 0):
                print("""
                -------------------------------
                The order of apples has arrived
                -------------------------------
                """)
                break

            soldOranges= int(input("How many oranges does the customer want to buy?: "))

            if(soldOranges > shelf.size()):
                print("We only have: " + str(shelf.size()) + " Oranges")

            else:
                for i in range(soldOranges):
                    deleteFruit()
                print("\n The number of oranges on the shelf is: " + str(shelf.size())+ "\n")

        for i in range(totalApples):
            addApples()

        print("The number of apples on the shelf is: " + str(shelf.size()))

        while flag:
            if(shelf.size() == 0):
                print(" \n Luckily we close in 5 min because we don't have more Fruits \n")
                break
            soldApples= int(input("How many apples does the customer want to buy?: "))

            if(soldApples > shelf.size()):
                print("We only have: " + str(shelf.size()) + " Oranges")

            else:
                for i in range(soldApples):
                    deleteFruit()

            print("The number of apples on the shelf is: " + str(shelf.size()))

        print(" ---- Financial Report ---- \n")
        print("Total invested: $" + str(((totalApples * 3) + (totalOranges * 2))))
        print("Total profit: $" + str(((totalApples * 2) + (totalOranges * 2))) + "\n")
    
    else:
        print("Please, Enter a valid value")
        main()

def addOranges():
    global shelf
    orange = Orange()
    shelf.add(orange)

def addApples():
    global shelf
    apple = Apple()
    shelf.add(apple)

def deleteFruit():
    global shelf
    shelf.delete()

main()