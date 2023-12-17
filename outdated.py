months = {
    "январь": "01",
    "февраль": "02",
    "март": "03",
    "апрель": "04",
    "май": "05",
    "июнь": "06",
    "июль": "07",
    "август": "08",
    "сентябрь": "09",
    "октябрь": "10",
    "ноябрь": "11",
    "декабрь": "12"
}

while True:
    date = input("Дата (дд.мм.гггг или дд месяц гггг): ")
    try:
        parts = date.replace(".", " ").split()
        if len(parts) == 3:
            day, month, year = parts
            if month in months:
                month = months[month]
            print(f"Результат: {year}-{month}-{day}")
            break
        else:
            print("Некорректный ввод, попробуйте снова.")
    except ValueError:
        print("Некорректный ввод, попробуйте снова.")
