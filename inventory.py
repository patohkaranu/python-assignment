def basic_inventory_system():
    inventory = {}  # Dictionary to store items: {item_name: quantity}

    while True:
        print("\n--- Basic Inventory Menu ---")
        print("1. Add/Update Item")
        print("2. View Item")
        print("3. Total Quantity")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter item name: ")
            quantity_str = input("Enter quantity: ")
            quantity = int(quantity_str) # Convert string to integer

            if item_name in inventory:
                inventory[item_name] += quantity
                print(f"Updated {item_name}. New quantity: {inventory[item_name]}")
            else:
                inventory[item_name] = quantity
                print(f"Added {item_name} with quantity {quantity}")

        elif choice == '2':
            item_name = input("Enter item name to view: ")
            if item_name in inventory:
                print(f"Item: {item_name}, Quantity: {inventory[item_name]}")
            else:
                print(f"{item_name} not found.")

        elif choice == '3':
            total_quantity = sum(inventory.values())
            print(f"Total items in inventory: {total_quantity}")

        elif choice == '4':
            print("Exiting system.")
            break # Exit the loop

        else:
            print("Invalid choice. Please try again.")

# Run the basic inventory system
basic_inventory_system()
