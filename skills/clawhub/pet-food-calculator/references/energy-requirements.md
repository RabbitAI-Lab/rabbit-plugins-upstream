# Energy Requirement Reference (Dogs & Cats)

## RER — Resting Energy Requirement

```
RER (kcal/day) = 70 × (body weight in kg)^0.75
```

RER is the energy a resting, fasting animal needs at thermoneutral
temperature. **Always compute at IDEAL (target) weight**, never current
weight for overweight animals.

Quick values: 5kg→234, 10kg→394, 20kg→662, 30kg→904, 40kg→1132, 50kg→1352.

## MER Factors — Dogs

| State | Factor × RER |
|---|---|
| Puppy 2-4 months | 3.0 |
| Puppy 4-9 months | 2.5 |
| Puppy 9-12 months | 2.0 (giant breeds extend to 18mo) |
| Adult neutered | 1.6 |
| Adult intact | 1.8 |
| Senior neutered | 1.4 |
| Senior intact | 1.6 |
| Weight loss | 1.0 |
| Light activity (<30 min/day) | use 1.4-1.5 |
| Moderate activity (1h/day) | 1.6-1.8 |
| Heavy/working (sporting, sled, agility) | 2.0-5.0 |
| Pregnant (last 3 weeks) | 2.0-3.0 stepping up |
| Lactating | 2.0 → up to 4.0 × (at weaning, per litter size) |

## MER Factors — Cats

| State | Factor × RER |
|---|---|
| Kitten 0-4 months | 2.5 |
| Kitten 4-12 months | 2.0 |
| Adult neutered (indoor) | 1.2 |
| Adult intact | 1.4 |
| Senior (10y+) | 1.1 |
| Weight loss | 0.8 (with hard floor, see below) |
| Pregnant | 1.6-2.0 |
| Lactating | 2.0-2.6 × (peaks weeks 3-4) |

## Weight-Loss Safety

**Dogs:** target 1-2% of body weight lost per week. Energy target typically
RER × 1.0 at ideal weight. Recheck every 2 weeks; adjust ±10%.

**Cats:** MAXIMUM 0.5-1% per week. Never below 0.5 × RER at ideal weight, and
never below 18 kcal per kg of ideal weight per day — prolonged underfeeding
triggers **hepatic lipidosis** (fatal liver failure). If a cat refuses the
diet food, stop and call the vet.

```
cat_floor_kcal = max(0.5 × RER, 0.8 × 60 × ideal_kg)  # conservative
```

## Body Condition Score (9-point scale)

Feel ribs and look from above/side:

| BCS | Description | Action |
|---|---|---|
| 1-3 | Ribs visible, no fat | Increase feeding / vet |
| 4-5 | Ribs palpable, waist visible | Maintain |
| 6-7 | Ribs hard to feel, waist losing definition | −10-15% calories |
| 8-9 | Fat deposits, no waist, abdominal distension | Weight-loss plan, vet check |

Rough guide: each BCS above 5 ≈ 10-15% excess body weight. A dog at BCS 7/9
whose ideal is 25kg likely weighs ~30kg.

Ideal-weight estimation from BCS:
```
ideal_kg ≈ current_kg × (1 − 0.10 × (BCS − 5))   (approximate)
```

## Growth Notes

- Large/giant-breed puppies (<18 months): keep lean (BCS 4-5); overfeeding
  growth correlates with skeletal disease. Use puppy food with controlled calcium.
- Kitten → adult food at ~12 months (18 for large-breed dogs).

## Activity Modifiers (applied to adult factors)

The calculator combines age factor with activity:
`final_factor = age_factor × activity_mult` where activity_mult ∈
{0.9 light, 1.0 moderate, 1.2 heavy, 1.6 extreme} — clamped to sane ranges
per species (cats' multiplier capped: an "extreme" cat is still a cat).

## Calories in Common Treats (against the 10% budget)

- Dentastix large: ~75 kcal
- Greenies: ~25-90 kcal by size
- Pig ear: ~150-250 kcal
- Churu/Lick treat tube: ~15-25 kcal
- Peanut butter (1 tbsp): ~90 kcal (xylitol danger!)
- Milk-Bone medium: ~40 kcal
- Cheese cube: ~70 kcal

One pig ear ≈ half a small dog's daily calories. This is why treats get a
hard budget in every report.
