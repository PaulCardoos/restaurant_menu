class Item:
    def __init__(self, itemName:str="", price:int=0, description:str="", quantity:int=1):
        self.itemName = itemName
        self.price = price
        self.description = description
        self.quantity = quantity

    #this value does not make sense for a restaurant bu
    def setQuantity(self, newQuantity):
        self.quantity = newQuantity
    
    def setName(self, newName):
        self.itemName = newName
    
    def setPrice(self, newPrice):
        self.price = newPrice
    
    def setDescription(self, newDescription):
        self.description = newDescription
    
    def printItem(self):
        print("Item Name : %s", self.itemName)
        print("\tPrice : %i", self.price)
        print("\tDescription : %s", self.description)
        print("\tQuantity : %i", self.quantity)
    
    def insertItem(self):
        # open a file to write to it for data persistence
        f = open("items.txt", "a")

        # ask the user for the food info they want to enter
        price = input(str("\nHow much would you like to charge people?\nInput price : "))
        description = input(tr())
    
     