# Словари ДЗ
def average_marks(students):
    result = {}
    for student, marks in students.items():
        if len(marks) > 0:
            result[student] = sum(marks) / len(marks)
        else:
            result[student] = 0
    return result


def group_by_mark(students):
    result = {}
    for student, marks in students.items():
        if marks not in result:
            result[marks] = []
        result[marks].append(student)
    return result


def word_statistics(words):
    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1

    most_found = ""
    max_count = 0
    for word, count in result.items():
        if count > max_count:
            max_count = count
            most_found = word
    return (result, most_found)

print(average_marks({"Анна": [5, 4, 5], "Иван": [3, 4], "Олег": []}))
print(group_by_mark({"Аня": 5, "Игорь": 4, "Лена": 5}))
print(word_statistics(["кот", "пёс", "кот", "лиса", "пёс", "кот"]))
