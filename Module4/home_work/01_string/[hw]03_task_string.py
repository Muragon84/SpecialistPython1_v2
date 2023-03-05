# Посчитайте количество согласных букв в данной строке.

text = ...

text = "В теории, теория и практика неразделимы. На практике это не так."
text_new = text.lower()
vowels = set("бвгджзйклмнпрстфхцчшще")
count = 0

for letter in text_new:
    if letter in vowels:
        count += 1

print("Согласных букв: ", count)
