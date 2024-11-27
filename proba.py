import random

from module_2_3 import my_list


def stone_1():
    random_numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    ram_num=random.choice(random_numbers)
    return ram_num

ram_num = stone_1()
print("Камень со случайным числом: ", ram_num)

number_for_password = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

a = []
for i in number_for_password:  #Создали список по 2 элемента
    for j in number_for_password:
        aa = [i,j]
        a.append(aa)
#print(a)

for item in a:  #Список вывели в столбик
    print(item)

print(a[0]) #а - это список в стобик сумм

len_a = a.__len__()  #длинна списка
print(len_a)

index = 0
new_list = []
for i in a: #цикл для вычисления пароля
    total=sum(a[index]) #считаем сумму по индексу
    #b.append(total)
    if ram_num % total == 0:
        new_list.append(a[index])
        index = index + 1
        continue
    if ram_num == total:
        new_list.append(a[index])
    else:
        index=index+1
    continue

'''index=0
list_1=[]
list_2=[]
for q in new_list:
    if new_list[index] == new_list[index]:
        list_1.append(new_list[index])
        index=index+1
        continue
    if new_list[index] != new_list[index]:
        list_2.append(new_list[index])
        index= index+1'''

#print(*new_list)
new_list_1 = []
index=0

'''for i in new_list:
    print(*i)

print(new_list[0][0])'''

'''list_of_tuples = list(map(lambda x: (x, None), new_list))

print(list_of_tuples, end='\n\n')
dict_new = {}
dict_new = dict(list_of_tuples)
print(type(dict_new))
print(dict_new, end='\n\n')

new_list3 = list(dict_new.keys())
print(new_list3, end='\n\n')'''
#print(new_list)
#print(new_list_1)

print("Камень со случайным числом: ", ram_num)




'''print(b)
print(b[0])

index=0


a[index] in new_list:
        new_list.remove(a[index])
        index = index + 1
        continue

for k in b:
    p = b[index]
    index = index + 1
    while ram_num % p == 0:
        new_list.append(b[index])
        break
    if ram_num == p:
        new_list.append(b[index])
    else:
        continue
        print("Все")'''

#print(new_list[])
#print(total)

'''sum1=0
for i in number_for_password:
    sum1 += i
    if ram_num % sum1 == 0:
        print(sum1)'''

