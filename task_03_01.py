# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lst1 = [2, 3, 4, 5, 6]
lst2 = []

while len(lst1) > 1:
    lst2.append(lst1[0] * lst1[-1])
    del lst1[0]
    del lst1[-1]
if len(lst1) == 1:
    lst2.append(lst1[0]**2)
print(lst2)