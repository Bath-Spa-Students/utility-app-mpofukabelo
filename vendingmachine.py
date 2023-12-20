class VendingMachine:
    def __init__(self):
        self.menu = {
            'A1': {'item': 'Soda', 'price': 3.50},
            'A2': {'item': 'Chips', 'price': 5.00},
            'B1': {'item': 'Water', 'price': 1.25},
            'B2': {'item': 'Chocolate', 'price': 16.75}
        }
        self.money_inserted = 0.0
        self.change = 0.0
        self.user_selection = None
        self.stock = {'A1': 5, 'A2': 5, 'B1': 5, 'B2': 5}

    def display_menu(self):
        print("===== VENDING MACHINE MENU =====")
        for code, item_info in self.menu.items():
            print(f"{code}: {item_info['item']} - ${item_info['price']:.2f}")

    def accept_money(self):
        while True:
            try:
                money = float(input("Insert money (press 0 when finished): $"))
                if money == 0:
                    break
                self.money_inserted += money
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

    def select_item(self):
        self.user_selection = input("Enter the code of the item you want to purchase: ")

    def dispense_item(self):
        if self.user_selection in self.menu:
            if self.stock[self.user_selection] > 0 and self.money_inserted >= self.menu[self.user_selection]['price']:
                self.stock[self.user_selection] -= 1
                self.change = self.money_inserted - self.menu[self.user_selection]['price']
                print(f"Dispensing {self.menu[self.user_selection]['item']}...")
                print(f"Change: ${self.change:.2f}")
            elif self.stock[self.user_selection] == 0:
                print("Sorry, this item is out of stock.")
            else:
                print("Insufficient funds. Please insert more money.")
        else:
            print("Invalid code. Please enter a valid code.")

    def run_vending_machine(self):
        self.display_menu()
        self.accept_money()
        self.select_item()
        self.dispense_item()


# Example usage
if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run_vending_machine()
