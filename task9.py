#9 сортировка чисел

num = []
a = int(input('Введите количество повторений:'))
for i in range(a):
    b = int(input('Введите число:'))
    num.append(b)
num.sort()
print(num)