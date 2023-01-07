# 1, 2, 3
# "abc"
# [10, 20, 30]

# print(type(1))
# print(type("abc"))
# print(type([10, 20, 30]))

# class Fruit:
# pass
#
# a = Fruit()
# b = Fruit()
#
# a.name = "apple"
# a.weight = 120
#
# b.name = "orange"
# b.weight = 150
#
# print(a.name, a.weight)
# print(b.name, b.weight)
#
# b.weight -= 50
#
# print(a.name, a.weight)
# print(b.name, b.weight)

# 1, 2, 3
# "abc"
# [10, 20, 30]

# print(type(1))
# print(type("abc"))
# print(type([10, 20, 30]))

# class Fruit:
# pass
#
# a = Fruit()
# b = Fruit()
#
# a.name = "apple"
# a.weight = 120
#
# b.name = "orange"
# b.weight = 150
#
# print(a.name, a.weight)
# print(b.name, b.weight)
#
# b.weight -= 50
#
# print(a.name, a.weight)
# print(b.name, b.weight)
 # class Hello:
# def hello_world(self):
# print("Привет, Мир!")
#
# def greeting(self, name):
# print(f"Привет, {name}")
#
# greet = Hello()
# greet.hello_world()
# greet.greeting("Bob")


# class Car:
#
# def __init__(self, color):
# self.e_on = False
# self.color = color
#
# def start(self):
# self.e_on = True
#
# def drive_to(self, city):
# if self.e_on:
# print(f"Едем в {city} на {self.color} авто")
# else:
# print("Никуда не едему - заведите авто")
#
# c = Car("красный")
# c.start()
# c.drive_to('Сочи')

# print(1 + 2)
# print(1.3 + 2.5)
# print('1.3' + '2.5')
#
# def f(x, y):
# return x + y
#
# print(f(1, 2))
# print(f('1.3', '2.5'))


# class Book:
# def __init__(self, name, auth):
# self.name = name
# self.auth = auth
#
# def get_name(self):
# return self.name
#
# def get_auth(self):
# return self.auth
#
# book = Book('Война и мир', 'Толстой')
#
# print(f"книга - {book.get_name()}, автор - {book.get_auth()}")
#om math import pi
#
# class Circle:
# def __init__(self, radius):
# self.radius = radius
#
# def area(self):
# return pi * self.radius ** 2
#
# def perimeter(self):
# return 2 * pi * self.radius
#
# class Square:
# def __init__(self, side):
# self.side = side
#
# def area(self):
# return self.side * self.side
#
# def perimeter(self):
# return 4 * self.side
#
#
#
# def print_shape_info(shape):
# print(f'Area = {shape.area()}, perimeter = {shape.perimeter()}')
#
# square = Square(10)
# # print(square.area())
# # print(square.perimeter())
# print_shape_info(square)
#
# circle = Circle(10)
# print_shape_info(circle)

# class Employee:
#     def __init__(self, name, id):
#         self.id = id
#         self.name = name
#
#     def display(self):
#         print("ID: %d \nName: %s" % (self.id, self.name))
#
#
# emp1 = Employee("John", 101)
# emp2 = Employee("David", 102)
#
# # accessing display() method to print employee 1 information
#
# emp1.display()
#
# # accessing display() method to print employee 2 information
# emp2.display()

# class Student:
#     count = 0
#     def __init__(self):
#         Student.count = Student.count + 1
# s1=Student()
# s2=Student()
# s3=Student()
# print("The number of students:",Student.count)

# class Student:
#     # Constructor - non parameterized
#     def __init__(self):
#         print("This is non parametrized constructor")
#     def show(self,name):
#         print("Hello",name)
# student = Student()
# student.show("John")

# class Student:
#     # Constructor - parameterized
#     def __init__(self, name):
#         print("This is parametrized constructor")
#         self.name = name
#     def show(self):
#         print("Hello",self.name)
# student = Student("John")
# student.show()

