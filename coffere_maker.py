menu = {
    "latte": {
        "ingredients": {
            "water": 500,
            "milk": 200,
            "coffee": 24,
        },
        "cost": 150
    },
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 100
    },
    "cappuccino": {
        "ingredients": {
            "water": 500,
            "milk": 200,
            "coffee": 24,
        },
        "cost": 200
    },
}

profit = 0
resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
}

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_notes():
    try:
        print("Please insert notes.")
        note_ten = int(input("How many R10 notes?: "))
        note_twenty = int(input("How many R20 notes?: "))
        note_fifty = int(input("How many R50 notes?: "))
        return note_ten * 10 + note_twenty * 20 + note_fifty * 50
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return 0

def is_payment_successful(money_received, coffee_cost):
    if money_received >= coffee_cost:
        global profit
        profit += coffee_cost
        change = money_received - coffee_cost
        print(f"Here is your R{change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(coffee_name, coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here is your {coffee_name} ☕. Enjoy!")

is_on = True
while is_on:
    choice = input("What would you like to have? (latte/espresso/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: R{profit}")
    elif choice in menu:
        coffee_type = menu[choice]
        if check_resources(coffee_type["ingredients"]):
            payment = process_notes()
            if is_payment_successful(payment, coffee_type["cost"]):
                make_coffee(choice, coffee_type['ingredients'])
    else:
        print("Invalid option. Please choose latte, espresso, or cappuccino.")
