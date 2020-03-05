def display_inventory(inventory): #Function that prints out inventory.
    print("Inventory:")
    itemCount = 0

    for key, value in inventory.items(): #Loops through dictionary adding total amount of items and displaying each item.
        print(str(value)+ ' ' + key)
        itemCount += value

    print("Total number of items: " + str(itemCount))


def add_to_inventory(inventory, newItems): #Function that adds items from a list to an inventory.
    for item in newItems:
        if (item in inventory):
            inventory[item] += 1
        else:
            inventory[item] = 1
