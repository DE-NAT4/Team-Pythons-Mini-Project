import csv
from display import display_header


# FUNCTION TO EXTRACT PRODUCT DATA FROM CSV
def create_product_menu():
    result = []
    with open('products.csv', mode='r', newline='') as data:
        reader = csv.reader(data)
        next(reader, None)
        for row in reader:
            result.append(row[0]) 
    return result



# FUNCTION TO REPLACE THE PRODUCT SIDE NAVIGATION MENU
def display_products_navigation_menu():
    print("TESTING NEW PRODUCTS FILE")
    display_header("PRODUCTS MENU")

    print("\n0: Return to main menu")
    print("1: View products")
    print("2: Add product")
    print("3: Update product")
    print("4: Delete product")


# FUNCTION TO REPLACE ELIF 1
def display_products(products_menu):
    lines = []
    for i in range(len(products_menu)):
        lines.append(f'{i}: {products_menu[i]}')
    
    printable_lines = '''\
''' + '\n'.join(lines) + '''
'''
    print('''
                ----  CAFFE APP  ----
                    -- Products --
          
          Products:''')
    print(printable_lines)


def add_product(Products): 
    new_product = input("Enter product name: ")
    Products.append(new_product)
    print(f" Here is the menu {Products}")
    print("Product successfully added!") 


# FUNCTION TO REPLACE ELIF 2: ADD PRODUCT
# STRETCH TASK FOR ISHAK, SAHOUR, MOHAMMED - FIRST COME FIRST SERVE
# Look at elif 2 code and more-or-less copy it over here 


# FUNCTION TO REPLACE ELIF 3
#def update_product(products_menu):
#   display_products(products_menu)
#   GET INPUT FOR WHICH PRODUCT TO CHANGE
#   GET INPUT FOR NEW PRODUCT NAME
#   ETC - Look at elif 3 for remaining steps

# FUNCTION TO REPLACE ELIF 4: DELETE A PRODUCT
# STRETCH TASK FOR ANYONE WHO HASN'T HAD A GO 