---
name: receipt-raccoon
description: >
  Extracts structured data from receipt text (OCR/photo description) and generates
  monthly spending reports. Parses merchant, date, line items, tax, total, and
  category. Produces summary stats: top merchants, category breakdown, total spend.
version: 1.0.0
author: Denis Voronin
license: MIT
tags:
  - receipts
  - expense-tracking
  - finance
  - ocr
  - budgeting
---

# Receipt Raccoon

Never manually enter receipt data again. Feed it receipt text and get clean structured data out.

## When to use

- The user provides receipt text from OCR, a photo description, or copy-paste.
- The user wants to track expenses from receipts.
- The user wants a monthly or category-based spending summary.
- The user wants to export receipt data as structured JSON.

## How it works

1. Receive raw receipt text (multiline string).
2. Run `scripts/receipt_parser.py parse --text "..."` or pipe via stdin.
3. The script extracts: merchant name, date, line items with prices, subtotal, tax, total.
4. Each item is categorised using keyword matching (groceries, dining, electronics, etc.).
5. Store parsed receipts in a JSONL ledger file for accumulation.
6. Run `scripts/receipt_parser.py report --ledger receipts.jsonl` to generate summary stats.

## Usage

### Parse a single receipt

```bash
# From command line argument
python3 scripts/receipt_parser.py parse --text "$(cat receipt.txt)"

# From stdin
cat receipt.txt | python3 scripts/receipt_parser.py parse

# From a file
python3 scripts/receipt_parser.py parse --file receipt.txt
```

### Accumulate receipts

```bash
# Parse and append to a ledger
python3 scripts/receipt_parser.py parse --file receipt.txt --append receipts.jsonl
```

### Generate reports

```bash
# Summary of all receipts in ledger
python3 scripts/receipt_parser.py report --ledger receipts.jsonl

# Filter by month
python3 scripts/receipt_parser.py report --ledger receipts.jsonl --month 2024-01

# JSON output
python3 scripts/receipt_parser.py report --ledger receipts.jsonl --json
```

### Output format

Parsed receipt JSON:
```json
{
  "merchant": "WHOLE FOODS MARKET",
  "date": "2024-01-15",
  "items": [
    {"name": "ORGANIC BANANAS", "price": 2.99, "category": "groceries"},
    {"name": "ALMOND MILK", "price": 3.49, "category": "groceries"}
  ],
  "subtotal": 6.48,
  "tax": 0.52,
  "total": 7.00,
  "currency": "USD"
}
```

Report output includes:
- Total spend, receipt count, average receipt
- Top merchants by spend
- Category breakdown with percentages
- Monthly trend
- Tax total

## Categorisation

Items are categorised using keyword matching against these categories:

| Category | Example keywords |
|----------|-----------------|
| Groceries | milk, bread, eggs, vegetable, fruit, meat, cheese |
| Dining | burger, pizza, coffee, restaurant, cafe, taco |
| Electronics | cable, charger, battery, phone, laptop, usb |
| Clothing | shirt, pants, shoes, dress, jacket |
| Health | pharmacy, medicine, vitamin, bandage |
| Household | soap, detergent, paper, cleaning |
| Transport | gas, fuel, uber, taxi, parking |
| Entertainment | movie, ticket, game, concert |
| Other | (fallback) |

## Files

- `scripts/receipt_parser.py` — main parser and report generator
- `references/categories.md` — full category keyword reference
- `references/receipt_formats.md` — notes on supported receipt formats
