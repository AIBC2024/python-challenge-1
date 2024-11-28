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
# Print menu dictionary
# First create the print_menu_items function then print it
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

# Call the print_menu_items function to print the menu

print("Welcome to the variety food truck. Here are our offerings:")
print(" ")
print_menu_items()

########################################################################
# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
# code snippet helper from Chat GPT modified heavily to learn and add my own variations
########################################################################

# Initialize the order list
order_list = []

# Helper function to find the price of an item (handling nested dictionaries)
def find_price(menu, item_name):
    for key, value in menu.items():
        if isinstance(value, dict):
            # Recursively search in nested dictionaries
            result = find_price(value, item_name)
            if result is not None:
                return result
        elif key == item_name:
            return value
    return None



#####################################################
# 2. Create a function to add items to the order list
# def add_to_order(item_name, quantity):
#####################################################

def add_to_order(item_name, quantity):
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




print(" ") ## do this to insert an empty line

"""
########################################
# Just for Ingrid's learning
# prompt to show what the customer order
########################################

def menu_selection(menu):
    print("Menu Categories:")
    categories = list(menu.keys())
    for idx, category in enumerate(categories, start=1):
        print(f"{idx}. {category}")
    
    # Prompt for category selection
    while True:
        try:
            total_categories = len(categories)
            category_choice = int(input(f"\nSelect a category by number from 1 to {total_categories}: ")) - 1
            if 0 <= category_choice < len(categories):
                selected_category = categories[category_choice]
                break
            else:
                print("Invalid choice. Please select a valid menu category number.")
        except ValueError:
            print("Invalid input. Please enter a number from provided menu categories.") ## this is for the main menu category

    # Display items in the selected category
    items = menu[selected_category]
    print(f"\nItems in {selected_category}:")
    if isinstance(items, dict):
        for idx, (item, value) in enumerate(items.items(), start=1):
            if isinstance(value, dict):
                print(f"{idx}. {item} (sub-options available)")
            else:
                print(f"{idx}. {item} - ${value:.2f}")

        # Prompt for item selection
        while True:
            try:
                total_items = len(items)
                item_choice = int(input(f"\nSelect a category item by number from 1 to {total_items}: ")) - 1
                item_names = list(items.keys())
                if 0 <= item_choice < len(item_names):
                    selected_item = item_names[item_choice]
                    sub_items = items[selected_item]
                    if isinstance(sub_items, dict):
                        print(f"\nSub-options for {selected_item}:")
                        for idx, (sub_item, price) in enumerate(sub_items.items(), start=1):
                            print(f"{idx}. {sub_item} - ${price:.2f}")
                        # Prompt for sub-option
                        while True:
                            try:
                                sub_choice = int(input("\nSelect a sub-option by number: ")) - 1
                                sub_item_names = list(sub_items.keys())
                                if 0 <= sub_choice < len(sub_item_names):
                                    final_selection = f"{selected_item} ({sub_item_names[sub_choice]})"
                                    return final_selection
                                else:
                                    print("Invalid sub-option selection. Please select a valid sub-option number.")
                            except ValueError:
                                print("Invalid input entry. Please enter a number.") ## this is for the category menu item
                    else:
                        return selected_item
                else:
                    print("Invalid choice selection. Please select a valid item number.")
            except ValueError:
                print("Invalid input entry. Please enter a number.")
    else:
        print(f"Error: {selected_category} does not contain valid items.")

# Example usage
menu_selection = menu_selection(menu)
print(f"\nYou selected: {menu_selection}")
"""



"""
    Add an item to the order list
    
    Parameters:
        item_name (str): Name of the menu item
        quantity (int): Quantity ordered
    
    # Look up the price in the menu dictionary
    price = None
    
    # Search through each category in the menu
    for category in menu:
        if item_name in menu[category]:
            # If item is found and has a direct price
            if isinstance(menu[category][item_name], (int, float)):
                price = menu[category][item_name]
                break
        else:
            # Check nested items (like Pizza, Burger, Drinks)
            for nested_item in menu[category]:
                if isinstance(menu[category][nested_item], dict):
                    if item_name in menu[category][nested_item]:
                        price = menu[category][nested_item][item_name]
                        break
    
    if price is not None:
        # Create the order dictionary
        order_item = {
            "item_name": item_name,
            "price": price,
            "quantity": quantity
        }
        # Add the order to the list
        order_list.append(order_item)
        print(f"Added {quantity} x {item_name} at ${price:.2f} each")
    else:
        print(f"Error: {item_name} not found in menu")

# Example usage:
# Add some items to the order list
add_to_order("Cookie", 2)
add_to_order("Banana", 1)

# Print the current order list
print("\nCurrent Order List:")
for item in order_list:
    print(f"Item: {item['item_name']}")
    print(f"Price: ${item['price']:.2f}")
    print(f"Quantity: {item['quantity']}")
    print(f"Subtotal: ${item['price'] * item['quantity']:.2f}")
    print("-" * 30)


# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number


            # 3. Check if the customer typed a number

                # Convert the menu selection to an integer


                # 4. Check if the menu selection is in the menu items

                    # Store the item name as a variable


                    # Ask the customer for the quantity of the menu item


                    # Check if the quantity is a number, default to 1 if not


                    # Add the item name, price, and quantity to the order list


                    # Tell the customer that their input isn't valid


                # Tell the customer they didn't select a menu option

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input

                # Keep ordering

                # Exit the keep ordering question loop

                # Complete the order

                # Since the customer decided to stop ordering, thank them for
                # their order

                # Exit the keep ordering question loop


                # Tell the customer to try again


                

"""


