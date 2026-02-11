from __future__ import annotations


class CalculatorError(Exception):
    """Base error for calculator operations."""


class DivisionByZeroError(CalculatorError):
    """Raised when division by zero occurs."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero.")
    return a / b
