# ЧАСТЬ 1
# 1 калькулятор возраста
#изучуть модуль дата и усовершенствовать код

from datetime import datetime


today = datetime.now()

print("Введите дату рождения в формате ДД.ММ.ГГГГ (например: 30.09.2008)")
date = input("Ваша дата рождения: ")


birth_date = datetime.strptime(date, "%d.%m.%Y")
age = today - birth_date


print(f"Ваш возраст: {age} лет")

