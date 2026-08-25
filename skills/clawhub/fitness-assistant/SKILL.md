---
name: fitness-assistant
description: Plan daily meals and workouts from a user's age and health profile, then schedule localized daily plans via OpenClaw automations.
---

# Fitness Assistant

Builds a personalized **one-day diet plan + workout plan** from the user's age, body data, and health condition, and can deliver it every day on a schedule in the user's chosen language and timezone.

Use this skill when the user asks for:
- a daily meal/diet plan, calorie or macro targets, or a workout plan;
- recurring daily fitness messages ("send me a plan every morning", "定时发每日计划", "daily plan", etc.).

## Workflow

### 1. Profile

Load the saved user profile if one exists; otherwise collect the fields listed in [references/profile.md](references/profile.md). Ask only for what is missing. Minimum required: age, sex, height, weight, activity level, goal, health conditions/limitations, dietary restrictions, training experience/equipment, daily routine, timezone (IANA), language.

### 2. Compute targets

Run the calculator and use its numbers:

```bash
python3 {baseDir}/scripts/plan.py --age 32 --sex male --height-cm 178 --weight-kg 78 --activity moderate --goal lose
```

Use `--unit imperial` for lb/in inputs and `--json` for machine-readable output. The script prints BMI, BMR, TDEE, the calorie target, and protein/fat/carbs grams. If the script cannot run, compute manually using the formulas and defaults in [references/meal-planning.md](references/meal-planning.md).

### 3. Build today's plan

- **Diet**: breakfast / lunch / dinner / optional snack split, water target, and macro-aware portions following [references/meal-planning.md](references/meal-planning.md). Respect dietary restrictions and the calorie floors.
- **Workout**: one session matched to experience, equipment, and time available, following [references/training.md](references/training.md); include warm-up, main work, and cooldown.
- **Language**: write the whole message in the user's chosen language from the 8 in [references/languages.md](references/languages.md), using that file's fixed labels so every language has the same structure.
- **Safety**: this is general lifestyle guidance, not medical advice. If the profile shows a chronic condition, age under 18, pregnancy, or medication that affects diet/training, adapt conservatively and recommend professional consultation before following the plan. Never go below the calorie floors in meal-planning.md.

### 4. Schedule daily delivery (when requested)

When the user wants the plan published on a schedule:

1. Confirm the delivery time (their local clock), timezone (IANA name), language, and where to deliver (this chat or another channel).
2. Create an automation with a cron schedule plus `tz`, whose payload prompt references this skill so each run produces a fresh daily plan — see [references/scheduling.md](references/scheduling.md) for the exact tool/CLI calls and the ready-to-use prompt template.
3. Confirm the created job and tell the user the next run time; if a job already exists, update it instead of creating a duplicate.

## Boundaries

- Do not invent health data or diagnose; use only what the user reports.
- Do not use languages outside the 8 supported ones, and do not mix languages in one message.
- Do not schedule without a confirmed timezone and delivery time.
- Do not add medical claims or guaranteed outcomes ("burn fat in 7 days").
