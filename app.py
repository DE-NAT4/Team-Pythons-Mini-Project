from products import *
from orders import *
from courier import *

# ================================================================================

Products = create_product_menu()
orders = create_order_menu()
couriers = load_couriers()

create_product_menu()
load_couriers()
# ================================================================================

order = {
    'customer_name': 'Alice Holmes',
    'customer_address': '22b Baker Street',
    'customer_phone_number': '07426 781978',
    'status': 'preparing',
}
orders.append(order)

order = {
    'customer_name': 'Bob Holmes',
    'customer_address': '22b Baker Street',
    'customer_phone_number': '07426 781978',
    'status': 'preparing',
}
orders.append(order)

# ================================================================================


#print("0: exit app")
#print("1: Products")
is_app_running = True

while is_app_running == True:
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
            display_products(Products)

        elif product_choice == 2:
            new_product = input("Enter product name: ")
            price = float(input("Enter product price: ")) #Float because of decminal points for price. 
            Products.append(f"{new_product} - ${price}") 
            with open('products.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([new_product, price])
            print(f" Here is the menu {Products}")
            print("Product successfully added!")
        

        elif product_choice == 3:
            print('Here are the menu items:')
            for i in range(len(Products)):
                print(f'{i} {Products[i]}')
            
            select_update_list = int(input("Select the product you would like to change: "))
            new_product_name = input("Enter new product name ")
            Products[select_update_list] = new_product_name
            print(f"{Products}")
            print("Product successfully updated!")

        elif product_choice == 4:
            print('Here are the menu items:')
            for i in range(len(Products)):
                print(f'{i} {Products[i]}')

            select_delete_product = int(input("Select the product you would like to remove: "))
            Products.pop(select_delete_product)
            print(f"{Products}")
            print("Product successfully removed")


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
            # MOHAMMED
        
        # ELIF CHOICE == 1:
            # SAHOUR 
        elif choice == 1: 
            view_orders(orders)


        elif choice == 2:
            add_order(order, orders) 

        # ELIF CHOICE == 3:
            # MOHAMMED
        elif choice == 3: 
            update_order_status(orders)

       #Edward - Edit Orders. 
        elif choice == 4:
            update_order_details(orders)

        # ELIF CHOICE == 5:
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

        if choice == 1:
            # SAHOUR
            pass

        if choice == 2:
            new_courier = input("Enter courier name: ")
            courier_Veichle = input("Enter veichle type: ")
            
            new_entry = {"Courier Name": new_courier, "Courier vehicle": courier_Veichle}

            couriers.append(new_entry)
             
            with open('courier.csv', 'a', newline='') as file:
                fieldnames = ["Courier Name", "Courier vehicle"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow(new_entry)
            
            print(f"{new_courier} added to the list.")

        if choice == 3:
            # PAWAN 
            pass

        #Edward - Delete Courier from the list. 
        if choice == 4:
            delete_courier(couriers)

