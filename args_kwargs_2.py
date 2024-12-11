# args kwargs 2

def single_root_words(root_word, *args):  # первое слово в root_word остальные в *args
    same_words = []
    root = root_word.lower()  # приводим корень в ниж рег.
    for word in args:
        word_l = word.lower()  # слово из args в ниж рег.
        if word_l in root or root in word_l:  # если есть одно в другом или другое в том, то
            same_words.append(word)

    return same_words


# def single_root_words(root_word, *args):  # еще один вариант исполнения с count()
#     same_words = []
#     root = root_word.lower()
#     for word in args:
#         word_l = word.lower()
#         if word_l.count(root) > 0 or root.count(word_l) > 0:
#             same_words.append(word)
#
#     return same_words

result1 = single_root_words('work', 'workable', 'walker', 'сo-working', 'worked')
print(result1)
result2 = single_root_words('КОЛ', 'Укол', 'КОЛУН', 'клоун', 'ПРОКОЛ')
print(result2)
