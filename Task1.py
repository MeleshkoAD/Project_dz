# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# n = int(input())
# a = set(map(int, input().split()))
# m = int(input())
# b = set(map(int, input().split()))
# result = sorted(a & b)
# for i in result:
#     print(i)


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

# n = int(input())
# a = list(map(int, input().split()))

# if n == 1:
#     print(a[0])
# else:
#     dp = [[0, 0] for _ in range(n)]
#     dp[0][0] = a[0]
#     dp[1][0] = a[1]
#     dp[1][1] = a[0] + a[1]
#     for i in range(2, n):
#         dp[i][0] = max(dp[i - 1][1], dp[i - 2][0]) + a[i]
#         dp[i][1] = max(dp[i - 2][0], dp[i - 2][1]) + a[i - 1] + a[i]
#     print(max(dp[n - 1]))
