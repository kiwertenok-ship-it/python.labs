import re
import sys


def ord_by_len():
    lines = []
    print("Введите строки (для завершения ввода нажмите Ctrl+D):")
    for line in sys.stdin:
        lines.append(line)
    return sorted(lines, key=lambda x: len(re.findall(r"\w(|;|,|!\?|:|!|\?) \w", x)))


print("Прочитать список строк с клавиатуры. Упорядочить по количеству слов в строке")
print("\n", *ord_by_len(), sep="")
