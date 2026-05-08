from products import *
from orders import *
from couriers import *

# ================================================================================

Products = create_product_menu()
orders = []

from courier import *

# ================================================================================

Products = ["Mocha", "Americano", "Chai Latte", "Cappaccino", "Cheese Sandwich"]
orders = create_order_menu()

couriers = load_couriers()


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

            add_product(Products)

            new_product = input("Enter product name: ")
            price = float(input("Enter product price: ")) #Float because of decminal points for price. 
            Products.append(f"{new_product} - ${price}") 
            print("Product successfully added!")

        
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
            # MOHAMMED

        
        elif choice == "1":
            print("\nOrders List:")
            for index, order in enumerate(orders):
                print(f"{index}: {order}")

        # ELIF CHOICE == 1:
            # SAHOUR 
        elif choice == 1: 
            view_orders(orders)



        elif choice == 2:
            add_order(order, orders) 

        # ELIF CHOICE == 3:

        elif choice == 3:
            print("--- Current Orders ---")
            for index, item in enumerate(orders):
                print(f"Index [{index}]: {item['customer_name']} - {item['status']}")

            order_to_update = input("Enter the index of the order to update status: ")

            if order_to_update.isdigit():
                order_to_update_index = int(order_to_update)

                if 0 <= order_to_update_index < len(orders):
                    print("0: preparing")
                    print("1: out-for-delivery")
                    print("2: delivered")

                    status_choice = input("Choose new status: ")

                    if status_choice == "0":
                        orders[order_to_update_index]['status'] = "preparing"
                    elif status_choice == "1":
                        orders[order_to_update_index]['status'] = "out-for-delivery"
                    elif status_choice == "2":
                        orders[order_to_update_index]['status'] = "delivered"
                    else:
                        print("Invalid choice")

                    print("Order status updated!")
                else:
                    print("Index out of range")
            else:
                print("Please enter a number")
       

            # MOHAMMED
        elif choice == 3: 
            update_order_status(orders)

       #Edward - Edit Orders. 

        elif choice == 4:
            update_order_details(orders)


        # ELIF CHOICE == 5: Ishak
        
        elif choice == 5:
            print("Current Orders")
            for index, item in enumerate(orders): #enumerate gives a cleaner output compared to for in range
                print(f"Index [{index}], {item['customer_name']}")
            order_delete = input("Enter the index of the order you want to delete: ")
            if order_delete. isdigit():#checks to see if its even an integer
                if int(order_delete) >= 0 and int(order_delete) < len(orders):
                    orders.pop(int(order_delete))
                    print(f"{orders}")
                    print("Order successfully removed")
                else:
                    print("Invalid index entered. Please try again")
            else:
                print("Please enter a number") # make sure to push (ask for verification first)
                   

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


        elif choice == 1:
            print("\nCouriers List:")
            for index, courier in enumerate(couriers):
                print(f"{index}: {courier}")

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


        elif choice == 2:
            new_courier = input("Enter courier name: ")
            couriers.append(new_courier)
            print(f"{new_courier} added to the list.")
            
        if choice == 3:
            # PAWAN 
            print('Here are couriers:')
            for i in range(len(couriers)):
                print(f'{i} {couriers[i]}')
            select_update_list = int(input("Select the courier you would like to change: "))
            new_courier_name = input("Enter new courier name ")
            couriers[select_update_list] = new_courier_name
            print(f"{couriers}")
            print("Courier successfully updated!")

        #Edward - Delete Courier from the list. 
        if choice == 4:
            delete_courier(couriers)

