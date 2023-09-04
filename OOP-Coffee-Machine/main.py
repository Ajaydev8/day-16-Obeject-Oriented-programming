from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
# menu_item = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = False

while is_on:
    options = menu.get_items()
    user_choice = input(f"“What would you like? {options}: ")

    if user_choice == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    elif user_choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(user_choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
