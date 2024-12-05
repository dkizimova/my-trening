def send_email(message, recipient, *, sender ='university.help@gmail.com' ):#a-message, b-recipient, c-sender

    def gram_fail(email):
        if '@' not in email or not email.endswith((".com",".ru",".net")):
            return True
        return False
    if any(map(gram_fail,(sender, recipient))):
        return print("Невозможно отправить письмо с адреса", sender , "на адрес ", recipient , ".")

    def send_rep(email):
        if sender == recipient:
            return True
        return False
    if any(map(send_rep,(sender, recipient))):
        return print("Нельзя отправить письмо самому себе!")

    if sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса ', sender, ' на адрес', recipient, '.')
        #break
    elif sender != 'university.help@gmail.com':
        print('Нестандартный отправитель! Письмо отправлено с адреса ', sender, 'на адрес', recipient, '.')

send_email("hello", "alex@mail.ru", sender="university.help@gmail.com")
send_email('back', "dikimail.com")
send_email("bool", "university.help@gmail.com")
send_email("help", "dili@gmail.com", sender="pavkix@rambler.ru")
