# Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.
number = 12, 14, 42, 65, 53, 76, 9, 1
number = list(number)
sum_numbers = 0

for i in number:
    if i % 2 == 0:
        sum_numbers += i
print(sum_numbers)
