"""Розрахунок підсумків та фільтрація транзакцій."""

from decimal import Decimal


def calculate_income(transactions: list[dict]) -> Decimal:
    """Повертає суму всіх доходів."""
    total = Decimal("0")
    for item in transactions:
        if item["type"] == "income":
            total += item["amount"]
    return total


def calculate_expenses(transactions: list[dict]) -> Decimal:
    """Повертає суму всіх витрат."""
    total = Decimal("0")
    for item in transactions:
        if item["type"] == "expense":
            total += item["amount"]
    return total


def calculate_balance(transactions: list[dict]) -> Decimal:
    """Повертає різницю між доходами та витратами."""
    return calculate_income(transactions) - calculate_expenses(transactions)


def filter_by_category(transactions: list[dict], category: str) -> list[dict]:
    """Повертає транзакції вказаної категорії без урахування регістру."""
    category = category.strip().casefold()
    return [item for item in transactions if item["category"].casefold() == category]
