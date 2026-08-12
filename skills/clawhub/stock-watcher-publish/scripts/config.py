#!/usr/bin/env python3
"""Shared configuration for stock-watcher scripts."""

import os
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parent.parent
WATCHLIST_DIR = Path(os.environ.get("STOCK_WATCHER_DATA_DIR", SKILL_DIR / "data")).expanduser()
WATCHLIST_FILE = WATCHLIST_DIR / "watchlist.txt"


def ensure_watchlist() -> None:
    WATCHLIST_DIR.mkdir(parents=True, exist_ok=True)
    WATCHLIST_FILE.touch(exist_ok=True)
