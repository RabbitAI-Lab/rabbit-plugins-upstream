---
name: exam-stress-coach
description: "Manage exam anxiety with adaptive breathing exercises, evidence-based study planning, stress visualization, and motivational coaching. Use when preparing for tests or feeling overwhelmed by academic pressure."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [education, stress, anxiety, exams, students, wellness, mindfulness]
---

# Exam Stress Coach

## Overview

Exam Stress Coach is an adaptive stress management toolkit for students. It combines evidence-based anxiety reduction techniques — box breathing, progressive muscle relaxation scripts, cognitive reframing — with smart study planning and progress visualization. The coach adapts to your current stress level (self-reported 1–10) and recommends interventions that match your state.

## When to Use

- A student (or parent of one) is preparing for exams and feels overwhelmed
- You need to build a realistic study schedule with spaced repetition and breaks
- You want guided breathing/relaxation exercises timed to your session
- You want to visualize stress trends over a study period
- **Don't use for:** clinical anxiety disorders — recommend a professional instead

## How It Works

1. **Stress Assessment** — On a 1–10 scale, classify stress into zones (green/amber/red) with recommended actions per zone.
2. **Breathing Exercises** — Generates timed box-breathing (4-4-4-4), 4-7-8, and coherent breathing scripts with visual cues and duration control.
3. **Study Plan Generator** — Given exam date, subjects, and available hours/day, produces a spaced study schedule using distributed practice and interleaving.
4. **Stress Tracker** — Logs daily stress scores to a JSON file and plots trends with matplotlib.
5. **Motivational Coach** — Pulls from a curated bank of evidence-backed motivational messages, adapted to current stress zone.

## Quick Start

```bash
# Assess current stress and get recommendations
python scripts/stress_coach.py assess --level 7

# Start a 5-minute box breathing session
python scripts/stress_coach.py breathe --technique box --duration 5

# Generate a study plan for 3 subjects, exam in 14 days, 3h/day
python scripts/stress_coach.py plan --subjects "Calculus,History,Biology" --days 14 --hours-per-day 3

# Log today's stress level
python scripts/stress_coach.py log --level 6 --note "Felt good after review session"

# Visualize stress trends over last 30 days
python scripts/stress_coach.py trend --days 30
```

## Detailed Workflows

### 1. Pre-Study Ritual (5 minutes)

Before opening a textbook:
1. Run `assess --level <N>` to check in with yourself
2. If amber or red, run `breathe --technique box --duration 3`
3. Review the recommended study approach for your zone

### 2. Weekly Study Planning

```bash
python scripts/stress_coach.py plan \
  --subjects "Organic Chem,Physics,Spanish" \
  --days 21 \
  --hours-per-day 4 \
  --output study_plan.json
```

The planner uses:
- **Distributed practice**: spreads topics across days, not crammed
- **Interleaving**: rotates between subjects within a day to improve retention
- **Deliberate rest**: builds in 10-min breaks every 50 minutes (Pomodoro-like)
- **Buffer days**: reserves the last 2 days before the exam for review only

### 3. During Study Sessions

If stress spikes mid-session:
```bash
python scripts/stress_coach.py breathe --technique 478 --duration 3
```

## Stress Zones

| Zone | Score | State | Primary Action |
|------|-------|-------|----------------|
| 🟢 Green | 1–3 | Calm / focused | Active study, tackle hardest material |
| 🟡 Amber | 4–6 | Manageable stress | Structured study with regular breaks |
| 🔴 Red | 7–10 | High anxiety | Breathing first, then lighter review |

## Common Pitfalls

1. **Cramming the night before.** The planner explicitly blocks new material 48h before the exam. Override only if absolutely necessary.
2. **Ignoring physical stress signs.** Stress scores ≥8 persisting for days warrant professional support — the tool will flag this.
3. **Treating breathing exercises as a one-off.** Consistency (2–3×/day during study periods) yields measurable improvement.
4. **Over-scheduling.** The planner caps at 6 productive hours/day; more leads to diminishing returns and burnout.
5. **Forgetting sleep.** Study plans always reserve the last 8 hours before any study block for sleep.

## Verification Checklist

- [ ] `stress_coach.py assess --level 5` prints zone + recommendations
- [ ] `stress_coach.py breathe --technique box --duration 1` runs a 1-min breathing cycle
- [ ] `stress_coach.py plan` produces a JSON schedule with spaced topics
- [ ] `stress_coach.py log` appends to `stress_log.json`
- [ ] `stress_coach.py trend` renders a stress-trend chart (if matplotlib available)

## References

See `references/` for:
- `techniques.md` — deep dive on each breathing technique and the evidence behind it
- `study-planning.md` — the cognitive science of distributed practice and interleaving
