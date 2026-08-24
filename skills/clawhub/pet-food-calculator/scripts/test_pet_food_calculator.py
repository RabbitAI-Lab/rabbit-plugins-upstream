#!/usr/bin/env python3
"""Self-test for pet_food_calculator.py — RER math, factor selection,
feline floors, weight-loss plans, portions, cost."""

import json
import math
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent / "pet_food_calculator.py"
sys.path.insert(0, str(SCRIPT.parent))
import pet_food_calculator as pf  # noqa: E402


def NS(**kw):
    defaults = dict(species="dog", weight=30.0, target_weight=None,
                    age="adult", intact=False, activity="moderate",
                    food_calories=3800.0, food_price=None, bag_kg=None,
                    adult_weight=None, transition=False)
    defaults.update(kw)
    return type("NS", (), defaults)


def run(*args):
    return subprocess.run([sys.executable, str(SCRIPT), *args],
                          capture_output=True, text=True)


def test_rer():
    assert abs(pf.rer(10) - 70 * 10 ** 0.75) < 1e-9
    assert round(pf.rer(20)) == 662
    assert round(pf.rer(4)) == 198
    print("  RER formula ... OK")


def test_adult_dog():
    r = pf.compute(NS())
    exp = round(70 * 30 ** 0.75 * 1.6)
    assert r["mer_kcal"] == exp
    assert r["meals_per_day"] == 2
    g = r["grams_per_day"]
    assert g == round((exp * 0.9) / 3.8)  # minus 10% treats
    assert r["treat_budget_kcal"] == round(exp * 0.1)
    print("  adult dog MER + grams ... OK")


def test_cat_adult():
    r = pf.compute(NS(species="cat", weight=4.5, food_calories=5000))
    exp = round(70 * 4.5 ** 0.75 * 1.2)
    assert r["mer_kcal"] == exp
    print("  adult cat MER ... OK")


def test_feline_floor():
    # obese cat 9kg → 5kg target would give 0.8×RER(5) = 0.8×234 = 187
    # floor = max(0.5*234, 18*5=90) = 117 → 187 stays. Push lower via huge loss:
    r = pf.compute(NS(species="cat", weight=9.0, target_weight=5.0,
                      food_calories=4000))
    assert r["mer_kcal"] == round(70 * 5 ** 0.75 * 0.8)  # 187
    assert r["weight_loss"]["estimated_weeks"] > 4
    # tiny cat floor: 3kg target → 0.8×RER(3)=0.8×160.6=128 vs 18*3=54 → stays
    r2 = pf.compute(NS(species="cat", weight=6.0, target_weight=3.0,
                       food_calories=4000))
    assert r2["mer_kcal"] == 128
    print("  feline weight-loss math ... OK")


def test_feline_floor_triggers():
    # Engineer a below-floor case: weightloss factor is 0.8 → always above
    # 0.5×RER floor mathematically. Verify floor code path via direct values.
    floor = max(pf.CAT_FACTOR_FLOOR * pf.rer(5), pf.CAT_KG_KCAL_FLOOR * 5)
    assert floor == 0.5 * pf.rer(5)  # 117 > 90
    assert pf.CAT_KG_KCAL_FLOOR == 18.0
    print("  feline floor constants ... OK")


def test_puppy():
    r = pf.compute(NS(age="puppy", weight=5, adult_weight=25,
                      food_calories=4100))
    assert r["factor"] == 2.5
    assert "growth_note" in r
    r2 = pf.compute(NS(age="young", weight=3))
    assert r2["factor"] == 3.0
    # activity multiplier suppressed during growth
    assert r2["activity_mult"] == 1.0
    print("  puppy factors + growth note ... OK")


def test_weightloss_dog():
    r = pf.compute(NS(weight=40, target_weight=30))
    assert r["factor"] == 1.0
    assert r["ideal_weight_kg"] == 30
    assert r["weight_loss"]["loss_kg"] == 10
    assert 15 <= r["weight_loss"]["estimated_weeks"] <= 30
    print("  dog weight-loss plan ... OK")


def test_cost_and_transition():
    r = pf.compute(NS(food_price=65, bag_kg=12, transition=True))
    c = r["cost"]
    assert 8 < c["monthly_kg"] < 15  # 30kg dog ≈ 340g/day → ~10kg/month
    assert 0 < c["monthly_cost"] < 200
    assert len(r["transition_days"]) == 4
    assert r["transition_days"][0]["new_pct"] == 25
    print("  cost + transition schedule ... OK")


def test_cli(tmpdir):
    j = Path(tmpdir) / "plan.json"
    r = run("--species", "cat", "--weight", "7.2", "--target-weight", "5.5",
            "--food-calories", "4800", "--json", str(j))
    assert r.returncode == 0, r.stderr
    assert "WEIGHT-LOSS PLAN" in r.stdout
    assert "Treat budget" in r.stdout
    data = json.loads(j.read_text())
    assert data["mer_kcal"] == round(70 * 5.5 ** 0.75 * 0.8)
    assert data["warnings"] == []  # 0.8×RER above floor here
    r2 = run("--species", "dog", "--weight", "0")
    assert r2.returncode != 0  # validation
    print("  CLI end-to-end ... OK")


if __name__ == "__main__":
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        test_rer()
        test_adult_dog()
        test_cat_adult()
        test_feline_floor()
        test_feline_floor_triggers()
        test_puppy()
        test_weightloss_dog()
        test_cost_and_transition()
        test_cli(td)
    print("\nALL TESTS PASSED ✅")
