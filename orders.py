def update_order_details(orders):
    print("--- Current Orders ---")
    for index, item in enumerate(orders):
        print(f"Index [{index}]: {item['customer_name']} - {item['status']}")

    order_to_update = input("Enter the index of the order to update: ")

    if order_to_update.isdigit():
        order_to_update_index = int(order_to_update)

        if order_to_update_index >= 0 and order_to_update_index < len(orders):
            selected_order = orders[order_to_update_index]

            print("\nUpdating orders. Press Enter to keep the current value.")

            new_order_name = input("New Name (" + selected_order['customer_name'] + "): ")
            if new_order_name != "":
                selected_order['customer_name'] = new_order_name

            new_phone = input("New Phone Number (" + selected_order['customer_phone_number'] + "): ")
            if new_phone != "":
                selected_order['customer_phone_number'] = new_phone
            
            new_address = input("New Address (" + selected_order['customer_address'] + "): ")
            if new_address != "":
                selected_order['customer_address'] = new_address

            new_status = input("New Status (" + selected_order['status'] + "): ")
            if new_status != "":
                selected_order['status'] = new_status

            print("Update complete!")
        else:
            print("Error: Index out of range.")
    else:
        print("Error: Please enter a number.")