import requests

API_URL = "https://api.github.com"


def get_user_profile(username):
    url = f"{API_URL}/users/{username}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        user = response.json()
        print(f"\nПрофиль: {user.get('name') or 'Нет имени'}")
        print(f"Профиль: {user['html_url']}")
        print(f"Репозитории: {user['public_repos']}")
        print(f"Подписки: {user['following']}")
        print(f"Подписчики: {user['followers']}")
    except requests.HTTPError:
        print("Ошибка: пользователь не найден или ошибка API.")


def get_repos(username):
    url = f"{API_URL}/users/{username}/repos"
    try:
        response = requests.get(url)
        response.raise_for_status()
        repos = response.json()
        if repos:
            print(f"\nРепозитории пользователя {username}:")
            for repo in repos:
                print(f"\nНазвание: {repo['name']}")
                print(f"Ссылка: {repo['html_url']}")
                print(f"Язык: {repo['language']}")
                print(f"Видимость: {'Публичный' if not repo['private'] else 'Приватный'}")
                print(f"Ветка по умолчанию: {repo['default_branch']}")
        else:
            print("Нет репозиториев.")
    except requests.HTTPError:
        print("Ошибка при получении репозиториев.")


def search_repos(query):
    url = f"{API_URL}/search/repositories"
    params = {'q': query, 'per_page': 5}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        results = response.json()
        print(f"\nНайдено: {results['total_count']} репозиториев.")
        for repo in results['items']:
            print(f"\nНазвание: {repo['name']}")
            print(f"Полное название: {repo['full_name']}")
            print(f"Ссылка: {repo['html_url']}")
            print(f"Язык: {repo['language']}")
            print(f"Видимость: {'Публичный' if not repo['private'] else 'Приватный'}")
    except requests.HTTPError:
        print("Ошибка при поиске репозиториев.")


def main():
    while True:
        print("\nМеню:\n1. Профиль пользователя\n2. Репозитории пользователя\n3. Поиск репозиториев\n4. Выход")
        choice = input("Выберите: ")
        if choice == '1':
            username = input("Введите имя пользователя: ")
            get_user_profile(username)
        elif choice == '2':
            username = input("Введите имя пользователя: ")
            get_repos(username)
        elif choice == '3':
            query = input("Введите название репозитория: ")
            search_repos(query)
        elif choice == '4':
            break
        else:
            print("Некорректный ввод.")


if __name__ == "__main__":
    main()