# Напишите программу, которая принимает на вход цифру,  
# обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input("Введите число дня недели: "))

if day < 1 or day > 7:
    print('такого дня недели нет')
elif day > 5:
    print('Выходной день')
else:
    print('будний день')