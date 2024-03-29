from src.track_orders import TrackOrders


class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.new_order = TrackOrders()
        self.ingredients_manager = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def add_new_order(self, customer, order, day):
        self.new_order.add_new_order(customer, order, day)

        for ingredient in self.INGREDIENTS[order]:
            if (self.ingredients_manager[ingredient]
               < self.MINIMUM_INVENTORY[ingredient]):
                self.ingredients_manager[ingredient] += 1
            else:
                return False

    def get_quantities_to_buy(self):
        return self.ingredients_manager

    def get_available_dishes(self):
        return self.INGREDIENTS.keys()
