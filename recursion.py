# recursion
def get_multiplied_digits(number):  # возвращает перемножение целых чисел
    global stack, itr  # stack - стек, itr - итерация
    itr += 1
    stack.append(itr)
    str_number = str(int(number))  # если в строке пришли первые "0", то избавляемся от них
    first = int(str_number[0])  # берем первый элемент строки как число
    if int(number) == False and stack == [1]:  # если при первом вызове функции передаются 00...0
        return 0
    elif first == 0:  # если элемент строки 0, то сохраняем множество неизменным
        return 1
    elif len(str_number) == 1:  # если в строке один элемент, то возвращаем его в first
        return first

    return first * get_multiplied_digits(int(str_number[1:]))  # перемножаем first с результатом след вывода -
    #  - get_multiplied_digits cо списком без first


params = [
    000,
    '0000',
    11111100000,
    '0000111111100000',
    102030400,
    '0000203040000'
]

itr = 0
stack = []

for param in params:
    print(get_multiplied_digits(param))
    itr = 0
    stack = []