# class Student:
#     roll_num = 101
#     name = "Joseph"
#
#     def display(self):
#         print(self.roll_num, self.name)
#
#
# st = Student()
# st.display()

# class Student:
#     def __init__(self):
#         print("The First Constructor")
#
#     def __init__(self):
#         print("The second contructor")
#
#
# st = Student()

# class Student:
#     def __init__(self, name, id, age):
#         self.name = name
#         self.id = id
#         self.age = age
#
#         # creates the object of the class Student
#
#
# s = Student("John", 101, 22)
#
# # prints the attribute name of the object s
# print(getattr(s, 'name'))
#
# # reset the value of attribute age to 23
# setattr(s, "age", 23)
#
# # prints the modified value of age
# print(getattr(s, 'age'))
#
# # prints true if the student contains the attribute with name id
#
# print(hasattr(s, 'id'))
# # deletes the attribute age
# delattr(s, 'age')
#
# # this will give an error since the attribute age has been deleted
# print(s.age)

# class Student:
#     def __init__(self,name,id,age):
#         self.name = name;
#         self.id = id;
#         self.age = age
#     def display_details(self):
#         print("Name:%s, ID:%d, age:%d"%(self.name,self.id))
# s = Student("John",101,22)
# print(s.__doc__)
# print(s.__dict__)
# print(s.__module__)

# class car:
#     def __init__(self, modelname, year):
#         self.modelname = modelname
#         self.year = year
#
#     def display(self):
#         print(self.modelname, self.year)
#
#
# c1 = car("Toyota", 2016)
# c1.display()

# class Vehicle(object):
#     """docstring"""
#
#     def __init__(self, color, doors, tires):
#         """Constructor"""
#         self.color = color
#         self.doors = doors
#         self.tires = tires
#
#     def brake(self):
#         """
#         Stop the car
#         """
#         return "Braking"
#
#     def drive(self):
#         """
#         Drive the car
#         """
#         return "I'm driving!"
#
#
# if __name__ == "__main__":
#     car = Vehicle("blue", 5, 4)
#     print(car.color)
#
#     truck = Vehicle("red", 3, 6)
#     print(truck.color)
#
# class Vehicle(object):
#     """docstring"""
#
#     def __init__(self, color, doors, tires, vtype):
#         """Constructor"""
#         self.color = color
#         self.doors = doors
#         self.tires = tires
#         self.vtype = vtype
#
#     def brake(self):
#         """
#         Stop the car
#         """
#         return "%s braking" % self.vtype
#
#     def drive(self):
#         """
#         Drive the car
#         """
#         return "I'm driving a %s %s!" % (self.color, self.vtype)
#
#
# if __name__ == "__main__":
#     car = Vehicle("blue", 5, 4, "car")
#     print(car.brake())
#     print(car.drive())
#
#     truck = Vehicle("red", 3, 6, "truck")
#     print(truck.drive())
#     print(truck.brake())
#
#
# class Car(Vehicle):
#     """
#     The Car class
#     """
#
#     # ----------------------------------------------------------------------
#     def brake(self):
#         """
#         Override brake method
#         """
#         return "The car class is breaking slowly!"
#
#
# if __name__ == "__main__":
#     car = Car("yellow", 2, 4, "car")
#     print(car.brake())
#     'The car class is breaking slowly!'
#     print(car.drive())
#     "I'm driving a yellow car!"
#
# class Rectangle:
#     'Это класс Rectangle'
#
#     # Способ создания объекта (конструктор)
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def getWidth(self):
#         return self.width
#
#     def getHeight(self):
#         return self.height
#
#     # Метод расчета площади.
#     def getArea(self):
#         return self.width * self.height
#
#
# r1 = Rectangle(10, 5)
# r2 = Rectangle(20, 11)
#
# print("r1.width = ", r1.width)
# print("r1.height = ", r1.height)
# print("r1.getWidth() = ", r1.getWidth())
# print("r1.getArea() = ", r1.getArea())
#
# print("-----------------")
#
# print("r2.width = ", r2.width)
# print("r2.height = ", r2.height)
# print("r2.getWidth() = ", r2.getWidth())
# print("r2.getArea() = ", r2.getArea())

