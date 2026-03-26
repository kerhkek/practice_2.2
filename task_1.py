import requests


urls = [
    "https://github.com/",
    "https://www.binance.com/en",
    "https://tomtit.tomsk.ru/",
    "https://jsonplaceholder.typicode.com/",
    "https://moodle.tomtit-tomsk.ru/"
]

def get_status(url):
    try:
        response = requests.get(url, timeout=10)
        code = response.status_code

        if code == 200:
            availability = 'доступен'
        elif code == 403:
            availability = 'вход запрещен'
        elif code == 404:
            availability = 'не найден'
        elif code == 500:
            availability = 'не доступен'
        else:
            availability = 'не доступен'
        print(f"{url} – {availability} – {code}")

    except requests.exceptions.ConnectionError:
        print(f"{url} – не доступен – N/A")
    except requests.exceptions.Timeout:
        print(f"{url} – не доступен – N/A")
    except requests.exceptions.TooManyRedirects:
        print(f"{url} – не доступен – N/A")

for url in urls:
    get_status(url)