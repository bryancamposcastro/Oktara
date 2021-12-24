from apple import Apple
from orange import Orange
from shelf import Shelf
from shelves import Shelves

totalOranges = 0
totalApples = 0
orangesAmount = 0
applesAmount = 0
orangesInShelves = 0
applesInShelves = 0
orangePrice = 0
applePrice = 0

def main():

    global totalOranges,totalApples,orangesInShelves,applesInShelves,orangePrice,applePrice,orangesAmount,applesAmount

    m = int(input("Amount of Shelves: "))
    n = int(input("Capacity for each shelf: "))

    print("--- Remember to buy merchandise before opening the store ---")
    totalOranges = int(input("How many oranges do you want to buy : "))
    orangesAmount = totalOranges
    totalApples = int(input("How many apples do you want to buy : "))
    applesAmount  = totalApples
    orangePrice = int(input("Price per Orange: $"))
    applePrice = int(input("Price per Apple: $"))

    print("--- Store Open ---")

    shelves = createShelves(n,m)
    fillShelves(shelves)

    ans = True
    while(ans):
        if(orangesInShelves > 0):
            ans=input("1. Sell an Orange:  ") 
            if ans=="1":
                if(shelves.items[0].size() > 0):
                    sellOrange(shelves.items[0]) 
                    totalFruits()
            if(shelves.items[0].size() == 0):
                deleteShelf(shelves)
        if(orangesInShelves == 0):
            ans = False
    ans = True
    while(ans):
        if(applesInShelves > 0):
            ans=input("1. Sell an Apple:  ") 
            if ans=="1":
                if(shelves.items[0].size() > 0):
                    sellApple(shelves.items[0]) 
                    totalFruits()
            if(shelves.items[0].size() == 0):
                deleteShelf(shelves)
        if(applesInShelves == 0):
            ans = False

    print("--- Financial Report ---")
    print("Money invested in oranges: $" + str(orangePrice * orangesAmount))
    print("Money invested in apples: $" + str(applePrice * applesAmount))

#Function that tells us the total number of fruits on the shelves
def totalFruits():
    global OrangesInShelves,applesInShelves
    print("Oranges on the shelves: " + str(orangesInShelves))
    print("Apples on the shelves: " + str(applesInShelves ))

#Function that removes the shelf when is empty
def deleteShelf(shelves):
    shelves.delete()

#Function that removes the orange from the shelf
def sellOrange(shelf):
    global orangesInShelves
    orangesInShelves -= 1
    shelf.delete()
#Function that removes the apple from the shelf
def sellApple(shelf):
    global applesInShelves
    applesInShelves -= 1
    shelf.delete()
            
#Function that fills the shelves with fruits
def fillShelves(shelves):
    #We fill with oranges first
    for i in range(shelves.size()):
        for j in range(shelves.items[i].size()):
            addOranges(totalOranges,shelves.items[i])

    #We fill with apples
    for i in range(shelves.size()):
        for j in range(shelves.items[i].size()):
            addApples(totalApples,shelves.items[i])
    
#Function in charge of adding an orange
def addOneOrange(shelf,position):
    global totalOranges, orangesInShelves
    orange = Orange()
    shelf.items[position] = orange
    totalOranges -= 1
    orangesInShelves += 1

#Function in charge of adding an apple
def addOneApple(shelf,position):
    global totalApples, applesInShelves
    apple = Apple()
    shelf.items[position] = apple
    totalApples -= 1
    applesInShelves += 1

#Function in charge of adding oranges to the shelf
def addOranges(amount,shelf):
    global Totaloranges
    for i in range(shelf.size()):
        if space(shelf) == True:
            orange = Orange()
            if(i < amount):
                addOneOrange(shelf,i)
        if space(shelf) == False:
            i = i + 1

#Function in charge of adding apples to the shelf
def addApples(amount,shelf):
    global totalApples
    for i in range(shelf.size()):
        if space(shelf) == True:
            if(i < amount):
                addOneApple(shelf,i)     
        if space(shelf) == False:
            i = i + 1   

# This function tells us if we have a field to add a fruit to the shelf           
def space(shelf):
    for i in range(shelf.size()):
        if shelf.items[i] == 0:
            return True
    return False

#Function in charge of creating a shelf
def createShelf(n):
    shelf = Shelf(n)
    return shelf

#Function in charge of creating shelves m with a n capacity to store fruits
def createShelves(m,n):
    shelves = Shelves(m)
    for i in range(m):
        shelf = createShelf(n)
        shelves.replace(i,shelf)
    return shelves
main()   