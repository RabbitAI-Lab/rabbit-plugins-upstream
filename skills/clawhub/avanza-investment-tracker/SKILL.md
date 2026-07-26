---
name: avanza-investment-tracker
description: "Process Avanza CSV exports, calculate TWRR/Modified Dietz returns, and track portfolio performance. Use when importing stock transactions, calculating investment returns, or managing portfolio data."
---

# Avanza Investment Tracker

Parse transaction CSVs and compute portfolio performance metrics.

## Quick Start

Run commands from your workspace root, specifying the paths to your database and CSV:

```bash
# 1. Import new transactions
python path/to/cli.py --database data/asset_data.db import path/to/transactions.csv

# 2. Update price cache and show statistics
python path/to/cli.py --database data/asset_data.db stats --update-prices auto

# 3. View portfolio allocation and APY
python path/to/cli.py --database data/asset_data.db portfolio --account default
```

## Data Storage Pattern

**User data lives OUTSIDE the skill directory.** Recommended structure:

```
workspace-finance/
├── skills/avanza-investment-tracker/   # Portable skill logic
│   ├── SKILL.md
│   ├── scripts/
│   └── assets/
└── data/avanza/                        # Private portfolio data
    ├── transactions.csv
    ├── special_cases.json
    └── asset_data.db
```

## CLI Reference

| Command | Description |
| :--- | :--- |
| `python scripts/cli.py import FILE [--allocate-virtual] [--allow-unsettled]` | Import transaction entries from Avanza CSV (auto-allocate buys to virtuals; defers unsettled/pending-nota trades — see CSV Format Support) |
| `python scripts/cli.py stats [OPTIONS]` | Calculate and display cohort performance statistics (TWRR, deposits) |
| `python scripts/cli.py accounts [OPTIONS]` | Display summary of all accounts with asset values and cash |
| `python scripts/cli.py portfolio [OPTIONS]` | Show portfolio holdings, market value, allocation %, and APY (alias to `stats --positions --summary`) |
| `python scripts/cli.py status` | Display system status (transaction counts, price dates, date range) |
| `python scripts/cli.py settings SUBCOMMAND` | Configure defaults and account nicknames |
| `python scripts/cli.py reset [--hard]` | Reset database state (`--hard` deletes data; default only marks unprocessed) |
| `python scripts/cli.py delete-tx [OPTIONS]` | Delete individual transaction(s) by `--tx-id`, `--date`+`--asset`, or `--since`, then rebuild derived tables (see below) |
| `python scripts/cli.py account SUBCOMMAND` | Manage accounts — virtual sub-portfolios (create/allocate/transfer/list/close/delete) and nicknames (see below) |
| `python scripts/cli.py report [OPTIONS]` | Investment report with a virtual-portfolio section and a virtual-vs-parent-vs-benchmark comparison |

### Deleting transactions

`delete-tx` removes specific real transactions and rebuilds the derived `assets` / cohort tables, so there is no need to `reset` the whole database after a bad import (e.g. a duplicate, or a row that slipped in before an unsettled trade was deferred). Targeting is mutually exclusive:

