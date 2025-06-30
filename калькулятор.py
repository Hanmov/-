print('Приветствую вас в калькуляторе')
print('Нажмите на ctrl и c чтоб закончить работу с калькулятором')
while True:
    onenum = int(input('Введите число: '))
    twonum = int(input('Введите число: '))
    print('Введите знак(+ сложение, - вычитание, * умножение, ** возвести первое число в степень, / деление, // деление с остатком, % остаток от деления).')
    znak = input('> ')


    if znak == '+':
        otvet = onenum + twonum
        print(f'{onenum} + {twonum} = {otvet}')
    elif znak == '-':
        otvet = onenum - twonum
        print(f'{onenum} - {twonum} = {otvet}')
    elif znak == '*':
        otvet = onenum * twonum
        print(f'{onenum} * {twonum} = {otvet}')
    elif znak == '**':
        otvet = onenum ** twonum
        print(f'{onenum} ** {twonum} = {otvet}')
    elif znak == '/':
        otvet = onenum / twonum
        print(f'{onenum} / {twonum} = {otvet}')
    elif znak == '//':
        otvet = onenum // twonum
        print(f'{onenum} // {twonum} = {otvet}')
    elif znak == '%':
        otvet = onenum % twonum
        print(f'{onenum} % {twonum} = {otvet}')