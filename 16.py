# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint


def count_values_in_list(random_list):
    value_to_count = get_number()
    counter = 0
    for value in random_list:
        if value == value_to_count:
            counter += 1
    return counter


def get_new_random_list(list_length):
    new_random_list = []
    for i in range(list_length):
        new_random_list.append(randint(1, 10))
    print(new_random_list)
    return new_random_list


def get_number():
    return int(input('Введите натуральное число: '))


print(count_values_in_list(get_new_random_list(get_number())))
