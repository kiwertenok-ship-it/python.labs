import re


def cnt_russian_words(string):
    """
    1. Дана строка. Необходимо найти общее количество русских символов.
    """
    alph = set(x for x in "йцукенгшщзхфывапролджэячсмитьбюъ")
    cnt = 0
    for x in string:
        cnt += (x.lower() in alph)
    return cnt


def is_palindrome(string):
    """
    2. Дана строка. Необходимо проверить образуют ли строчные символы
    латиницы палиндром
    """
    alph = set('abcdefghijklmnopqrstuvwxyz')
    word = ""
    word_turned = ""
    for letter in string:
        if letter in alph:
            word += letter
            word_turned = letter + word_turned
    return word_turned == word and word != ""


def find_dates(string):
    """
    3. Найти в тексте даты формата «день.месяц.год»
    """
    answer_group = re.findall(r"([0-2]\d|3[0-1])\.(0\d|1[0-2])\.(\d{4})", string)
    return tuple(map(lambda x: '.'.join(x), answer_group))


choice = {1: cnt_russian_words, 2: is_palindrome, 3: find_dates}
choice_by_user = int(input(f"Выберите задачу:{choice[1].__doc__}, {choice[2].__doc__}, {choice[3].__doc__}"))
print(choice[choice_by_user](input("Введите входные данные: ")))
