import csv

# FUNCTION TO EXTRACT COURIER DATA FROM CSV
def load_couriers():
    result = []
    with open ('couriers.csv', mode='r', newline='') as data:
        reader = csv.reader(data)
        next(reader, None) #skips header
        for row in reader:
            result.append(row[0])
    return result


# Function to add a new courier --- elif choice == 2:
def add_courier(couriers):
    new_courier = input("\nEnter courier name: ")
    couriers.append(new_courier)
    print(f"\n{new_courier} added to the courier list.")

# Function to update courier information --- elif choice == 3:
def update_courier(couriers):
    print("\nHere are the current couriers:")

    for index, courier in enumerate(couriers):
        print(f"{index}: {courier}")

    courier_to_update = input("\nSelect the courier you would like to change: ")

    if courier_to_update.isdigit():
        courier_to_update_index = int(courier_to_update)

        if courier_to_update_index >= 0 and courier_to_update_index < len(couriers):
            new_courier_name = input("Enter new courier name: ")
            couriers[courier_to_update_index] = new_courier_name
            print("\nCourier successfully updated!")
        else:
            print("Invalid index entered.")
    else:
        print("Please enter a number.")

