import random

random_id = random.randint(1, 1000)
random_rub_amount = random.randint(500, 8000)
random_currency_amout = random_rub_amount * random.uniform(0.1, 1)
process_status = ["В обработке", "Выполнен", "Отказано"]
random_status = random.choice(process_status)

order_data = {
    "id": random_id,
    "player_nickname": "Kasta",
    "rub_amount": random_rub_amount,
    "currency_amout": random_currency_amout,
    "status": random_status,
}

print(order_data)
