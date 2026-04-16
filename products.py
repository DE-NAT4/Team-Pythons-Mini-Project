

# FUNCTION TO REPLACE THE PRODUCT SIDE NAVIGATION MENU
def display_products_navigation_menu():
    print('''
                ----  CAFFE APP  ----
                    -- Products --
          
          0: Return to main menu
          1: View Products
          2: Add a Product
          3: Update a Product
          4: Delete a Product
          ''')


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