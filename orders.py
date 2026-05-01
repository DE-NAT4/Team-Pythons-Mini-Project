import csv

def create_order_menu():
    orders_list = []
    try:
        with open('orders.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                orders_list.append(dict(row))
                print(orders_list)
        return orders_list
    except FileNotFoundError:
        return []

def save_orders_to_csv(orders_list):
    with open('orders.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['customer_name', 'customer_address', 'customer_phone_number', 'status'])
        writer.writeheader()
        writer.writerows(orders_list) 


def update_order_details(orders):
    print("--- Current Orders ---")
    for index, item in enumerate(orders):
        print(f"Index [{index}]: {item['customer_name']} - {item['status']}")

    order_to_update = input("Enter the index of the order to update: ")

    if order_to_update.isdigit():
        order_to_update_index = int(order_to_update)

        if order_to_update_index >= 0 and order_to_update_index < len(orders):
            selected_order = orders[order_to_update_index]

            print("Updating orders. Press Enter to keep the current value.")

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