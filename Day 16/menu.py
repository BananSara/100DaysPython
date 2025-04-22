class MenuItem():
    def __init__(self, name, water, coffee, milk, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            'water': water,
            'milk': milk,
            'coffee': coffee
        }


class Menu():
    def __init__(self):
        self.menu = [
            MenuItem('latte' , water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        choices = ''
        for item in self.menu:
            choices += f'{item.name}/'
        return choices

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
