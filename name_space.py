# name_space
import random


def count_calls():  # функция подсчета ее вызова
    global calls  # пишет в глобальную переменную
    calls += 1
    return calls


def string_info(string):  # функция преобразования строки
    count_calls()
    list_ = []
    list_.append(len(string))
    list_.append(string.upper())
    list_.append((string.lower()))
    tup_ = tuple(list_)
    return tup_


def is_contains(string, list_to_search):  # функция поиска строки в списке
    count_calls()
    list_ = list_to_search  # переопределяем переменные
    l_str = string.lower()  # Определяем локал.перем. как string в ниж. рег.
    count = 0
    for elem in list_:  # для каждой elem в list_
        list_[count] = elem.lower()  # в list_ запишем elem в ниж.рег.
        if l_str == list_[count]:  # Если строка и текущий эл. списка равны
            return True
            break
        count += 1
    return False


calls = 0  # назначим переменную calls
cnt = 0  # счетчик пригодится
string_list = ['KnoPpoCHka', 'ShiShkA', 'vEnEk', 'OreshNik', 'КняZz']  # строка на выбор
contains_list = ['knoPPoCHka', 'Sh_IShkA', 'venek', 'AreshNik', 'svoBol', 'КНЯzz']  # список для поиска

while cnt != 5:
    a = str(*random.sample(string_list, 1))  # случаный 1 элемент из string_list
    b = random.sample(contains_list, 3)  # случаные 3 элемента из contains_list
    print('string: ', a)
    print('list_to_search: ', b)
    print(string_info(a))
    print(is_contains(a, b))
    print('calls: ', calls)
    print()
    cnt += 1
