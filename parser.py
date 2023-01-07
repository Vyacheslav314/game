# import  requests
#
# # response = requests.get('http://mail.ru')
# # print(response.text)
#
# # https://openweathermap.org/
# # 901d71a26b8430f61eb61e74f7810100
# API_key = '4321a3d417b53045aa1b6617c529c910'
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



