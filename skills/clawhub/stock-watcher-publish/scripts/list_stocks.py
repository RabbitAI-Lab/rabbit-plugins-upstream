#!/usr/bin/env python3
"""List all stocks in the local watchlist."""

from config import WATCHLIST_FILE, ensure_watchlist


def list_stocks() -> None:
    ensure_watchlist()

    with WATCHLIST_FILE.open("r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]

    if not lines:
        print("Watchlist is empty.")
        return

    print("Your Stock Watchlist:")
    print("-" * 40)
    for index, line in enumerate(lines, 1):
        parts = line.split("|", 1)
        if len(parts) == 2:
            code, name = parts
            print(f"{index}. {code} - {name}")
        else:
            print(f"{index}. {line}")


if __name__ == "__main__":
    list_stocks()
