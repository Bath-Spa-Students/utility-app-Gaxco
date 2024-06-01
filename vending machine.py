import time

class VendingMachine:
    def _init_(inventory):
        # Dictionary to store items with their details
        inventory.categories = {
            'Drinks': {
                '1': {'name': 'Coke', 'price': 1.5, 'quantity': 15},
                '2': {'name': 'Pepsi', 'price': 1.5, 'quantity': 12},
                '5': {'name': 'Gatorade', 'price': 2.5, 'quantity': 8},
                '9': {'name': 'Water', 'price': 1.0, 'quantity': 25}
            },
            'Snacks': {
                '3': {'name': 'Snickers', 'price': 1.0, 'quantity': 20},
                '4': {'name': 'Pringles', 'price': 2.0, 'quantity': 10},
                '6': {'name': 'Granola Bar', 'price': 1.25, 'quantity': 15},
                '7': {'name': 'Twix', 'price': 1.0, 'quantity': 18},
                '8': {'name': 'Doritos', 'price': 1.75, 'quantity': 12},
                '10': {'name': 'Baked Lays', 'price': 1.5, 'quantity': 15}
            }
        }
        inventory.balance = 0
        inventory.sales = []
        inventory.maintenance_mode = False
        inventory.transaction_log = []

    def display_items(inventory):
        # Print the available items with their details in a table format
        print("Available items:")
        for category, items in inventory.categories.items():
            print(f"\n{category}:")
            print("{:<10} {:<15} {:<10} {:<10}".format("Item Code", "Name", "Price", "Quantity"))
            print("-" * 45)
            for code, item in items.items():
                print("{:<10} {:<15} €{:<9.2f} {:<10}".format(code, item['name'], item['price'], item['quantity']))

    def insert_money(inventory, amount):
        # Add the inserted amount to the balance
        inventory.balance += amount
        print(f"Inserted: €{amount:.2f}, Total Balance: €{inventory.balance:.2f}")

    def purchase_item(inventory, item_code):
        # Check if the item code is valid
        for category in inventory.categories.values():
            if item_code in category:
                item = category[item_code]
                # Check if the item is in stock and the balance is sufficient
                if item['quantity'] > 0 and inventory.balance >= item['price']:
                    inventory.balance -= item['price']
                    item['quantity'] -= 1
                    inventory.sales.append(item['name'])
                    inventory.transaction_log.append({'item': item['name'], 'price': item['price'], 'timestamp': time.time()})
                    print(f"You have purchased {item['name']} for €{item['price']:.2f}. Remaining Balance: €{inventory.balance:.2f}")
                elif item['quantity'] == 0:
                    print(f"Sorry, {item['name']} is out of stock.")
                else:
                    print(f"Insufficient balance to purchase {item['name']}.")
                break
        else:
            print("Invalid item code. Please try again.")

    def return_change(inventory):
        # Return the remaining balance as change
        if inventory.balance > 0:
            print(f"Returning change: €{inventory.balance:.2f}")
            inventory.balance = 0

    def enter_maintenance_mode(inventory, password):
        # Enter maintenance mode with correct password
        if password == "maintainstock":
            inventory.maintenance_mode = True
            print("Entered maintenance mode.")
        else:
            print("Incorrect password. Access denied.")

    def restock_item(inventory, item_code, quantity):
        # Restock an item in maintenance mode
        if inventory.maintenance_mode:
            for category in inventory.categories.values():
                if item_code in category:
                    category[item_code]['quantity'] += quantity
                    print(f"Restocked {quantity} units of {category[item_code]['name']}.")
                    inventory.transaction_log.append({'action': 'restock', 'item': category[item_code]['name'], 'quantity': quantity, 'timestamp': time.time()})
                    break
            else:
                print("Invalid item code.")
        else:
            print("Access denied. Maintenance mode required.")

    def exit_maintenance_mode(inventory):
        # Exit maintenance mode
        inventory.maintenance_mode = False
        print("Exited maintenance mode.")

    def generate_sales_report(inventory):
        # Generate a sales report
        print("\nSales Report:")
        print("-" * 20)
        for item in inventory.sales:
            print(item)
        print("-" * 20)
        print(f"Total Sales: €{sum(inventory.categories[cat][item]['price'] for cat in inventory.categories for item in inventory.sales):.2f}")

    def generate_transaction_log(inventory):
        # Generate a transaction log
        print("\nTransaction Log:")
        print("-" * 20)
        for transaction in inventory.transaction_log:
            if 'item' in transaction:
                print(f"Item: {transaction['item']}, Price: €{transaction['price']:.2f}, Timestamp: {time.ctime(transaction['timestamp'])}")
            elif 'action' in transaction:
                print(f"Action: {transaction['action']}, Item: {transaction['item']}, Quantity: {transaction['quantity']}, Timestamp: {time.ctime(transaction['timestamp'])}")
        print("-" * 20)

def main():
    # Create an instance of the VendingMachine class
    vending_machine = VendingMachine()
    while True:
        print("\nOptions:")
        print("1. Display Items")
        print("2. Insert Money")
        print("3. Purchase Item")
        print("4. Return Change")
        print("5. Enter Maintenance Mode")
        print("6. Restock Item")
        print("7. Exit Maintenance Mode")
        print("8. Generate Sales Report")
        print("9. Generate Transaction Log")
        print("10. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            # Display the available items
            vending_machine.display_items()
        elif choice == '2':
            # Prompt the user to insert money
            amount = float(input("Insert money: €"))
            vending_machine.insert_money(amount)
        elif choice == '3':
            # Prompt the user to enter the item code
            item_code = input("Enter the item code: ")
            vending_machine.purchase_item(item_code)
        elif choice == '4':
            # Return the remaining change
            vending_machine.return_change()
        elif choice == '5':
            # Enter maintenance mode with password
            password = input("Enter maintenance password: ")
            vending_machine.enter_maintenance_mode(password)
        elif choice == '6':
            # Restock an item
            if vending_machine.maintenance_mode:
                item_code = input("Enter item code to restock: ")
                quantity = int(input("Enter quantity to restock: "))
                vending_machine.restock_item(item_code, quantity)
            else:
                print("Access denied. Maintenance mode required.")
        elif choice == '7':
            # Exit maintenance mode
            vending_machine.exit_maintenance_mode()
        elif choice == '8':
            # Generate and display sales report
            vending_machine.generate_sales_report()
        elif choice == '9':
            # Generate and display transaction log
            vending_machine.generate_transaction_log()
        elif choice == '10':
            print("Thank you for using the vending machine!")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()