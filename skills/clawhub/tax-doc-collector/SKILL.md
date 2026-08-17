---
name: tax-doc-collector
version: 1.0.0
author: Denis Voronin
license: MIT
description: >
  Track deductible expenses year-round with smart categorization, receipt
  logging, and tax-ready export. Organizes by IRS schedule categories,
  estimates tax savings per deduction, flags audit risks, and generates
  Schedule C / Schedule A ready reports. Never scramble at tax time again.
tags:
  - taxes
  - finance
  - expenses
  - deductions
  - tax-prep
---

# Tax Doc Collector

A standalone command-line tool for tracking tax-deductible expenses throughout
the year. Instead of a shoebox of receipts in April, maintain a clean,
categorized, audit-ready expense log with real-time tax savings estimates.

## Quick Start

```bash
# Set your tax bracket
python3 scripts/tax_docs.py setup --bracket 24

# Log deductible expenses as they happen
python3 scripts/tax_docs.py add --amount 45.99 --category "office supplies" --merchant "Staples" --note "printer ink"
python3 scripts/tax_docs.py add --amount 120.00 --category "meals" --merchant "Business Lunch" --note "client meeting"
python3 scripts/tax_docs.py add --amount 250.00 --category "charity" --merchant "Red Cross"

# Add a mileage deduction
python3 scripts/tax_docs.py add-mileage --miles 45 --purpose "client visit"

# See your year-to-date summary
python3 scripts/tax_docs.py summary

# Check audit risk
python3 scripts/tax_docs.py audit-risk

# Export for tax filing
python3 scripts/tax_docs.py export schedule-c
python3 scripts/tax_docs.py export schedule-a
```

## Commands

| Command | Description |
|---------|-------------|
| `setup --bracket <percent>` | Set your marginal tax bracket |
| `add --amount <N> --category <cat> --merchant <name> [--note text] [--date YYYY-MM-DD]` | Log a deductible expense |
| `add-mileage --miles <N> --purpose <text> [--date YYYY-MM-DD]` | Log deductible mileage |
| `add-home-office --sqft <N>` | Calculate home office deduction |
| `summary [--year YYYY]` | Year-to-date deduction summary with tax savings |
| `by-category <category> [--year YYYY]` | Show all expenses in a category |
| `audit-risk [--year YYYY]` | Flag high audit-risk deductions |
| `export schedule-c [--year YYYY]` | Export Schedule C format |
| `export schedule-a [--year YYYY]` | Export Schedule A format |
| `export csv [--year YYYY]` | Export all data as CSV |
| `categories` | List all IRS categories with limits |
| `mileage-rate [--year YYYY]` | Show current IRS mileage rate |
| `list [--year YYYY] [--category cat]` | Browse logged expenses |
| `delete <id>` | Delete an expense |

## How It Works

### IRS Category Matching
Expenses are categorized into IRS-recognized categories:

**Schedule C (Self-employed / Business):**
- Advertising, Car/truck expenses, Commissions, Contract labor, Depletion
- Depreciation, Employee benefits, Insurance, Interest (mortgage/other)
- Legal/professional services, Office expenses, Pension/profit-sharing
- Rent/lease, Repairs/maintenance, Supplies, Taxes/licenses
- Travel/meals, Utilities, Wages, Other

**Schedule A (Itemized Personal):**
- Medical/dental, Taxes paid (state/local, property), Mortgage interest
- Charity (cash and non-cash), Casualty/theft losses, Miscellaneous

### Real-Time Tax Savings
Each expense instantly shows estimated tax savings:
```
Savings = Amount × Marginal Tax Rate
```

### Audit Risk Scoring
The system flags deductions that are statistically more likely to trigger
IRS scrutiny:
- Meals/entertainment exceeding norms
- Charitable donations exceeding 5% of typical income
- Home office deductions without corresponding income
- Vehicle expenses without mileage logs
- Large cash transactions

### Mileage Deductions
Uses current IRS standard mileage rates:
- 2024 Business: 67 cents/mile
- 2024 Medical/moving: 21 cents/mile
- 2024 Charity: 14 cents/mile

### Home Office
Calculates the simplified home office deduction ($5/sqft, max 300 sqft)
or detailed method (percentage of home expenses).

## Data Storage

Data is stored in `~/.tax_docs.json`. Sensitive — keep backups.

## References

- [IRS Deduction Categories](references/irs-categories.md)
- [Audit Risk Factors](references/audit-risk.md)

## License

MIT © Denis Voronin
