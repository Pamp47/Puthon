# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

num_day = int(input('enter the number of the day of the week '))
# num_day = 28

if num_day > 31:
    print('there is no such day')
elif num_day % 7 == 6 or num_day % 7 == 0:
    print('weekend')
else:
    print('working day')
