import requests
import json

URL = "https://www.cbr-xml-daily.ru/daily_json.js"
FILE = "save.json"

def get_values():
    resp = requests.get(URL)
    return resp.json()['Valute']

def all_values():
    value = get_values()
    for code, v in value.items():
        print(f"{code}: {v['Name']} - {v['Value']} руб.")

def one_value():
    code = input("Код валюты: ").upper()
    value = get_values()
    v = value.get(code)
    if v:
        print(f"{v['Name']} ({code}): {v['Value']} руб.")
    else:
        print("Нет такой валюты.")

def load_groups():
    try:
        with open(FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_groups(groups):
    with open(FILE, 'w') as f:
        json.dump(groups, f)

def create_groups():
    groups = load_groups()
    name = input("Имя группы: ")
    codes = input("Коды через запятую: ").upper().split(',')
    groups[name] = [i.strip() for i in codes]
    save_groups(groups)
    print("Группа сохранена.")

def all_groups():
    groups = load_groups()
    for name, codes in groups.items():
        print(f"{name}: {codes}")

def edit_group():
    groups = load_groups()
    name = input("Имя группы: ")
    if name not in groups:
        print("Нет такой группы.")
        return
    action = input("Добавить или убрать: ").lower()
    code = input("Код валюты: ").upper()
    if action == 'add':
        groups[name].append(code)
    elif action == 'remove':
        if code in groups[name]:
            groups[name].remove(code)
        else:
            print("Код не найден в группе.")
    save_groups(groups)
    print("Обновлено.")


while True:
    print("\n1. Все валюты")
    print("2. Одна валюта")
    print("3. Создать группу")
    print("4. Все группы")
    print("5. Редактировать группу")
    print("0. Выход")
    choice = input("Выбор: ")

    if choice == '1':
        all_values()
    elif choice == '2':
        one_value()
    elif choice == '3':
        create_groups()
    elif choice == '4':
        all_groups()
    elif choice == '5':
        edit_group()
    elif choice == '0':
        break