# class Person:
#     # Параметры возраста и пола имеют значение по умолчанию.
#     def __init__(self, name, age=1, gender="Male"):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def showInfo(self):
#         print("Name: ", self.name)
#         print("Age: ", self.age)
#         print("Gender: ", self.gender)
#
#
# aimee = Person("Aimee", 21, "Female")
# aimee.showInfo()
# print(" --------------- ")
#
# # возраст по умолчанию, пол.
# alice = Person("Alice")
# alice.showInfo()
#
# print(" --------------- ")
#
# # Пол по умолчанию.
# tran = Person("Tran", 37)
# tran.showInfo()
#
# class Player:
#     # Переменная класса
#     minAge = 18
#     maxAge = 50
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# player1 = Player("Tom", 20)
#
# player2 = Player("Jerry", 20)
#
# print("player1.name = ", player1.name)
# print("player1.age = ", player1.age)
#
# print("player2.name = ", player2.name)
# print("player2.age = ", player2.age)
#
# print(" ------------ ")
#
# print("Assign new value to player1.age = 21 ")
#
# # Присвойте новое значение атрибуту возраста player1.
# player1.age = 21
#
# print("player1.name = ", player1.name)
# print("player1.age = ", player1.age)
#
# print("player2.name = ", player2.name)
# print("player2.age = ", player2.age)
#
# player1 = Player("Tom", 20)
# player2 = Player("Jerry", 20)
#
# # Создайте новый атрибут с именем «address» для player1.
# player1.address = "USA"
#
# print("player1.name = ", player1.name)
# print("player1.age = ", player1.age)
# print("player1.address = ", player1.address)
#
# print(" ------------------- ")
#
# print("player2.name = ", player2.name)
# print("player2.age = ", player2.age)
#
# # player2 е имеет атрибута 'address' (Error!!)
# print("player2.address = ", player2.address)


# class Student:
#     def __init__(self, full_name="", group_number="", progress=[]):
#         self.full_name = full_name
#         self.group_number = group_number
#         self.progress = progress
#     def __repr__(self):
#         return repr(("Студент: " + self.full_name + "  Группа: " + self.group_number))
#     def addStu(self):
#         print("Введите Фио: ")
#         self.full_name = input()
#         print("Введите номер группы: ")
#         self.group_number = input()
#         print("Введите последние 5 отценок : ")
#         self.progress = []
#         for i in range(3):
#             score = int(input())
#             self.progress.append(score)
#     def getMarks(self): # возвращает список оценок
#         return self.progress
# st_size = 2
# sz_ocenki = 5
# students = [] # список студентов
# for i in range(st_size):
#     st = Student()
#     st.addStu()
#     students.append(st)
#
# for student in students:
#     print(student.getMarks())
#     print(student.__repr__())
#
# class Student:
#         def __init__(self, name, grade, age):
#             self.name = name
#             self.grade = grade
#             self.age = age
#         def __repr__(self):
#             return repr((self.name, self.grade, self.age))
#         def weighted_grade(self):
#             return 'CBA'.index(self.grade) / self.age
#
# student_objects = [
#         Student('john', 'A', 15),
#         Student('jane', 'B', 12),
#         Student('dave', 'B', 10),
#     ]
# sorted(student_objects, key=lambda student: student.age)
# print(student_objects.__repr__())
#
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# importing the BeautifulSoup Library

import requests
from bs4 import BeautifulSoup as bs

# Creating the requests

res = requests.get('https://www.litres.ru/new/')
print("The object type:", type(res))

# Convert the request object to the Beautiful Soup Object
soup = bs(res.text, 'html.parser')
print("The object type:", type(soup))
soup.select('.GenreSearchInput-module__wrapper_wHZgK')

print(soup.text, end=',')


