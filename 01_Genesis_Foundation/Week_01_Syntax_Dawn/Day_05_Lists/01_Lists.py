import random

nick_name = "Kasta"
active_orders = []
random_rub_amount = random.randint(500, 8000)
new_order = {"player": nick_name, "amount": random_rub_amount}

active_orders.append(new_order)

print(active_orders)
