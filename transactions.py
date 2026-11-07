"""Додавання, перегляд та видалення транзакцій."""

from decimal import Decimal, InvalidOperation


def add_transaction(
    transactions: list[dict],
    transaction_type: str,
    amount: Decimal | int | float | str,
    category: str,
    description: str,
) -> dict:
    """Перевіряє дані, додає транзакцію і повертає створений словник."""
    if transaction_type not in ("income", "expense"):
        raise ValueError("Тип транзакції має бути income або expense.")

    try:
        amount = Decimal(str(amount).strip().replace(",", "."))
    except InvalidOperation:
        raise ValueError("Введіть числову суму, наприклад 25,50.") from None

    if not amount.is_finite() or amount <= 0:
        raise ValueError("Сума має бути додатним скінченним числом.")

    category = category.strip()
    description = description.strip()
    if not category or not description:
        raise ValueError("Категорія та опис не можуть бути порожніми.")

    transaction_id = max((item["id"] for item in transactions), default=0) + 1
    transaction = {
        "id": transaction_id,
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "description": description,
    }
    transactions.append(transaction)
    return transaction
