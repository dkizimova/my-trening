print('Вводите данные студентов по алфавиту')
a= input('Введите фамилию студента: ')              #множество для 1 студента
aa= input('Введите оценки студента без пробела: ')  #список для 1 студ
b=input('Введите фамилию студента: ')               #множество для 2 студ
bb= input('Введите оценки студента без пробела: ')  #список для 2 студ
c=input('Введите фамилию студента: ')               #множество для 3 студ
cc= input('Введите оценки студента без пробела: ')  #список для 3 студ
d=input('Введите фамилию студента: ')               #множество для 4 студ
dd= input('Введите оценки студента без пробела: ')  #список для 4 студ


students = { a, b, c, d } #просвоили студентам множества( по заданию они не упорядочены)
grades = [aa, bb, cc, dd]    #присвоили оценкам список( по заданию они стоят по алфавиту)
print(students)
print(grades)

student_list = list(students) #перевели множество в список, для выборки по алфавиту
print(student_list)
student_list.sort() #отсортировали фамилии по алфавиту
print(student_list) #вывели отсортированный список

grades1 = grades[0] #вытаскиваем оценки в переменную
print(grades1)
grades2 = grades[1]
print(grades2)
grades3 = grades[2]
print(grades3)
grades4 = grades[3]
print(grades4)

##grades2 = int(grades[0])
grades1 = grades1.__len__() #считаем количество оценок
print(grades1) #выводим количество оценок
grades2 = grades2.__len__()
print(grades2)
grades3 = grades3.__len__()
print(grades3)
grades4 = grades4.__len__()
print(grades4)

sum1=0
for i in aa:
    sum1 +=int(i)
print(str(sum1)) #Сумма оценок 1
sum2=0
for i in bb:
    sum2 +=int(i)
print(str(sum2)) #Сумма оценок 2
sum3=0
for i in cc:
    sum3 +=int(i)
print(str(sum3)) #Сумма оценок 3
sum4=0
for i in dd:
    sum4 +=int(i)
print(str(sum4)) #Сумма оценок 4

sred_bal1= sum1 / grades1
print(sred_bal1) #считаем и выводим средний балл 1
sred_bal2= sum2 / grades2
print(sred_bal2) #считаем и выводим средний балл 2
sred_bal3= sum3 / grades3
print(sred_bal3) #считаем и выводим средний балл 3
sred_bal4= sum4 / grades4
print(sred_bal4) #считаем и выводим средний балл 4


book= [
    [student_list[0], sred_bal1],
    [student_list[1], sred_bal2],
    [student_list[2], sred_bal3],
    [student_list[3], sred_bal4]
] #создаем список из фамилий и среднего балла
print(book)
dict_book = dict(book)
print(dict_book)
print(type(dict_book))
