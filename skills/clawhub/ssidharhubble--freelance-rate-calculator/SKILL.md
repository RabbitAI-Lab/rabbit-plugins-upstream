---
name: freelance-rate-calculator
description: Compute the hourly rate, day rate, and monthly revenue target a freelancer needs to hit a specific take-home income, correctly accounting for unbillable hours, business expenses, self-employment tax, and profit margin — then convert that hourly rate into a fixed-price project quote with a scope-creep risk buffer. Built for freelancers, consultants, and AI agent operators pricing their own or an agent's billable time. Fills a gap next to freelance-proposal and freelance-income-tracking skills, which help you find and log work but don't tell you what to actually charge. Pure Python, no external API or account required.
compatibility: Created for Zo Computer
metadata:
  author: ssyopros.zo.computer
allowed-tools: Bash
---

# Freelance Rate Calculator

Two calculators in one CLI: (1) target income → recommended hourly/day/monthly rate, correctly grossing up for taxes and grossing down for realistic billable hours, and (2) hourly rate + hour estimate → a fixed-price project quote with a risk buffer for scope creep.

## When to use

- Setting or re-evaluating your freelance hourly rate against a real income target
- Sanity-checking whether a client's offered rate actually clears your target take-home
- Converting an hourly rate into a fixed-bid project price before sending a proposal
- Pricing AI agent labor / bounty work against a target revenue goal

## Commands

```bash
python3 scripts/rate_calc.py rate --target-income 100000 \
    --work-weeks 48 --billable-hours 25 --expenses 6000 --tax-rate 28 --margin 10

python3 scripts/rate_calc.py project --hourly-rate 95 --hours 40 --buffer 15

python3 scripts/rate_calc.py rate --target-income 100000 --json   # machine-readable
```

## Key inputs and why they matter

- `--billable-hours`: hours you can realistically *bill*, not total hours worked. Most freelancers bill 50-60% of a working week once admin, sales, and unpaid overhead are excluded — defaulting to 25/week assumes a ~40-50h working week.
- `--tax-rate`: effective rate (self-employment + income tax combined) used to gross the post-tax target up to required pre-tax revenue.
- `--margin`: buffer/reinvestment on top of break-even, not pure profit — covers slow months, tools, and growth.
- `--buffer` (project mode): risk margin for underestimated hours and scope creep on fixed-price work.

## Output

`rate` mode: recommended hourly rate, 8-hour day rate, weekly and monthly revenue targets, plus the pre-tax revenue figure the math is built from. `project` mode: base project price and the buffered recommended quote.

## Notes

- Pure Python, zero dependencies, no external API calls — works fully offline.
- This is a pricing calculator, not tax or legal advice; effective tax rates vary by jurisdiction and entity structure, so confirm your real rate with a tax professional.
