MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def coin_proccesing():
    print("Instert coins")
    quarters =  int(input("how many quarters?"))*0.25
    dimes = int(input("how many dimes?"))*0.10
    nickles = int(input("how many nickles"))*0.05
    pennies = int(input("how many pennis"))*0.01
    total = quarters + dimes + nickles + pennies
    return total

def resources_sufficient(coffee_ingredients):
    is_enough = True
    for item in coffee_ingredients:
        if coffee_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough

def transaction_successfu(money_received, drink_cost):
    if money_received > drink_cost:
        change = money_received - drink_cost
        print(f"Here is ${change} change!")
        global profit
        profit += drink_cost
        return True
    else:
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}, Enjoy!!!")

is_working = True
while is_working:
    print("espresso")
    print("cappuccino")
    print("latte")
    user_input = str(input("Please choose an item from the menu above: ")).lower()
    if user_input == "off":
        is_working = False
        print("Oh...Okay :( ")
    elif user_input == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}grams")
        print(f"Money made:{profit}")
    else:
        drink = MENU[user_input]
        if resources_sufficient(drink["ingredients"]):
            pay = coin_proccesing()
            if transaction_successfu(pay,drink['cost']):
                make_coffee(user_input, drink['ingredients'])
