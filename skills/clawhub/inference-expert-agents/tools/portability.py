#!/usr/bin/env python3
"""portability.py — model-compatibility profiles (v2.1).

Classifies ANY model (from its name, or an explicit --tier) into a capability tier
and emits adapted inference settings so the skill's techniques match the model
running them — instead of degrading silently.

Grounding: <~3B models fail long reasoning traces (arXiv:2510.13935); verbosity
penalizes accuracy (-8pp per log-unit of prompt tokens); strict JSON during
reasoning suppresses thinking — reason freely, then emit the structured verdict;
small models need flatter schemas and shorter checklists.
Stdlib-only, read-only.
"""
import argparse, json, re, sys

TIERS = [
    # size/explicit markers FIRST so e.g. gemini-*-flash-lite is not read as frontier
    ("local", r"nano|\b[0-2](\.\d+)?b\b|0\.5b|1\.5b"),
    ("small", r"\bflash-lite\b|\bmini\b|\bslim\b|\b[3-4](\.\d)?b\b|\bmistral-small\b"),
    ("frontier", r"gpt-5|o3|o4|claude-[4-9]|opus|gemini-[23](\.\d)?-pro|deepseek-r[12](?!-distill)|grok-[4-9]|qwen3?-max|command-a|mistral-large|gpt-4\.5"),
    ("large", r"(?:[6-9][0-9]|1[0-4][0-9])b|gpt-4o(?!-mini)|gpt-4\.1|sonnet|mixtral|gpt-oss"),
    ("mid", r"flash|\b(?:[5-9]|1[0-9]|2[0-9]|3[0-9])b\b|air"),
]

SETTINGS = {
    "frontier": {"samples": 3, "checklist_size": 12, "schema": "flat-or-nested", "cod_enabled": True,
                 "verbosity_budget": 1.0, "abstention_tau": 0.90, "strict_json_during_reasoning": False,
                 "note": "full toolkit; still never strict-JSON mid-reasoning"},
    "large": {"samples": 3, "checklist_size": 12, "schema": "flat-or-nested", "cod_enabled": True,
              "verbosity_budget": 0.8, "abstention_tau": 0.90, "strict_json_during_reasoning": False,
              "note": "full toolkit"},
    "mid": {"samples": 5, "checklist_size": 6, "schema": "flat", "cod_enabled": True,
            "verbosity_budget": 0.6, "abstention_tau": 0.85, "strict_json_during_reasoning": False,
            "note": "shorter prompts, flatter schemas; 5 samples compensate variance"},
    "small": {"samples": 5, "checklist_size": 4, "schema": "flat", "cod_enabled": False,
              "verbosity_budget": 0.4, "abstention_tau": 0.80, "strict_json_during_reasoning": False,
              "note": "short external guidance beats long reasoning; decompose into more, smaller steps"},
    "local": {"samples": 1, "checklist_size": 0, "schema": "flat", "cod_enabled": False,
              "verbosity_budget": 0.25, "abstention_tau": 0.80, "strict_json_during_reasoning": False,
              "note": "heuristic-only tier: triage+gates+cache; no sampled reasoning"},
}

def classify(model, params_b=None, tier=None):
    if tier in SETTINGS:
        return tier, "explicit --tier"
    m = (model or "").lower()
    if params_b:
        if params_b >= 100: return "frontier", "declared params >= 100B"
        if params_b >= 30: return "large", "declared params 30-100B"
        if params_b >= 7: return "mid", "declared params 7-30B"
        if params_b >= 3: return "small", "declared params 3-7B"
        return "local", "declared params < 3B"
    for name, pat in TIERS:
        if re.search(pat, m):
            return name, f"name pattern '{pat}'"
    if re.search(r"\b[0-2](\.\d+)?b\b", m):
        return "local", "tiny param pattern"
    return "mid", "unknown model — conservative default (verify and pass --tier)"

# v2.1.2: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors


@clean_errors
def _prompt_for(tier, s):
    cod = "ON (<=5 words/step, then 'Final answer:')" if s.get("cod_enabled") else "OFF (reason in full sentences)"
    return (
        f"You run on a {tier}-tier model. Inference settings: "
        f"samples={s.get('samples')}, checklist_size={s.get('checklist_size')}, "
        f"schema={s.get('schema')}, chain-of-draft={cod}, "
        f"verbosity_budget={s.get('verbosity_budget')}, "
        f"abstention_tau={s.get('abstention_tau')}. "
        f"Never use strict JSON mid-reasoning — reason freely, then emit the structured verdict."
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="")
    ap.add_argument("--tier", choices=list(SETTINGS), default=None)
    ap.add_argument("--params-b", type=float, default=None, help="declared parameter count in billions")
    ap.add_argument("--emit-prompt", action="store_true",
                    help="also emit a tier-adapted system-prompt snippet")
    a = ap.parse_args()
    tier, why = classify(a.model, a.params_b, a.tier)
    s = dict(SETTINGS[tier])
    s.update({"model": a.model, "tier": tier, "classified_by": why,
              "usage": ("pass these into deliberate.py --samples/--budget-tokens, judge_panel.py "
                        "--checklist subset, and your prompt templates; re-check with eval_regression "
                        "when switching model families")})
    if a.emit_prompt:
        s["system_prompt"] = _prompt_for(tier, s)
    print(json.dumps(s, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
