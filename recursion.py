# recursion
def get_multiplied_digits(number):  # возвращает перемножение целых чисел
    str_number = str(int(number))  # если в строке пришли первые "0", то избавляемся от них
    first = int(str_number[0])  # берем первый элемент строки ка число
    if first == 0:
        return 1
    if len(str_number) == 1:  # если в строке один элемент, то возвращаем его в first
        return first
    return first * get_multiplied_digits(int(str_number[1:]))  # перемножаем first с результатом след вывода
                                                               #  get_multiplied_digits cо списком без first


print(get_multiplied_digits(10203040))
print(get_multiplied_digits('002030400'))
