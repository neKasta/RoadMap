import json

try:
    with open("orders.json", "r", encoding="utf-8") as file:
        loaded_orders = json.load(file)

    print(f"✅ Файл загружен. Тип данных: {type(loaded_orders)}")
    print(f"📊 Количество заказов в файле: {len(loaded_orders)}")

    print("\n📋 Список всех заказов:")
    for index, order in enumerate(loaded_orders, 1):
        print(f"{index}. Игрок: {order['player']}, Сумма: {order['amount']} руб.")

except FileNotFoundError:
    print(
        "❌ Файл orders.json не найден. Сначала запустите программу для создания заказов."
    )
except json.JSONDecodeError:
    print("❌ Ошибка чтения JSON. Файл поврежден или имеет неверный формат.")
