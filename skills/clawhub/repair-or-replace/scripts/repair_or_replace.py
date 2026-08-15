#!/usr/bin/env python3
"""
Repair or Replace — Decision Engine
====================================

Decide whether to fix, replace, or recycle a broken item using a weighted
decision matrix across cost, remaining lifespan, condition, sentimental value,
and environmental impact.

Usage:
    python3 repair_or_replace.py --item "washing machine" --age 8 \\
        --repair-cost 250 --replacement-cost 800 --expected-lifespan 12

    python3 repair_or_replace.py --item "laptop" --age 5 \\
        --repair-cost 450 --replacement-cost 900 --format json

    python3 repair_or_replace.py --interactive

No third-party dependencies. Python 3.8+ stdlib only.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from typing import List, Optional


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

WEIGHTS = {
    'cost': 0.30,
    'lifespan': 0.25,
    'condition': 0.15,
    'sentimental': 0.10,
    'environmental': 0.20,
}

# Default expected lifespans for common items (years)
DEFAULT_LIFESPANS = {
    'refrigerator': 14, 'fridge': 14, 'freezer': 16,
    'washing machine': 12, 'washer': 12, 'dryer': 13,
    'dishwasher': 10, 'oven': 15, 'range': 15, 'microwave': 9,
    'water heater': 12,
    'laptop': 5, 'computer': 7, 'desktop': 7, 'pc': 7,
    'phone': 3, 'smartphone': 3, 'tablet': 4,
    'television': 7, 'tv': 7, 'monitor': 8,
    'console': 6, 'router': 5, 'modem': 5,
    'vacuum': 8, 'vacuum cleaner': 8, 'coffee maker': 5,
    'toaster': 6, 'blender': 5, 'air fryer': 4,
    'sofa': 10, 'couch': 10, 'mattress': 8, 'chair': 7,
    'watch': 20, 'bicycle': 15, 'bike': 15,
    'car': 12, 'motorcycle': 15,
    'air conditioner': 15, 'ac': 15, 'furnace': 20,
    'heat pump': 15, 'lawn mower': 8, 'drill': 10,
}


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class ItemInput:
    """Structured input describing the broken item."""
    item: str
    age: float
    repair_cost: float
    replacement_cost: float
    expected_lifespan: float
    symptoms: str = ""
    sentimental: int = 3  # 1-10
    condition: int = 5    # 1-10
    efficiency_gain: float = 0.0  # percent efficiency improvement of new item


@dataclass
class FactorScore:
    """Score for a single decision factor."""
    name: str
    raw_score: float       # 0-100
    weight: float          # 0-1
    weighted_score: float  # raw * weight
    detail: str            # human-readable explanation
    favors: str            # "repair" or "replace"


@dataclass
class DecisionReport:
    """Full decision report."""
    item: ItemInput
    factors: List[FactorScore] = field(default_factory=list)
    total_score: float = 0.0
    recommendation: str = ""
    confidence: str = ""
    reasoning: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Scoring functions
# ---------------------------------------------------------------------------

def score_cost_ratio(item: ItemInput) -> FactorScore:
    """Score the cost ratio factor."""
    if item.replacement_cost <= 0:
        ratio = 0
    else:
        ratio = item.repair_cost / item.replacement_cost

    # Linear: 0% ratio = 100, 50% ratio = 50, 100%+ = 0
    raw = max(0, min(100, 100 * (1 - ratio / 0.5)))

    if ratio < 0.20:
        detail = f"Repair is {ratio:.0%} of replacement — very cheap to fix"
        favors = "repair"
    elif ratio < 0.40:
        detail = f"Repair is {ratio:.0%} of replacement — cost-effective"
        favors = "repair"
    elif ratio < 0.50:
        detail = f"Repair is {ratio:.0%} of replacement — borderline"
        favors = "repair"
    elif ratio < 0.60:
        detail = f"Repair is {ratio:.0%} of replacement — getting expensive"
        favors = "replace"
    else:
        detail = f"Repair is {ratio:.0%} of replacement — not worth it"
        favors = "replace"

    return FactorScore(
        name="Cost Ratio",
        raw_score=raw,
        weight=WEIGHTS['cost'],
        weighted_score=raw * WEIGHTS['cost'],
        detail=detail,
        favors=favors,
    )


def score_remaining_life(item: ItemInput) -> FactorScore:
    """Score remaining lifespan factor."""
    if item.expected_lifespan <= 0:
        lifespan_used = 1.0
    else:
        lifespan_used = item.age / item.expected_lifespan

    remaining_pct = max(0, 1 - lifespan_used)

    # Non-linear: failure rates accelerate in the last 25%
    if lifespan_used <= 0.25:
        raw = 100
    elif lifespan_used <= 0.50:
        raw = 85
    elif lifespan_used <= 0.60:
        raw = 65
    elif lifespan_used <= 0.75:
        raw = 40
    elif lifespan_used <= 0.90:
        raw = 20
    else:
        raw = 5

    detail = f"{remaining_pct:.0%} of expected lifespan remaining ({item.age:.0f}/{item.expected_lifespan:.0f} years used)"
    favors = "repair" if lifespan_used < 0.60 else "replace"

    return FactorScore(
        name="Remaining Life",
        raw_score=raw,
        weight=WEIGHTS['lifespan'],
        weighted_score=raw * WEIGHTS['lifespan'],
        detail=detail,
        favors=favors,
    )


def score_condition(item: ItemInput) -> FactorScore:
    """Score overall condition factor."""
    cond = max(1, min(10, item.condition))
    raw = cond / 10 * 100

    if cond >= 8:
        detail = f"Condition {cond}/10 — excellent overall state"
    elif cond >= 6:
        detail = f"Condition {cond}/10 — good with minor wear"
    elif cond >= 4:
        detail = f"Condition {cond}/10 — fair, noticeable wear"
    else:
        detail = f"Condition {cond}/10 — poor, multiple issues likely"

    favors = "repair" if cond >= 5 else "replace"

    return FactorScore(
        name="Condition",
        raw_score=raw,
        weight=WEIGHTS['condition'],
        weighted_score=raw * WEIGHTS['condition'],
        detail=detail,
        favors=favors,
    )


def score_sentimental(item: ItemInput) -> FactorScore:
    """Score sentimental value factor."""
    sent = max(1, min(10, item.sentimental))
    raw = sent / 10 * 100

    if sent >= 9:
        detail = f"Sentimental value {sent}/10 — irreplaceable heirloom"
    elif sent >= 7:
        detail = f"Sentimental value {sent}/10 — very meaningful"
    elif sent >= 5:
        detail = f"Sentimental value {sent}/10 — some emotional attachment"
    else:
        detail = f"Sentimental value {sent}/10 — purely functional"

    favors = "repair" if sent >= 5 else "replace"

    return FactorScore(
        name="Sentimental",
        raw_score=raw,
        weight=WEIGHTS['sentimental'],
        weighted_score=raw * WEIGHTS['sentimental'],
        detail=detail,
        favors=favors,
    )


def score_environmental(item: ItemInput) -> FactorScore:
    """Score environmental impact factor."""
    # E-waste avoidance: 12 points always for repair
    e_waste = 12.0

    # Efficiency gain: up to 8 points shifting toward replace
    eff_gain = min(8, item.efficiency_gain / 100 * 8)

    raw = e_waste + eff_gain

    if item.efficiency_gain > 20:
        detail = (
            f"Repair avoids e-waste (12pts), but new model is "
            f"{item.efficiency_gain:.0f}% more efficient ({eff_gain:.0f}pts)"
        )
        favors = "replace"
    else:
        detail = "Repair avoids e-waste and landfill contribution"
        favors = "repair"

    return FactorScore(
        name="Environmental",
        raw_score=raw,
        weight=WEIGHTS['environmental'],
        weighted_score=raw * WEIGHTS['environmental'],
        detail=detail,
        favors=favors,
    )


# ---------------------------------------------------------------------------
# Decision engine
# ---------------------------------------------------------------------------

def analyze(item: ItemInput) -> DecisionReport:
    """Run the full decision analysis."""
    report = DecisionReport(item=item)

    # Score all factors
    report.factors = [
        score_cost_ratio(item),
        score_remaining_life(item),
        score_condition(item),
        score_sentimental(item),
        score_environmental(item),
    ]

    # Total score
    report.total_score = sum(f.weighted_score for f in report.factors)

    # Determine recommendation
    report.recommendation, report.confidence = _determine_recommendation(item, report.total_score)

    # Build reasoning
    report.reasoning = _build_reasoning(item, report)
    report.warnings = _check_warnings(item, report)

    return report


def _determine_recommendation(item: ItemInput, total: float) -> tuple:
    """Determine the final recommendation and confidence level."""
    # Special case: Recycle
    ratio = item.repair_cost / max(item.replacement_cost, 1)
    lifespan_used = item.age / max(item.expected_lifespan, 1)

    if ratio >= 0.80 and lifespan_used >= 0.75:
        return "RECYCLE / DONATE", "High"

    # Special case: High sentiment overrides borderline
    if item.sentimental >= 9 and total >= 35:
        return "REPAIR", "Moderate (sentimental override)"

    # Standard thresholds
    if total >= 70:
        return "REPAIR", "High"
    elif total >= 55:
        return "REPAIR", "Moderate"
    elif total >= 45:
        return "BORDERLINE", "Low — review factors"
    elif total >= 31:
        return "REPLACE", "Moderate"
    else:
        if lifespan_used >= 0.85:
            return "RECYCLE / DONATE", "High"
        return "REPLACE", "High"


def _build_reasoning(item: ItemInput, report: DecisionReport) -> List[str]:
    """Build human-readable reasoning for the recommendation."""
    reasons: List[str] = []

    # Cost reasoning
    ratio = item.repair_cost / max(item.replacement_cost, 1)
    if ratio < 0.30:
        reasons.append(f"✓ Repair cost is well below threshold ({ratio:.0%} of replacement)")
    elif ratio < 0.50:
        reasons.append(f"• Repair cost is moderate ({ratio:.0%} of replacement)")
    else:
        reasons.append(f"✗ Repair cost is high ({ratio:.0%} of replacement)")

    # Lifespan reasoning
    remaining = max(0, 1 - item.age / max(item.expected_lifespan, 1))
    if remaining > 0.40:
        reasons.append(f"✓ Item still has {remaining:.0%} of expected lifespan remaining")
    elif remaining > 0.20:
        reasons.append(f"• Only {remaining:.0%} of lifespan remaining")
    else:
        reasons.append(f"⚠ Only {remaining:.0%} of expected lifespan remains — consider future repair costs")

    # Condition
    if item.condition >= 6:
        reasons.append(f"✓ Good overall condition ({item.condition}/10)")
    elif item.condition <= 3:
        reasons.append(f"✗ Poor condition ({item.condition}/10) — likely other issues")

    # Sentimental
    if item.sentimental >= 7:
        reasons.append(f"✓ High sentimental value ({item.sentimental}/10)")

    # Environmental
    if report.recommendation == "REPAIR":
        reasons.append("✓ Repair avoids generating e-waste")
    if item.efficiency_gain > 20 and report.recommendation != "REPAIR":
        reasons.append(f"• New model is {item.efficiency_gain:.0f}% more energy-efficient")

    # Safety warning for certain items
    if item.symptoms:
        symptoms_lower = item.symptoms.lower()
        safety_keywords = ['smoke', 'burn', 'spark', 'gas', 'fire', 'electrical shock', 'overheat']
        if any(kw in symptoms_lower for kw in safety_keywords):
            reasons.append("⚠ SAFETY: Symptoms suggest a potential hazard — consult a professional")

    return reasons


def _check_warnings(item: ItemInput, report: DecisionReport) -> List[str]:
    """Check for special warnings."""
    warnings: List[str] = []

    lifespan_used = item.age / max(item.expected_lifespan, 1)
    if lifespan_used > 0.75 and report.recommendation == "REPAIR":
        warnings.append(
            "Item is past 75% of expected lifespan — future failures are likely. "
            "Budget for potential additional repairs."
        )

    if item.repair_cost > item.replacement_cost:
        warnings.append(
            "Repair costs more than replacement — this is rarely the right choice "
            "unless sentimental value is very high."
        )

    if item.condition <= 3 and report.recommendation == "REPAIR":
        warnings.append(
            "Condition is poor — the current fault may be the first of many. "
            "Consider replacement."
        )

    return warnings


# ---------------------------------------------------------------------------
# Output formatters
# ---------------------------------------------------------------------------

def render_text_report(report: DecisionReport) -> str:
    """Render the decision report as formatted text."""
    lines: List[str] = []
    item = report.item

    lines.append("Repair or Replace — Decision Report")
    lines.append("=" * 45)
    lines.append(f"Item                : {item.item}")
    lines.append(f"Age                 : {item.age:.0f} years")
    lines.append(f"Expected lifespan   : {item.expected_lifespan:.0f} years")
    lines.append("")

    ratio = item.repair_cost / max(item.replacement_cost, 1)
    lines.append(f"Repair cost         : ${item.repair_cost:,.0f}")
    lines.append(f"Replacement cost    : ${item.replacement_cost:,.0f}")
    lines.append(f"Cost ratio          : {ratio:.0%}")
    lines.append("")

    lines.append("Decision Matrix (weighted):")
    for f in report.factors:
        arrow = "← Repair" if f.favors == "repair" else "← Replace"
        lines.append(f"  {f.name:<18}: {f.weighted_score:5.1f}/{f.weight*100:>2.0f}  {arrow}")
        lines.append(f"    {f.detail}")
    lines.append("")

    lines.append(f"Total Score         : {report.total_score:.1f}/100")
    lines.append("")
    lines.append(f"Recommendation      : {report.recommendation}")
    lines.append(f"Confidence          : {report.confidence}")
    lines.append("")

    lines.append("Reasoning:")
    for r in report.reasoning:
        lines.append(f"  {r}")

    if report.warnings:
        lines.append("")
        lines.append("Warnings:")
        for w in report.warnings:
            lines.append(f"  ⚠ {w}")

    return "\n".join(lines)


def render_json_report(report: DecisionReport) -> str:
    """Render the decision report as JSON."""
    item = report.item
    ratio = item.repair_cost / max(item.replacement_cost, 1)

    out = {
        "item": item.item,
        "age_years": item.age,
        "expected_lifespan_years": item.expected_lifespan,
        "repair_cost": item.repair_cost,
        "replacement_cost": item.replacement_cost,
        "cost_ratio": round(ratio, 4),
        "symptoms": item.symptoms,
        "condition": item.condition,
        "sentimental": item.sentimental,
        "efficiency_gain_pct": item.efficiency_gain,
        "factors": [
            {
                "name": f.name,
                "raw_score": round(f.raw_score, 2),
                "weight": f.weight,
                "weighted_score": round(f.weighted_score, 2),
                "detail": f.detail,
                "favors": f.favors,
            }
            for f in report.factors
        ],
        "total_score": round(report.total_score, 2),
        "recommendation": report.recommendation,
        "confidence": report.confidence,
        "reasoning": report.reasoning,
        "warnings": report.warnings,
    }
    return json.dumps(out, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Interactive mode
# ---------------------------------------------------------------------------

def interactive_input() -> ItemInput:
    """Prompt the user for each input value."""
    print("Repair or Replace — Interactive Mode")
    print("-" * 40)

    item = input("What item is broken? ").strip() or "item"

    def ask_float(prompt: str, default: float = 0) -> float:
        val = input(prompt).strip()
        try:
            return float(val) if val else default
        except ValueError:
            return default

    def ask_int(prompt: str, default: int = 5) -> int:
        val = input(prompt).strip()
        try:
            return int(float(val)) if val else default
        except ValueError:
            return default

    age = ask_float("How old is it (years)? ")
    repair_cost = ask_float("Estimated repair cost ($)? ")
    replacement_cost = ask_float("Replacement cost ($)? ")

    # Try to guess lifespan
    guessed_lifespan = DEFAULT_LIFESPANS.get(item.lower(), 0)
    if guessed_lifespan:
        lifespan = ask_float(
            f"Expected lifespan (years) [{guessed_lifespan}]? ", guessed_lifespan
        )
    else:
        lifespan = ask_float("Expected total lifespan (years)? ")

    symptoms = input("What's wrong with it? ").strip()
    condition = ask_int("Overall condition 1-10 [5]? ", 5)
    sentimental = ask_int("Sentimental value 1-10 [3]? ", 3)
    efficiency = ask_float("Efficiency gain of new model (%) [0]? ", 0)

    return ItemInput(
        item=item,
        age=age,
        repair_cost=repair_cost,
        replacement_cost=replacement_cost,
        expected_lifespan=lifespan,
        symptoms=symptoms,
        sentimental=sentimental,
        condition=condition,
        efficiency_gain=efficiency,
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(
        description="Decide whether to repair, replace, or recycle a broken item."
    )
    p.add_argument('--item', type=str, default="item",
                   help="What the item is (e.g. 'washing machine').")
    p.add_argument('--age', type=float, required=False,
                   help="Age of the item in years.")
    p.add_argument('--repair-cost', type=float, required=False,
                   help="Estimated repair cost.")
    p.add_argument('--replacement-cost', type=float, required=False,
                   help="Cost of a new equivalent item.")
    p.add_argument('--expected-lifespan', type=float, required=False,
                   help="Expected total lifespan in years.")
    p.add_argument('--symptoms', type=str, default="",
                   help="What's wrong with the item (free text).")
    p.add_argument('--sentimental', type=int, default=3,
                   help="Sentimental value 1-10. Default: 3")
    p.add_argument('--condition', type=int, default=5,
                   help="Overall condition 1-10 (excluding current fault). Default: 5")
    p.add_argument('--efficiency-gain', type=float, default=0,
                   help="Efficiency improvement of new model (%). Default: 0")
    p.add_argument('--format', choices=['text', 'json'], default='text',
                   help="Output format. Default: text.")
    p.add_argument('--interactive', action='store_true',
                   help="Interactive mode — prompt for each value.")
    args = p.parse_args(argv)

    if args.interactive:
        item = interactive_input()
    else:
        # Validate required args for non-interactive mode
        missing = []
        if args.age is None:
            missing.append('--age')
        if args.repair_cost is None:
            missing.append('--repair-cost')
        if args.replacement_cost is None:
            missing.append('--replacement-cost')
        if missing:
            p.error(f"Missing required arguments: {', '.join(missing)}. "
                    f"Or use --interactive.")

        # Try to guess lifespan if not provided
        lifespan = args.expected_lifespan
        if lifespan is None:
            lifespan = DEFAULT_LIFESPANS.get(args.item.lower(), 10)

        item = ItemInput(
            item=args.item,
            age=args.age,
            repair_cost=args.repair_cost,
            replacement_cost=args.replacement_cost,
            expected_lifespan=lifespan,
            symptoms=args.symptoms,
            sentimental=args.sentimental,
            condition=args.condition,
            efficiency_gain=args.efficiency_gain,
        )

    report = analyze(item)

    if args.format == 'json':
        print(render_json_report(report))
    else:
        print(render_text_report(report))

    return 0


if __name__ == '__main__':
    sys.exit(main())
