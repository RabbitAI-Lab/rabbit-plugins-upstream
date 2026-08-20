---
name: expiry-tracker
description: "Track food expiry dates from grocery receipts. Get daily alerts before food goes bad, 'use this today' suggestions, and reduce food waste. Scan receipts or add items manually."
version: 1.0.0
author: Denis Voronin
license: MIT
metadata:
  hermes:
    tags: [food, expiry, grocery, waste-reduction, household, tracker]
    related_skills: [leftover-chef, receipt-raccoon]
---

# Expiry Tracker

## Overview

Food waste is a massive problem — the average household throws away 30% of the food they buy. Most of it spoils simply because people forget what's in the fridge and when it expires.

Expiry Tracker solves this by maintaining a simple inventory of perishable items with their expiry dates, then proactively suggesting what to cook before things go bad.

## When to Use

- After grocery shopping — add items to track
- Daily check — "what expires soon?"
- Before cooking — "what should I use today?"
- When planning meals for the week
- Before traveling — check what needs to be consumed first

**Don't use for:** Non-perishables (pasta, rice, canned goods with 1+ year shelf life), frozen items (unless thawing).

## Commands

```bash
# Add an item
python scripts/expiry_tracker.py add "milk" --days 7
python scripts/expiry_tracker.py add "chicken breast" --expiry 2026-08-15

# List items expiring soon
python scripts/expiry_tracker.py list --days 3

# Get today's "use this first" suggestions
python scripts/expiry_tracker.py today

# Remove consumed/expired item
python scripts/expiry_tracker.py remove "milk"

# Show full inventory sorted by expiry
python scripts/expiry_tracker.py inventory

# Weekly summary / waste report
python scripts/expiry_tracker.py report

# Bulk add from receipt text
python scripts/expiry_tracker.py batch "milk, eggs, bread, chicken, yogurt"
```

## How It Works

1. Items are stored in `~/.expiry_tracker.json` — a simple JSON database
2. Each item has: name, category, purchase date, expiry date, quantity, optional note
3. Default shelf life is inferred from category (dairy=7d, meat=3d, bread=5d, etc.)
4. `today` command shows items expiring within 48h, sorted by urgency
5. `report` shows waste statistics: how much expired vs consumed

## Default Shelf Life by Category

| Category | Days | Examples |
|----------|------|----------|
| Dairy | 7 | Milk, yogurt, cheese |
| Meat | 3 | Chicken, beef, pork, fish |
| Produce-Leafy | 4 | Spinach, lettuce, herbs |
| Produce-Root | 14 | Carrots, potatoes, onions |
| Produce-Fruit | 7 | Berries, bananas, apples |
| Bakery | 5 | Bread, pastries, tortillas |
| Deli | 5 | Cold cuts, prepared salads |
| Eggs | 21 | Eggs |
| Condiments | 180 | Opened sauces, dressings |
| Tofu | 7 | Tofu, tempeh |

## Common Pitfalls

1. **Forgetting to remove consumed items.** Always run `remove` when you eat something, otherwise the waste report is inaccurate.

2. **Overly optimistic expiry dates.** "Best before" ≠ "goes bad on." Use smell/visual check before tossing. The tracker errs on the side of caution.

3. **Not adding items on shopping day.** The tracker is only as good as its data. Make it a habit to batch-add after unpacking groceries.

4. **Ignoring the `today` command.** Set up a daily cron/reminder to check it every morning.

## Verification Checklist

- [ ] Database file created at `~/.expiry_tracker.json`
- [ ] `add` command works with both `--days` and `--expiry` flags
- [ ] `list --days 3` shows only items expiring within 3 days
- [ ] `today` shows actionable suggestions
- [ ] `report` shows waste statistics
- [ ] `batch` mode parses comma-separated items correctly
