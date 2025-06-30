#7 поиск макс числа

num = []
a = int(input('Введите количество повторений:'))

for i in range(a):
    c = input('Введите число:')
    num.append(c)

b = max(num)
c = min(num)
print(f'Максимальное число {b} минимальное число {c}')

