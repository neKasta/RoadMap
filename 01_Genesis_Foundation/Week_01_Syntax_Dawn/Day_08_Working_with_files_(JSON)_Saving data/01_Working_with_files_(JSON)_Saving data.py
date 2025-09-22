import json

new_order = '{"name":"Kasta", "age":16, "city":"Saint Petersburg"}'
json_to_python = json.loads(new_order)
print("Из json в python", json_to_python["name"])


old_order = {"name": "Kasta", "age": 16, "city": "Saint Petersburg"}

python_to_json = json.dumps(old_order)
print("Из python в json", python_to_json)
