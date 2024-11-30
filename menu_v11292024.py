#################
# Menu dictionary
#################
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

##########################################################
# Print menu dictionary function
##########################################################
def print_menu_items():
    for category in menu:
        print(f"\n{category}:")
        for item, price in menu[category].items():
            if isinstance(price, dict):
                # Handle nested items (like Pizza, Burger, Drinks)
                print(f"  {item}:")
                for variant, variant_price in price.items():
                    print(f"    - {variant}: ${variant_price:.2f}")
            else:
                # Handle simple items
                print(f"  - {item}: ${price:.2f}")

########################################################################
# Initialize order list and helper functions
# Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
########################################################################
order_list = []

def find_price(menu, item_name):
    """Helper function to find price of an item in nested menu"""
    for key, value in menu.items():
        if isinstance(value, dict):
            # Recursively search in nested dictionaries
            result = find_price(value, item_name)
            if result is not None:
                return result
        elif key == item_name:
            return value
    return None

def add_to_order(item_name, quantity):
    """Add an item to the order list"""
    price = find_price(menu, item_name)
    if price is not None:
        order_list.append({
            "item_name": item_name,
            "item_price": price,
            "quantity": quantity
        })
        print(f"Added {quantity} x {item_name} to the order list.")
    else:
        print(f"Item '{item_name}' not found in the menu.")

########################################################################
# Launch the store and present a greeting to the customer
########################################################################

print("Welcome to the variety food truck.")

# Display full menu at start
print("\nHere's our full menu:")
print_menu_items()

#####################################################
# # Customers may want to order multiple items, 
# so let's create a continuous loop
# menu_selection is a variable for a "place order steps"
#####################################################
menu_selection = True
while menu_selection:
    # Ask the customer from which menu category they want to order
    print("\nFrom which menu would you like to order?")
    
    # Create menu number mapping
    menu_items = {i+1: category for i, category in enumerate(menu.keys())}
    
    # Display menu categories
    for num, category in menu_items.items():
        print(f"{num}: {category}")

    # Get customer's menu category choice
    menu_category = input("\nType menu number: ")
    
    if menu_category.isdigit():
        category_num = int(menu_category)
        if category_num in menu_items:
            menu_category_name = menu_items[category_num]
            print(f"\nYou selected {menu_category_name}")
            
            # Display items in selected category
            print(f"\nWhat {menu_category_name} item would you like to order?")
            print("\nItem # | Item name                | Price")
            print("-------|--------------------------|-------")
            
            # Create dictionary for available items
            available_items = {}
            i = 1
            
            # Store items and prices as variables
            for item, price in menu[menu_category_name].items():
                if type(price) is dict:
                    # Handle nested items (like Pizza variants)
                    for variant, var_price in price.items():
                        spaces = " " * (24 - len(f"{item} - {variant}"))
                        print(f"{i}      | {item} - {variant}{spaces} | ${var_price:.2f}")
                        available_items[i] = {"name": f"{item} - {variant}", "price": var_price}
                        i += 1
                else:
                    # Handle regular items
                    spaces = " " * (24 - len(item))
                    print(f"{i}      | {item}{spaces} | ${price:.2f}")
                    available_items[i] = {"name": item, "price": price}
                    i += 1
            
            # Get item selection
            item_choice = input("\nEnter item number: ")
            if item_choice.isdigit():
                choice_num = int(item_choice)
                if choice_num in available_items:
                    selected_item = available_items[choice_num]
                    
                    # Get quantity, check if it's a number, default to 1 if not
                    while True:
                        quantity = input("Enter quantity (default is 1): ").strip()
                        if not quantity:  # Empty input defaults to 1
                            quantity = 1
                            break
                        elif quantity.isdigit() and int(quantity) > 0:
                            quantity = int(quantity)
                            break
                        print("Please enter a valid positive number.")
                    
                    # Add item name, price, and quantity to the order list
                    order_list.append({
                        "item_name": selected_item["name"],
                        "item_price": selected_item["price"],
                        "quantity": quantity
                    })
                    # print the item name, price, and quantity to the order list
                    print(f"\nAdded {quantity} x {selected_item['name']} to your order.")
                else:
                    print("Invalid item number.")
            else:
                # tell the customer that their input is not valid
                print("Please enter a valid number.")
        else:
            # tell the customer they did not select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # tell the customer they did not select a number
        print("Please enter a valid number.")

    # Ask the customer if they would like to order anything else
    while True:
        keep_ordering = input("\nWould you like to keep ordering? (Y)es or (N)o: ").lower()
        if keep_ordering in ['y', 'yes']:
            break
        elif keep_ordering in ['n', 'no']:
            menu_selection = False
            print("\nThank you for stopping by!")
            break            
        print("Try again. Please enter Y or N.")

#############################
# Print final customer order
#############################
if order_list:
    print("\nThis is what we are preparing for you.\n")
    print("Item name                 | Price    | Quantity | Total")
    print("--------------------------|----------|----------|-------")
    
    total_cost = 0
    for item in order_list:
        # Calculate item total
        item_total = item["item_price"] * item["quantity"]
        total_cost += item_total
        
        # Format output with proper spacing
        name_space = " " * (24 - len(item["item_name"]))
        print(f"{item['item_name']}{name_space}  | ${item['item_price']:<7.2f} | {item['quantity']:<8} | ${item_total:.2f}")
    
    print("-" * 56)
    print(f"Total order cost: ${total_cost:.2f}")
    print("\nThank you for your payment!\n")
else:
    print("\nNo items were ordered.\n")