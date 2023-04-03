# Задача 1
# Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. Вычислите результат.
# Пример
# Ввод

# 8-5+2-1
# Вывод
# 4

# s = input()
# stack = []
# num = 0
# sign = 1
# for c in s:
#     if c.isdigit():
#         num = num * 10 + int(c)
#     elif c == '+':
#         stack.append(sign * num)
#         num = 0
#         sign = 1
#     elif c == '-':
#         stack.append(sign * num)
#         num = 0
#         sign = -1
# stack.append(sign * num)
# print(sum(stack))

# Задача 2
# Словом в данной задаче считается последовательность букв, ограниченная пробелами или началом или концом строки.
# Выведите все слова из строки в столбик. НЕЛЬЗЯ ПОЛЬЗОВАТЬСЯ МЕТОДАМИ СТРОК (split)

# Формат ввода
# Вводится строка.

# Формат вывода
# Выведите слова из строки по одному.

# Пример 1
# Ввод

# Hello, world!
# Вывод
# Hello,
# world!
# Пример 2
# Ввод

# My heart in the Highland
# Вывод
# My
# heart
# in
# the
# Highland

# s = input()
# word = ''
# flag = False
# for c in s:
#     if c == ' ':
#         if word:
#             if flag:
#                 print()
#             print(word)
#             word = ''
#             flag = True
#     else:
#         word += c
# if word:
#     if flag:
#         print()
#     print(word)

