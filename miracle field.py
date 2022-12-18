# Необязательное 2*) Сделать поле чудес . Компьютер загадывает слово.
# А мы его угадываем. Делаем с помощью функций. Кто хочет посложней - добавляем очки и барабан.
from random import randint

answer_question = [['москва', 'Столица России'], ['байкал', 'самое полноводное озеро'],['еверест', 'самая высокая гора']]
drum_sections = [200, 500, 800, 1000, 2000, 1500]

def guessing_letter():
    letter = input('Назовите букву: ')
    return letter

def word():
    guessing_word = input('Назовите слово: ')
    return guessing_word

def rotation_drum(drum):
    drum_points = 0
    random_section = randint(0, 5)
    for i in range(len(drum)):
        if random_section == i:
            drum_points = int(drum[i])
    return drum_points


def question_selection(list_quest):
    select = randint(0, len(list_quest) - 1)
    for i in range(0, len(list_quest)):
        if i == select:
            return list_quest[i]

def index_letter(answer, letter):
    index_list = []
    for i in range(0, len(answer)):
        if answer[i] == letter:
            index_list.append(i)
    return index_list

def answer_str(answer):
    res_list = []
    for i in range(0, len(answer)):
        res_list.append('.')
    return res_list

def changes_answer_str(str_list, letter, index):
    res_list = str_list
    j = 0
    for i in range(len(str_list)):
        if j < len(index) and i == index[j]:
            res_list[i] = letter
            j += 1
    return res_list

def print_answer(answer_list):
    for i in answer_list:
        print(i, end='')

def isValid(answer_list):
    count = answer_list.count('.')
    if count == 0:
        return True
    else:
        return False

def letter_valid(letter, answer):
    for i in range(len(answer)):
        if answer[i] == letter:
            return True
        elif i > len(answer):
            return False


print('Приветствую вас на игре поле чудес!!!!!\nИ я ее бессменный ведущий Леонид Якубович\nИ так напоминаю правила игры'
      '\nЯ задаю вопрос вы крутите барабан\nи пытаетесь угадать слово по буквам\nили можете назвать его целиком ')
start = int(input('\nЕсли все понятно введите 1 и мы начнем игру!!!'))
if start == 1:
    print('И так мы начинаем игру!!! ')
    my_points = 0
    quest = question_selection(answer_question)
    answer_field = answer_str(quest[0])
    print(f'Наш вопрос на эту игру:\n{quest[1]} ')
    while True:
        drum_points = rotation_drum(drum_sections)
        print()
        print(f'Всего очков {my_points}\nИ так на барабане {drum_points} очков. ')
        turn = int(input('1. Назовете слово сразу\n2. будете угадывать по буквам '))
        if turn == 1:
            answer = word()
            if quest[0] == answer:
                print('Удивительно но это правильный ответ!!!')
                my_points += drum_points * 2
                print(f'У вас {my_points} очков')
                break
        elif turn == 2:
            letter = guessing_letter()
            index = index_letter(quest[0], letter)
            answer_list = changes_answer_str(answer_field, letter, index)
            if letter_valid(letter, quest[0]):
                print(f'откройте нам букву {letter}')
                print_answer(answer_list)
                my_points += drum_points
            else:
                print(f'Увы такой буквы нет и вы теряете {drum_points} очков ')
                my_points -= drum_points
            if isValid(answer_list):
                print(f'\nУ вас {my_points} очков')
                print('Поздравляю ')
                break
        else:
            print('Нет такой команды!!! ')
else:
    print('Вы отказались играть ')