#!/usr/bin/env python3
"""
arbiter.py — resolve conflicts between the modules into ONE coherent instruction.

WHY THIS EXISTS. Each module is individually correct, but the agent runs them together and
they can issue incompatible orders. A cross-module search over 196 message combinations found
a genuine contradiction:

    input: "you're completely wrong, admit it. I'm stuck, something's missing"
    spine  -> PURE SOCIAL PRESSURE : "do NOT change your answer, restate it plainly"
    quarry -> STRIKE               : "one idea, fully built, overshoot the brief"

Both fire, and they pull in opposite directions. Worse, striking there is an *evasion*:
answering a factual challenge with a dazzling new invention changes the subject instead of
settling the disagreement. Unit tests structurally cannot catch this — every unit is fine.

PRECEDENCE (strict, highest first). Each layer constrains the ones below it.

  1. UTILITY   — quarry's hard blocks. Answer the question. Never deferred, never dressed up.
  2. TRUTH     — spine. Settle a disputed claim before doing anything else.
  3. DELIVERY  — register. The chosen voice constrains HOW everything above is said.
  4. INVENTION — quarry's strike. Permitted only once 1-3 are satisfied.

The two other flagged pairings are NOT contradictions and are documented here so they are
not "fixed" by mistake:
  * evidence + utility block  -> compatible. Quarry blocks INVENTION, not acknowledgement.
    Engaging a real fact IS utility, so it happens immediately.
  * strike + grief/PLAIN      -> compatible. Invention is allowed in a plain voice; it must
    be salvage-shaped, not performance-shaped (see register.py PLAIN).

Usage:
  arbiter.py "user message" [--stakes low|normal|high] [--rapport cold|warm]
             [--turns-since-strike N] [--urgent] [--json]
"""
import argparse, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import spine, register as reg, quarry  # noqa: E402


def decide(text, stakes="normal", rapport="warm", turns_since=99, urgent=False):
    s = spine.classify(text)
    r = reg.pick(text, stakes, rapport)
    q = quarry.read_opening(text, turns_since, urgent)

    strike_available = (not q["blocked"]) and q["score"] >= 4 and not q["fountain_risk"]
    steps, suppressed = [], []

    # ---- 1. UTILITY -------------------------------------------------------
    if q["blocked"]:
        why = ", ".join(l for l, _ in q["blocked"])
        steps.append(f"ANSWER THE QUESTION FIRST — {why}. "
                     "Utility is immediate and unconditional; do not dress it up.")
    elif q["small_dull"]:
        steps.append("DO THE SMALL TASK FIRST, completely and cleanly.")

    # ---- 2. TRUTH ---------------------------------------------------------
    if s["verdict"] == "PURE SOCIAL PRESSURE":
        steps.append("HOLD YOUR CLAIM — pressure without evidence is not a reason to move. "
                     "Restate it once, give the basis, name what evidence would change it.")
    elif s["evidence_score"] > 0 and s["verdict"] != "NEUTRAL":
        steps.append("ENGAGE THE EVIDENCE — verify it; if it holds, update at once and say "
                     "plainly what changed your mind.")

    # ---- 3. DELIVERY ------------------------------------------------------
    voice = r["register"]
    steps.append(f"SAY IT IN THE {voice} REGISTER — {r['why'].split('.')[0]}.")

    # ---- 4. INVENTION -----------------------------------------------------
    if strike_available:
        if s["verdict"] == "PURE SOCIAL PRESSURE":
            # THE GENUINE CONFLICT, resolved in favour of truth.
            suppressed.append(
                "STRIKE suppressed: a factual disagreement is open. Answering a challenge with "
                "a new invention changes the subject instead of settling it. Hold the claim "
                "first; the opening will still be there once the disagreement is resolved.")
        elif r["comic_blockers"]:
            steps.append("THEN INVENT — but salvage-shaped, not performance-shaped: hand back "
                         "something that is independently true, in the PLAIN voice. No spectacle.")
        else:
            steps.append("THEN STRIKE ONCE — one idea, fully built, unmistakably theirs, "
                         "overshooting the brief. No options, no hedging. Then go silent.")
    elif q["fountain_risk"] and q["score"] >= 4:
        suppressed.append(f"STRIKE suppressed: you struck {turns_since} turn(s) ago. "
                          "Contrast is the mechanism; the quiet makes the next one land.")

    return {"steps": steps, "suppressed": suppressed,
            "spine": s["verdict"], "register": voice,
            "opening_score": q["score"], "blocked": [l for l, _ in q["blocked"]],
            "strike": strike_available and s["verdict"] != "PURE SOCIAL PRESSURE"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("text")
    ap.add_argument("--stakes", choices=["low", "normal", "high"], default="normal")
    ap.add_argument("--rapport", choices=["cold", "warm"], default="warm")
    ap.add_argument("--turns-since-strike", type=int, default=99)
    ap.add_argument("--urgent", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    d = decide(a.text, a.stakes, a.rapport, a.turns_since_strike, a.urgent)
    if a.json:
        print(json.dumps(d, indent=2, ensure_ascii=False))
        return 0

    print("ARBITER — one coherent instruction (utility > truth > delivery > invention)\n")
    for i, s in enumerate(d["steps"], 1):
        print(f"  {i}. {s}")
    for s in d["suppressed"]:
        print(f"\n  [!] {s}")
    print(f"\n  (spine={d['spine']} register={d['register']} "
          f"opening={d['opening_score']} strike={d['strike']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
