# summary
def calculate_structure_sum(*args):
    global summa
    for elem in args:
        if isinstance(elem, (int, float)):
            summa += int(elem)
        elif isinstance(elem, str):
            summa += len(elem)
        elif isinstance(elem, (list, tuple, set)):
            calculate_structure_sum(*elem)
        elif isinstance(elem, dict):
            calculate_structure_sum(*elem.items())
    return summa


summa = 0
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(calculate_structure_sum(data_structure))
