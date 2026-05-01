def delete_courier(couriers):
    print('Here are the current couriers:')
    # Print courier names and indexes.
    for i in range(len(couriers)):
        print(f'{i} {couriers[i]}') 

    # Moved outside the loop so it only asks once
    courier_to_del = int(input("Enter the index of the courier to remove: "))

    couriers.pop(courier_to_del)
    print(couriers)
    print("Courier successfully removed")