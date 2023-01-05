# 2)Нужно напистаь программу
# В ней используем классы - имя студента name, номер группы group и список полученных оценок progress.
# В самой программе вводим список всех студентов.
# В программе нужно вывести список студентов, отсортированный по имени, А так же студентов, у которых низкие оценки

class Student:
    def __init__(self, name=[], group=[], progress=[]):
        self.name = name
        self.group = group
        self.progress = progress

    def show_students(self):
        for i in range(len(self.name)):
            print((f'Студент: {self.name[i]}\nГруппа: {self.group[i]}\nСредний балл: {self.progress[i]}'))
            print('---------------')

    def add_Student(self):
        self.name.append(input("Введите Фио: "))
        self.group.append(input("Введите номер группы: "))
        self.progress.append(input("Введите средний балл: "))

    def sort_name(self, indx):
        my_list = []
        for i in range(len(self.name)):
            my_list2 = []
            my_list2.append(self.name[i])
            my_list2.append(self.group[i])
            my_list2.append(self.progress[i])
            my_list.append(my_list2)
            my_list2 = []
        return sorted(my_list, key=lambda x: x[indx])

    def show_sort_list(self, lis):
        for i in range(len(lis)):
                print((f'Студент: {lis[i][0]}\nГруппа: {lis[i][1]}\nСредний балл: {lis[i][2]}'))
                print('---------------')


st = Student()

while True:
    command = int(input('Введите номер команды: \n1.Показать всех студентов\n2.Сортировка по имени\n3.Сортировка по успеваемости\n4.Добавить студента\n'))
    if command == 1:
        st.show_students()
    elif command == 2:
        sort_list = st.sort_name(0)
        st.show_sort_list(sort_list)
    elif command == 3:
        sort_score = st.sort_name(2)
        st.show_sort_list(sort_score)
    elif command == 4:
        st.add_Student()




