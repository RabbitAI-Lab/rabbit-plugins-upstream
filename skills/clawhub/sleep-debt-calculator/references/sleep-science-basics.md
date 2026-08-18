# Sleep Science Basics

This reference covers the fundamental science behind sleep, sleep cycles, and
sleep debt mechanics — the knowledge that powers the Sleep Debt Calculator.

## Table of Contents

1. [Sleep Cycles](#sleep-cycles)
2. [Sleep Debt Mechanics](#sleep-debt-mechanics)
3. [Why You Can't "Bank" Sleep Long-Term](#why-you-cant-bank-sleep-long-term)
4. [Age-Based Sleep Requirements](#age-based-sleep-requirements)
5. [Quality vs Quantity](#quality-vs-quantity)

---

## Sleep Cycles

The brain cycles through distinct stages roughly every **90 minutes** (range:
70–120 min). A full night contains **4–6 complete cycles**.

### The Stages

| Stage | Type | Description |
|-------|------|-------------|
| N1 | Light | Transition from wakefulness, ~5% of sleep |
| N2 | Light | Core light sleep, ~45-50% of sleep, memory consolidation |
| N3 | Deep (Slow-Wave) | Physical restoration, growth hormone release, immune repair |
| REM | Dreaming | Memory consolidation, emotional processing, creative integration |

### Cycle Importance

- **Deep sleep (N3)** dominates the **first half** of the night. This is when
  physical recovery occurs.
- **REM sleep** dominates the **second half** of the night. This handles
  cognitive and emotional processing.
- **Cutting sleep short** disproportionately destroys REM, because most REM
  happens in the last 2–3 hours.

> **Implication:** If your optimal is 8h and you sleep 6h, you don't lose 25%
> of sleep quality — you may lose 60–90% of REM, which is far worse for
> cognitive function than the raw hours suggest.

## Sleep Debt Mechanics

Sleep debt accumulates from **every night** that you get less sleep than your
biological need. It's a running deficit, much like financial debt.

### Key Findings

- **Van Dongen et al. (2003):** Two weeks of 6h/night produces cognitive
  impairment equivalent to **2 nights of total sleep deprivation** (48h awake).
  Subjects were unaware they were impaired.
- **Carskadon & Dement:** Sleep debt doesn't plateau — it accumulates linearly.
  Recovery requires more than just "normal" sleep; you need a surplus.

### How Debt Accumulates

```
Night 1: Need 8h, get 6h → debt = 2h
Night 2: Need 8h, get 7h → debt = 3h (2+1)
Night 3: Need 8h, get 8h → debt = 3h (unchanged — normal sleep doesn't pay it down)
Night 4: Need 8h, get 9h → debt = 2h (surplus pays it down)
```

### Debt Symptoms by Accumulation

| Debt (hours) | Symptoms |
|-------------|----------|
| 1–3 | Mild: slight attention dips, less patience |
| 4–8 | Moderate: reaction time slows, cravings increase, mood affected |
| 9–16 | Severe: equivalent to being legally drunk in reaction-time studies |
| 17+ | Critical: microsleeps (falling asleep involuntarily for 1–30 seconds) |

## Why You Can't "Bank" Sleep Long-Term

This is one of the most important and counterintuitive findings in sleep science.

### The Problem with "Pre-loading"

**You cannot stockpile sleep in advance of deprivation.** Studies show:

1. **Dinges et al.** — Sleeping extra before a period of sleep deprivation
   provides **no protective benefit**. The extra sleep simply gets wasted.
2. **The body only stores what it needs now.** Unlike fat (energy storage) or
   muscle (built over time), there is no biological mechanism to "store" sleep.

### The Problem with "Banking" Recovery

**Recovery sleep is also not 1:1.** After accumulating 10h of debt:

- You might need only **3–4 nights of recovery sleep** to clear the debt
  (because the body "over-recovers" with deeper, more efficient sleep).
- But cognitive performance **does not fully recover** even after the debt is
  "cleared." Some deficits persist for days.

### What This Means Practically

- **Consistency beats binges.** Sleeping 8h every night is far superior to
  sleeping 6h on weekdays and 10h on weekends.
- **Weekend recovery is partial.** Sleeping in on weekends helps but doesn't
  fully undo the damage.
- **Chronic debt becomes invisible.** After weeks of insufficient sleep, you
  stop feeling "tired" but cognitive deficits remain measurable.

> **The calculator accounts for this:** it tracks both total debt and recent
> trends, and weights weekend recovery as helpful but not a full reset.

## Age-Based Sleep Requirements

Based on [National Sleep Foundation](https://www.sleepfoundation.org/) recommendations:

| Age Range | Recommended | Optimal (used by calculator) |
|-----------|------------|------------------------------|
| 6–13 years (school age) | 9–11h | **9.5h** |
| 14–17 years (teen) | 8–10h | **9.0h** |
| 18–25 years (young adult) | 7–9h | **8.0h** |
| 26–64 years (adult) | 7–9h | **8.0h** |
| 65+ years (senior) | 7–8h | **7.5h** |

### Why Teens Need More

- Puberty shifts the circadian rhythm **later** by ~2 hours (this is biological,
  not behavioral).
- The teenage brain is undergoing massive remodeling (synaptic pruning,
  myelination) requiring extra sleep.
- Early school start times conflict with this biological reality.

## Quality vs Quantity

**6 hours of deep, uninterrupted sleep is more restorative than 8 hours of
restless, fragmented sleep.** This is why the calculator applies quality
weighting.

### What Destroys Quality

| Factor | Impact | Notes |
|--------|--------|-------|
| **Caffeine** | Delays sleep onset, reduces deep sleep | Half-life: 5–6h. Even afternoon coffee hurts |
| **Alcohol** | Suppresses REM, causes fragmentation | "Nightcap" helps you fall asleep but ruins sleep quality |
| **Temperature** | Optimal: 18–19°C (65–67°F) | Too warm = less deep sleep |
| **Screens** | Blue light suppresses melatonin | Particularly bad in the last hour before bed |
| **Irregular schedule** | Confuses circadian rhythm | Even 1 hour of variation matters |

### Quality Weighting in the Calculator

```
Effective Sleep = Time in Bed × Quality Weight

Quality 5 (excellent): 100% → 8h in bed = 8.0h effective
Quality 3 (average):   80%  → 8h in bed = 6.4h effective
Quality 1 (terrible):  45%  → 8h in bed = 3.6h effective
```

This means that **improving quality can recover debt without adding time.**
