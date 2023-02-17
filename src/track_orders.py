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
        menu = {line[1] for line in self.orders}
        requests_customer = {
            line[1] for line in self.orders if line[0] == customer
        }
        return menu.difference(requests_customer)

    def get_days_never_visited_per_customer(self, customer):
        days = {line[2].replace('\n', '') for line in self.orders}

        days_that_customer_did_not_attend = {
            line[2] for line in self.orders if line[0] == customer
        }
        return days.difference(days_that_customer_did_not_attend)

    def get_busiest_day(self):
        days = [line[2] for line in self.orders]
        count = {}
        most_frequented = days[0]

        for day in days:
            if day in count:
                count[day] += 1
            else:
                count[day] = 1

        if count[day] > count[most_frequented]:
            most_frequented = day

        return most_frequented

    def get_least_busy_day(self):
        days = [line[2] for line in self.orders]
        count = {}
        most_frequented = days[0]

        for day in days:
            if day in count:
                count[day] += 1
            else:
                count[day] = 1

        if count[day] < count[most_frequented]:
            most_frequented = day

        return most_frequented
