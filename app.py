from products import *
from orders import *
from couriers import *

# ================================================================================

Products = create_product_menu()
orders = create_order_menu()
couriers = load_couriers()


# ================================================================================


is_app_running = True

while is_app_running == True:
    display_header('Main Menu')
    print("0: exit app")
    print("1: Open product side")
    print("2: Open the orders side")
    print("3: Open the courier side")
    choice = int(input("Select 0, 1, 2 or 3: "))

    if choice == 0: 
        print("Exiting app") 
        is_app_running = False # This will finally fail the while loop condition


# ==================================================================================
# This is our product side of the app

    elif choice == 1: 
        display_products_navigation_menu()
        product_choice = int(input("Choose an Option: "))

        if choice == 0:
            pass

        elif product_choice == 1:
            view_products(Products)

        elif product_choice == 2:
            add_product(Products)
 
        elif product_choice == 3:
            update_product(Products)

        elif product_choice == 4:
            delete_product(Products) 


# ============================================================================
# This is the order side of the app

    elif choice == 2:
        
        print('''
                ----  CAFFE APP  ----
                     -- Orders --
              
        0: Return to main menu
        1: View orders
        2: Add order
        3: Update order status
        4: Update order info
        5: Delete order
              ''')
        choice = int(input("Choose an Option:  "))

        if choice == 0:
            pass

        elif choice == 1: 
            view_orders(orders)


        elif choice == 2:
            add_order(orders) 


        elif choice == 3:
            update_order_status(orders)


        elif choice == 4:
            update_order_details(orders)


        elif choice == 5:
            delete_order(orders)



# ============================================================================
# This is the courier side of the app


    elif choice == 3:
        
        print('''
                ----  CAFFE APP  ----
                     -- Couriers --
              
        0: Return to main menu
        1: View couriers
        2: Add a courier
        3: Update courier information
        4: Delete courier information
              ''')
        choice = int(input("Choose an Option:  "))

        if choice == 0:
            # MOHAMMED
            pass


        elif choice == 1:
            print("\nCouriers List:")
            for index, courier in enumerate(couriers):
                print(f"{index}: {courier}")


        if choice == 2:
            update_courier(couriers)

            
        if choice == 3:
            update_courier(couriers)


        if choice == 4:
            delete_courier(couriers)


# ============================================================================
# APP CLOSED - SAVE TO CSV FILES NOW

# FUNCTION TO SAVE PRODUCTS TO CSV

# FUNCTION TO SAVE ORDERS TO CSV

# FUNCTION TO SAVE COURIERS TO CSV

