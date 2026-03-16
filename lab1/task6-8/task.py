import re


def find_max_number_float(string):
    """
    1. Дана строка. Необходимо найти максимальное из имеющихся в ней
    вещественных чисел.
    """
    numbers = list(map(float, re.findall(r"-?\d+\.\d+", string)))
    return max(numbers)


def find_min_number_rational(string):
    """
    2. Дана строка. Необходимо найти минимальное из имеющихся в ней
    рациональных чисел.
    """
    def convert_to_float(string_rational):
        num1, num2 = string_rational.split("/")
        return round(int(num1) / int(num2), 5)

    numbers = list(map(convert_to_float, re.findall(r"-?\d+/\d+", string)))
    return min(numbers)


def cnt_numbers(string):
    """
    3. Дана строка. Необходимо найти наибольшее количество идущих
    подряд цифр.
    """
    cnt_num = 0
    cnt_num_max = 0
    for letter in string:
        if letter in "0123456789":
            cnt_num += 1
        else:
            cnt_num_max = max(cnt_num_max, cnt_num)
            cnt_num = 0
    return cnt_num_max


choice = {1: find_max_number_float, 2: find_min_number_rational, 3: cnt_numbers}
choice_by_user = int(input(f"Выберите задачу:{choice[1].__doc__}, {choice[2].__doc__}, {choice[3].__doc__}"))
print(choice[choice_by_user](input("Введите входные данные: ")))