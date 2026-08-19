---
name: repair-or-replace
description: >
  Decide whether to fix, replace, or recycle a broken item. Takes item type,
  age, symptoms, and repair estimate, then produces a scored recommendation
  across cost, lifespan, sentimental value, and environmental impact.
version: 1.0.0
author: Denis Voronin
license: MIT
tags:
  - decision-making
  - consumer
  - repair
  - sustainability
  - cost-analysis
  - environment
---

# Repair or Replace

> Don't guess. Score it.

`Repair or Replace` is a skill that helps you decide whether to fix a broken
item, buy a replacement, or recycle it. It builds a weighted decision matrix
across five factors — repair cost, replacement cost, remaining lifespan,
sentimental value, and environmental impact — then outputs a clear,
score-backed recommendation with reasoning.

## When to Use

Activate this skill when:

- An appliance, device, or tool is broken and you're unsure whether to fix it
- You have a repair estimate and want to compare it against replacement
- You want to factor environmental impact into a purchasing decision
- You're helping someone else decide what to do with a broken item
- You want a structured, defensible decision rather than a gut call

## How It Works

The script takes structured input about the item and its condition:

| Parameter           | Description                                         | Example            |
| ------------------- | --------------------------------------------------- | ------------------ |
| `--item`            | What the item is                                    | "washing machine"  |
| `--age`             | How old it is (years)                               | `8`                |
| `--repair-cost`     | Estimated repair cost                               | `250`              |
| `--replacement-cost`| Cost of a new equivalent                            | `800`              |
| `--expected-lifespan`| Expected total lifespan of this item type (years)  | `12`               |
| `--symptoms`        | What's wrong (free text)                            | "won't spin"       |
| `--sentimental`     | Sentimental value (1-10)                            | `3`                |
| `--condition`       | Overall condition aside from the fault (1-10)      | `6`                |

It then scores the decision across five dimensions, applies weights, and
produces a recommendation: **Repair**, **Replace**, or **Recycle/Donate**.

## Decision Matrix

| Factor              | Weight | Repair Favors                          | Replace Favors                      |
| ------------------- | ------ | -------------------------------------- | ----------------------------------- |
| **Cost Ratio**      | 30%    | Repair < 50% of replacement            | Repair > 50% of replacement         |
| **Remaining Life**  | 25%    | <50% of expected lifespan used         | >50% of expected lifespan used      |
| **Condition**       | 15%    | Good condition otherwise               | Multiple issues, poor condition     |
| **Sentimental**     | 10%    | High sentimental value                 | Low sentimental value               |
| **Environmental**   | 20%    | Repair avoids e-waste                  | New item is more efficient           |

See `references/decision-matrix.md` for the full scoring algorithm.

## Quick Reference

| Need                              | Command                                                                     |
| --------------------------------- | --------------------------------------------------------------------------- |
| Basic decision                    | `python3 scripts/repair_or_replace.py --item "laptop" --age 5 --repair-cost 300 --replacement-cost 1000` |
| With symptoms and condition       | `python3 scripts/repair_or_replace.py --item "fridge" --age 10 --repair-cost 200 --replacement-cost 900 --symptoms "not cooling" --condition 4` |
| Factor in sentiment               | `python3 scripts/repair_or_replace.py --item "watch" --age 20 --repair-cost 150 --replacement-cost 500 --sentimental 9` |
| JSON output                       | `python3 scripts/repair_or_replace.py ... --format json`                    |
| Interactive mode                  | `python3 scripts/repair_or_replace.py --interactive`                        |

## Recommendations

The script outputs one of three recommendations:

- **Repair** — the item is worth fixing. Cost-effective, has remaining lifespan,
  or has sentimental/environmental value.
- **Replace** — buying new is the better choice. Repair cost is too high
  relative to replacement, or the item is near end-of-life.
- **Recycle/Donate** — the item is beyond economic repair. Dispose of it
  responsibly or donate if still partially functional.

Each recommendation includes a confidence score (0-100) and itemized reasoning.

## Files

- `references/decision-matrix.md` — full scoring algorithm and weight rationale
- `references/item-lifespans.md` — expected lifespan data for common items
- `references/environmental-impact.md` — e-waste and sustainability considerations
- `scripts/repair_or_replace.py` — the main decision engine
- `scripts/sample_run.sh` — example invocations for different item types

## Common Pitfalls

1. **Ignoring hidden repair costs.** The repair estimate often excludes
   diagnosis fees, shipping, or secondary issues discovered during repair. Add
   15-20% to the estimate for a realistic comparison.

2. **Overestimating remaining lifespan.** An 8-year-old washing machine with a
   12-year expected lifespan doesn't have 4 "good" years left — the last
   quarter of lifespan tends to have escalating failure rates.

3. **Forgetting energy efficiency.** A new appliance may be significantly more
   energy-efficient, saving money over time. Factor this into the replacement
   cost (see `references/environmental-impact.md`).

4. **Sentimental bias.** It's easy to over-value items with emotional
   attachment. Be honest with the `--sentimental` score.

5. **Not considering safety.** Some failures (gas appliances, electrical) carry
   safety risks if repaired poorly. If in doubt, replace.

## Verification Checklist

- [ ] Repair estimate is realistic (includes diagnosis, parts, labor)
- [ ] Replacement cost reflects a comparable-quality item
- [ ] Expected lifespan matches the item type (see `references/item-lifespans.md`)
- [ ] Condition score accounts for wear beyond the current fault
- [ ] Environmental factor considered (especially for large appliances)

## License

MIT © Denis Voronin
