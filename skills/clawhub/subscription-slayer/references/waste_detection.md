# Waste Detection Methodology

Subscription Slayer uses a multi-factor scoring system to estimate the probability that a subscription is wasting your money. Each subscription receives a **waste score from 0–100**.

## Scoring Factors

### 1. Days Since Last Use — 40 points max (40%)

The strongest single signal. If you haven't used a service recently, you're likely paying for nothing.

| Days Unused | Points |
|-------------|--------|
| 180+ (6 months) | 40 |
| 90–179 (3–6 months) | 35 |
| 60–89 (2–3 months) | 28 |
| 30–59 (1–2 months) | 20 |
| 14–29 (2 weeks–1 month) | 10 |
| 7–13 (1–2 weeks) | 5 |
| 0–6 (this week) | 0 |
| No data available | 5 (uncertainty penalty) |

### 2. Cost vs. Usage Efficiency — 25 points max (25%)

Combines cost and usage recency. An expensive service you haven't used in a month is a bigger waste than a cheap one.

| Condition | Points |
|-----------|--------|
| 30+ days unused AND monthly cost ≥ $10 | 25 |
| 30+ days unused AND monthly cost ≥ $5 | 18 |
| 30+ days unused (any cost) | 10 |
| 14+ days unused AND monthly cost ≥ $15 | 15 |
| No usage data AND monthly cost ≥ $20 | 15 |
| No usage data AND monthly cost ≥ $10 | 8 |

### 3. Subscription Age — 15 points max (15%)

Old subscriptions are more likely to be forgotten. The "set it and forget it" problem.

| Age | Points |
|-----|--------|
| 730+ days (2+ years) | 15 |
| 365–729 days (1–2 years) | 10 |
| 180–364 days (6–12 months) | 5 |
| < 180 days | 0 |

### 4. Auto-Renew Status — 10 points max (10%)

Auto-renewing subscriptions silently drain money without any action required from you.

| Auto-Renew | Points |
|------------|--------|
| Yes | 10 |
| No | 0 |

### 5. Category Tendency — 10 points max (10%)

Some categories are statistically more likely to be forgotten or underutilised.

**High-waste categories (10 pts):** news, magazine, newsletter, cloud storage, backup, app, software

**Medium-waste categories (5 pts):** music, entertainment, streaming, video, fitness, gym, health, productivity, education

**Low-waste categories (0 pts):** utilities, insurance, phone, internet

## Score Interpretation

| Score | Label | Meaning |
|-------|-------|---------|
| 80–100 | 🔴 Critical | Almost certainly wasting money. Cancel immediately. |
| 60–79 | 🟠 High | Likely unused. Strong cancellation candidate. |
| 40–59 | 🟡 Moderate | Possibly underutilised. Review usage. |
| 0–39 | 🟢 Low | Probably in active use. Keep monitoring. |

## How to Improve Accuracy

### Provide `last_used` dates
The waste detection is dramatically more accurate when you provide the date you last used each service. Even approximate dates help ("about 3 months ago" → estimate the date).

### Use accurate categories
The category field affects scoring. Be specific: "streaming" is better than "entertainment", "cloud storage" is better than "software".

### Include `start_date`
Subscription age is a meaningful factor. If you don't know the exact start date, estimate.

## Limitations

- **No bank integration**: The tool can't automatically detect subscriptions from your bank statements. You provide the data.
- **Static analysis**: Scores are computed at analysis time. For ongoing monitoring, re-run periodically.
- **Subjective factors**: The scoring weights are heuristic, not derived from your personal usage data. Adjust thresholds as needed.
- **No usage telemetry**: The tool relies on self-reported `last_used` dates. It can't check actual usage automatically.
