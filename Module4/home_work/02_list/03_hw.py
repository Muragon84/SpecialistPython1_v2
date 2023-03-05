# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here

import random

n = int(input("Ведите количество элементов n: "))
numbers = []
if n >= 0:
    for i in range(n):
        numbers.append(random.randint(-100, 100))
        i += 1
    print(numbers)
else:
    print("n должно быть больше нуля")

summa = 0
for element in numbers:
     if element >= 0 and element % 2 == 0:
        summa += element

print("Cумма всех положительных элементов кратных двум: ", summa)
