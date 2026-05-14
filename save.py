import csv


def save_products_to_csv(Products):
    with open("products.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "price"])

        for product in Products:
            writer.writerow([product["name"], product["price"]])


def save_orders_to_csv(orders):
    with open("orders.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["customer_name", "customer_address", "customer_phone_number", "status"])

        for order in orders:
            writer.writerow([
                order["customer_name"],
                order["customer_address"],
                order["customer_phone_number"],
                order["status"]
            ])

def save_couriers_to_csv(couriers):
    with open("couriers.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "vehicle"])

        for courier in couriers:
            writer.writerow([courier["name"], courier["vehicle"]])