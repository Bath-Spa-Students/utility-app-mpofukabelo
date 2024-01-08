import time
import random

def delay_print(text, delay):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Snacks and drinks in dictionary
items_menu = {
    "Snacks": {
        'S01': {"S": "Potato Chips", 'price': 2.50, 'stock': 10},
        'S02': {"S": "Chocolate Bar", 'price': 1.50, 'stock': 8},
        'S03': {"S": "Pretzels", 'price': 2.00, 'stock': 5},
        'S04': {"S": "Trail Mix", 'price': 2.50, 'stock': 7},
        'S05': {"S": "Granola Bar", 'price': 1.75, 'stock': 12},
    },
    "Cold Drinks": {
        'C01': {"S": "Cola", 'price': 1.75, 'stock': 15},
        'C02': {"S": "Iced Tea", 'price': 1.50, 'stock': 10},
        'C03': {"S": "Orange Juice", 'price': 2.00, 'stock': 8},
        'C04': {"S": "Bottled Water", 'price': 1.00, 'stock': 20},
        'C05': {"S": "Energy Drink", 'price': 2.50, 'stock': 5},
    },
    "Hot Drinks": {
        'H01': {"S": "Coffee", 'price': 1.50, 'stock': 12},
        'H02': {"S": "Tea", 'price': 1.25, 'stock': 15},
        'H03': {"S": "Hot Chocolate", 'price': 2.00, 'stock': 8},
        'H04': {"S": "Cappuccino", 'price': 2.50, 'stock': 5},
        'H05': {"S": "Herbal Tea", 'price': 1.75, 'stock': 10},
    }
}

# Display for the vending machine
def display_menu():
    delay_print("""              𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 𝚁𝙴𝙰𝙳𝚈 𝙽 𝙶𝙾 𝚅𝙴𝙽𝙳𝙸𝙽𝙶 𝙼𝙰𝙲𝙷𝙸𝙽𝙴
                          𝚂𝙽𝙰𝙲𝙺𝚂 𝚃𝙷𝙰𝚃 𝚈𝙾𝚄 𝙽𝙴𝙴𝙳""", 0.01)
    print()
    delay_print(" * SNACKS and DRINKS AVAILABLE * ", 0.01)
    print()
    delay_print(" * Ready n Go 𝙼𝙴𝙽𝚄: * ", 0.01)
    print()

    # Print functions
    delay_print("Please Choose What Items You Want To Purchase:", 0.1)
    print()

    # ----------------------SNACKS PRINT---------------------------------
    print("\t\t------------------- Snacks -----------------------\n")
    delay_print("\t\tCode        Name           Price             Stock\n", 0.01)
    # For Loops to print the snacks items
    snacks_items = items_menu["Snacks"]
    for code, item_info in snacks_items.items():
        print(f"\t\t{code}:        {item_info['S']} \t   AED {item_info['price']}\t\t{item_info['stock']}")
    print()
    # ----------------------COLD DRINKS PRINT---------------------------------
    print("\t\t------------------- Cold Drinks ------------------\n")
    delay_print("\t\tCode        Name           Price             Stock\n", 0.01)
    # For Loops to print the Cold drinks items
    cold_drinks_items = items_menu["Cold Drinks"]
    for code, item_info in cold_drinks_items.items():
        print(f" \t\t{code}:        {item_info['S']} \t   AED {item_info['price']}\t\t{item_info['stock']}")
    print()
    # ----------------------HOT DRINKS PRINT---------------------------------
    print("\t\t------------------- Hot Drinks -------------------\n")
    delay_print("\t\tCode        Name           Price             Stock\n", 0.01)
    # For Loops to print the Hot drinks items
    hot_drinks_items = items_menu["Hot Drinks"]
    for code, item_info in hot_drinks_items.items():
        print(f"\t\t{code}:        {item_info['S']} \t   AED {item_info['price']}\t\t{item_info['stock']}")
    print()

#--------------------------------------------------------------------------

snacks_items = items_menu["Snacks"]
cold_drinks_items = items_menu["Cold Drinks"]
hot_drinks_items = items_menu["Hot Drinks"]

# Add a function for random suggestions
def suggest_item():
    category = random.choice(list(items_menu.keys()))  # Choose a random category
    item_code = random.choice(list(items_menu[category].keys()))  # Choose a random item code from the selected category
    return items_menu[category][item_code]

while True:
    user_input = input("\nPlease, enter the code of the item you want: ")  # User input
    print()
    print("Your selected item is " + user_input)
    print()

    if user_input in snacks_items:
        selected_item = snacks_items[user_input]
    elif user_input in cold_drinks_items:
        selected_item = cold_drinks_items[user_input]
    elif user_input in hot_drinks_items:
        selected_item = hot_drinks_items[user_input]
    else:
        print("No code found. Please, enter a valid code.")  # Wrong code input of the user
        print()
        continue

    if selected_item['stock'] <= 0:  # Stock management will tell the user that the item is out of stock
        print("Sorry, this item is out of stock. Please enter another code.")
        print()
        continue

    suggested_item = suggest_item()
    suggestion_response = input(delay_print(f"Do you also want {suggested_item['S']} (Category: {suggested_item['S']}, Price: AED {suggested_item['price']}) with that? yes/no ", 0.01))
    print()

    if suggestion_response.lower() == "yes":
        print("Your selected item is " + selected_item['S'] + " and suggested item is " + suggested_item['S'])
    elif suggestion_response.lower() == "no":
        print("Your selected item is " + selected_item['S'])
    else:
        print("Invalid Input")
        continue

    payment = float(input("Enter the amount of money: "))

    if payment < selected_item['price'] + suggested_item['price']:
        print("Insufficient balance. Please try again.")
        print()
        continue

    change = payment - (selected_item['price'] + suggested_item['price'])
    selected_item['stock'] -= 1  # Stock management will decrease by 1, item will dispensed, and user will get change
    suggested_item['stock'] -= 1  # Stock management will decrease by 1, item will dispensed, and user will get change
    delay_print(f"Your selected item has been dispensed: {selected_item['S']}. Your change is AED {change:.2f}", 0.01)
    print()

    additional_purchase = input("Do you want to buy additional items? (yes/no): ").lower()
    if additional_purchase != 'yes':
        break

print()
delay_print("Thank You For Choosing READY n GO, Enjoy your snacks", 0.01)
  
         
     




    
   
  
   




       

    
 
