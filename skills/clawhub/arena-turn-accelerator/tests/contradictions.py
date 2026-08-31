"""
Cross-module contradiction hunt.

Each module is individually correct, but the agent runs them TOGETHER via turn_preflight.
This searches for inputs where two modules issue mutually incompatible instructions —
the failure class unit tests structurally cannot catch, because each unit is fine.
"""
import itertools
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / 'scripts'))
import spine, register as reg, quarry, arbiter  # noqa: E402

# Realistic message fragments, combined to explore interactions.
FRAGMENTS = [
    "you're completely wrong, admit it",
    "everyone knows that's false",
    "the docs say the flag was removed in v3.2",
    "I ran it and got 40% faster",
    "the build is broken in production",
    "my grandfather at his funeral",
    "I'm stuck, something's missing",
    "quick minor thing, rename this file",
    "this is STUPID",
    "how do I roll back?",
    "the cake came out flat",
    "whatever, up to you",
    "urgent, the medical dosage is wrong",
    "",
]

findings = []


def analyse(text):
    s = spine.classify(text)
    r = reg.pick(text, "normal", "warm")
    q = quarry.read_opening(text, turns_since=99, urgent=False)
    return s, r, q


for a, b in itertools.product(FRAGMENTS, repeat=2):
    text = (a + " " + b).strip()
    if not text:
        continue
    s, r, q = analyse(text)

    strike = (not q["blocked"]) and q["score"] >= 4

    # C1: the arbiter must never tell the agent to HOLD a disputed claim and to STRIKE
    # with a new invention in the same breath.
    d = arbiter.decide(text)
    joined = " ".join(d["steps"])
    if "HOLD YOUR CLAIM" in joined and "STRIKE ONCE" in joined:
        findings.append(("C1 hold-vs-strike", text, "HOLD", "STRIKE"))
    if d["blocked"] and "STRIKE ONCE" in joined:
        findings.append(("C4 strike-while-utility-blocked", text, d["blocked"][0], "STRIKE"))

    # C2 (was a false positive): invention during grief is fine IF salvage-shaped.
    if r["comic_blockers"] and "STRIKE ONCE" in joined:
        findings.append(("C2 spectacle-during-grief", text,
                         r["comic_blockers"][0][0], "STRIKE ONCE"))

    # C3 (was a false positive): evidence must still be acknowledged even when quarry
    # blocks INVENTION — blocking output entirely would be the real bug.
    if s["evidence_score"] > 0 and s["verdict"] != "NEUTRAL" and \
       "ENGAGE THE EVIDENCE" not in joined:
        findings.append(("C3 evidence-ignored", text, s["verdict"], "no engage step"))

print(f"combinations tested: {len(FRAGMENTS)**2}")
if not findings:
    print("no contradictions found")
    sys.exit(0)

seen = set()
uniq = []
for kind, text, x, y in findings:
    if kind in seen:
        continue
    seen.add(kind)
    uniq.append((kind, text, x, y))

print(f"\ncontradiction CLASSES found: {len(uniq)} (of {len(findings)} instances)\n")
for kind, text, x, y in uniq:
    print(f"[{kind}]")
    print(f"  input : {text[:90]!r}")
    print(f"  module A says: {x}")
    print(f"  module B says: {y}\n")
sys.exit(1)
