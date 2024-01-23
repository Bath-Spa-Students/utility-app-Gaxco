class VendingMachine:
    def __init__(self):
        self.items = {
            1: {'name': 'Soda', 'price': 1.50},
            2: {'name': 'Chips', 'price': 1.00},
            3: {'name': 'Chocolate', 'price': 2.00},
            4: {'name': 'Candy', 'price': 0.75},
            5: {'name': 'Water', 'price': 1.25},
            6: {'name': 'Cookies', 'price': 1.80},
            7: {'name': 'Juice', 'price': 2.50},
            8: {'name': 'Gum', 'price': 0.50},
            9: {'name': 'Energy Drink', 'price': 3.00},
            10: {'name': 'Popcorn', 'price': 2.20}
        }
        self.balance = 0.0

    def display_items(self):
        print("Vending Machine Items:")
        for code, item in self.items.items():
            print(f"{code}. {item['name']} - ${item['price']:.2f}")

    def insert_money(self, amount):
        self.balance += amount

    def select_item(self, item_code):
        if item_code in self.items:
            item = self.items[item_code]
            if self.balance >= item['price']:
                print(f"Dispensing {item['name']}...")
                self.balance -= item['price']
                print(f"Remaining balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds. Please insert more money.")
        else:
            print("Invalid item code. Please select a valid item.")

# Example Usage:
if __name__ == "__main__":
    vending_machine = VendingMachine()

    while True:
        print("\nOptions:")
        print("1. Display Items")
        print("2. Insert Money")
        print("3. Select Item")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '0':
            break
        elif choice == '1':
            vending_machine.display_items()
        elif choice == '2':
            try:
                amount = float(input("Insert money: $"))
                vending_machine.insert_money(amount)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == '3':
            try:
                item_code = int(input("Enter item number to purchase: "))
                vending_machine.select_item(item_code)
            except ValueError:
                print("Invalid input. Please enter a valid item number.")
        else:
            print("Invalid choice. Please select a valid option.")

    print("Thank you for using the vending machine!")