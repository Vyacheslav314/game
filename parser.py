# import  requests
#
# # response = requests.get('http://mail.ru')
# # print(response.text)
#
# # https://openweathermap.org/
# city_name = 'Мытищи'
# response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&lang=ru&units=metric")
# temp = response.json()['main']
# print(temp['temp'])

import requests
from bs4 import BeautifulSoup as bs

url = 'https://ru.wikipedia.org'
response = requests.get(url).text
soup = bs(response, 'html.parser')
weather = soup.find('div', class_='mw-page-base')
print(weather.text)