- `delete-tx --tx-id ROWID` — most precise (use `status`/`export` to find the rowid).
- `delete-tx --date YYYY-MM-DD --asset "Name" [--account ACCOUNT]` — the common surgical case.
- `delete-tx --since YYYY-MM-DD [--account ACCOUNT]` — remove everything from a date onward (e.g. undo today's import).

`--cascade` widens a `--date`+`--asset` match across the account family (parent + its virtuals) so a trade and its allocated split are removed together; `--dry-run` previews the deletion. When an allocated buy on a virtual is deleted, its orphaned funding `Intern överföring` transfer is removed automatically (mirroring `account allocate --undo`). After every deletion all transactions are reprocessed, so the `assets`/cohort tables always reflect the remaining transactions — never a half-deleted state.

### Global Options
- `--database PATH` (default: `data/asset_data.db`)
- `--special-cases PATH` (default: `data/special_cases.json`)

### Calculation & Output Options
- `--account ACCOUNTS`: Limit to specific accounts (e.g. `12345,67890`, `default`, or `all`). Omitting the flag (default) shows **physical accounts only** (excludes virtual portfolios); pass `all` to include virtual portfolios in aggregates.
- `--update-prices {auto,always,never}` (stats only): Controls when to fetch latest stock/fund prices from Avanza API
- `--update-all` (stats only): Update prices for all assets in the database, held or not
- `--as-of DATE`: View snapshot/stats as of a historical date (`YYYY-MM-DD`)
- `--cohorts-start DATE --cohorts-end DATE`: Filter which deposit cohorts are displayed
- `--cohort DATE`: Shorthand to filter by a single cohort month (`YYYY-MM`) or year (`YYYY`) (e.g. `--cohort 2024` groups yearly, `--cohort 2024-12` groups monthly)
- `--from DATE --to DATE`: Set the performance valuation window (double snapshot)
- `--positions`, `-p` (stats only): Show positions holdings breakdown under each cohort (or summary)
- `--summary`, `-s` (stats only): Consolidate cohort statistics into a single overview block
- `--apy-mode {mwrr,twrr}`: APY calculation method (`mwrr` uses Modified Dietz; `twrr` uses Time-Weighted)
- `--format {table,json}`: Output formatting (default: `table`)
- `--quiet`, `-q`: Suppress price data staleness warnings
- `--no-interpolation`: Disable linear interpolation for sparse historical price data (falls back to nearest prior price, which may trigger staleness warnings)
- `--risk`: Calculate and display portfolio-level risk metrics (Annualized Standard Deviation, Sharpe Ratio, Sortino Ratio, Maximum Drawdown with peak/trough calendar months)
- `--beta [TICKER]`: Include the portfolio Beta calculation vs the specified benchmark (e.g. `^OMXSPI`, `ACWI`). Defaults to `^OMXSPI` if the flag is passed without a ticker value. Specifying `--beta` automatically enables risk metrics.

### Guidelines: When to use what date boundaries
1. **To see how cohorts from a certain period look today:**
   Use `--cohorts-start YYYY-MM` / `--cohorts-end YYYY-MM`
   *Example:* `python scripts/cli.py stats --cohorts-start 2024-01`
2. **To see all cohorts' performance over a specific valuation window:**
   Use `--from YYYY-MM` / `--to YYYY-MM` (or `--as-of YYYY-MM`)
   *Example:* `python scripts/cli.py stats --from 2024-01 --to 2024-12`
3. **To see only a single cohort month or year:**
   Use `--cohort YYYY-MM` or `--cohort YYYY`
   *Example:* `python scripts/cli.py stats --cohort 2024-12` (sets date range to `2024-12` and default grouping to monthly)
   *Example:* `python scripts/cli.py stats --cohort 2024` (sets date range to `2024-01` to `2024-12` and default grouping to yearly)

> [!NOTE]
> In double-snapshot mode (`--from` / `--to`), the cohort-level output displays **`Start Value`** instead of **`Deposited`** for any cohorts created before the start date. Additionally, the **`Withdrawal`** line displays withdrawals made *specifically within the selected date range*, while withdrawals made prior to the start date are already accounted for in `Start Value`.

### Settings Subcommands
- `default-accounts ACCOUNTS`: Set default accounts (comma-separated list of IDs, or `all`)
- `default-stats-period {month,year}`: Set default period for performance reports


## Special Cases

Corporate actions (splits, spin-offs, zero-priced deposits) can be overridden by copying the template and defining rules:
```bash
cp assets/special_cases_template.json ../data/avanza/special_cases.json
```


## See Also

- **Detailed workflows**: [references/workflows.md](references/workflows.md)
- **Troubleshooting guide**: [references/troubleshooting.md](references/troubleshooting.md)
