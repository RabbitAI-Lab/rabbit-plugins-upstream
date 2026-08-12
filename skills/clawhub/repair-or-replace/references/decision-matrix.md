# Decision Matrix — Scoring Algorithm

This document details the scoring algorithm used by `repair_or_replace.py`.

## Overview

The decision engine scores the item across five factors, each weighted to
reflect its importance in the repair-vs-replace decision. Factor scores are
normalized to 0-100, multiplied by their weight, and summed. The total
determines the recommendation.

## Factors and Weights

| Factor           | Weight | Range   | Higher = Repair |
| ---------------- | ------ | ------- | --------------- |
| Cost Ratio       | 30%    | 0-100   | Yes             |
| Remaining Life   | 25%    | 0-100   | Yes             |
| Condition        | 15%    | 0-100   | Yes             |
| Sentimental      | 10%    | 0-100   | Yes             |
| Environmental    | 20%    | 0-100   | Mixed           |

## Scoring Details

### 1. Cost Ratio (30%)

The ratio of repair cost to replacement cost:

```
cost_ratio = repair_cost / replacement_cost
```

| Cost Ratio | Score | Interpretation                       |
| ---------- | ----- | ------------------------------------ |
| 0-20%      | 100   | Repair is very cheap — definitely fix |
| 20-30%     | 90    | Repair is cost-effective              |
| 30-40%     | 75    | Repair is reasonable                  |
| 40-50%     | 60    | Borderline — consider other factors   |
| 50-60%     | 40    | Replace starts looking better         |
| 60-80%     | 20    | Replace is strongly favored           |
| 80-100%+   | 0     | Repair makes no financial sense       |

**Formula:** `score = max(0, min(100, 100 * (1 - cost_ratio / 0.5)))`

This creates a linear scale where a 50% ratio scores 50, and the score
decreases as the ratio increases.

### 2. Remaining Life (25%)

How much of the expected lifespan is left:

```
lifespan_used = age / expected_lifespan
remaining_pct = 1 - lifespan_used
```

| Lifespan Used | Score | Interpretation                           |
| ------------- | ----- | ---------------------------------------- |
| 0-25%         | 100   | Nearly new — lots of life left           |
| 25-50%        | 85    | Still in the prime of life               |
| 50-60%        | 65    | Past midpoint but functional             |
| 60-75%        | 40    | Entering failure-prone years             |
| 75-90%        | 20    | Near end of life                         |
| 90-100%+      | 5     | At or beyond expected lifespan           |

**Depreciation curve:** The score isn't linear because failure rates accelerate
in the last 25% of lifespan. A 50% penalty applies after 75% lifespan used.

### 3. Condition (15%)

Overall condition of the item beyond the current fault (user-supplied, 1-10):

```
normalized = condition_score / 10 * 100
```

| Condition (1-10) | Score | Meaning                          |
| ---------------- | ----- | -------------------------------- |
| 8-10             | 90-100| Excellent — like new             |
| 6-7              | 65-80 | Good — minor wear               |
| 4-5              | 40-55 | Fair — noticeable wear          |
| 1-3              | 10-30 | Poor — multiple issues          |

### 4. Sentimental Value (10%)

Emotional or irreplaceable value (user-supplied, 1-10):

| Sentimental (1-10) | Score | Meaning                        |
| ------------------ | ----- | ------------------------------ |
| 9-10               | 90-100| Irreplaceable (heirloom)       |
| 7-8                | 70-80 | Very meaningful                |
| 5-6                | 50-60 | Some attachment                |
| 3-4                | 30-40 | Minor attachment               |
| 1-2                | 10-20 | Purely functional              |

### 5. Environmental Impact (20%)

Two sub-factors:

**a) E-waste avoidance (12 of 20 points):**
Repairing avoids sending the item to landfill. Always favors repair.

**b) Energy efficiency of replacement (8 of 20 points):**
If the replacement is significantly more energy-efficient (user supplies
`--efficiency-gain` as a percentage), some points shift toward replace.

```
e_waste_score = 12  # always awarded for repair
efficiency_score = min(8, efficiency_gain_pct / 100 * 8)
environmental = e_waste_score + efficiency_score
```

If no efficiency data is provided, the full 20 points favor repair.

## Total Score and Recommendation

```
total = (cost_score * 0.30) + (life_score * 0.25) + (condition_score * 0.15)
      + (sentimental_score * 0.10) + (environmental_score * 0.20)
```

| Total Score | Recommendation | Confidence |
| ----------- | -------------- | ---------- |
| 70-100      | REPAIR         | High       |
| 55-69       | REPAIR         | Moderate   |
| 45-54       | BORDERLINE     | Low        |
| 31-44       | REPLACE        | Moderate   |
| 0-30        | REPLACE / RECYCLE | High    |

### Special Cases

- **Repair cost ≥ 80% of replacement + age > 75% of lifespan → RECYCLE**.
  The item is at end-of-life and repair isn't economical.
- **Sentimental score = 10 → always at least REPAIR (borderline)**, regardless
  of cost. Heirlooms deserve a chance.
- **Safety-critical items** (gas, electrical): If symptoms suggest a safety
  risk, the script adds a warning to consult a professional.

## Weight Rationale

- **Cost (30%)**: The dominant factor for most decisions. People care most
  about money.
- **Remaining Life (25%)**: Even a cheap repair isn't worth it if the item will
  fail again soon.
- **Environmental (20%)**: E-waste is a growing crisis. Giving it 20% ensures
  it's a real factor, not a tiebreaker.
- **Condition (15%)**: A well-maintained item deserves repair more than a
  neglected one.
- **Sentimental (10%)**: Real but shouldn't override economics for most items.
  Weighted enough to tip borderline cases.

## Customization

All weights are constants at the top of `repair_or_replace.py`. Adjust them to
match your priorities:

```python
WEIGHTS = {
    'cost': 0.30,
    'lifespan': 0.25,
    'condition': 0.15,
    'sentimental': 0.10,
    'environmental': 0.20,
}
```

For example, an environmentally-focused user might set `environmental: 0.35`
and `cost: 0.20`.
