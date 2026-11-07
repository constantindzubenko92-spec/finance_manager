"""Точка входу до консольного меню обліку доходів і витрат."""

from statistics import (
    calculate_balance,
    calculate_expenses,
    calculate_income,
    filter_by_category,
)
from transactions import add_transaction, delete_transaction, show_transactions

MENU = """
========== FINANCE MANAGER ==========

1. Додати дохід
2. Додати витрату
3. Переглянути всі транзакції
4. Показати загальний дохід
5. Показати загальні витрати
6. Показати поточний баланс
7. Фільтрація за категорією
8. Видалити транзакцію
0. Вихід
"""


def main() -> None:
    """Приймає команди користувача до вибору виходу."""
    transactions: list[dict] = []
    while True:
        print(MENU)
        choice = input("Оберіть дію: ").strip()

        if choice == "0":
            print("До побачення!")
            break
        elif choice in ("1", "2"):
            transaction_type = "income" if choice == "1" else "expense"
            amount = input("Сума: ")
            category = input("Категорія: ")
            description = input("Опис: ")
            try:
                transaction = add_transaction(
                    transactions, transaction_type, amount, category, description
                )
            except ValueError as error:
                print(error)
            else:
                print(f"Додано транзакцію ID {transaction['id']}.")
        elif choice == "3":
            show_transactions(transactions)
        elif choice == "4":
            print(f"Загальний дохід: {calculate_income(transactions)}")
        elif choice == "5":
            print(f"Загальні витрати: {calculate_expenses(transactions)}")
        elif choice == "6":
            print(f"Поточний баланс: {calculate_balance(transactions)}")
        elif choice == "7":
            category = input("Оберіть категорію: ")
            show_transactions(filter_by_category(transactions, category))
        elif choice == "8":
            try:
                transaction_id = int(input("Введіть ID транзакції: "))
            except ValueError:
                print("ID має бути цілим числом.")
                continue
            if delete_transaction(transactions, transaction_id):
                print("Транзакцію видалено.")
            else:
                print("Транзакцію з таким ID не знайдено.")
        else:
            print("Невідома дія. Оберіть пункт меню.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nДо побачення!")
