# Вариант 7
# Функция 1 Найти сумму простых делителей числа.
# Функция 2 Найти количество нечетных цифр числа, больших 3
# Функция 3 Найти произведение таких делителей числа, сумма цифр
# которых меньше, чем сумма цифр исходного числа.


def find_sum(num):
    sum_ = 1
    for div in range(2, num + 1):
        if num % div == 0 and is_prime(div):
            sum_ += div
    return sum_


def is_prime(num):
    for div in range(2, num):
        if num % div == 0:
            return False
    return True


def count_not_even(num):
    cnt = 0
    while num > 0:
        digit = num % 10
        cnt += 1 if digit > 3 and digit & 1 == 1 else 0
        num //= 10
    return cnt


def find_multiply(num):
    def sum_digits(number):
        sum_ = 0
        while number > 0:
            sum_ += number % 10
            number //= 10
        return sum_

    sum_digit_num = sum_digits(num)
    sum_digit_divs = 0
    multi_digit_divs = 1
    for div in range(1, num + 1):
        if num % div == 0:
            sum_digit_div = sum_digits(div)
            if sum_digit_divs + sum_digit_div >= sum_digit_num:
                break
            multi_digit_divs *= div
    return multi_digit_divs

num = int(input("Введите число: "))
print(f"Найти сумму простых делителей числа - ", find_sum(num))
print(f"Найти количество нечетных цифр числа, больших 3 - ", count_not_even(num))
print(f"Найти произведение таких делителей числа, сумма цифр которых меньше,\
чем сумма цифр исходного числа - ", find_multiply(num))