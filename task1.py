# ЧАСТЬ 1
# 1 калькулятор возраста
#изучуть модуль дата и усовершенствовать код



# from datetime import datetime


# today = datetime.now()

# print("Введите дату рождения в формате ДД.ММ.ГГГГ (например: 30.09.2008)")
# date = input("Ваша дата рождения: ")


# birth_date = datetime.strptime(date, "%d.%m.%Y")
# age = today - birth_date


# print(f"Ваш возраст: {age} лет")



from datetime import datetime

def main():
    # Получаем текущую дату
    today = datetime.now().date()  # Используем .date() для работы только с датой
    
    # Запрашиваем дату рождения
    print("Введите дату рождения в формате ДД.ММ.ГГГГ (например: 15.03.1990)")
    
    while True:
        try:
            birth_str = input("> ")
            birth_date = datetime.strptime(birth_str, "%d.%m.%Y").date()
            break
        except ValueError:
            print("Ошибка! Введите дату в формате ДД.ММ.ГГГГ (например: 15.03.1990)")
    
    # Вычисляем возраст
    age = today.year - birth_date.year
    
    # Проверяем, был ли уже день рождения в этом году
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    # Выводим результат
    print(f"Ваш возраст: {age} лет")

if __name__ == "__main__":
    main()
