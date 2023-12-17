menu = {
    "кофе": 20.00,
    "чай": 10.00,
    "булочка": 5.00,
    "салат": 30.40,
    "пирожное": 45.50
}

total_cost = 0

while True:
    try:
        order = input("Блюдо: ").lower()
        if order in menu:
            total_cost += menu[order]
    except EOFError:  # Catching the Ctrl+D signal
        break

print(f"Сумма: {total_cost:.2f}")
