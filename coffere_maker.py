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


