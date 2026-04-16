
Products = ["Mocha", "Americano", "Chai Latte", "Cappaccino", "Cheese Sandwich"]
orders = []

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
    choice = int(input("Select 0, 1 or 2: "))

    if choice == 0: 
        print("Exiting app") 
        is_app_running = False # This will finally fail the while loop condition


# ==================================================================================
# This is our product side of the app

    elif choice == 1: 
        print(f"1: {Products}")
        print("2: Add Product")
        print("3: Update Product")
        print("4: Delete Product")
        product_choice = int(input("Choose an Option: "))

        if product_choice == 1:
            print(Products)

        elif product_choice == 2:
            new_product = input("Enter product name: ")
            Products.append(new_product)
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


        elif choice == 2:
            customer_name = input('Enter the customer name:  ')
            customer_address = input('Enter the customer address:  ')
            customer_phone_number = input('Enter the customer phone number:  ')

            order = {}
            order['customer_name'] = customer_name
            order['customer_address'] = customer_address
            order['customer_phone_number'] = customer_phone_number
            order['status'] = 'preparing'

            orders.append(order)

        # ELIF CHOICE == 3:
            # MOHAMMED 

       
        elif choice == 4:
            print("--- Current Orders ---")
            # Print the current orders.  
            for index, item in enumerate(orders):
                print(f"Index [{index}]: {item['customer_name']} - {item['status']}")

            # User enters number for which order to update from that list.
            order_to_update = input("Enter the index of the order to update: ")

            # Check if number is valid
            if order_to_update.isdigit():
                order_to_update_index = int(order_to_update)

                if order_to_update_index >= 0 and order_to_update_index < len(orders):
                    
                    selected_order = orders[order_to_update_index]

                    print("\nUpdating orders. Press Enter to keep the current value.")

                    # Updating order name
                    new_order_name = input("New Name (" + selected_order['customer_name'] + "): ")
                    if new_order_name != "":
                        selected_order['customer_name'] = new_order_name

                    # Updating Phone Number 
                    new_phone = input("New Phone Number (" + selected_order['customer_phone_number'] + "): ")
                    if new_phone != "":
                        selected_order['customer_phone_number'] = new_phone
                    
                    #Updating Address
                    new_address = input("New Address (" + selected_order['customer_address'] + "): ")
                    if new_address != "":
                        selected_order['customer_address'] = new_address
                    #Updating Order status
                    new_status = input("New Status (" + selected_order['status'] + "): ")
                    if new_status != "":
                        selected_order['status'] = new_status

                        
                    print("Update complete!")
                else:
                    print("Error: Index out of range.")
            else:
                print("Error: Please enter a number.")


        # ELIF CHOICE == 5:
            # ISHAK 





# LETS START FRESH ABOVE, AND LEAVE WEEK TWO'S MESS BEHIND
# ===========================================================

        # if choice == 0:
        #     is_app_running == False
        #     print("Exiting app") 
        
        # elif choice == 1:
        #     print(f'{Orders}')

        # elif choice == 2:
        #     customer_name = input("Name for order:")
        #     customer_address = input("Address for order:")
        #     customer_Phone = input("Phone Number For Order: ")
        #     order_status = "Preparing"
        #     Orders[customer_name] = [customer_Phone, customer_address, order_status]

        #     print(f"Order for {customer_name} is now {order_status}")
        #     print(Orders)
        #     # customer name = input(name)
        #     # customer address = input(address)

        #     # Orders[customer_name] = customer_name
        #     # Please build this part together if possible :)

        # elif choice == 3:
        #     print("Update Order status")
        #     list_from_dict = list(Orders.items())
            
        #     for i in range(len(list_from_dict)):
        #         name = list_from_dict[i][0]
        #         current_status = list_from_dict[i][1][3]
        #         print(f'{i} Name: {name} | Current Status: {current_status}')
             
        #     order_to_update_status= int(input("Select the order number to update: "))
        #     selected_order_to_updatestatus = list_from_dict[order_to_update_status][0]
        #     status_options = ["Pending", "Preparing", "Out for Delivery", "Delivered"]
        #     print("Available Statuses:")
        #     for i in range(len(status_options)):
        #         print(f"{i}: {status_options[i]}")

            
        #     user_select_order_status = int(input("Select the new status number: "))
        #     new_order_status = status_options[user_select_order_status]

        #     Orders[selected_order_to_updatestatus][3] = new_order_status
            
        #     print(f"Success.{selected_order_to_updatestatus}'s status updated to {new_order_status}.")