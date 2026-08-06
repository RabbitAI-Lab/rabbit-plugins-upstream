#!/usr/bin/env python3
"""Add a stock to the local watchlist."""

import sys

import requests
from bs4 import BeautifulSoup

from config import WATCHLIST_FILE, ensure_watchlist


def get_stock_name_from_code(stock_code: str) -> str | None:
    """Best-effort stock name lookup from 10jqka HTML."""
    url = f"https://stockpage.10jqka.com.cn/{stock_code}/"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = "utf-8"
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("title")
        if not title:
            return None

        title_text = title.get_text()
        if "(" in title_text and ")" in title_text:
            return title_text.split("(")[0].strip()
    except requests.RequestException:
        return None

    return None


def add_stock(stock_code: str, stock_name: str | None = None) -> bool:
    ensure_watchlist()

    if not stock_code.isdigit() or len(stock_code) != 6:
        print("Stock code must be a 6-digit A-share code.")
        return False

    stock_name = stock_name or get_stock_name_from_code(stock_code) or stock_code

    existing_stocks = []
    with WATCHLIST_FILE.open("r", encoding="utf-8") as file:
        existing_stocks = [line.strip() for line in file if line.strip()]

    if any(stock.startswith(f"{stock_code}|") for stock in existing_stocks):
        print(f"Stock {stock_code} already in watchlist")
        return False

    existing_stocks.append(f"{stock_code}|{stock_name}")
    with WATCHLIST_FILE.open("w", encoding="utf-8") as file:
        for stock in existing_stocks:
            file.write(stock + "\n")

    print(f"Added stock {stock_code} ({stock_name}) to watchlist")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 add_stock.py <stock_code> [stock_name]")
        sys.exit(1)

    code = sys.argv[1]
    name = sys.argv[2] if len(sys.argv) > 2 else None
    add_stock(code, name)
