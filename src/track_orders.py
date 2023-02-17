class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        f_dish = [line[1] for line in self.orders if line[0] == customer]
        count = {}
        most_requested = f_dish[0]

        for dish in f_dish:
            if dish in count:
                count[dish] += 1
            else:
                count[dish] = 1

        if count[dish] > count[most_requested]:
            most_requested = dish

        return most_requested

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
