def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
	# def feet2meter(v):
    v = v.replace('ft', '')  # Удаляем 'ft' из строки
    feet = float(v)  # Преобразуем строку в число с плавающей точкой
    meter = feet * 0.3048  # Переводим футы в метры
    return meter
main()
