from copy import deepcopy
from collections import Counter


def cycle_shift(array):
    """
    1. Дан целочисленный массив. Необходимо осуществить циклический
    сдвиг элементов массива вправо на две позиции.
    """
    len_array = len(array)
    array_new = deepcopy(array)
    for i in range(len_array):
        array_new[(i + 2) % (len_array)] = array[i]
    return array_new


def cycle_shift_2(array):
    """
    2. Дан целочисленный массив. Необходимо осуществить циклический
    сдвиг элементов массива вправо на одну позицию.
    """
    len_array = len(array)
    array_new = deepcopy(array)
    for i in range(len_array):
        array_new[(i + 1) % (len_array)] = array[i]
    return array_new


def cnt_even_num(array):
    """
    3. Дан целочисленный массив. Найти количество чётных элементов.
    """
    cnt_even = 0
    for num in array:
        if num.isdigit():
            num = int(num)
            if num & 1 == 0:
                cnt_even += 1
    return cnt_even


def cnt_even_min_num(array):
    """
    4. Дан целочисленный массив. Необходимо найти количество минимальных элементов.
    """
    min_num = float("inf")
    for num in array:
        if num.isdigit():
            min_num = min(int(num), min_num)
    cnt = 0
    for num in array:
        if num == str(min_num):
            cnt += 1
    return cnt


def sort_by_cnt(array):
    """
    5. Для введенного списка построить новый список, который получен из
    начального упорядочиванием по количеству встречаемости элемента, то есть
    из списка [5,6,2,2,3,3,3,5,5,5] необходимо получить список [5,5,5,5,3,3,3,2,2,6].
    """
    counts = Counter(array)
    sorted_lst = sorted(array, key=lambda x: (-counts[x], x))
    return sorted_lst




choice = {1: cycle_shift, 2: cycle_shift_2, 3: cnt_even_num, 4: cnt_even_min_num, 5: sort_by_cnt}
choice_by_user = int(input(f"Выберите задачу:{choice[1].__doc__}, {choice[2].__doc__}, {choice[3].__doc__}, {choice[4].__doc__}, {choice[5].__doc__}"))
print(choice[choice_by_user](list(input("Введите входные данные слитно: "))))
