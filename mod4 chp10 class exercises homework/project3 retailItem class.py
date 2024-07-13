## Author: Francisco Bumanglag
## Project: Retail Item Class
## Assignment: Module 4 Project 5
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: July 10, 2023


class RetailItem:
    def __init__(self, description, units_in_inventory, price):
        self.description = description
        self.units_in_inventory = units_in_inventory
        self.price = price

def main():
    #create three RetailItem objects with the given data
    item1 = RetailItem("Jacket", 12, 59.95)
    item2 = RetailItem("Designer Jeans", 40, 34.95)
    item3 = RetailItem("Shirt", 20, 24.95)

    #display the data for each item
    print("Retail Item Information:")
    print("Item #1:")
    print("Description:", item1.description)
    print("Units in Inventory:", item1.units_in_inventory)
    print("Price:", item1.price)
    print()
    print("Item #2:")
    print("Description:", item2.description)
    print("Units in Inventory:", item2.units_in_inventory)
    print("Price:", item2.price)
    print()
    print("Item #3:")
    print("Description:", item3.description)
    print("Units in Inventory:", item3.units_in_inventory)
    print("Price:", item3.price)

#run the main function
main()


