#  arguments_of_function

def send_email(message, recipient, *, sender="university.help@gmail.com"):
    emailes = [recipient, sender]  # список адресов почты в запросе
    flag = True
    for e in emailes:  # Поочередно провермяем получателя и отправителя
        if '@' not in e:  # если нет '@'
            flag = False
        elif '.ru' not in e and '.com' not in e and '.net' not in e:  # если неправильный домен
            flag = False
    if flag == False:  # если неправильный домен или нет '@'
        print(f"Невозможно отправить письмо с адреса '{sender}' на адрес '{recipient}'")
    else:
        if recipient == sender:  # если отправитель = получателю
            print(f"Невозможно отправить письмо самому себе")
        elif sender == 'university.help@gmail.com':  # если отправитель по умолчанию
            print(f"Письмо успешно отправлено с адреса '{sender}' на адрес '{recipient}'")
        elif sender != 'university.help@gmail.com':  # если отправитель не по умолчанию
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса '{sender}' на адрес '{recipient}'")


message_pull = ['Заберите свой диплом', 'дратути. вы уволены((() дотвидания.', 'Avada Kedavra']
email_pull = ['love.mail.ru', 'love@mail.uk', 'love.@mail.ru', 'hate@mail.com']

send_email(message_pull[0], email_pull[2])  # успешно отправлено
send_email(message_pull[0], email_pull[0])  # Невозможно отправить
send_email(message_pull[0], email_pull[1])  # Невозможно отправить
send_email(message_pull[1], email_pull[2], sender=email_pull[2])  # Невозможно отправить письмо самому себе
send_email(message_pull[1], email_pull[2], sender=email_pull[3])  # НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!

