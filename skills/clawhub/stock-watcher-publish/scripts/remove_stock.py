#!/usr/bin/env python3
"""Remove a stock from the local watchlist."""

import sys

from config import WATCHLIST_FILE, ensure_watchlist


def remove_stock(stock_code: str) -> bool:
    ensure_watchlist()

    with WATCHLIST_FILE.open("r", encoding="utf-8") as file:
        existing_stocks = [line.strip() for line in file if line.strip()]

    updated_stocks = [
        stock for stock in existing_stocks
        if not stock.startswith(f"{stock_code}|")
    ]

    if len(updated_stocks) == len(existing_stocks):
        print(f"Stock {stock_code} not found in watchlist")
        return False

    with WATCHLIST_FILE.open("w", encoding="utf-8") as file:
        for stock in updated_stocks:
            file.write(stock + "\n")

    print(f"Removed stock {stock_code} from watchlist")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 remove_stock.py <stock_code>")
        sys.exit(1)

    remove_stock(sys.argv[1])
