# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 4, 3, 1, 8]
# Ввод: 10
# [-10, -9, ...-4, -3, -2, -1, 0, 1, 2, 3,4....10]
num1 = 10
lst = []

for i in range(-num1, num1 + 1):
    lst.append(i)
print(lst)

lst_idx = []
for i in input('введи индексы ').split():
    lst_idx.append(int(i))

answer = 1
for i in lst_idx:
    answer *= lst[i]
print(answer)
