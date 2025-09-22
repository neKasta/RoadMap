import json
import random
import time


nick_name = "Kasta"  # имя
active_orders = []  # пустой списо ордеров
random_rub_amount = random.randint(500, 8000)  # Сумма заказа
player_amount = random.randint(0, 10000)  # средства пользователя


if player_amount < random_rub_amount:
    status = False
elif player_amount == random_rub_amount:
    status = True
else:
    status = True


if status == False:
    money = random_rub_amount - player_amount
else:
    money = player_amount - random_rub_amount


new_order = {"player": nick_name, "amount": random_rub_amount}  # поступивший заказ
active_orders.append(new_order)  # новый список заказа

for order in active_orders:
    player_nickname = order["player"]
    rub_amount = order["amount"]

if status == True:
    print("Начинаю обработку заказов")
    time.sleep(2)
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.4)
    print("1")
    print(f"Заказ для {player_nickname}. Сумма {rub_amount}.")

elif status == False:
    print(
        f"Заказ для - {player_nickname}, не обработан. Балланс: {player_amount}, стоимость заказа: {rub_amount}, не хватает: {money}"
    )


with open("orders.json", "w", encoding="utf-8") as file:
    json.dump(active_orders, file, ensure_ascii=False, indent=4)


print("✅ Все заказы сохранены в файл orders.json")
