#!/usr/bin/env python3
"""Clear the local watchlist."""

from config import WATCHLIST_FILE, ensure_watchlist


def clear_watchlist() -> None:
    ensure_watchlist()
    WATCHLIST_FILE.write_text("", encoding="utf-8")
    print("Watchlist cleared successfully.")


if __name__ == "__main__":
    clear_watchlist()
