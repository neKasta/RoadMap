import random

# user_name = "Kasta"  # имя
user_id = random.randint(1, 10000)  # айдишник
currency_value = random.uniform(0.1, 1)  # стоимость валюты
# number_of_purchases = random.uniform(1000000, 100000000)  # покупка колличество
before_finall_сost = number_of_purchases * currency_value


def create_order(user_name, number_of_purchases):
    comission = random.randint(1, 100000)
    finall_сost = before_finall_сost - comission

    order = {
        "name": user_name,
        "id": user_id,
        "comission": comission,
        "currency_value": currency_value,
        "number_of_purchases": number_of_purchases,
        "finall_сost": finall_сost,
    }
    return order


if __name__ == "__main__":
    order_list = []

    order_list.append(create_order("Kasta", 5000))
    order_list.append(create_order("Player2", 3000))
    order_list.append(create_order("Player3", 7000))

    for order in order_list:
        print(
            f"Заказ для {order['name']}: {order['finall_сost']} руб. (включая комиссию {order['commission']} руб.)"
        )
