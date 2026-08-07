---
name: stock-watcher
description: Manage and monitor a local Chinese A-share watchlist. Use when the user asks to add, remove, list, clear, or summarize watched stocks using 10jqka structured quote data with HTML fallback.
---

# Stock Watcher

Use this skill to manage a local A-share watchlist and summarize current quotes.

## Scope

- Supports common 6-digit A-share stock codes.
- Infers 同花顺 market `17` for `6xxxxx`; infers market `33` for `0xxxxx` and `3xxxxx`.
- Stores watchlist data inside this skill folder at `data/watchlist.txt`.
- Supports `STOCK_WATCHER_DATA_DIR` to override the watchlist directory.
- Uses the 同花顺 structured quote API first.
- Falls back to parsing `https://stockpage.10jqka.com.cn/{stock_code}/` when the API path fails.

Do not store browser cookies, user login tokens, or other credentials in this skill.

## Commands

Run scripts from the skill folder or by passing their full path:

```bash
bash scripts/install.sh
python3 scripts/list_stocks.py
python3 scripts/add_stock.py 600188 兖矿能源
python3 scripts/remove_stock.py 600188
python3 scripts/clear_watchlist.py
python3 scripts/summarize_performance.py
```

If dependencies are missing, install them first:

```bash
python3 -m pip install -r requirements.txt
```

## Watchlist Format

`data/watchlist.txt` uses one stock per line:

```text
600188|兖矿能源
002384|东山精密
```

Set `STOCK_WATCHER_DATA_DIR` when the watchlist should live outside the skill folder:

```bash
STOCK_WATCHER_DATA_DIR="$HOME/.stock-watcher" python3 scripts/list_stocks.py
```

## Output

`summarize_performance.py` prints concise quote summaries:

```text
600188 - 兖矿能源 - 最新价: 20.27 - 涨跌幅: 1.35% - 涨跌额: 0.27 - 成交额: 1229165230.0 - 来源: API
```

If the API fails but HTML parsing succeeds, output is marked `来源: HTML`.

## Limitations

- 同花顺 endpoints are not official public APIs and may change or block requests.
- Output may be delayed or unavailable depending on network and market status.
- The data is for analysis and monitoring only, not investment advice.
