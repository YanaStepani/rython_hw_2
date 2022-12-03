# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = float(input('Введите число: '))
sum_of_digits = 0
if number < 0:
    number *= -1
for i in str(number):
    if i != '.':
        sum_of_digits += int(i)
print(sum_of_digits)

