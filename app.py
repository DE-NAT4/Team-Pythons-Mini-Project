
Products = ["Mocha", "Americano", "Chai Latte", "Cappaccino", "Cheese Sandwich"]
Orders = {
    'Alice': ['address', 'phone number',"Customer Adress" , "Order Status"],
    'Bob': ['address', 'phone number', "Customer Adress" ,"Order Status"],
}

#print("0: exit app")
#print("1: Products")
is_app_running = True

while is_app_running == True:
    Products = ["Mocha", "Americano", "Chai Latte", "Cappaccino", "Cheese Sandwich"]
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
        
        print(f'{Orders}')
        print('What would you like to do?')
        print("0. Close app")
        print("1. Print order list")
        print("2. Add an order")
        print("3. Update Order status")
       

        choice = int(input("Please select a number: "))

        if choice == 0:
            is_app_running == False
            print("Exiting app") 
        
        elif choice == 1:
            print(f'{Orders}')

        elif choice == 2:
            customer_name = input("Name for order:")
            customer_address = input("Address for order:")
            customer_Phone = input("Phone Number For Order: ")
            order_status = "Preparing"
            Orders[customer_name] = [customer_Phone, customer_address, order_status]

            print(f"Order for {customer_name} is now {order_status}")
            print(Orders)
            # customer name = input(name)
            # customer address = input(address)

            # Orders[customer_name] = customer_name
            # Please build this part together if possible :)

        elif choice == 3:
            print("Update Order status")
            list_from_dict = list(Orders.items())
            
            for i in range(len(list_from_dict)):
                name = list_from_dict[i][0]
                current_status = list_from_dict[i][1][3]
                print(f'{i} Name: {name} | Current Status: {current_status}')
             
            order_to_update_status= int(input("Select the order number to update: "))
            selected_order_to_updatestatus = list_from_dict[order_to_update_status][0]
            status_options = ["Pending", "Preparing", "Out for Delivery", "Delivered"]
            print("Available Statuses:")
            for i in range(len(status_options)):
                print(f"{i}: {status_options[i]}")

            
            user_select_order_status = int(input("Select the new status number: "))
            new_order_status = status_options[user_select_order_status]

            Orders[selected_order_to_updatestatus][3] = new_order_status
            
            print(f"Success.{selected_order_to_updatestatus}'s status updated to {new_order_status}.")