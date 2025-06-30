#5 угадай число

import random

print("Приветствую вас в игре угадай число")
print("Вам нужно угадать число от 1 до 100")

rec = 0

snum = random.randint(1, 100)
while True:
    a = int(input('Ваше число: '))
    rec += 1
    
    if a < snum:
        print('мое число больше')
    elif a > snum:
        print('Мое число меньше')
    else:
        print(f'Поздравляю вы уадали число за {rec} попыток!')
        break