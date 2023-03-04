# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B 
# с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

def pow_ab(a, b):
    if b == 1:
        return a
    elif b == 0:
        return 1 # the number in ^0 = 1
    return a * pow_ab(a, b - 1)

a = int(input("Введите число А = "))
b = int(input("Введите число B = "))

print("A = {}; B = {} -> {}".format(a, b, pow_ab(a, b)))