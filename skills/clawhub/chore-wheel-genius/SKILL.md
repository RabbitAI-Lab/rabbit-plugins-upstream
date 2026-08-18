---
name: chore-wheel-genius
version: 1.0.0
author: Denis Voronin
license: MIT
description: >
  Smart chore assignment for families and households. Assigns tasks based on
  skills, schedule, and fairness scoring. Tracks who did what, detects
  freeloaders, rotates unpleasant tasks equitably, and generates visual
  chore charts and fairness reports.
tags:
  - household
  - chores
  - family
  - fairness
  - scheduling
---

# Chore Wheel Genius

A standalone command-line tool for assigning household chores fairly across
family members. Instead of random rotation or nagging, this system considers
each person's skills, availability, chore history, and fairness score to
generate optimal weekly chore assignments.

## Quick Start

```bash
# Add household members
python3 scripts/chore_wheel.py add-member Mom --skills cooking,laundry
python3 scripts/chore_wheel.py add-member Dad --skills repair,cooking
python3 scripts/chore_wheel.py add-member Alice 14
python3 scripts/chore_wheel.py add-member Bob 10

# Define chores
python3 scripts/chore_wheel.py add-chore "Cook dinner" --effort 5 --freq daily --skills cooking
python3 scripts/chore_wheel.py add-chore "Take out trash" --effort 2 --freq daily
python3 scripts/chore_wheel.py add-chore "Clean bathroom" --effort 4 --freq weekly

# Generate this week's assignments
python3 scripts/chore_wheel.py assign

# Mark chores as done
python3 scripts/chore_wheel.py done Mom "Cook dinner"

# Check fairness
python3 scripts/chore_wheel.py fairness

# Weekly report
python3 scripts/chore_wheel.py report
```

## Commands

| Command | Description |
|---------|-------------|
| `add-member <name> [age] [--skills s1,s2]` | Register a household member |
| `add-chore <name> [--effort 1-5] [--freq daily\|weekly\|monthly] [--skills s1,s2]` | Define a chore |
| `assign [week]` | Generate fair chore assignments |
| `done <member> <chore>` | Mark a chore as completed |
| `skip <member> <chore> <reason>` | Log a skipped chore |
| `fairness` | Show fairness score for each member |
| `report [weeks]` | Generate a multi-week chore report |
| `chart` | Display this week's visual chore chart |
| `swap <chore> <from_member> <to_member>` | Swap a chore between members |
| `list-chores` | Show all defined chores |
| `list-members` | Show all household members |
| `history <member> [weeks]` | Show a member's chore history |

## How It Works

### Fairness Scoring Algorithm
Each member has a **fairness score** based on:
- **Total effort** accumulated over time (weighted by chore difficulty)
- **Age adjustment** — younger children get lighter loads
- **Skill matching** — if you're skilled at cooking, you cook more (but not exclusively)
- **Recency penalty** — whoever did the unpleasant chore last time gets a break

### Effort-Weighted Rotation
Chores are weighted by effort (1-5):
- Effort 1: Take out trash, water plants
- Effort 2: Load dishwasher, feed pets
- Effort 3: Vacuum, mop floors
- Effort 4: Clean bathroom, deep clean kitchen
- Effort 5: Cook a full meal, yard work

The algorithm distributes total effort evenly, not just chore count.

### Unpleasant Chore Rotation
Chores like "clean the toilet" or "unclog the drain" are tracked specifically
and rotated so no one person always gets stuck with them.

### Age-Based Adjustments
- Under 8: Only effort 1-2 chores
- 8-12: Up to effort 3
- 13+: All chores (with fairness balancing)
- Adults: Slightly higher baseline effort tolerance

## Data Storage

Data is stored in `~/.chore_wheel.json`. Delete to reset.

## References

- [Fairness Algorithm](references/fairness-algorithm.md)
- [Age-Appropriate Chores](references/age-chores.md)

## License

MIT © Denis Voronin
