# ЧАСТЬ 2
# 6 переверни строку

a = input('Напишите что-нибудь: ')
reversed_a = a[::-1]

if len(reversed_a) > 1:
    reversed_a = reversed_a[0].upper() + reversed_a[1:-1] + reversed_a[-1].lower()
else:
    reversed_a = reversed_a.upper()
    
print(reversed_a)