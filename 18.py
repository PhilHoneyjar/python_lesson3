# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint


def find_closest_value(random_list):
    custom_value = get_number()
    closest_value = random_list[0]
    minimal_difference = abs(random_list[0] - custom_value)
    for value in random_list:
        if abs(value - custom_value) < minimal_difference:
            minimal_difference = abs(value - custom_value)
            closest_value = value
    return closest_value


def get_new_random_list(list_length):
    new_random_list = []
    for i in range(list_length):
        new_random_list.append(randint(1, 100))
    print(new_random_list)
    return new_random_list


def get_number():
    return int(input('Введите натуральное число: '))


print(find_closest_value(get_new_random_list(get_number())))
