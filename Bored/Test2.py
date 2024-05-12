import requests

# URL веб-приложения
url = "http://www.boredapi.com/api/activity?price=0.0"
# Полезная нагрузка
payload={}
# Заголовки запроса
headers = {}
# Отправка HTTP запроса
response = requests.request("GET", url, headers=headers, data=payload)

# Вывод статуса запроса
print(response.status_code)
# Вывод json-ответа
print(response.json())