"""
# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order

    # 7. Store the dictionary items as variables


    # 8. Calculate the number of spaces for formatted printing


    # 9. Create space strings


    # 10. Print the item name, price, and quantity


# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
"""

def menu_selection(menu):
    print("Menu Categories:")
    categories = list(menu.keys())
    for idx, category in enumerate(categories, start=1):
        print(f"{idx}. {category}")
    
    # Prompt for category selection
    while True:
        try:
            total_categories = len(categories)
            category_choice = int(input(f"\nSelect a category by number from 1 to {total_categories}: ")) - 1
            if 0 <= category_choice < len(categories):
                selected_category = categories[category_choice]
                break
            else:
                print("Invalid choice. Please select a valid menu category number.")
        except ValueError:
            print("Invalid input. Please enter a number from the provided menu categories.")

    # Display items in the selected category
    items = menu[selected_category]
    print(f"\nItems in {selected_category}:")
    if isinstance(items, dict):
        for idx, (item, value) in enumerate(items.items(), start=1):
            if isinstance(value, dict):
                print(f"{idx}. {item} (sub-options available)")
            else:
                print(f"{idx}. {item} - ${value:.2f}")

        # Prompt for item selection
        while True:
            try:
                total_items = len(items)
                item_choice = int(input(f"\nSelect a category item by number from 1 to {total_items}: ")) - 1
                item_names = list(items.keys())
                if 0 <= item_choice < len(item_names):
                    selected_item = item_names[item_choice]
                    sub_items = items[selected_item]
                    if isinstance(sub_items, dict):
                        print(f"\nSub-options for {selected_item}:")
                        for idx, (sub_item, price) in enumerate(sub_items.items(), start=1):
                            print(f"{idx}. {sub_item} - ${price:.2f}")
                        # Prompt for sub-option
                        while True:
                            try:
                                sub_choice = int(input("\nSelect a sub-option by number: ")) - 1
                                sub_item_names = list(sub_items.keys())
                                if 0 <= sub_choice < len(sub_item_names):
                                    final_selection = f"{selected_item} ({sub_item_names[sub_choice]})"
                                    final_price = sub_items[sub_item_names[sub_choice]]
                                    break
                                else:
                                    print("Invalid sub-option selection. Please select a valid sub-option number.")
                            except ValueError:
                                print("Invalid input entry. Please enter a number.")
                        break
                    else:
                        final_selection = selected_item
                        final_price = sub_items
                        break
                else:
                    print("Invalid choice selection. Please select a valid item number.")
            except ValueError:
                print("Invalid input entry. Please enter a number.")
        # Prompt for quantity
        while True:
            try:
                quantity = input(f"\nEnter quantity for {final_selection} (default is 1): ")
                if not quantity.strip():
                    quantity = 1
                else:
                    quantity = int(quantity)
                if quantity > 0:
                    break
                else:
                    print("Quantity must be a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Append to order list
        order_list.append({
            "item_name": final_selection,
            "item_price": final_price,
            "quantity": quantity
        })
        print(f"\nAdded {quantity} x {final_selection} (${final_price:.2f} each) to the order list.")
    else:
        print(f"Error: {selected_category} does not contain valid items.")

# Continuation with match-case
while True:
    menu_selection(menu)
    while True:
        keep_ordering = input("\nWould you like to keep ordering? (y/n): ").strip().lower()
        match keep_ordering:
            case "y":
                print("\nLet's add more items!")
                break
            case "n":
                print("\nThank you for your order! This is what we are preparing for you: \n")
                print("Item name                      | Price  | Quantity  | Total Price ")
                print("-------------------------------|--------|---------- |-------------")
                total_cost = 0 # To calculate the total cost of the order
                for order in order_list:
                    item_name = order['item_name'].ljust(30)  # Left align the item name
                    price = f"${order['item_price']:.2f}".rjust(7)  # Right align the price
                    quantity = str(order['quantity']).rjust(8)  # Right align the quantity
                    total_price = order['item_price'] * order['quantity']  # Calculate total price per item
                    total_cost += total_price  # Add to total cost
                    total_price_str = f"${total_price:.2f}".rjust(11)  # Format total price
                    print(f"{item_name}| {price} | {quantity}  | {total_price_str}")
                print("--------------------------|--------|----------|-------------")
                print(f"Your total order cost: ${total_cost:.2f}\n")
                exit()
            case _:
                print("Invalid input. Please enter 'y' or 'n'.")
