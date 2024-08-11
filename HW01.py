'''
Нужно выполнить две задачи:
1. найти элементы, которые есть в каждом списке;
2. найти элементы из первого списка, которых нет во втором и третьем
списках.
Каждую задачу нужно выполнить двумя способами:
1. без использования множеств;
2. с использованием множеств
'''


array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]


# Решение 1-1

check_list = array_1 + array_2 + array_3
result_1_1 = []
for number in check_list:
    if all([number in array_1, number in array_2, number in array_3]) and number not in result_1_1:
        result_1_1.append(number)

print('Решение 1 без множеств: ', *result_1_1)

# Решение 1-2

set_1_1 = set(array_1)
set_1_2 = set(array_2) 
set_1_3 = set(array_3) 

result_1_2 = set_1_1.intersection(set_1_2).intersection(set_1_3)

print('Решение 1 с множествами: ', *result_1_2)

# Решение 2-1

result_2_1 = []

for number in array_1:
    if all([number not in array_2, number not in array_3]) and number not in result_2_1:
        result_2_1.append(number)

print('Решение 2 без множеств: ', *result_2_1)

# Решение 2-2

control_set = set(array_2 + array_3) 
set_1 = set(array_1)

result_2_2 = set_1.difference(control_set)


print('Решение 2 с множествами: ', *result_2_2)