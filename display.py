# Header fucntion
def display_header(section_name):
    print("\n" + "=" * 60)
    print(f"{'CAFE PYTHONS':^60}")
    print(f"{section_name:^60}")
    print("=" * 60)

def display_main_menu():
    display_header("Main Menu")
    print("\n0: Exit app")
    print("1: Open product side")
    print("2: Open orders side")
    print("3: Open courier side")

# DISPLAY_PRODUCT_NAVIGATION_MENU TO BE MOVED HERE
def display_product_navigation_menu():
    display_header("Products")
    print("\n0: Return to main menu")
    print("1: View products")
    print("2: Add product")
    print("3: Update product")
    print("4: Delete product")

# CREATE FUNCTION FOR DISPLAY_ORDER_MENU
def display_order_menu():
    display_header("Orders")
    print("\n0: Return to main menu")
    print("1: View orders")
    print("2: Add order")
    print("3: Update order status")
    print("4: Update order info")
    print("5: Delete order")

# CREATE FUNCTION FOR DISPLAY_COURIER_MENU
def display_courier_menu():
    display_header("Couriers")
    print("\n0: Return to main menu")
    print("1: View couriers")
    print("2: Add a courier")
    print("3: Update courier information")
    print("4: Delete courier information")

