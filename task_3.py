import requests
import json
import os

SAVE_FILE = "save.json"
API_URL = "https://www.cbr-xml-daily.ru/daily_json.js"

def fetch_rates():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Ошибка сети: {e}")
        return None

def load_groups():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_groups(groups):
    with open(SAVE_FILE, 'w', encoding='utf-8') as f:
        json.dump(groups, f, ensure_ascii=False, indent=4)

def show_all_currencies(data):
    for c in data['Valute'].values():
        print(f"{c['CharCode']}: {c['Name']} - {c['Value']} руб.")

def find_currency(data, code):
    return data['Valute'].get(code.upper())

def main():
    groups = load_groups()
    while True:
        data = fetch_rates()
        if not data:
            break
        print("\n1. Просмотреть все валюты")
        print("2. Посмотреть валюту по коду")
        print("3. Создать группу")
        print("4. Добавить валюту в группу")
        print("5. Удалить валюту из группы")
        print("6. Просмотреть группы")
        print("7. Выйти")
        choice = input("Выберите: ")

        if choice == '1':
            show_all_currencies(data)
        elif choice == '2':
            code = input("Введите код валюты: ")
            c = find_currency(data, code)
            if c:
                print(f"{c['CharCode']}: {c['Name']} - {c['Value']} руб.")
            else:
                print("Валюта не найдена.")
        elif choice == '3':
            name = input("Введите название группы: ")
            if name in groups:
                print("Такая группа уже есть.")
            else:
                groups[name] = []
                save_groups(groups)
        elif choice == '4':
            group_name = input("Группа: ")
            if group_name not in groups:
                print("Группа не найдена.")
                continue
            code = input("Код валюты: ").upper()
            if code in data['Valute']:
                if code not in groups[group_name]:
                    groups[group_name].append(code)
                    save_groups(groups)
                else:
                    print("Валюта уже в группе.")
            else:
                print("Валюта не найдена.")
        elif choice == '5':
            group_name = input("Группа: ")
            if group_name not in groups:
                print("Группа не найдена.")
                continue
            code = input("Код валюты: ").upper()
            if code in groups[group_name]:
                groups[group_name].remove(code)
                save_groups(groups)
            else:
                print("Валюта не в группе.")
        elif choice == '6':
            for g_name, codes in groups.items():
                print(f"\nГруппа: {g_name}")
                for c in codes:
                    val = data['Valute'].get(c)
                    if val:
                        print(f"{c}: {val['Name']} - {val['Value']} руб.")
                    else:
                        print(f"{c}: Не найдено.")
        elif choice == '7':
            break
        else:
            print("Некорректный ввод.")

if __name__ == "__main__":
    main()