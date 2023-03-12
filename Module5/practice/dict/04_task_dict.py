# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]
# Вычислите:
print("Имя и Фамилию сотрудника с самой высокой зарплатой:")

max_employee = staff[0]
for employee in staff:
    if employee["salary"] > max_employee["salary"]:
        max_employee = employee
print(f'Самая высокая зарплата: {max_employee["name"]} {max_employee["surname"]}')

print("Имя и Фамилию сотрудника с самой низкой зарплатой:")

min_employee = staff[0]
for employee in staff:
    if employee["salary"] < min_employee["salary"]:
        min_employee = employee
print(f'Самая низкая зарплата: {min_employee["name"]} {min_employee["surname"]}')

print("Среднеарифметическую зарплату всех сотрудников")

all_salary = 0
for salary in staff:
    all_salary += salary["salary"]
print(f'Среднеарифметическая зарплата всех сотрудников: {round(all_salary / len(staff), 2)}')

print("Количество однофамильцев в организации")

surnames = []
counter = {}
result = 0

for surname in staff:
    surnames.append(surname["surname"])
for last_surname in surnames:
    if last_surname in counter:
        if counter[last_surname] == 1:
            result += 2
        else:
            result += 1
        counter[last_surname] += 1
    else:
        counter[last_surname] = 1

print(f'Количество однофамильцев в организации: {result}')
print(f'Сколько штук одной фамилии: {counter}')

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")

staff.sort(key=lambda dictionary: dictionary['salary'])
for num, employee in enumerate(staff, 1):
    print(num, employee["name"], employee["surname"])
