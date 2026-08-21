---
name: price-predator
version: 1.0.0
author: Denis Voronin
license: MIT
description: Track product prices across time and stores, alert on price drops, and predict the best time to buy.
---

# Price Predator

Track product prices across time and stores, get alerts on price drops, and predict the best time to buy.

## Quick Start

```bash
# Track a product with its current price
python3 scripts/price_predator.py track --name "Sony WH-1000XM5" --price 350.00 --category electronics

# Record a new price observation
python3 scripts/price_predator.py update <product-id> --price 299.99

# View ASCII sparkline price history
python3 scripts/price_predator.py history <product-id>

# Check for price drop alerts (all products)
python3 scripts/price_predator.py alert

# Check best time to buy by category
python3 scripts/price_predator.py best-time --category electronics

# Full report
python3 scripts/price_predator.py report
```

## Commands

| Command | Description |
|---------|-------------|
| `track` | Add a product to track (name + price + category + optional URL/target) |
| `update` | Record a new price observation for a tracked product |
| `history` | Show price history with ASCII sparkline chart |
| `alert` | Check for price drops exceeding threshold (>10% below median by default) |
| `best-time` | Predict best time to buy based on seasonal patterns by category |
| `report` | Full summary report of all tracked products |
| `list` | List all tracked products |
| `remove` | Remove a tracked product |
| `info` | Show detailed info about a product |

## How It Works

- **Database**: JSON file (`~/.price_predator_db.json` by default). Override with `--db`.
- **Price tracking**: Each `update` records price + timestamp + source. Build a history over time.
- **Alerts**: When the latest price drops more than the threshold (default 10%) below the median of all recorded prices, an alert fires.
- **Seasonal prediction**: Uses a built-in calendar of best months to buy each category (see `references/seasonal-buying-calendar.md`).
- **Depreciation**: Category-aware annual depreciation rates provide a rough price prediction model.

## Category-Aware Patterns

Price Predator knows seasonal discount windows for 15+ categories:

- **Electronics / TVs / Laptops** → Black Friday (Nov), Cyber Monday
- **Mattresses** → May (Memorial Day), February (Presidents' Day)
- **Appliances** → September (Labor Day), May (Memorial Day)
- **Smartphones** → September (new model launches), November (Black Friday)
- **Furniture** → January & July (inventory clearance)
- See `references/seasonal-buying-calendar.md` for the full calendar.

## Options

- `--db <path>` — Use a custom database file (global flag, before subcommand)
- `--target <price>` — Set a target buy price when tracking
- `--threshold <frac>` — Set alert threshold as a fraction (0.15 = 15%)
- `--category <cat>` — Set product category for seasonal predictions

## Files

- `scripts/price_predator.py` — Main script (Python stdlib only, no dependencies)
- `references/seasonal-buying-calendar.md` — Best months to buy each category
- `references/price-tracking-strategies.md` — Strategies for effective price tracking
