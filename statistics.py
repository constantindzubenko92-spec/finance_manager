"""Розрахунок підсумків та фільтрація транзакцій."""

from decimal import Decimal


def calculate_income(transactions: list[dict]) -> Decimal:
    """Повертає суму всіх доходів."""
    total = Decimal("0")
    for item in transactions:
        if item["type"] == "income":
            total += item["amount"]
    return total
