# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
numbers = [5, 9, -4, 0, 6, 7]
summa = 0

for number in numbers:
    if number > 0:
        summa += number
print("Сумма элементов ", summa)
