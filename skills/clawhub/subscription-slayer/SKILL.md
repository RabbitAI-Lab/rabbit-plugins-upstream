---
name: subscription-slayer
description: >
  Tracks subscriptions, calculates monthly and annual costs, detects likely-unused
  services based on last-used patterns, and generates ready-to-send cancellation
  email templates. Helps users stop wasting money on forgotten subscriptions.
version: 1.0.0
author: Denis Voronin
license: MIT
tags:
  - subscriptions
  - finance
  - budgeting
  - money-saving
  - cancellation
---

# Subscription Slayer

Find and slay the subscriptions draining your wallet every month.

## When to use

- The user wants to audit their recurring subscriptions.
- The user wants to know how much they spend monthly/yearly on subscriptions.
- The user suspects they're paying for services they don't use.
- The user wants to cancel a subscription and needs a cancellation email.

## How it works

1. Receive a list of subscriptions as JSON (see format below).
2. Run `scripts/subscription_tracker.py analyze subs.json` to get:
   - Monthly and annual cost totals
   - Each subscription ranked by **waste probability** (how likely it's unused)
   - Ready-to-send cancellation email templates for high-waste subscriptions
3. The agent presents the analysis and offers to generate/send cancellation emails.

## Subscription JSON Format

```json
[
  {
    "name": "Netflix",
    "cost": 15.49,
    "billing_cycle": "monthly",
    "category": "entertainment",
    "last_used": "2024-01-15",
    "start_date": "2022-03-01",
    "auto_renew": true,
    "cancel_url": "https://www.netflix.com/cancel"
  },
  {
    "name": "Adobe Creative Cloud",
    "cost": 54.99,
    "billing_cycle": "monthly",
    "category": "software",
    "last_used": "2023-06-01",
    "start_date": "2021-01-15",
    "auto_renew": true,
    "cancel_url": "https://account.adobe.com"
  }
]
```

### Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | ✅ | Subscription name |
| `cost` | ✅ | Cost per billing cycle |
| `billing_cycle` | ✅ | "monthly", "yearly", "weekly", "quarterly" |
| `category` | ❌ | Entertainment, software, news, fitness, etc. |
| `last_used` | ❌ | ISO date of last use (for waste detection) |
| `start_date` | ❌ | When the subscription started |
| `auto_renew` | ❌ | Whether it auto-renews (default true) |
| `cancel_url` | ❌ | URL to manage/cancel the subscription |
| `notes` | ❌ | Free text notes |

## Usage

```bash
# Analyze subscriptions
python3 scripts/subscription_tracker.py analyze subs.json

# JSON output
python3 scripts/subscription_tracker.py analyze subs.json --json

# Generate cancellation emails for high-waste subscriptions
python3 scripts/subscription_tracker.py cancel subs.json --name "Netflix"

# Generate cancellation emails for all high-waste subscriptions
python3 scripts/subscription_tracker.py cancel subs.json --threshold 70

# Show only subscriptions above a waste threshold
python3 scripts/subscription_tracker.py analyze subs.json --threshold 50

# Run demo with sample data
python3 scripts/subscription_tracker.py demo
```

## Waste Detection

The waste probability score (0–100) is calculated from:

| Factor | Weight | Logic |
|--------|--------|-------|
| Days since last use | 40% | >90 days unused = high waste signal |
| Cost vs. usage frequency | 25% | Expensive + rarely used = waste |
| Subscription age | 15% | Very old subs you forgot about |
| Auto-renew status | 10% | Auto-renewing = easy to forget |
| Category tendencies | 10% | Some categories are more forgettable |

**Score interpretation:**
- **80–100**: Almost certainly wasting money. Cancel now.
- **60–79**: Likely unused. Strong cancellation candidate.
- **40–59**: Possibly underutilised. Review.
- **0–39**: Probably in use. Keep.

## Cancellation Emails

The script generates ready-to-send email templates with:
- Subject line
- Formal cancellation request
- Account identification placeholders
- Request for confirmation
- Legal phrasing (effective date, pro-rated refunds)

## Files

- `scripts/subscription_tracker.py` — main analysis and email generation script
- `references/waste_detection.md` — detailed scoring methodology
- `references/cancellation_template.md` — email template reference
