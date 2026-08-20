---
name: home-inventory
description: >
  Document everything you own for insurance, moving, or estate planning.
  Manage a JSON database of household items with depreciation tracking,
  insurance-ready reports, and moving box labeling.
version: 1.0.0
author: Denis Voronin
license: MIT
metadata:
  hermes:
    tags:
      - inventory
      - insurance
      - home
      - moving
      - estate-planning
      - documentation
---

# Home Inventory

Track everything you own — for insurance claims, moving logistics, or estate planning.

## Quick Start

```bash
# Add an item
python scripts/inventory.py add \
  --name "MacBook Pro" \
  --category "electronics" \
  --room "office" \
  --value 2400 \
  --brand "Apple" \
  --model "MacBook Pro 14 M3" \
  --serial "C02XK1234ABC" \
  --purchase-date "2024-03-15" \
  --notes "AppleCare+ until 2027"

# List all items
python scripts/inventory.py list

# Search by keyword
python scripts/inventory.py search "MacBook"

# Items in a specific room
python scripts/inventory.py by-room kitchen

# Total value of everything
python scripts/inventory.py total-value

# Export to CSV (for spreadsheets / insurance upload)
python scripts/inventory.py export-csv --output inventory.csv

# Insurance report (replacement cost, room-by-room breakdown)
python scripts/inventory.py insurance-report

# Depreciation report (current vs purchase value by category)
python scripts/inventory.py depreciation-report

# Assign items to moving boxes and generate box manifests
python scripts/inventory.py assign-box --item-id 3 --box "BOX-001"
python scripts/inventory.py box-manifest BOX-001
```

## Data Storage

All items are stored in `inventory.json` (configurable via `--db`). Each item has:

| Field           | Description                         |
|-----------------|-------------------------------------|
| id              | Auto-incremented unique ID          |
| name            | Item name                           |
| category        | electronics, furniture, jewelry, …  |
| room            | Where the item lives                |
| purchase_date   | ISO date (YYYY-MM-DD)               |
| estimated_value | Current replacement value (float)   |
| brand_model     | Manufacturer and model              |
| serial_number   | Serial number for ID/claims         |
| photo_path      | Path to a photo of the item         |
| qr_label_id     | QR label identifier                 |
| box_id          | Moving box assignment               |
| notes           | Free-text notes                     |

## Depreciation Model

Depreciation rates are defined by category in `references/depreciation-tables.md`:

- **Electronics**: fast depreciation (~25%/yr, ~5yr lifespan)
- **Furniture**: slow depreciation (~8%/yr, ~15yr lifespan)
- **Appliances**: moderate (~12%/yr, ~10yr lifespan)
- **Clothing**: fast (~20%/yr, ~5yr lifespan)
- **Jewelry**: appreciates (~3%/yr)
- **Art/Collectibles**: appreciates (~5%/yr)

See `references/depreciation-tables.md` for full details.

## Insurance Reports

The insurance report provides:
- Total replacement cost across all items
- Room-by-room breakdown
- Category subtotals
- High-value item flags (>$1,000)

See `references/insurance-claims-guide.md` for claim documentation best practices.

## Moving Box System

- Assign items to boxes with `assign-box`
- Generate QR-friendly manifests with `box-manifest`
- Each manifest lists all items, total value, and a compact QR-encodable summary
