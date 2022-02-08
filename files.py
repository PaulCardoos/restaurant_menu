from item import Item

def saveFile(items):
    with open("items.txt", "w") as f:
        for item in items:
            f.write(item.itemName + "," + str(item.price) + "," + item.description + "," + str(item.quantity)+"\n")

def checkForFile():
    items = []
    
    # try except is basic error handling in python
    try:
        with open("items.txt", "r") as f:
            # read contents from file
            contents = f.readlines()
            # loop through contents and split
            for line in contents:
                # split line contents
                itemDesc = line.split(",")
                # you will now have an array describing one item
                item = Item(itemDesc[0], itemDesc[1], itemDesc[2], itemDesc[3])
                items.append(item)

        return items
    except FileNotFoundError:
        return []

