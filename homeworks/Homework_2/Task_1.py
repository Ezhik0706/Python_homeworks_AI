"""
Создать список и заполнить его элементами
различных типов данных. Реализовать скрипт
проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""
my_list = [674, 35.08, "bingo", True, [45, 83], {0, 1, 2}, (23, 40), {"1": 'Name', "2": 'Surname'}]
print(my_list)
for i in range(len(my_list)):
    print(my_list[i], "-", type(my_list[i]))