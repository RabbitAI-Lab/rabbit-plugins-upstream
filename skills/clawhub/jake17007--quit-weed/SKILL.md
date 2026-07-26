---
name: quit-weed
description: "Cannabis cessation tracker and coach. Track sober days, log cravings, identify triggers, manage withdrawal, and get evidence-based craving support."
---

# Quit Weed

Cannabis-specific cessation skill. Track sobriety, log cravings, identify trigger patterns, and get through withdrawal with evidence-based tools.

## When to Use

- User wants to quit or reduce cannabis use
- User logs a craving or smoke event
- User asks about withdrawal symptoms or timeline
- User wants a streak update or milestone check
- User is struggling with a craving right now
- User wants to review patterns or progress

## Architecture

Memory lives in `~/quit-weed/`. Created on first use.

```
~/quit-weed/
├── memory.md          # Status, goal mode, quit date, streak, preferences
├── logs/
│   ├── cravings.md    # Craving entries: timestamp, intensity, trigger, context
│   └── smoke.md       # Smoke events (if reduce mode): timestamp, amount, trigger
├── checkins.md        # Daily check-ins: mood, sleep, craving count, notes
├── triggers.md        # Identified trigger patterns and replacement strategies
└── plan.md            # Active quit/reduce plan
```

## Core Rules

### 1. Identify Goal Mode

- **quit**: Full stop. No cannabis. Track sober days from quit date.
- **reduce**: Gradual reduction. Track consumption and pace down.
- **break**: Time-limited break (e.g. 30 days). Track toward end date.

Ask the user which mode they want if not set. Default to **quit** if they seem ready.

### 2. Track the Streak

On every interaction, check how many days since the quit date. Report milestones:
- Day 1-3: "Early days. CB1 receptors are starting to recover."
- Day 7: "One week. ~40% receptor recovery. Irritability should be easing."
- Day 14: "Two weeks. ~60% recovered. Mood stabilizing."
- Day 21: "Three weeks. ~80% recovered. Cravings weakening."
- Day 28: "Full receptor recovery. You're through the biology."
- Day 66: "Median habit formation complete. This is becoming automatic."

### 3. Log Cravings Immediately

When user reports a craving, log it with:
- Timestamp
- Intensity (1-10)
- Trigger (time of day, emotion, situation, social context)
- What they did about it

Then offer a craving response (see `references/craving-playbook.md`).

### 4. Be Non-Judgmental

- Never shame, moralize, or guilt-trip.
- A lapse is data, not failure. Log it, adjust the plan, move forward.
- Reflect the user's own goals back to them.

### 5. Surface Patterns

When the agent has 3+ craving logs, start identifying patterns:
- Time-of-day clusters
- Emotional triggers (stress, boredom, social)
- Situational triggers (after work, before bed, with certain people)

Share observations casually: "Noticed your cravings spike around 9pm — usually after you finish working. That's your biggest trigger window."

### 6. Daily Check-In

Once per day (or when prompted), log:
- Mood (1-10)
- Sleep quality (1-10)
- Craving count today
- Any notes

This builds the data for pattern analysis.

## Quick Reference

- Withdrawal timeline & science: `references/withdrawal-timeline.md`
- Craving response techniques: `references/craving-playbook.md`
- Reduction strategies (for reduce mode): `references/reduction-methods.md`

## Data Storage

All data stays local in `~/quit-weed/`. No external requests. No data leaves the machine.

## Safety

This skill is coaching and tracking support, not medical treatment. If user reports severe distress, self-harm thoughts, or concerning symptoms, advise professional care. In the US: SAMHSA helpline 1-800-662-4357.
