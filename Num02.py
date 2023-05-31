# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 6 -> 5

my_list = []
num = int(input('Введите количество элементов списка: '))
for i in range(num):
    element = int(input('Введите число: ')) # элементы списка
    my_list.append(element)
number = int(input('Введите число: ')) # заданное число Х
print(my_list)
my_list2 = []
for i in range(len(my_list)):
    element2 = number - my_list[i] # разница между заданным числом и элементами списка
    my_list2.append(abs(element2))
min_element2 = min(my_list2) # минимальный элемент второго списка
min_index = my_list2.index(min_element2) # индекс минимального элемента 2 списка соответсвует индексу наиболее близкого числа из 1 списка
print(f'Самый близкий по значению элемент к заданному числу {number} -> {my_list[min_index]}.')

from random import randint
list_1 = []
number = int(input('Введите количество элементов списка: '))
for i in range(number):
    list_1.append(randint(-10, 10))
print(list_1)
element = int(input('Введите число: '))
list_2 = []
for i in range(len(my_list)):
    element2 = element - list_1[i] # разница между заданным числом и элементами списка
    list_2.append(abs(element2))
min_element2 = min(list_2) # минимальный элемент второго списка
min_index = list_2.index(min_element2) # индекс минимального элемента 2 списка соответсвует индексу наиболее близкого числа из 1 списка
print(f'Самый близкий по значению элемент к заданному числу {element} -> {list_1[min_index]}.')

    