from random import randint

size = 3


def generation_field(n):
    game_field = []
    game_field2 = []
    for i in range(0, n):
        for j in range(0, n):
            game_field2.append(0)
        game_field.append(game_field2)
        game_field2 = []

    return game_field


game_field = generation_field(size)


def fill_field(field):
    for i in range(0, len(field)):
        for j in range(0, len(field[i])):
            if field[i][j] == 0:
                print('.', end='  ')
            elif field[i][j] == 1:
                print('x', end='  ')
            else:
                print('0', end='  ')
        print()


fill_field(game_field)


def turn_man(field):
    print('Ходят х ')
    line_selection = int(
        input('Введите номер строки. номер строки начинается с 1 и заканчивается 3  '))
    column_selection = int(
        input('Введите номер столбца. номер столбца начинается с 1 и заканчивается 3  '))
    while True:
        if field[line_selection - 1][column_selection - 1] != 1 and field[line_selection - 1][column_selection - 1] != 2:
            field[line_selection - 1][column_selection - 1] = 1
            break
        else:
            print('выбранные координаты не доступны ')
            line_selection = int(
                input('Введите номер строки. номер строки начинается с 1 и заканчивается 3  '))
            column_selection = int(
                input('Введите номер столбца. номер столбца начинается с 1 и заканчивается 3  '))


def turn_bot(field):
    print('Ходят 0 ')
    line_selection = int(
        input('Введите номер строки. номер строки начинается с 1 и заканчивается 3  '))
    column_selection = int(
        input('Введите номер столбца. номер столбца начинается с 1 и заканчивается 3  '))
    while True:
        if field[line_selection - 1][column_selection - 1] != 2 and field[line_selection - 1][column_selection - 1] != 1:
            field[line_selection - 1][column_selection - 1] = 2
            break
        else:
            print('выбранные координаты не доступны ')
            line_selection = int(
                input('Введите номер строки. номер строки начинается с 1 и заканчивается 3  '))
            column_selection = int(
                input('Введите номер столбца. номер столбца начинается с 1 и заканчивается 3  '))


def check(field, turn):
    is_valid = (
            field[0][0] == field[0][1] == field[2][0] == turn
            or field[0][1] == field[1][1] == field[1][2] == turn
            or field[0][2] == field[1][2] == field[2][2] == turn
            or field[0][0] == field[1][1] == field[2][2] == turn
            or field[0][2] == field[1][1] == field[2][0] == turn
            or field[0][0] == field[0][1] == field[0][2] == turn
            or field[1][0] == field[1][1] == field[1][2] == turn
            or field[2][0] == field[2][1] == field[2][2] == turn
    )
    return is_valid

turn = 1
while True:
    turn_man(game_field)
    fill_field(game_field)
    if check(game_field, turn):
       print('Победили x ')
       break
    else:
        turn += 1
    turn_bot(game_field)
    fill_field(game_field)
    if check(game_field, turn):
        print('Победили 0 ')
        break
    else:
        turn -= 1