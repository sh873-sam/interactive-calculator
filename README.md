Assignment #3 – Command-Line Calculator

This project is a Python-based interactive command-line calculator that implements a REPL (Read–Eval–Print Loop). It supports basic arithmetic operations, input validation, graceful error handling, and enforces test coverage using automated GitHub Actions.

Project Structure
interactive-calculator/
├── calculator/
│   ├── __init__.py
│   ├── operations.py
│   └── repl.py
├── tests/
│   ├── test_operations.py
│   └── test_repl.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
└── README.md

Features
Calc Operations:
Addition, Subtraction, Multiplication and Division (with division-by-zero handling)

REPL Interface
Continuous user interaction
Clear prompts and instructions
Graceful handling of invalid input

Error Handling
Invalid numeric input
Invalid operation selection
Division by zero with meaningful error messages

Design Principles
All arithmetic logic is centralized in operations.py
The REPL (repl.py) only handles user interaction and delegates logic
Tests reuse shared functionality and avoid duplicated logic

Testing
Written using pytest

Includes parameterized tests for arithmetic operations

Tests cover:
Valid calculations
Invalid inputs
Edge cases (e.g., division by zero)

Running my project locally
Cloned the repository
created and activated a virtual environment
installed dependencies
ran the calculator
ran tests
ran tests with coverage

The project uses GitHub Actions to automatically:
run al tests on each push
enforce code coverage
fail the build if any test fails or coverage is insufficient

This can be found in
.github/workflows/ci.yml

