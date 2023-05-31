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
    element = int(input('Введите число: '))
    my_list.append(element)
number = int(input('Введите число: '))
print(my_list)
my_list2 = []
for i in range(len(my_list)):
    element2 = number - my_list[i] 
    #print(element2)
    my_list2.append(abs(element2))
print(my_list2)
print(min(my_list2))


    