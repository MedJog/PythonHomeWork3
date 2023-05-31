# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 3 -> 1
# вариант 1
my_list = []
num = int(input('Введите количество элементов списка: '))
for i in range(num):
    element = int(input('Введите число: '))
    my_list.append(element)
number = int(input('Введите число: '))
print(my_list)
count = 0
for i in range(len(my_list)):
    if my_list[i] == number:
        count += 1
if count > 0:
    print(f' Элемент {number} встречается в списке {count} раз.')
else:
    print(f'Такого элемента в списке нет.')

# вариант 2
from random import randint
list_1 = []
number = int(input('Введите количество элементов списка: '))
for i in range(number):
    list_1.append(randint(0, 20))
print(list_1)
element = int(input('Введите искомый элемент: '))
count = 0
for i in range(len(list_1)):
    if list_1[i] == element:
        count += 1
if count > 0:
    print(f' Элемент {element} встречается в списке {count} раз.')
else:
    print(f'Такого элемента в списке нет.')

