#create vending machine using python
print("""

░█──░█ ░█▀▀▀ ░█─── ░█▀▀█ ░█▀▀▀█ ░█▀▄▀█ ░█▀▀▀ 　 ▀▀█▀▀ ░█▀▀▀█ 　 ░█▀▄▀█ ░█──░█ 　 ░█──░█ ░█▀▀▀ ░█▄─░█ ░█▀▀▄ ▀█▀ ░█▄─░█ ░█▀▀█ 
░█░█░█ ░█▀▀▀ ░█─── ░█─── ░█──░█ ░█░█░█ ░█▀▀▀ 　 ─░█── ░█──░█ 　 ░█░█░█ ░█▄▄▄█ 　 ─░█░█─ ░█▀▀▀ ░█░█░█ ░█─░█ ░█─ ░█░█░█ ░█─▄▄ 
░█▄▀▄█ ░█▄▄▄ ░█▄▄█ ░█▄▄█ ░█▄▄▄█ ░█──░█ ░█▄▄▄ 　 ─░█── ░█▄▄▄█ 　 ░█──░█ ──░█── 　 ──▀▄▀─ ░█▄▄▄ ░█──▀█ ░█▄▄▀ ▄█▄ ░█──▀█ ░█▄▄█ 

░█▀▄▀█ ─█▀▀█ ░█▀▀█ ░█─░█ ▀█▀ ░█▄─░█ ░█▀▀▀ 
░█░█░█ ░█▄▄█ ░█─── ░█▀▀█ ░█─ ░█░█░█ ░█▀▀▀ 
░█──░█ ░█─░█ ░█▄▄█ ░█─░█ ▄█▄ ░█──▀█ ░█▄▄▄""")
print("__________________________________________________________________________________________________________________")

# Define the VendingMachine class
class VendingMachine:
    def __init__(self):
        # Dictionary to store items with their details
        self.items = {'1': {'name': 'Coke', 'price': 1.5, 'quantity': 15},
                      '2': {'name': 'Pepsi', 'price': 1.5, 'quantity': 12},
                      '3': {'name': 'Snickers', 'price': 1.0, 'quantity': 20},
                      '4': {'name': 'Pringles', 'price': 2.0, 'quantity': 10},
                      '5': {'name': 'Gatorade', 'price': 2.5, 'quantity': 8},
                      '6': {'name': 'Granola Bar', 'price': 1.25, 'quantity': 15},
                      '7': {'name': 'Twix', 'price': 1.0, 'quantity': 18},
                      '8': {'name': 'Doritos', 'price': 1.75, 'quantity': 12},
                      '9': {'name': 'Water', 'price': 1.0, 'quantity': 25},
                      '10':{'name': 'Baked Lays', 'price': 1.5, 'quantity': 15}}
        self.balance = 0

    def display_items(self):
        # Print the available items with their details in a table format
        print("Available items:")
        print("{:<10} {:<15} {:<10} {:<10}".format("Item Code", "Name", "Price", "Quantity"))
        print("-" * 45)
        for code, item in self.items.items():
            print("{:<10} {:<15} €{:<9.2f} {:<10}".format(code, item['name'], item['price'], item['quantity']))

    def insert_money(self, amount):
        # Add the inserted amount to the balance
        self.balance += amount
        print(f"Inserted: €{amount:.2f}, Total Balance: €{self.balance:.2f}")

    def purchase_item(self, item_code):
        # Check if the item code is valid
        if item_code in self.items:
            item = self.items[item_code]
            # Check if the item is in stock and the balance is sufficient
            if item['quantity'] > 0 and self.balance >= item['price']:
                self.balance -= item['price']
                item['quantity'] -= 1
                print(f"You have purchased {item['name']} for €{item['price']:.2f}. Remaining Balance: €{self.balance:.2f}")
            elif item['quantity'] == 0:
                print(f"Sorry, {item['name']} is out of stock.")
            else:
                print(f"Insufficient balance to purchase {item['name']}.")
        else:
            print("Invalid item code. Please try again.")

    def return_change(self):
        # Return the remaining balance as change
        if self.balance > 0:
            print(f"Returning change: €{self.balance:.2f}")
            self.balance = 0

def main():
    # Create an instance of the VendingMachine class
    vending_machine = VendingMachine()
    while True:
        print("\nOptions:")
        print("1. Display Items")
        print("2. Insert Money")
        print("3. Purchase Item")
        print("4. Return Change")
        print("5. Exit")
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
            print("Thank you for using the vending machine!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()