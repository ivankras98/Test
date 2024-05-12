import requests

# URL веб-приложения
url = "https://v1.basketball.api-sports.io/seasons"
# Полезная нагрузка
payload={}
# Заголовки запроса
headers = {
  'x-rapidapi-key': 'e7d0c706d1197f0aacade90e067006a0',
  'x-rapidapi-host': 'v1.basketball.api-sports.io'
}
# Отправка HTTP запроса
response = requests.request("GET", url, headers=headers, data=payload)

# Вывод статуса запроса
print(response.status_code)
# Вывод json-ответа
print(response.json())