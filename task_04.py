# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('enter the quarter number '))
if quarter == 1:
    print('x > and y > 0')
elif quarter == 2:
    print('x < 0 and y > 0')
elif quarter == 3:
    print('x < 0 and y < 0')
elif quarter == 4:
    print('x > 0 and y < 0')
elif quarter > 4:
    print('there is no such quarter')
