# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

a = 3
b = (bin(a))
print('Ответ ', b[2::])


n = 3
v = []
while n > 0:
    v.append(n % 2)
    n = n // 2

str_2 = ''
for i in v[::-1]:
    str_2 += str(i)
print(str_2)