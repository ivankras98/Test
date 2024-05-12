import requests

# URL веб-приложения
url = "http://www.boredapi.com/api/activity?minaccessibility=0&maxaccessibility=0.1"
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