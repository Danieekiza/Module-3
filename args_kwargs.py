# *args * kwargs
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# def append_to_list(*args, list_my=None): # не входит в основоне дз
#     if list_my is None:
#         list_my = []
#     for item in args:
#         list_my.append(item)
#     print(list_my)


print_params()
print_params(2, 'qwerty', [1, 2, 3])
print_params('True', True, 1)
print_params(c='True', a=2, b=False)
print_params(c=[1, 2, 3])
print()

value_list = ['false', False, 0]
value_dict = {'a': 'true', 'b': True, 'c': 1}
print_params(*value_list)
print_params(**value_dict)
print()

value_list_2 = [54.4, 'bbbb']
print_params(*value_list_2, 42)
print()

# value_list_3 = [1, 11.1, 'qwerty', True, False] #  не входит в основное дз
# append_to_list(*value_list_3, list_my=['first_value'])
