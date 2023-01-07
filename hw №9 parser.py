# Написать простой парсер для извлечения информации с любого сайта.
# Например - новость, или погоду с сайта mail.ru

import requests
from bs4 import BeautifulSoup as bs

url = 'https://pogoda.mail.ru/prognoz/moskva/'
response = requests.get(url).text
soup = bs(response, 'html.parser')

def get_weather(teg):
    weather = soup.find('div', class_=teg)
    weather = weather.text.split()
    return weather

def read_weather(data):
    my_list = []
    temp_list = []
    for i in range(len(data)):
        if i % 12 == 0 and i != 0:
            continue
        else:
            temp_list.append(data[i])
            if len(temp_list) == 11:
                my_list.append(temp_list)
                temp_list = []
    return my_list

def show_weather(data):
    for i in range(len(data)):
        print(f'День: {data[i][0]}\nТемпература днем: {data[i][1]}\nТемпература ночью: {data[i][2]}\n'
              f'Небо: {data[i][3]}\nДавление: {data[i][4]}{data[i][5]}\nВлажность: {data[i][6]}\n'
              f'Скорость ветра: {data[i][7]}{data[i][8]}\nИндекс ульрафиолета: {data[i][9]}\n'
              f'Вероятность осадков: {data[i][10]}')
        print('*' * 30)

while True:
    print('Введите команду\n1.посмотреть погоду на неделю.\n2.прогноз на завтра\n3.Завершить работу')
    command = int(input())
    if command == 1:
        data_weather = get_weather('days__wrapper')
        data_weather2 = read_weather(data_weather)
        print(read_weather(data_weather))
        show_weather(data_weather2)
    elif command == 2:
        data_weather = get_weather("day day_index")
        data_weather = read_weather(data_weather)
        show_weather(data_weather)
    elif command == 3:
        print('работа программы завершена')
        break
    else:
        print('Вы ввели неверную команду. Попробуйте еще раз!!!')