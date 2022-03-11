# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# RClabots,3.6.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
ListOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        RClabots,3.6.2022,Modified code to complete assignment 8
    """

    # Constructor
    def __init__(self, product_name, product_price):
        # Attributes
        try:
            self.__strproductname = str(product_name)
            self.__strproductprice = float(product_price)
        except Exception as e:
            print(e)

    # Properties
    # Product Name
    @property
    def product_name(self):
        return str(self.__strproductname)

    @product_name.setter
    def product_name(self, value):
        if str(product_name).isnumeric == False:
            self.__strproductname = value
        else:
            print("Name cannot be a number")

    # Product Price
    @property
    def product_price(self):
        return str(self.__strproductprice)

    @product_price.setter
    def product_price(self, value):
        if str(product_price).isnumeric:
            self.__strproductprice = value
        else:
            print("Price must be a number")

    # Methods
    def to_str(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + "," + str(self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        RClabots,3.6.2022,Modified code to complete assignment 8
    """

    # Add Code to process data to a file
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        try:
            with open(strFileName, 'w') as file_obj:
                for product in list_of_product_objects:
                    file_obj.write(product.__str__() + '\n')
                file_obj.close()
        except Exception as e:
            print("A general error has occured")
            print(e)
            print(e.__doc__)

    # Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name):

        list_of_product_rows = []
        try:
            with open(strFileName, 'r') as file_obj:
                for row in file_obj:
                    data = row.split(",")
                    line = Product(data[0], data[1])
                    list_of_product_rows.append(line)
                file_obj.close()
                return list_of_product_rows
        except Exception as e:
            print("A general error has occured")
            print(e)
            print(e.__doc__)

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Input/Output Methods:

        methods:
            output_menu_tasks():

            input_menu_choice():

            output_current_products_in_list(list_of_rows):

            input_new_product_and_price(): -> (Product Object)

        changelog: (When,Who,What)
            RRoot,1.1.2030,Created Class
            RClabots,3.6.2022,Modified code to complete assignment 8
        """

    # Add code to show menu to user
    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show Current Products
        2) Add a new Product
        3) Save Data to File and Exit Program        
        ''')
        print()  # Add an extra line for looks

    # Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice_str = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice_str

    # Add code to show the current data from the file to user
    @staticmethod
    def output_current_products_in_list(list_of_rows):
        """ Shows the current Products in the list of rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Products are: *******")
        for row in list_of_rows:
            print(row.product_name + " (" + str(row.product_price) + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    # Add code to get product data from user
    @staticmethod
    def input_new_product_and_price():
        """  Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        try:
            name = input("Enter a product: ")
            price = input("What is the price of this product?: ")
            objP1 = Product(product_name=name, product_price=price)
        except Exception as e:
            print(e)
        return objP1

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
try:
    # Load data from file into a list of product objects when script starts
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

    while (True):
        # Show user a menu of options
        IO.output_menu_tasks()

        # Get user's menu option choice
        choice_str = IO.input_menu_choice()

        # Show user current data in the list of product objects
        if choice_str.strip() == '1':
            IO.output_current_products_in_list(ListOfProductObjects)

        # Let user add data to the list of product objects
        if choice_str.strip() == '2':
            ListOfProductObjects.append(IO.input_new_product_and_price())

        # let user save current data to file and exit program
        if choice_str.strip() == '3':
            FileProcessor.save_data_to_file(strFileName, ListOfProductObjects)
            print("Goodbye!")
            break
except Exception as e:
    print(e, e.__doc__, type(e))

# Main Body of Script  ---------------------------------------------------- #
