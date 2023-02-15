# Importing tabulate module here
from tabulate import tabulate


# ========The beginning of the class==========
class Shoe:

    # Creating constructor and initialising required attributes
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Adding the code to return the cost of the shoe in this method
    def get_cost(self):
        return self.cost

    def get_country(self):
        return self.country

    def get_code(self):
        return self.code

    def get_product(self):
        return self.product

    def get_quantity(self):
        return self.quantity

    # Adding the code to set the new quantity value
    def set_quantity(self, quantity_update):
        self.quantity = quantity_update

    # Adding a code to returns a string representation of a class
    def __str__(self):
        output = f"Country: {self.country}\n"
        output += f"Shoe code is: {self.code}\n"
        output += f"Product name is :{self.product}\n"
        output += f"Cost of the shoe is: {self.cost}\n"
        output += f"Quantity of the shoe is: {self.quantity}\n"
        return output


# shoe_list stores list of shoes as string
# The shoe_obj stores list of objects of shoes.
shoe_list = []
shoe_obj = []


# ==========Functions outside the class==============

# Defining function read_shoes_data
def read_shoes_data():
    while True:
        file = None
        try:
            # Open the file inventory.txt and read the data from this file and creating object
            with open('inventory.txt', 'r') as file:
                data = file.readlines()
                for i, line in enumerate(data):
                    split_data = line.strip().split(",")

                    # Skipping the first line and append this object into the shoes list
                    if i != 0:
                        shoe_list.append(split_data)

                for i in range(len(shoe_list)):
                    shoe_1 = Shoe(shoe_list[i][0], shoe_list[i][1], shoe_list[i][2], shoe_list[i][3], shoe_list[i][4])
                    shoe_obj.append(shoe_1)
            break

        # Except block will be executed here, thereby printing the error message
        except FileNotFoundError as error:
            print(error)
            break

        # Closing the file object in the 'finally' block
        finally:
            if file is not None:
                file.close()


# Defining function capture_shoes
def capture_shoes():
    # Asking user to input all data about shoe object
    new_country = input("Enter the country name: ")
    new_code = input("Enter the product code of the shoe: ").upper()
    new_product = input("Enter the product name of the shoe: ")

    # Using defensive programming to prevent the user from entering incorrect values for the quantity and cost of a shoe
    while True:
        try:
            new_cost = int(input("Enter cost of the shoe: "))
            new_quantity = int(input("Enter the quantity of the shoe: "))
            break
        except ValueError:
            print("Oops! That was not a valid number for Cost/Quantity. Try again...")

    # Appending new shoe in shoe_obj
    new_shoe = Shoe(new_country, new_code, new_product, new_cost, new_quantity)
    shoe_obj.append(new_shoe)


    # Opening the text file and adding object to textfile
    with open('inventory.txt', 'a+') as file1:
        file1.write(f"\n{new_country},{new_code},{new_product},{new_cost},{new_quantity}")
        file1.close()



# Defining function view_all
def view_all():

    # Creating table format by using Python’s tabulate module, as a new try
    print('\33[34m')
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    table = [[shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity] for shoe in shoe_obj]
    print(tabulate(table, headers, tablefmt="outline"))
    print('\33[0m')


# Defining function re_stock
def re_stock():

    # finding the shoe object with the lowest quantity and asking user to update quantity or not
    lowest_quantity = int(min([int(shoe.quantity) for shoe in shoe_obj]))
    for i, obj in enumerate(shoe_obj):
        if lowest_quantity == int(obj.quantity):

            print(f"\33[32m{obj.country} has the lowest quantity of shoe {obj.product}: {lowest_quantity}")
            while True:
                try:
                    quantity_update = int(input("Enter the quantity you want to re-stock, if no stock needed enter 0:\33[0m"))
                    break
                except ValueError:
                    print("Oops! That was not a valid number for Cost/Quantity. Try again...")
            if quantity_update > 0:

                # Adding old stock value with the new stock value entered by user
                new_quantity = lowest_quantity + quantity_update
                shoe_obj[i].set_quantity(new_quantity)

                file2 = open("inventory.txt", "w")
                file2.write("country,code,product,cost,quantity")
                for item in shoe_obj:
                    file2.write(f"\n{item.country},{item.code},{item.product},{item.cost},{item.quantity}")
                file2.close()
                print(f"Your stock quantity has been updated!")
            elif quantity_update == 0:
                break
            else:
                print("\33[31mEntered number is not valid! Try positive number\33[0m")


# Defining function search_shoe
def search_shoe():

    # Asking user to enter shoe code to be searched and printing shoe details
    shoe_code = input("\33[31mPlease enter the shoe code: \33[0m").upper()
    for i, obj in enumerate(shoe_obj):
        if obj.code == shoe_code:
            country = obj.country
            product = obj.product
            cost = obj.cost
            quantity = obj.quantity
            print(f"\33[32mCountry: {country}\nProduct name: {product}\nShoe cost: {cost}\nIn stock: {quantity}\33[0m")
            break
    else:
        print("\33[31mInvalid shoe code\33[32m")


# Defining function value_per_item to calculate total value for each item
def value_per_item():
    for i, obj in enumerate(shoe_obj):
        value = int(obj.cost) * int(obj.quantity)

        # Printing this information on the console for all the shoes
        print(f"\33[33m---------------------------------Country: {obj.country}-------------------------------------\33[0m")
        print(f"\33[32mProduct name: {obj.product}, Shoe code: {obj.code}, Total cost: {value}\33[0m")
        print("\33[33m_________________________________________________________________________________________\33[0m")


# Defining function highest_qty to find the product with the highest quantity and printing that shoe as being for sale
def highest_qty():
    for i, obj in enumerate(shoe_obj):
        highest_quantity = int(max([int(shoe.quantity) for shoe in shoe_obj]))

        if highest_quantity == int(obj.quantity):
            print(
                f"\33[32m Country: {obj.country}, Product code '{obj.code}',  Product Name: {obj.product} is on SALE!!!!!!!\33[0m")
            break


# ==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

# Declaring colors and style to use throughout the program
CEND = '\33[0m'
CBOLD = '\33[1m'
CITALIC = '\33[3m'
CRED = '\33[31m'
CGREEN = '\33[32m'
CYELLOW = '\33[33m'
CBLUE = '\33[34m'
CGREY = '\33[90m'

# Reading function read_shoes_data once
read_shoes_data()

# presenting the menu to user and converting user input to lowercase.
while True:
    menu = input('''Select one of the following Options below: \33[1m \33[3m
                    c - Capturing shoe data
                    va - View all shoes
                    re - Re-stock shoe
                    ss - search shoe
                    tv - Total value for each item
                    sa - Item on Sale
                    e - Exit  \33[0m 
                    : ''').lower()

    # using if/elif statement calling appropriate function
    if menu == 'c':
        capture_shoes()
    elif menu == 'va':
        view_all()
    elif menu == 're':
        re_stock()
    elif menu == 'ss':
        search_shoe()
    elif menu == 'tv':
        value_per_item()
    elif menu == 'sa':
        highest_qty()
    elif menu == 'e':
        print('\33[33mGoodbye!!!\33[0m')
        exit()

    # if user typed somthing not from menu option, print below statement
    else:
        print("\33[31mYou have made a wrong choice, Please Try again!\33[0m")
