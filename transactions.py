"""Додавання, перегляд та видалення транзакцій."""

from decimal import Decimal, InvalidOperation

MAX_AMOUNT = Decimal("999999999999.99")
CENT = Decimal("0.01")
_next_transaction_id = 1


def add_transaction(
    transactions: list[dict],
    transaction_type: str,
    amount: Decimal | int | float | str,
    category: str,
    description: str,
) -> dict:
    """Перевіряє дані, додає транзакцію і повертає створений словник."""
    global _next_transaction_id

    if transaction_type not in ("income", "expense"):
        raise ValueError("Тип транзакції має бути income або expense.")

    try:
        amount = Decimal(str(amount).strip().replace(",", "."))
    except InvalidOperation:
        raise ValueError("Введіть числову суму, наприклад 25,50.") from None

    if not amount.is_finite() or amount <= 0:
        raise ValueError("Сума має бути додатним скінченним числом.")
    if amount > MAX_AMOUNT:
        raise ValueError(f"Максимальна сума транзакції: {MAX_AMOUNT}.")
    if amount != amount.quantize(CENT):
        raise ValueError("Сума має містити не більше двох знаків після коми.")

    category = category.strip()
    description = description.strip()
    if not category or not description:
        raise ValueError("Категорія та опис не можуть бути порожніми.")

    largest_existing_id = max((item["id"] for item in transactions), default=0)
    transaction_id = max(_next_transaction_id, largest_existing_id + 1)
    transaction = {
        "id": transaction_id,
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "description": description,
    }
    transactions.append(transaction)
    _next_transaction_id = transaction_id + 1
    return transaction


def show_transactions(transactions: list[dict]) -> None:
    """Виводить транзакції з вирівняними колонками."""
    if not transactions:
        print("Транзакцій не знайдено.")
        return

    headings = ("ID", "TYPE", "AMOUNT", "CATEGORY", "DESCRIPTION")
    rows = [
        (
            str(item["id"]),
            item["type"],
            str(item["amount"]),
            item["category"],
            item["description"],
        )
        for item in transactions
    ]
    widths = [
        max(len(heading), max(len(row[index]) for row in rows))
        for index, heading in enumerate(headings)
    ]
    header = " | ".join(text.ljust(width) for text, width in zip(headings, widths))
    print(header)
    print("-" * len(header))
    for row in rows:
        print(" | ".join(text.ljust(width) for text, width in zip(row, widths)).rstrip())


def delete_transaction(transactions: list[dict], transaction_id: int) -> bool:
    """Видаляє транзакцію за ID. Повертає False, якщо її немає."""
    for index, item in enumerate(transactions):
        if item["id"] == transaction_id:
            del transactions[index]
            return True
    return False
