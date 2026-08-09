# Stock Watcher

A Codex skill for managing a local Chinese A-share watchlist and summarizing current quotes from 同花顺.

## Features

- Add, list, remove, and clear watched stocks.
- Store watchlist data locally in the skill folder.
- Fetch quote summaries through 同花顺 structured quote API.
- Fall back to 同花顺 HTML parsing when the API path fails.
- Avoid browser cookies and user login tokens.

## Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

## Usage

```bash
bash scripts/install.sh
python3 scripts/add_stock.py 600188 兖矿能源
python3 scripts/list_stocks.py
python3 scripts/summarize_performance.py
python3 scripts/remove_stock.py 600188
```

Use a custom data directory when desired:

```bash
STOCK_WATCHER_DATA_DIR="$HOME/.stock-watcher" python3 scripts/list_stocks.py
```

## Notes

同花顺 endpoints used here are not official public APIs and may change. Output is for analysis and monitoring only, not investment advice.
