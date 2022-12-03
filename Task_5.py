#Реализуйте алгоритм перемешивания списка.

from random import randint

original_list = []
n = int(input('Введите число: '))
for i in range(n):
    original_list.append(i+1)
print(original_list)

mixed_list = original_list
for i in range (len(mixed_list)):
    random_i = randint(0, (len(mixed_list) - 1))
    tmp = mixed_list[i]
    mixed_list[i] = mixed_list[random_i]
    mixed_list[random_i] = tmp
print(mixed_list)
