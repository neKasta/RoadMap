import random

order_amount = int(input())
price_per_million = random.uniform(0.1, 1)
commission = random.randint(1, 10000)

currency_to_deliver = (order_amount * price_per_million) + commission

print(currency_to_deliver)
