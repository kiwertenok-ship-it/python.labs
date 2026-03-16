# Вариант 5

def create_files(cnt_files):
    files = {}
    for i in range(cnt_files):
        file = input().split()
        files[file[0]] = "".join(file[1:])
    return files


def check_files(cnt_operations, files):
    operations = {
        'read': "R",
        "write": "W",
        "execute": "X"
    }
    for i in range(cnt_operations):
        operation, file_name = input().split()
        if operations[operation] in files[file_name]:
            print("OK")
        else:
            print("Access denied")


cnt_files = int(input("Введите количество файлов: "))
print("Введите файлы и права доступа")
files = create_files(cnt_files)
cnt_operations = int(input("Введите количество операций над файлами: "))
print("Введите операции:")
check_files(cnt_operations, files)
