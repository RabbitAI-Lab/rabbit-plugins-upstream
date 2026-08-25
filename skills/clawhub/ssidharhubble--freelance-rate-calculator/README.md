# Freelance Rate Calculator

Computes the hourly/day/project rate a freelancer needs to charge to hit a real take-home income target, accounting for unbillable hours, expenses, taxes, and margin.

## Why

ClawHub has freelance proposal generators, autobots, and income trackers, but nothing that answers the upstream question: what should I actually charge? Pricing built on a target take-home income (not a guessed market rate) is a distinct, missing piece.

## Usage

```bash
python3 scripts/rate_calc.py rate --target-income 100000 --billable-hours 25 --expenses 6000 --tax-rate 28
python3 scripts/rate_calc.py project --hourly-rate 95 --hours 40 --buffer 15
```

See `SKILL.md` for the full input reference.

## How it works

1. Grosses up the post-tax target income to the pre-tax revenue required, using your effective tax rate.
2. Adds annual business expenses and a profit/reinvestment margin.
3. Divides by realistic annual billable hours (work weeks × billable hours/week) to get the hourly rate.
4. `project` mode multiplies that rate by an hour estimate and adds a risk buffer for scope creep.

## Limitations

- Pricing math only — not tax, legal, or market-rate advice. It tells you what you need to charge to hit your target, not what the market will bear.
- Assumes a single blended tax rate; doesn't model bracket-by-bracket tax calculations or jurisdiction-specific rules.
