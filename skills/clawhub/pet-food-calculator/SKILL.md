---
name: pet-food-calculator
description: "Calculate exact daily calorie needs and food portions for dogs and cats from species, breed, weight, age, activity level, and body condition. Compares feeding costs across food types, generates feeding schedules for multi-pet households, and flags weight-loss plans. Use when the user asks how much to feed their dog or cat, whether their pet is overweight, or how to switch foods safely."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [pets, dogs, cats, nutrition, feeding, calories, weight, health]
---

# Pet Food Calculator 🐾

Compute **exactly how much to feed your dog or cat** — daily calories, grams per meal, feeding schedule, cost per month, and weight-loss trajectory — from species, weight, age, activity, and body-condition score. Flags weight-loss plans with safe calorie floors (never starve a cat) and builds transition schedules for switching foods.

## Overview

Pet obesity affects **over half of dogs and cats**, shaving ~2 years off life expectancy, and the #1 cause is simple overfeeding — owners guess portions, food bags' guidelines are deliberately generous, and cups are imprecise. Vet nutrition formulas (RER → MER) are well-established but require a calculator nobody owns.

`pet_food_calculator.py` implements the veterinary-standard math:

- **RER** (Resting Energy Requirement) = 70 × (ideal weight kg)^0.75
- **MER** (Maintenance) = RER × factor from species/age/activity/reproductive status
- **Weight loss**: targeted at RER × 0.8-1.0 for dogs, **never below ~0.5×RER / strict floors for cats** (hepatic lipidosis risk)
- Portions in **grams/day** from any food's kcal/kg (printed on every bag)
- **Cost comparison** across foods (dry/wet/premium/vet prescription)
- **Food transition schedule** (25/50/75% over 7 days)
- Multi-pet household plan with per-animal feeding windows

## When to Use

- "How much should I feed my dog/cat?" — daily portions in grams and calories
- "Is my pet overweight?" — body-condition scoring guide + target weight
- "My vet said to put him on a diet" — safe weight-loss plan with timeline
- Comparing food costs before switching brands
- "How do I switch foods without stomach upset?" — transition schedule
- Puppy/kitten growth feeding (their energy factors are wildly different)
- Senior pets, pregnant/nursing animals, working/sporting dogs

**Don't use for:** diagnosing illness, prescription diets for renal/urinary
conditions (follow vet guidance), or exotic pets (formulas are dog/cat only).

## Quick Start

```bash
# Adult neutered dog, 30 kg, moderate activity, food is 3800 kcal/kg
python3 scripts/pet_food_calculator.py --species dog --weight 30 \
  --age adult --activity moderate --food-calories 3800

# Overweight cat: 7.2 kg current, target 5.5 kg
python3 scripts/pet_food_calculator.py --species cat --weight 7.2 \
  --target-weight 5.5 --food-calories 4800

# Puppy, 5 kg, expecting ~25 kg adult
python3 scripts/pet_food_calculator.py --species dog --weight 5 \
  --age puppy --adult-weight 25 --food-calories 4100

# Compare monthly cost of two foods
python3 scripts/pet_food_calculator.py --species dog --weight 30 \
  --age senior --food-calories 3400 --food-price 65 --bag-kg 12

# Full household plan (JSON out)
python3 scripts/pet_food_calculator.py --species cat --weight 4.5 \
  --age adult --food-calories 5000 --json plan.json
```

## The Math (what the vet does)

1. **RER** = 70 × W^0.75 (W = ideal/target weight, not current!)
2. **Factor** — dog adult neutered 1.6, intact 1.8, senior 1.4, puppy 4-month ~2.7→1.6 by 12mo, weight loss 1.0; cat adult neutered 1.2, intact 1.4, senior 1.1, weight loss 0.8×RER (floor!)
3. **MER** = RER × factor → kcal/day
4. **Grams/day** = MER ÷ (food kcal/kg ÷ 1000)
5. Treats ≤ 10% of daily calories — the report reserves that budget

## Common Pitfalls

1. **Using current weight for overweight pets.** Energy needs are computed at *ideal/target* weight — feeding a 40 kg obese dog like a 40 kg dog perpetuates the obesity. Use `--target-weight`.
2. **Crash-dieting cats.** Cats fasting or severely underfed develop hepatic lipidosis, which is life-threatening. The calculator enforces feline floors (~0.5×RER and ≥18 kcal per kg ideal weight) and warns.
3. **Trusting bag guidelines.** They're set for the most active animals and rounded up; calculating from kcal/kg is exact.
4. **Ignoring treats.** A dental chew can be 10% of a small dog's daily calories. Keep the 10% budget.
5. **Switching foods cold-turkey.** GI upset follows; the generated 7-day transition (25→50→75→100%) prevents it.
6. **Volume ≠ weight.** A "cup" of dense kibble can vary 20% in calories; grams on a kitchen scale are the only honest unit.

## Verification Checklist

- [ ] Species/age/activity factors match the animal's real state
- [ ] Target weight (not current) used for overweight pets
- [ ] Food kcal/kg read from the bag's "metabolizable energy" line (kcal/kg, not kcal/cup)
- [ ] Weight-loss rate for dogs ≤ 1-2% body weight per week
- [ ] Cat plans respect the calorie floor and show no fasting
- [ ] Transition schedule printed when switching foods (`--transition`)

## References

- `references/energy-requirements.md` — full factor tables, growth curves, BCS guide
- `references/feeding-guide.md` — meal frequency by age, transition schedules, treat budget, food-label decoding
