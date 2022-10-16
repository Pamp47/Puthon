# Задайте число N. Составьте список чисел Фибоначчи, N - количество чисел в списке

n = 5


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


lst1 = []
for i in range(1, n+1):
    lst1.append(fib(i))
print(lst1)
