import random


def stone_1(): #создаем рандомное число
    random_numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    ran_num = random.choice(random_numbers)
    return ran_num


def get_passcode(ran_num):  # создаём словарь с кодами и паролями
    passdict = {}
    passdict.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645})
    passdict.update({10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867})
    passdict.update({14: 1611325212343114105968, 15: 1214114232133124115106978})
    passdict.update({16: 1317115262143531341251161079, 17: 11621531441351261171089})
    passdict.update({18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910})
    passdict.update({20: 13141911923282183731746416515614713812911})
    passcode = passdict.get(ran_num)
    return passcode


ran_num = stone_1()
print("Камень со случайным числом: ", ran_num)

number_for_password = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
new_list = []
result = ' '

for i in number_for_password:
    for j in number_for_password:
        pn1 = i
        pn2 = j
        if pn1 >= pn2:
            continue
        else:
            kratno = ran_num % (pn1 + pn2)
            if kratno == 0:
                new_list.append([pn1, pn2])
                result = result + str(pn1) + str(pn2)

m = (''.join((map(str, new_list))))
print(m)
print("Введите пароль: ", result)
if int(result) == get_passcode(ran_num):
    print("Ворота открыты")
