from typing import Callable

from example_app.config import settings

Compute_Fun = Callable[[int], int]


def add_three(x: int) -> int:
    x = x + 3
    return x


def multiple_by_two(input: float) -> float:
    return input * 2


def main() -> None:
    compute: Compute_Fun = add_three
    print(f"Hello {compute(5)} {settings.DB_PASSWORD}")


if __name__ == "__main__":
    main()
