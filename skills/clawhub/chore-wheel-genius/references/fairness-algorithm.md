# Fairness Algorithm

## Core Principle

Fairness in a household is not about doing the same *number* of chores — it's
about contributing the same *amount of effort* adjusted for age and ability.

## Effort Scoring

Each chore has an effort score (1-5):

| Effort | Description | Examples |
|--------|-------------|----------|
| 1 | Minimal | Water plants, feed pet, sort mail |
| 2 | Light | Take out trash, load dishwasher, dust |
| 3 | Moderate | Vacuum, mop, grocery shopping |
| 4 | Heavy | Clean bathroom, deep clean kitchen, yard work |
| 5 | Very Heavy | Cook full meal, major repair, move furniture |

## Fairness Calculation

### Per-Member Effort Target

For a household of N members, the weekly effort target per member is:

```
target = total_chore_effort / N × age_multiplier
```

### Age Multipliers

| Age | Multiplier | Rationale |
|------|-----------|-----------|
| < 6 | 0.0 | Too young for chores |
| 6-7 | 0.3 | Light participation |
| 8-10 | 0.5 | Half the adult load |
| 11-13 | 0.7 | Growing responsibility |
| 14-17 | 0.85 | Nearly adult |
| 18+ | 1.0 | Full responsibility |

### Skill Bonus

When a member has a skill relevant to a chore, their effort for that chore is
reduced by 20% (it's easier for them), but the chore still counts full effort
for fairness. This naturally assigns skilled members to matching chores while
keeping the effort ledger fair.

### Recency Penalty

For the most unpleasant chores (effort 4-5), whoever did it last gets a
+0.5 weight against being assigned again. This prevents one person from
always getting the worst tasks.

## Assignment Algorithm

```
1. Calculate each member's cumulative effort deficit/surplus
2. Sort members by deficit (most behind gets priority)
3. For each chore (sorted by effort, highest first):
   a. Filter members who have the required skills (if any)
   b. Filter by age appropriateness
   c. Apply recency penalty for unpleasant chores
   d. Assign to the eligible member with the highest deficit
4. Log assignments and update fairness ledger
```

## Compliance Tracking

Completed chores add to a member's effort ledger. Skipped chores don't.
Over time:

- **Effort surplus** → Member doing more than their share → Praise them
- **Effort deficit** → Member doing less → Address gently
- **Consistent skipper** → Pattern detection → Flag for family discussion

## Edge Cases

- **Guests/visitors**: Not assigned chores
- **Illness**: Member can be marked unavailable (`set-available <name> false`)
- **Vacation**: Chores redistributed during absence
- **New chore**: Automatically weighted and added to next rotation
