from menu import Menu
from money_machiine import MoneyMachine
from coffee_maker import CoffeeMaker

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


machine_is_on = True

while machine_is_on:
    options = menu.get_items()
    choice = input(f"What would you like to have ? ({options}) ? ").lower()

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        machine_is_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
