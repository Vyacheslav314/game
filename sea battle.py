# 1) Сделать игру морской бой
from random import randint


def difficulty_selection():
    complexity = int(input('Выберите уровень сложности 1.легкий уровень 2.средний уровень 3.сложный уровень '))
    n = 0
    while True:
        if complexity == 1:
            n = 5
            break
        elif complexity == 2:
            n = 7
            break
        elif complexity == 3:
            n = 11
            break
        else:
            print('выбранного уровня сложности нет ')
    return n


size = difficulty_selection()


def generation_field(n):
    game_field = []
    game_field2 = []
    x_init = ' абвгдежзик'
    for i in range(0, n):
        for j in range(0, n):
            if i == 0:
                game_field2.append(x_init[j])
            elif i > 0 and j == 0:
                game_field2.append(i)
            else:
                game_field2.append('0')
        game_field.append(game_field2)
        game_field2 = []

    return game_field


player_field = generation_field(size)


def create_ships(field, size):
    if size == 5:
        count = 2
        row = randint(1, size - 1)
        col = randint(1, size - 1)
        while count > 0:
            if field[row][col] == '0':
                field[row][col] = '3'
                count -= 1
            else:
                row = randint(1, size - 1)
                col = randint(1, size - 1)
    if size == 7:
        count = 7
        row = randint(1, size - 1)
        col = randint(1, size - 1)
        while count > 0:
            if field[row][col] == '0':
                field[row][col] = '3'
                count -= 1
            else:
                row = randint(1, size - 1)
                col = randint(1, size - 1)
    if size == 11:
        count = 10
        row = randint(1, size - 1)
        col = randint(1, size - 1)
        while count > 0:
            if field[row][col] == '0':
                field[row][col] = '3'
                count -= 1
            else:
                row = randint(1, size - 1)
                col = randint(1, size - 1)


def player_turn(size1):
    coord = input('Введите координаты через пробел ').split(' ')
    x = ' абвгдежзик'
    while True:
        if len(coord) == 2 and not coord[0].isdigit() and coord[1].isdigit() and int(coord[1]) < size1:
            for i in range(1, len(x)):
                if coord[0] == x[i]:
                    coord[0] = i
            coord[1] = int(coord[1])
            break
        else:
            coord = input('Вы ввели неверные координаты попробуйте еще раз ').split(' ')
    return coord

def fill_field(field):
    for i in range(0, len(field)):
        for j in range(0, len(field[i])):
            if field[i][j] == '0':
                print('.', end='  ')
            elif field[i][j] == '2':
                print('x', end='  ')
            elif field[i][j] == '1':
                print('@', end='  ')
            elif field[i][j] == '3':
                print('.', end='  ')
            else:
                if field[i][j] == 10:
                    print(field[i][j], end=' ')
                else:
                    print(field[i][j], end='  ')
        print()


print("Начнем игру в Морской бой!")
fill_field(player_field)
create_ships(player_field, size)

if size == 5:
    turn = 10
    count = 2
elif size == 7:
    turn = 20
    count = 7
else:
    turn = 40
    count = 10
for i in range(turn):
    print("Ход: ", i)
    shot = player_turn(size)
    if count > 1:
        if player_field[shot[1]][shot[0]] == '3':
            player_field[shot[1]][shot[0]] = '1'
            count -= 1
            print(f'Поздравляю, ты потопил мой корабль! Кораблей осталось {count} ')
            fill_field(player_field)
        else:
            if player_field[shot[1]][shot[0]] == '2':
                print("Эти координаты вы уже называли.")
                fill_field(player_field)
            elif player_field[shot[1]][shot[0]] == '0':
                print("Мимо!")
                player_field[shot[1]][shot[0]] = '2'
                fill_field(player_field)
        if i == turn - 1:
            print('Игра окончена! Вы проиграли !')
    else:
        fill_field(player_field)
        print('Поздравляю ты победил!!!')
        break
