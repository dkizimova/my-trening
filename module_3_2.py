def send_email(message, recipient, *, sender ='university.help@gmail.com' ):#a-message, b-recipient, c-sender
    for i in range(1): #блок поиска @ .net, .ru, .com
        s = recipient.find("@")
        d = recipient.find('.com')
        q = recipient.find('.net')
        w = recipient.find('.ru')
        #print(s, d, q, w)
        for j in range(1):
            z = sender.find("@")
            f = sender.find(".com")
            e = sender.find(".ru")
            r = sender.find(".net")
            #print(z, f, e, r)
            #t = recipient.find(sender)
            if s < 0 or (d < 0 and q < 0 and w < 0):
                print("Невозможно отправить письмо с адреса", sender , "на адрес ", recipient , ".")
                break
            elif z < 0 or (f < 0 and e < 0 and r < 0):
                print("Невозможно отправить письмо с адреса", sender ,  "на адрес ", recipient, ".")
                break
            elif sender == recipient:
                print("Нельзя отправить письмо самому себе!")
                break
            elif sender == 'university.help@gmail.com':
                print('Письмо успешно отправлено с адреса ', sender ,' на адрес', recipient ,'.')
                break
            elif sender!= 'university.help@gmail.com':
                print ('Нестандартный отправитель! Письмо отправлено с адреса ',  sender , 'на адрес', recipient, '.')



            else:
                break


    #return send_email(a, b, c)
#print(send_email("hello", aka@mail.ru, ckula@koala.com ))

send_email("hello", "alex@mail.ru" , sender="university.help@gmail.com")
send_email('back', "dikimail.com")
send_email("bool", "university.help@gmail.com")
send_email("help", "dili@gmail.com", sender="pavkix@rambler.ru")


