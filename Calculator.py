import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())  # считывания поля
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    value = num1 + num2
    insert_values(value)


def sub():
    num1, num2 = get_values()
    value = num1 - num2
    insert_values(value)


def mul():
    num1, num2 = get_values()
    value = num1 * num2
    insert_values(value)


def div():
    num1, num2 = get_values()
    value = num1 / num2
    insert_values(value)


window = tk.Tk()  # Создание окна интерфейса
window.title('Калькулятор')  # Название окна
window.geometry('350x350')  # Размеры окна
window.resizable(False, False)  # Изменяемость размера окна
button_add = tk.Button(window, text='+', width=2, height=2, command=add)  # создание кнопки +, выст, шир
button_add.place(x=100, y=250)  # размеры кнопки
button_sub = tk.Button(window, text='-', width=2, height=2, command=sub)
button_sub.place(x=150, y=250)
button_mul = tk.Button(window, text='*', width=2, height=2, command=mul)
button_mul.place(x=200, y=250)
button_div = tk.Button(window, text='/', width=2, height=2, command=div)
button_div.place(x=250, y=250)
number1_entry = tk.Entry(window, width=28)  # поле для ввода, ширина 28
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=130)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=200)
number1 = tk.Label(window, text="Введите первое число:")  # надпись
number1.place(x=100, y=50)
number2 = tk.Label(window, text="Введите второе число:")
number2.place(x=100, y=105)
answer = tk.Label(window, text="Ответ:")
answer.place(x=100, y=175)
window.mainloop()  # задает цикл обновление окна в конце
