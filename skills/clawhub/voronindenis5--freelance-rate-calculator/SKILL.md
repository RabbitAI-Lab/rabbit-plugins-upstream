---
name: freelance-rate-calculator
description: "Calculate a sustainable freelance or contract hourly rate that survives taxes, unpaid non-billable time, bench months, self-funded benefits, and overhead — then price fixed-bid projects safely. Use when the user is going freelance, quoting an hourly rate or project price, evaluating whether a client's offered rate pays enough, deciding between freelance and a salaried job, or raising existing rates."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [freelance, pricing, rates, contracting, self-employment, career]
---

# Freelance Rate Calculator

Freelancers systematically underprice. They anchor on `salary ÷ 2080`, forget that only ~60% of hours are billable, that both halves of payroll tax land on them, that vacation and health insurance are self-funded, and that contracts end. The result is being broke while busy. This skill runs the real math: target take-home → sustainable hourly rate → safe fixed-bid quotes.

## Overview

`scripts/freelance_rate.py` (offline, stdlib-only) answers four questions that keep freelancers up at night:

- **`rate`** — "I need $70k take-home: what's my hourly rate?" Full breakdown: tax gross-up, overhead, benefits load, billable ratio, bench cushion → hourly / day / weekly rates
- **`salary`** — "I'm leaving a $95k job: what rate replaces it?" (Spoiler: not $45.67/h. It's ~2.4× that once benefits and taxes are honest.)
- **`check`** — "A client offers $60/h — what does that actually pay?" Reverse-engineers the offered rate into annual/monthly net and equivalent salaried pay, and flags shortfalls against your minimum
- **`project`** — "This looks like 60 hours: what do I quote fixed-bid?" Hours × rate × risk buffer (+ rush premium), with effective-rate exposure if scope creeps

Every assumption (billable ratio 60%, 46 workweeks, SE tax 15.3%, income tax 18%, 1 bench month) is documented and overridable per flag.

## When to Use

- User is going freelance / taking a first contract and asks "what should I charge?"
- Quoting an hourly rate to a client or recruiter
- Evaluating an offered rate ("is $65/h good?")
- Pricing a fixed-bid project (hours estimate → safe quote)
- Deciding between freelancing and a salaried offer
- Annual rate review / raising rates ("my costs went up 10%")

**Don't use for:** salaried offer negotiation (that's salary-negotiator territory — different tax/overhead shape), or formal tax filing (estimates only; a CPA does the real numbers).

## How It Works

1. **Tax gross-up**: `keep_ratio = 1 − income_tax − SE_tax × 0.9235` (SECA deduction folded in). Revenue must be `net ÷ keep_ratio` before personal take-home.
2. **Costs stack**: overhead (software, hardware, insurance, CPA) + benefits load (health premiums, retirement you self-fund) add to required revenue.
3. **Billable reality**: working year = 46 weeks × 40 h; only the billable ratio (default 60% — sales, admin, learning are unpaid) produces revenue. Bench months shrink it further.
4. **Rate** = required revenue ÷ billable hours. Day/weekly rates derive from it.
5. **Fixed-bid safety**: quote = hours × (1 + risk buffer 15%) × rate, +25% rush premium, optionally capped by client value ceiling — with the effective hourly rate shown if the estimate slips.

## Quick Start

```bash
# The rate that nets you $70k with honest costs
python3 scripts/freelance_rate.py rate --target-net 70000 \
  --overhead 4000 --benefits 9600

# Leaving a $95k job? The replacement rate
python3 scripts/freelance_rate.py salary --salary 95000 --benefits 9600

# Is $60/h enough? (checks against $70k minimum)
python3 scripts/freelance_rate.py check --rate 60 --min-net 70000 --benefits 9600

# Fixed-bid quote for a ~60h project
python3 scripts/freelance_rate.py project --hours 60 --rate 115 --rush

python3 scripts/freelance_rate.py demo
```

## Steps (Agent Workflow)

1. Establish the target: desired take-home, or the salary being replaced.
2. Gather honest costs: annual software/tools, insurance, health premiums, retirement contributions, expected gap months.
3. Run `rate` (or `salary`). Sanity-check the billable ratio — new freelancers sell less (0.50); established ones with repeat clients bill more (0.70).
4. If a client named a number, run `check` with `--min-net` to see the shortfall and the rate actually needed.
5. For fixed bids, run `project` — never quote estimate × rate without the buffer.
6. Raise annually: rerun `rate` with the new target; communicate increases 30 days ahead, grandfathering current clients one quarter.

## Output Shape

```
FREELANCE RATE CALCULATOR
==================================================================
  Target take-home:        $70,000/yr
  Tax keep-ratio:          67.9% of revenue is yours
  Gross needed (taxes):    $103,138
  Overhead + benefits:     $13,600/yr
  Revenue needed:          $116,738

  Working year:            46w × 40h = 1,840h total
  Billable ratio:          60% → 1,012h billable
  Bench cushion:           1.0 months folded in

  ══ HOURLY RATE: $115.35/h ══
  Day rate (8h):  $923
  Weekly rate:    $2,768
```

## Common Pitfalls

1. **Anchoring on `salary ÷ 2080`.** A $95k job is $45.67/h — but that number comes with health insurance, 7% employer payroll, paid leave, and zero sales admin. The honest replacement is ~2.4× naive. `salary` computes it.
2. **Assuming 40 billable hours/week.** Invoices only cover ~60% (industry norm 50–70%): proposals, invoicing, taxes, learning, and sales are real hours. Override with `--billable-ratio`, but don't override reality.
3. **Forgetting bench months.** Contracts end. One unpaid month per year must be priced into the other eleven — `--bench-months` (default 1.0).
4. **Quoting fixed-bid at estimate × rate.** Estimates slip; scope creeps. The 15% buffer is not optional padding, it's the price of certainty. `project` adds it (and +25% for rush jobs).
5. **Ignoring benefits load.** Health insurance ($6–15k/yr in the US) and retirement matching come out of your revenue now. `--benefits` makes the rate honest.
6. **Discounting "to win the client."** A below-floor rate wins a client you'll resent. If you must discount, discount scope, never the rate.
7. **Never re-raising.** Costs rise ~3-5%/yr. Review the rate every year and communicate increases 30 days out — churn is cheaper than a decade of underpricing.

## Verification Checklist

- [ ] Target net (or replaced salary) explicitly stated
- [ ] Overhead + benefits entered honestly (not 0 by default bias)
- [ ] Billable ratio matches your sales reality (0.50 new, 0.70 established)
- [ ] Bench months reflect your contract pipeline
- [ ] Fixed quotes include risk buffer; rush work carries premium
- [ ] Offered rates checked with `check --min-net` before accepting
- [ ] Estimates are planning aids, not tax advice — CPA does the filing

## One-Shot Recipes

**"First freelance gig, recruiter asks my rate tomorrow"**
```bash
python3 scripts/freelance_rate.py salary --salary 85000 --benefits 9000
# → quote the computed number, rounded up to nearest $5
```

**"Client says their budget is $75/h; I need $80k net"**
```bash
python3 scripts/freelance_rate.py check --rate 75 --min-net 80000
# → see the shortfall; counter at the computed needed rate or trim scope
```

**"Scope agreed: ~80 hours of work, they want fixed price"**
```bash
python3 scripts/freelance_rate.py project --hours 80 --rate 110 --buffer 0.20
# → quote with 20% buffer; keep the change-order script ready
```

## References

- [`references/rate-theory.md`](references/rate-theory.md) — the economics: billable ratio benchmarks, tax gross-up math, value vs hourly pricing, negotiation scripts
