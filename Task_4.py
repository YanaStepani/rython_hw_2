# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# -2 -1 0 1 2
# Позиции: 0,1 -> 2


n = int(input('Введите число: '))
list_from_minus_n_to_n = []
for i in range (-n, n):
    list_from_minus_n_to_n.append(i)
print(list_from_minus_n_to_n)
count = (len(list_from_minus_n_to_n))

first_index = int(input(f'Введите индекс первого числа от 1 до {count}: '))
second_index = int(input(f'Введите индекс второго числа от 1 до {count}: '))
mult_of_digits = list_from_minus_n_to_n[first_index-1]*list_from_minus_n_to_n[second_index-1]
print(mult_of_digits)


# как разобраться с файлом я так и не поняла :(