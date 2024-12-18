# summary
def calculate_structure_sum(*args):
    global result  # глобальная переменная, что бы каждый раз не обнулять при след. итерации
    for elem in args:  # type(args) == tuple
        if isinstance(elem, (int, float)):  # если элемент число
            result += elem  # прибавляем к результату число
        elif isinstance(elem, str):  # если элемент строка
            result += len(elem)  # прибавляем к результату длину строки
        elif isinstance(elem, (list, tuple, set)):  # если спископодобный* элемент
            calculate_structure_sum(*elem)  # передаем в новую итерацию раскрытый список*
        elif isinstance(elem, dict):  # если словарь
            calculate_structure_sum(*elem.items())  # передаем распакованную пару ключ-значение

    return result


result = 0
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(calculate_structure_sum(data_structure))
