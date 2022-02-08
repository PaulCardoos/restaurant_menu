# print menu
# accept user input
# 
from item import Item
from files import checkForFile
from files import saveFile

def deleteItems(items, deleteItem:str):
    obj = filter(lambda x : x.itemName != deleteItem, items)
    return list(obj)

def insertNewItem(item:Item):
    name = input(str("\nWhat is foood item name?\nEnter name : "))
    price = int(input(str("\nHow much would you like to charge?\nEnter price : ")))
    description = input(str("\nType a short description of the food\nEnter Description : "))
    quantity = int(input(str("\nHow many do you have available?\nEnter Quantity : " )))

    # set receieved data in obj
    item.setName(name)
    item.setQuantity(quantity)
    item.setPrice(price)
    item.setDescription(description)

    return item

def main():
    # check for existing items from File
    items = checkForFile()
    
    # continuing looping until user quits
    while True:
        printMenu()
        choice = input(str("\nWhat would you like to do?\nEnter Choice: "))
        if choice == "1":
            item = Item()
            insertNewItem(item)
            items.append(item)
            saveFile(items)
        if choice == "2":
            deleteItem = input(str("\nWhat is the name of the item you want to delete?\nEnter Item name : "))
            items = deleteItems(items, deleteItem)
            saveFile(items)
        if choice == "3":
            continue
        if choice == "4":
            print("Thank you for shopping at To Dine For")
            quit()


def printMenu():
    print("1. insert an item\n2. delete an item\n3. shop\n4. quit")


main()
