# Написать программу, где создадим класс Soup (для определения типа супа), принимающий
# 1 аргумент - который отвечает за основной продукт к выбираемому супу.
# В этом классе создать метод show_my_soup(), выводящий на печать «Суп - {Основной продукт}» в случае наличия добавки
# Это как доп к этой задаче - иначе отобразится следующая фраза: «Обычный кипяток»


class Soup:
    def __init__(self):
        self.ingredient = False

    def main_ingredient(self):
        self.ingredient = True

    def show_my_soup(self, temp):
        if self.ingredient:
            print(f'Суп - {temp}')
        else:
            print('Кипяток')

my_soup = Soup()
my_soup.ingredient = input('Введите ингридиент: ')
my_soup.show_my_soup(my_soup.ingredient)