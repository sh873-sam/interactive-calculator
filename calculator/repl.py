from __future__ import annotations

from dataclasses import dataclass

from calculator.operations import (
    add,
    subtract,
    multiply,
    divide,
    DivisionByZeroError,
)


@dataclass(frozen=True)
class ParsedCommand:
    op: str
    a: float
    b: float


SUPPORTED_OPS = {"+", "-", "*", "/"}


def parse_input(user_input: str) -> ParsedCommand:
    """
    Parse input in the form: "<op> <num1> <num2>"
    Example: "+ 2 3"
    """
    text = user_input.strip()
    if not text:
        raise ValueError("Empty input.")

    parts = text.split()
    if len(parts) != 3:
        raise ValueError("Expected format: <op> <num1> <num2> (example: + 2 3)")

    op = parts[0]
    if op not in SUPPORTED_OPS:
        raise ValueError("Operation must be one of: + - * /")

    try:
        a = float(parts[1])
        b = float(parts[2])
    except ValueError as exc:
        raise ValueError("Both numbers must be valid numeric values.") from exc

    return ParsedCommand(op=op, a=a, b=b)


def compute(cmd: ParsedCommand) -> float:
    if cmd.op == "+":
        return add(cmd.a, cmd.b)
    if cmd.op == "-":
        return subtract(cmd.a, cmd.b)
    if cmd.op == "*":
        return multiply(cmd.a, cmd.b)
    return divide(cmd.a, cmd.b)


def format_result(value: float) -> str:
    if value.is_integer():
        return str(int(value))
    return str(value)


def repl() -> int:
    print("Interactive Calculator")
    print("Enter: <op> <num1> <num2>  (example: + 2 3)")
    print("Operations: + - * /")
    print("Type 'q' or 'quit' to exit.\n")

    while True:
        user_input = input("> ").strip()
        if user_input.lower() in {"q", "quit"}:
            print("Goodbye!")
            return 0

        try:
            cmd = parse_input(user_input)
            result = compute(cmd)
            print(f"= {format_result(result)}")
        except DivisionByZeroError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
