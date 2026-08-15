---
name: utility-bill-analyzer
version: 1.0.0
author: Denis Voronin
license: MIT
description: Analyze electricity, water, and gas bills to detect anomalies, compare usage, forecast costs, and suggest savings.
category: productivity
---

# Utility Bill Analyzer

Track and analyze monthly utility bills (electricity, water, gas) to detect anomalies, compare year-over-year usage, forecast costs, and get actionable savings suggestions.

## Quick Start

```bash
# Record a bill
python3 scripts/bill_analyzer.py add --type electricity --date 2025-01-15 --usage 450 --cost 67.50

# View history with ASCII bar chart
python3 scripts/bill_analyzer.py history

# Compare same month across years
python3 scripts/bill_analyzer.py compare --month 01

# Detect usage spikes (>1.5× rolling average)
python3 scripts/bill_analyzer.py anomaly

# Forecast next bill based on seasonal patterns
python3 scripts/bill_analyzer.py forecast

# Full annual report with savings suggestions
python3 scripts/bill_analyzer.py report
```

All commands accept an optional `--type electricity|water|gas` filter (except `add`, which requires it) and `--db <path>` to specify a custom database file.

## Commands

| Command | Description |
|---------|-------------|
| `add` | Record a new bill (type, date, usage, cost) |
| `history` | Show usage/cost trend with ASCII bar chart |
| `compare` | Compare same month across different years |
| `anomaly` | Detect bills where usage exceeds 1.5× the rolling average |
| `forecast` | Predict next bill based on seasonal averages and recent trend |
| `report` | Annual summary with seasonal breakdown, year-over-year comparison, and savings suggestions |

## Data Storage

Bills are stored in `scripts/bills.json` (configurable with `--db`). Each record:

```json
{
  "type": "electricity",
  "date": "2025-01-15",
  "month": 1,
  "year": 2025,
  "usage": 450,
  "cost": 67.50,
  "cpu": 0.15,
  "season": "winter"
}
```

## Features

- **Anomaly Detection**: Flags bills where usage exceeds 1.5× the 3-bill rolling average, with season-aware explanations (winter heating, summer AC).
- **Seasonal Patterns**: Recognizes winter/spring/summer/autumn usage patterns and reports seasonal averages.
- **Cost per Unit Tracking**: Tracks effective rate ($/kWh, $/m³) over time to distinguish rate increases from usage increases.
- **ASCII Bar Chart**: Visual usage trend directly in the terminal.
- **Forecasting**: Predicts next bill using historical same-month data (preferred) or recent average.
- **Savings Suggestions**: Generates type-specific tips based on detected patterns (high winter usage, rate increases, etc.).

## References

- `references/utility-savings-checklist.md` — 108 actionable savings tips by category
- `references/rate-analysis-guide.md` — How to read utility bills, spot billing errors, compare plans
