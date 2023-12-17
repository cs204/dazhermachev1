amount_due = 50
change_owed = 0

while change_owed < amount_due:
    coin = int(input("Вставьте монету: "))
    change_owed += coin
    print(f"Нужная сумма: {amount_due - change_owed} осталось")

if change_owed >= amount_due:
    print(f"Ваша сдача: {change_owed - amount_due} рублей")
