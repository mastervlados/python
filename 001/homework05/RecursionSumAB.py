# Задача 28: 
# Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

def sum(a, b):
    if b == 1:
        return a + 1
    return 1 + sum(a, b - 1)

a = int(input("Введите число А = "))
b = int(input("Введите число B = "))

print("{} + {} = {}".format(a, b, sum(a, b)))