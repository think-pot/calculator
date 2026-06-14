"""
CLI interface for the calculator module using Click.
Provides operations: add, subtract, multiply, divide, power, square_root.
"""

import sys
import click
from src.calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation: str, num1: float, num2: float = None) -> None:
    """Perform a calculation based on the given operation and numbers."""
    try:
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "power":
            result = power(num1, num2)
        elif operation in ("square_root", "sqrt"):
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        if result == int(result):
            click.echo(int(result))
        else:
            click.echo(f"{result:.2f}")

    except (TypeError, ValueError) as err:
        click.echo(f"Error: {err}")
        sys.exit(1)


def main() -> None:
    """Entry point for CLI."""
    calculate.main(standalone_mode=True)


if __name__ == "__main__":
    main()
