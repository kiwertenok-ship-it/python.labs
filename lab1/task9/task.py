import sys


def ord_by_len():
    lines = []
    print("Введите строки (для завершения ввода нажмите Ctrl+D):")
    for line in sys.stdin:
        lines.append(line)
    return sorted(lines, key=len)

print("Прочитать список строк с клавиатуры. Упорядочить по длине cтроки")
print("\n", *ord_by_len(), sep="")
