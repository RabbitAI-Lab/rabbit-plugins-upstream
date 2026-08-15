---
name: child-screen-time
version: 1.0.0
author: Denis Voronin
license: MIT
description: >
  Negotiate and enforce screen time contracts with children using a fair
  AI-mediated system. Set per-child daily limits, create educational vs
  entertainment budgets, track actual usage, generate compliance report
  cards, and auto-grant/extend time for chores, homework, and good behavior.
tags:
  - parenting
  - children
  - screen-time
  - contracts
  - family
---

# Child Screen Time Negotiator

A standalone command-line tool for managing children's screen time through
fair, transparent, AI-mediated contracts. Instead of arbitrary limits and
power struggles, screen time becomes an earned currency: educational time
is more generous, entertainment time must be earned through chores, homework,
and good behavior, and compliance is tracked through a report-card system.

## Quick Start

```bash
# Add your children
python3 scripts/screen_time.py add-child Alice 10
python3 scripts/screen_time.py add-child Bob 7

# Set base daily limits (minutes)
python3 scripts/screen_time.py set-limit Alice 120
python3 scripts/screen_time.py set-limit Bob 90

# Log screen time usage
python3 scripts/screen_time.py log Alice 45 "Minecraft" fun
python3 scripts/screen_time.py log Alice 30 "Khan Academy math" edu

# Award bonus time for chores/homework
python3 scripts/screen_time.py award Alice 15 "finished homework early"

# Check status
python3 scripts/screen_time.py status Alice

# Generate weekly report card
python3 scripts/screen_time.py report-card Alice 7
```

## Commands

| Command | Description |
|---------|-------------|
| `add-child <name> <age>` | Register a child in the system |
| `set-limit <name> <minutes>` | Set base daily entertainment screen limit |
| `set-edu-limit <name> <minutes>` | Set daily educational screen limit (default: unlimited) |
| `log <name> <minutes> <activity> <fun\|edu>` | Log screen time usage |
| `award <name> <minutes> <reason>` | Award bonus time for good behavior/chores |
| `deduct <name> <minutes> <reason>` | Remove time as a consequence |
| `status <name>` | Show today's remaining time and recent usage |
| `report-card <name> [days]` | Generate a compliance report card |
| `contract <name>` | Display the current screen-time contract |
| `negotiate <name> <minutes> <reason>` | Child requests more time; system evaluates fairness |
| `balance` | Show all children's remaining time today |
| `history <name> [days]` | Show usage history |
| `weekly-summary` | Compare all children's usage this week |

## How It Works

### Two-Category Budget System
Screen time is split into two categories:

1. **Educational (`edu`)**: Khan Academy, Duolingo, coding, documentaries,
   research. These have generous or unlimited limits — learning is encouraged.
2. **Entertainment (`fun`)**: Games, YouTube, social media, streaming.
   These draw from the earned daily budget.

### Earned-Time Economy
Children earn bonus entertainment minutes through:
- **Homework completion**: +15 min per subject
- **Chores done without being asked**: +10 min each
- **Reading (physical books)**: +5 min per 15 min reading
- **Good behavior / kindness reports**: +10 min
- **Outdoor play**: +5 min per 30 min outside

### Negotiation System
When a child asks for more time, the system evaluates the request based on:
- How much they've already used today
- How much educational time they've logged
- Their recent compliance history (did they stop when asked?)
- Whether they have pending chores/homework
- Age-appropriateness

The system responds with: **Approved**, **Conditional** (do X first), or
**Denied** (with explanation).

### Report Cards
Weekly report cards show:
- Total screen time vs. educational time
- Bonus minutes earned and how
- Compliance score (stopped when asked, transitioned smoothly)
- Comparison to age-based recommendations (AAP guidelines)
- Areas for praise and improvement

## Data Storage

Data is stored in `~/.screen_time.json`. Delete to reset.

## References

- [AAP Screen Time Guidelines](references/aap-guidelines.md)
- [Earned-Time Economy](references/earned-time-economy.md)

## License

MIT © Denis Voronin
