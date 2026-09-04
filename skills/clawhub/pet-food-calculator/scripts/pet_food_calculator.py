#!/usr/bin/env python3
"""Pet Food Calculator — veterinary-standard daily energy and portion math
for dogs and cats.

RER = 70 × W^0.75 at IDEAL weight; MER = RER × species/age/activity factor.
Outputs kcal/day, grams/day for the given food, meals, treat budget,
weight-loss plan with timeline, food cost, and transition schedule.
Enforces feline safety floors (hepatic lipidosis prevention).
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Factor tables
# ---------------------------------------------------------------------------

DOG_FACTORS = {
    "puppy": 2.5,       # 4-12 months (2-4mo = 3.0 via --activity extreme? no: age bands below)
    "puppy-young": 3.0,  # 2-4 months
    "adult": 1.6,        # neutered
    "adult-intact": 1.8,
    "senior": 1.4,
    "weightloss": 1.0,
}

CAT_FACTORS = {
    "kitten": 2.0,
    "kitten-young": 2.5,
    "adult": 1.2,        # neutered indoor
    "adult-intact": 1.4,
    "senior": 1.1,
    "weightloss": 0.8,
}

ACTIVITY_MULT = {"light": 0.9, "moderate": 1.0, "heavy": 1.2, "extreme": 1.6}

# feline safety
CAT_FACTOR_FLOOR = 0.5 * 1.0          # never below 0.5 × RER
CAT_KG_KCAL_FLOOR = 18.0              # kcal per kg ideal weight per day

MEALS_BY_AGE = {
    "puppy": 3, "puppy-young": 4, "kitten": 3, "kitten-young": 4,
    "adult": 2, "adult-intact": 2, "senior": 2, "weightloss": 2,
}


def rer(weight_kg: float) -> float:
    return 70 * weight_kg ** 0.75


def age_key(args) -> str:
    if args.target_weight and args.target_weight < args.weight - 0.05:
        return "weightloss"
    if args.age == "young":           # <4 months equivalent
        return "puppy-young" if args.species == "dog" else "kitten-young"
    if args.age == "puppy" or args.age == "kitten":
        return args.age
    if args.age == "senior":
        return "senior"
    if args.age == "adult" and args.intact:
        return "adult-intact"
    return "adult"


def compute(args) -> dict:
    sp = args.species
    ideal = args.target_weight if (args.target_weight and
                                   args.target_weight < args.weight) else args.weight
    key = age_key(args)
    factors = DOG_FACTORS if sp == "dog" else CAT_FACTORS
    factor = factors[key]

    act = ACTIVITY_MULT.get(args.activity, 1.0)
    # cats: cap activity multiplier (an extreme cat is still a cat)
    if sp == "cat":
        act = min(act, 1.1)
    # puppies/kittens: growth dominates; don't multiply activity further
    if key in ("puppy", "puppy-young", "kitten", "kitten-young"):
        act = 1.0

    r = rer(ideal)
    mer = r * factor * act
    warnings = []

    if sp == "cat" and key == "weightloss":
        floor = max(CAT_FACTOR_FLOOR * r, CAT_KG_KCAL_FLOOR * ideal)
        if mer < floor:
            warnings.append(
                f"Calorie target {mer:.0f} kcal is below the feline safety "
                f"floor ({floor:.0f} kcal). Raising to floor — cats must not "
                "be crash-dieted (hepatic lipidosis risk). Expect slower loss.")
            mer = floor

    treat_kcal = round(mer * 0.10)
    food_kcal = mer - treat_kcal
    grams_per_day = food_kcal / (args.food_calories / 1000.0) \
        if args.food_calories else None

    res = {
        "species": sp, "age_class": key, "ideal_weight_kg": ideal,
        "current_weight_kg": args.weight,
        "rer_kcal": round(r), "factor": factor, "activity_mult": act,
        "mer_kcal": round(mer), "treat_budget_kcal": treat_kcal,
        "food_kcal_kg": args.food_calories,
        "grams_per_day": round(grams_per_day) if grams_per_day else None,
        "meals_per_day": MEALS_BY_AGE.get(key, 2),
        "grams_per_meal": round(grams_per_day / MEALS_BY_AGE.get(key, 2))
        if grams_per_day else None,
        "warnings": warnings,
    }

    # growth projection for puppies
    if sp == "dog" and args.age == "puppy" and args.adult_weight:
        months_left = max(1, 12 - 6)  # rough: mid-puppy
        res["growth_note"] = (
            f"Estimated adult weight {args.adult_weight} kg — recompute "
            "portions every 2 weeks during growth; keep BCS 4-5 (lean) to "
            "protect joint development.")

    # weight-loss plan
    if key == "weightloss":
        sp_loss_rate = 0.01 if sp == "cat" else 0.015  # per week
        loss_kg = args.weight - ideal
        weeks = max(1, round(loss_kg / (args.weight * sp_loss_rate)))
        # recompute: weekly loss applies to roughly average weight
        weeks = max(2, round(loss_kg / ((args.weight + ideal) / 2 * sp_loss_rate)))
        res["weight_loss"] = {
            "loss_kg": round(loss_kg, 2),
            "target_rate_pct_per_week": round(sp_loss_rate * 100, 1),
            "estimated_weeks": weeks,
            "weigh_cadence": "every 2 weeks",
            "adjust_rule": "+/-10% food if losing >2%/wk (dog) or <0.5%/wk",
        }

    # cost
    if args.food_price and args.bag_kg and grams_per_day:
        monthly_kg = grams_per_day * 30.4 / 1000.0
        res["cost"] = {
            "monthly_kg": round(monthly_kg, 2),
            "monthly_cost": round(monthly_kg / args.bag_kg * args.food_price, 2),
            "currency_note": "in the same currency as --food-price",
            "bag_lasts_days": round(args.bag_kg / monthly_kg * 30.4),
        }

    # transition
    if args.transition:
        res["transition_days"] = [
            {"days": "1-2", "new_pct": 25, "old_pct": 75},
            {"days": "3-4", "new_pct": 50, "old_pct": 50},
            {"days": "5-6", "new_pct": 75, "old_pct": 25},
            {"days": "7+", "new_pct": 100, "old_pct": 0},
        ]
    return res


def render(res: dict) -> str:
    out = []
    a = out.append
    sp = res["species"].capitalize()
    a("=" * 58)
    a(f" {sp} FEEDING PLAN")
    a("=" * 58)
    a(f" Life stage   : {res['age_class']} (×{res['factor']} RER, "
      f"activity ×{res['activity_mult']})")
    if res["current_weight_kg"] != res["ideal_weight_kg"]:
        a(f" Weight       : {res['current_weight_kg']} kg now → "
          f"{res['ideal_weight_kg']} kg target")
    else:
        a(f" Weight       : {res['ideal_weight_kg']} kg")
    a(f" RER          : {res['rer_kcal']} kcal/day")
    a(f" Daily energy : {res['mer_kcal']} kcal/day (MER)")
    a("")
    if res["grams_per_day"]:
        a(f" PORTION      : {res['grams_per_day']} g/day of food "
          f"({res['food_kcal_kg']} kcal/kg)")
        a(f"              = {res['grams_per_meal']} g × "
          f"{res['meals_per_day']} meals")
    else:
        a(" PORTION      : pass --food-calories (kcal/kg from the bag) "
          "for grams/day")
    a(f" Treat budget : ≤ {res['treat_budget_kcal']} kcal/day (10% rule)")
    if "growth_note" in res:
        a("")
        a(f" 🐕 {res['growth_note']}")
    if "weight_loss" in res:
        wl = res["weight_loss"]
        a("")
        a(" WEIGHT-LOSS PLAN")
        a(f"   Lose {wl['loss_kg']} kg at ~{wl['target_rate_pct_per_week']}%/week"
          f" → ≈ {wl['estimated_weeks']} weeks")
        a(f"   Weigh {wl['weigh_cadence']}; {wl['adjust_rule']}")
        a("   Recompute portions after every kg lost.")
    if "cost" in res:
        c = res["cost"]
        a("")
        a(" COST")
        a(f"   {c['monthly_kg']} kg/month → {c['monthly_cost']} "
          f"({c['currency_note']})")
        a(f"   One {'' }bag lasts ≈ {c['bag_lasts_days']} days")
    if res.get("transition_days"):
        a("")
        a(" FOOD TRANSITION (7 days)")
        for t in res["transition_days"]:
            a(f"   Days {t['days']:>4}: {t['new_pct']}% new / {t['old_pct']}% old")
    if res["warnings"]:
        a("")
        for w in res["warnings"]:
            a(f" ⚠  {w}")
    a("")
    a(" Scale beats cup: weigh portions. Fresh water always.")
    a("=" * 58)
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Veterinary-standard feeding calculator for dogs & cats.")
    ap.add_argument("--species", required=True, choices=["dog", "cat"])
    ap.add_argument("--weight", type=float, required=True,
                    help="current body weight, kg")
    ap.add_argument("--target-weight", type=float,
                    help="ideal/target weight (starts weight-loss plan)")
    ap.add_argument("--age", default="adult",
                    choices=["young", "puppy", "kitten", "adult", "senior"],
                    help="young=<4mo; puppy/kitten=growing; adult; senior")
    ap.add_argument("--intact", action="store_true",
                    help="not spayed/neutered")
    ap.add_argument("--activity", default="moderate",
                    choices=["light", "moderate", "heavy", "extreme"])
    ap.add_argument("--food-calories", type=float,
                    help="metabolizable energy kcal/kg (printed on the bag)")
    ap.add_argument("--food-price", type=float, help="price of one bag")
    ap.add_argument("--bag-kg", type=float, help="bag size in kg")
    ap.add_argument("--adult-weight", type=float,
                    help="expected adult weight for puppies")
    ap.add_argument("--transition", action="store_true",
                    help="include 7-day food-switch schedule")
    ap.add_argument("--json", type=Path, help="write plan as JSON")
    args = ap.parse_args()

    if args.age == "puppy" and args.species == "cat":
        args.age = "kitten"
    if args.age == "kitten" and args.species == "dog":
        args.age = "puppy"
    if args.weight <= 0:
        ap.error("--weight must be positive")
    if args.target_weight and args.target_weight >= args.weight:
        print("Note: target weight ≥ current weight — no weight-loss plan "
              "will be generated.", file=sys.stderr)

    res = compute(args)
    print(render(res))
    if args.json:
        args.json.write_text(json.dumps(res, indent=2))
        print(f"\nJSON plan → {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
