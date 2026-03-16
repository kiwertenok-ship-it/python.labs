"""
Вариант 7
"""
n = int(input())
set_yes = set()
set_no = set()
switch = {
    "yes": lambda x: set_yes.update(x),
    "no": lambda x: set_no.update(x),
}
question = input()
while question.lower() != "help":
    question = question.split()
    question_filter = []
    for i in question:
        if int(i) <= n:
            question_filter.append(i)
    answer = input().lower()
    switch[answer](question_filter)
    set_yes.difference_update(set_no)
    question = input()
numbers = sorted(list(set_yes))
print(*numbers)

