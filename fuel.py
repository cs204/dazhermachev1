while True:
    try:
        fraction = input("Дробь (в формате x/y): ")
        x, y = map(int, fraction.split('/'))
        if x < 0 or y <= 0 or x > y:
            print("Некорректный ввод, попробуйте снова.")
            continue
        percent = round(x / y * 100)
        if percent <= 1:
            print("E (empty)")
        elif percent >= 99:
            print("F (full)")
        else:
            print(f"{percent}%")
        break
    except (ValueError, ZeroDivisionError):
        print("Некорректный ввод, попробуйте снова.")
