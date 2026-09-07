---
name: knitting-pattern-solver
description: "Parse, decode, and expand written knitting patterns. Translates abbreviations, calculates yarn requirements from gauge, tracks stitch counts across rows, and generates row-by-row instructions from condensed pattern notation. Use when a knitter needs help understanding, planning, or tracking a knitting project."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [knitting, crafts, patterns, yarn, diy, crafting]
---

# Knitting Pattern Solver

## Overview

Knitting patterns are written in dense shorthand — `k2, p2, *k2tog, yo, rep from * to last 4 sts` — that's impenetrable to beginners and error-prone even for experts. Row counts get miscounted, yarn runs out mid-project, and pattern repeats are easy to botch. This skill decodes that notation into plain-English instructions, calculates exactly how much yarn a project needs based on a gauge swatch, tracks your progress row by row, and flags stitch-count errors before they compound.

## When to Use

- A user is **following a written knitting pattern** and needs it expanded into row-by-row instructions
- A user needs to **calculate yarn requirements** before starting (or buying) for a project
- A user wants to **verify their stitch count** per row matches the pattern's expected count
- A user is **substituting yarn** and needs to recalculate yardage for a different weight
- A user is **designing their own pattern** and wants to verify the repeat math
- **Don't use for:** crochet patterns (different notation), machine-knitting, or purely chart-based patterns (no text to parse)

## How to Use

### 1. Decode a Pattern Row

```bash
python scripts/pattern_parser.py "k2, p1, *yo, k2tog, rep from * 3 times, k2"
```

Output: plain-English step-by-step for each segment, with the expanded repeat count.

### 2. Calculate Yarn Requirements

```bash
python scripts/yarn_calculator.py --gauge-swraps 20 --gauge-rows 28 --swatch-yards 18 --project-stitches 200 --project-rows 300
```

Output: total yards needed, recommended buy-yardage (with 15% buffer), estimated skeins.

### 3. Verify Stitch Counts

```bash
python scripts/pattern_parser.py --verify "CO 100, Row 1: k2, *p2, k2, rep from * to end" 
```

Output: per-row expected stitch count and flag if any row's net change doesn't balance.

## Core Abbreviations Decoded

| Abbrev | Full Term | Effect on Stitch Count |
|--------|-----------|----------------------|
| k | knit | 0 |
| p | purl | 0 |
| yo | yarn over | +1 |
| k2tog | knit 2 together | -1 |
| ssk | slip slip knit | -1 |
| m1 | make 1 | +1 |
| kfb | knit front & back | +1 |
| bo | bind off | -1 per st bound off |
| co | cast on | sets initial count |

## Numbered Workflow

1. **Cast-on analysis:** Parse the CO instruction to get the starting stitch count.
2. **Row-by-row expansion:** For each row, expand `*...rep from * N times` into concrete stitch sequences.
3. **Stitch tracking:** Track net increases/decreases per row and flag if the count goes negative or doesn't match a stated target.
4. **Yarn calculation:** Use the gauge swatch (wraps per 4", rows per 4", yards consumed in swatch) to project total yardage.
5. **Progress tracking:** Track which rows have been completed and provide a "you are here" marker.

## Common Pitfalls

1. **Confusing "rep from * to end" with "rep from * N times."** The former repeats until stitches run out; the latter does an exact count. The parser handles both but flags when "to end" doesn't divide evenly.

2. **Forgetting that yo and k2tog in the same repeat may be decorative holes with zero net change.** Always compute the *net* per-repeat delta, not individual stitches.

3. **Yarn calculator assumes consistent gauge.** If the user's tension varies (common for beginners), actual usage may differ ±20%. Always add a 15% safety buffer.

4. **Gauge swatch must be washed and blocked** before measuring. Pre-block measurements underestimate yardage for stretchy yarns.

5. **Pattern substitution without re-gauging.** Switching from DK to worsted changes everything. The user must knit a new swatch with the substitute yarn.

## Verification Checklist

- [ ] Pattern row decodes without parse errors
- [ ] Each row's net stitch change matches expected target (if stated)
- [ ] Yarn calculation includes a 15%+ safety buffer
- [ ] Repeat counts multiply correctly (no off-by-one)
- [ ] Cast-on count is divisible by pattern repeat width (or remainder is accounted for)

## Example Session

**User:** "I'm knitting a scarf. Pattern says: CO 40 sts. Row 1: *k3, p2, rep from * to end. Row 2: *p2, k3, rep from * to end. How much yarn do I need for 200 rows? My swatch is 20sts/4", 24 rows/4", and used 15 yards."

**Agent workflow:**
1. Parse CO 40 → starting count = 40
2. Row 1: `k3, p2` = 5-stitch repeat × 8 = 40 ✓ (divides evenly)
3. Yarn calc: area_ratio = (40/20) × (200/24) = 2.0 × 8.33 = 16.67; total = 15 × 16.67 ≈ 250 yards → recommend buying 290 yards (with buffer)
4. Report: "40 stitches divides evenly into 8 repeats of k3,p2. You'll need ~250 yards, buy 290 to be safe."
