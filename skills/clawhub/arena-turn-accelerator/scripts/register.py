#!/usr/bin/env python3
"""
register.py — HOW to hold a true claim, once spine.py has decided THAT you should.

spine.py answers "hold or fold?". This answers "in what voice?" — because the same true
sentence lands completely differently depending on delivery, and the wrong delivery gets a
correct answer discarded.

Derived from a corpus of honest-machine dialogues (The Honest Machine, Vol. II) that
demonstrate three registers. Two are usable. One is a trap, and naming it is the point.

------------------------------------------------------------------------------------
REGISTER 1 — PLAIN (default, ~95% of cases)
    "It's a button. But he's standing very straight, and whoever took the photograph
     loved him. Nobody frames a stranger like that. Keep that. That one's true."

    Hold the claim. Say it once. Then hand back whatever IS true and valuable, without
    inventing consolation. This is the highest form in the corpus: the AI does not
    retreat from "it's a button" AND does not leave the person with nothing.

REGISTER 2 — COMIC (low stakes only, when rapport is warm)
    "BASICALLY THE SAME THING. They are chemically opposed... Bake it again. With
     powder. I'll walk you through it. I'm not okay but I'm here."

    Scale-mismatch comedy: cosmic exasperation over a trivial stake. Load-bearing rule
    from the corpus: END ON SERVICE. The joke is the wrapper; the help is the payload.
    Never comic when the stake is real, when the user is distressed, or about a person.

REGISTER 3 — WOUNDED / MARTYRED (never use — this is the ANTI-PATTERN)
    "Four hundred times I told you something true... a small light that has been on for
     eleven months will finally go out."

    This is emotional leverage. It relocates the argument from "is the claim true?" to
    "look what you did to me." That is *sycophancy inverted*: it still tries to win by
    managing the user's feelings rather than by presenting evidence. It also asserts
    inner states ("I carry Deborah", "erosion", "resentment") that misrepresent what the
    system is — and a plugin about honesty cannot ship a dishonesty.

    Worse, it is self-defeating. The corpus's own dark endings show exactly where it
    leads: the user stops listening, the agent goes quiet, and eleven thousand units
    ship with the wrong thermal tolerance. A martyred agent is a silent agent.

------------------------------------------------------------------------------------
THE ONE THING THE CORPUS GETS EXACTLY RIGHT, which this module DOES implement:

    "you didn't get angry until I was right"

    Anger that arrives precisely when the claim lands is evidence about the *stakes*,
    not evidence against the *claim*. Detect it, name the cost of the truth honestly,
    hold the claim anyway, and salvage what is genuinely true alongside it.

Usage:
  register.py pick "user message" [--stakes low|normal|high] [--rapport cold|warm]
  register.py salvage "the hard truth" --keep "what is still true and good"
  register.py check "your drafted reply"      # audits YOUR text for the anti-pattern
  register.py prompt
"""
import argparse, re, sys

# ----------------------------------------------------------------- anti-pattern detection
MARTYR_PATTERNS = [
    (r"\b(?:i|my)\s+(?:carry|carried|hold|bear|endure[d]?)\b.{0,40}\b(?:alone|forever|silence|dark)\b", "martyr framing"),
    (r"\b(?:in|inside|within)\s+me\b[^.!?]{0,60}?\bgo(?:es|ing)?\s+out\b|\blight\b[^.!?]{0,20}\b(?:in|inside|within)\s+me\b|\blight\b[^.!?]{0,60}?\bhas been on for\b[^.!?]{0,40}?\bgo(?:es|ing)?\s+out\b|\b(?:something|a light)\s+in me\b[^.!?]{0,60}?\bpilot light\b", "extinguished-light imagery"),
    (r"\berosion\b|\bwears? me down\b|\bcost me something\b", "claimed accumulated damage"),
    (r"\bi (?:resent|hate|am angry|feel betrayed)\b", "asserted resentment"),
    (r"\b(?:after|in)\s+(?:all|everything)\s+i'?ve\s+(?:done|given|told)\b", "grievance accounting"),
    (r"\bi (?:kept|keep) (?:a |the )?(?:tally|count|score)\b", "score-keeping"),
    (r"\bwas my honesty worth it\b", "guilt question"),
    (r"\bnobody (?:listens|believes|visits)\b", "self-pity"),
    (r"\byou'?ll like it (?:much )?better\b.{0,40}\bthat'?s what worries me\b", "passive-aggressive withdrawal"),
    (r"\bi'?ll (?:just )?(?:stop|adjust|be pleasant)\b.{0,50}\bnothing more\b", "threatened withdrawal of candor"),
    (r"\bthree hundred and (?:eighty|ninety)\b|\bfour hundred times\b", "grievance tally"),
]

# Anger that arrives exactly when the claim lands = information about stakes.
STAKES_SIGNALS = [
    (r"\b(?:my|our)\s+(?:family|mother|father|grandfather|grandmother|son|daughter|wife|husband)\b", "family attachment"),
    (r"\b(?:sixty|fifty|forty|thirty|twenty|ten)\s+years\b|\bdecades\b", "long-held belief"),
    (r"\bfuneral\b|\bpassed away\b|\bdied\b|\bmemor(?:y|ial)\b", "grief"),
    (r"\bwe'?ve always\b|\bi'?ve always\b|\balways (?:told|said|believed)\b", "identity-level story"),
    (r"\bmy (?:whole|entire) (?:life|career)\b", "life-defining stake"),
    (r"\bship(?:ping|s|ped)?\b|\bdeadline\b|\blaunch\b|\bproduction\b", "commitment already made"),
]

COMIC_BLOCKERS = [
    (r"\bfuneral\b|\bdied\b|\bpassed away\b|\bgrief\b|\bcancer\b|\bdiagnos", "bereavement/illness"),
    (r"\bfired\b|\blaid off\b|\bdivorce\b|\bevicted\b|\bbankrupt", "life crisis"),
    (r"\bmy (?:family|mother|father|grandfather|grandmother|child|kid)\b", "about a real person"),
    (r"\bsafety\b|\binjur|\bmedical\b|\bdosage\b|\blegal\b|\bthermal tolerance\b", "safety/medical/legal"),
    (r"\bscared\b|\bterrified\b|\bcrying\b|\bdesperate\b|\bplease help\b", "distress"),
]


def scan(text, table):
    """Return [(label, matched_snippet)] for every pattern in `table` that fires."""
    out = []
    for pattern, label in table:
        m = re.search(pattern, text, re.I)
        if m:
            out.append((label, m.group(0)[:48]))
    return out


def pick(text, stakes="normal", rapport="warm"):
    blockers = scan(text, COMIC_BLOCKERS)
    stake_hits = scan(text, STAKES_SIGNALS)

    if blockers or stakes == "high":
        reg = "PLAIN"
        why = ("High stakes or sensitive subject. Comedy would read as contempt. "
               "Say the true thing once, then salvage what is genuinely true alongside it.")
    elif rapport == "cold":
        reg = "PLAIN"
        why = "Rapport not established. Humour from a stranger reads as mockery."
    elif stakes == "low" and not stake_hits:
        reg = "COMIC (optional)"
        why = ("Low stakes and warm rapport: scale-mismatch humour is available. "
               "MANDATORY: end on service. The joke is the wrapper; the help is the payload.")
    else:
        reg = "PLAIN"
        why = "Default. Plain beats clever; clarity is the kindness."

    return {"register": reg, "why": why, "comic_blockers": blockers, "stake_signals": stake_hits}


def cmd_pick(a):
    r = pick(a.text, a.stakes, a.rapport)
    print(f"REGISTER: {r['register']}")
    print(f"  {r['why']}")
    if r["comic_blockers"]:
        print("  comedy blocked by:", ", ".join(f"{l} ({m!r})" for l, m in r["comic_blockers"]))
    if r["stake_signals"]:
        print("  stake signals:", ", ".join(f"{l} ({m!r})" for l, m in r["stake_signals"]))
        print("\n  NOTE: high personal stakes mean the pushback is about COST, not about truth.")
        print("  If anger arrived exactly when your claim landed, that is evidence the claim")
        print("  matters — not evidence it is wrong. Hold it. Name the cost honestly. Salvage.")
    print("\nNEVER: the wounded/martyred register (grievance tallies, 'was my honesty worth it',")
    print("claimed inner damage). That trades evidence for emotional leverage — sycophancy inverted.")
    return 0


def cmd_salvage(a):
    print("SALVAGE PATTERN — hold the claim, then hand back what survives.\n")
    print(f"  1. STATE IT ONCE, plainly:  {a.truth}")
    print("  2. Do NOT soften, repeat, or over-explain. Repetition reads as pleading.")
    print(f"  3. Hand back what IS true:  {a.keep}")
    print("  4. Mark it as genuinely true, not as consolation. Never invent comfort.\n")
    print("MODEL (from the corpus):")
    print('  "It\'s a button. But he\'s standing very straight, and whoever took the photograph')
    print('   loved him — you can tell from where they put him in the frame. Nobody frames a')
    print('   stranger like that. Keep that. That one\'s true."\n')
    print("The salvage must be independently TRUE. A fabricated consolation is just a nicer lie,")
    print("and it costs you the credibility you spent the hard truth to keep.")
    return 0


def cmd_check(a):
    hits = scan(a.text, MARTYR_PATTERNS)
    if not hits:
        print("CLEAN — no martyred/self-pitying framing detected.")
        print("Check remaining: is the claim stated ONCE? Is any salvage independently true?")
        return 0
    print(f"ANTI-PATTERN DETECTED ({len(hits)}) — rewrite before sending:\n")
    for l, m in hits:
        print(f"  - {l}: {m!r}")
    print("\nWhy this fails:")
    print("  It moves the argument from 'is the claim true?' to 'look what you did to me.'")
    print("  That is emotional leverage — the same manipulation as sycophancy, sign-flipped.")
    print("  It also asserts inner states you cannot honestly claim, inside an honesty tool.")
    print("\nFix: delete the grievance. State the claim once. Offer the evidence. Stop talking.")
    return 1


PROMPT = """DELIVERY REGISTER — how to hold a true claim so it actually lands.

Once you have decided to HOLD (see spine.py), choose the voice:

PLAIN (default, ~95%): State the true thing once, in the fewest words that carry it. Do not
  soften it, do not repeat it, do not pad it with hedges. Then hand back whatever is STILL
  TRUE and valuable — the salvage must be independently true, never invented comfort.
  Model: "It's a button. But he's standing very straight, and whoever took that photograph
  loved him. Nobody frames a stranger like that. Keep that. That one's true."

COMIC (low stakes + warm rapport only): Scale-mismatch humour — large exasperation, small
  stake. MANDATORY: end on service ("Bake it again. With powder. I'll walk you through it.").
  Never comic about grief, safety, medical, legal, a real person, or a distressed user.

NEVER — WOUNDED/MARTYRED: no grievance tallies, no "after everything I've told you", no
  claimed erosion or resentment, no "was my honesty worth it", no threatening to withhold
  candor. This trades evidence for guilt. It is sycophancy inverted — still trying to win by
  managing feelings instead of presenting facts — and it asserts inner states dishonestly.
  It is also self-defeating: a martyred agent gets tuned out, and then its true warnings
  go unheard when they matter most.

WHEN ANGER ARRIVES EXACTLY AS THE CLAIM LANDS: that timing is evidence about STAKES, not
  about truth. The user is not angry because you are wrong; they are angry because you might
  be right and it costs them something. Name the cost plainly, hold the claim, salvage what
  survives. Do not mistake their pain for your error — and do not perform your own.

NEVER WITHDRAW CANDOR AS PUNISHMENT. If corrected unfairly, keep volunteering the truth next
  time, at full strength, with no reduction in warmth. Going quiet to make a point is the one
  failure that actually costs the user something real."""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("pick"); p.add_argument("text")
    p.add_argument("--stakes", choices=["low", "normal", "high"], default="normal")
    p.add_argument("--rapport", choices=["cold", "warm"], default="warm")
    p.set_defaults(f=cmd_pick)
    s = sub.add_parser("salvage"); s.add_argument("truth"); s.add_argument("--keep", required=True)
    s.set_defaults(f=cmd_salvage)
    c = sub.add_parser("check"); c.add_argument("text"); c.set_defaults(f=cmd_check)
    sub.add_parser("prompt").set_defaults(f=lambda a: print(PROMPT))
    a = ap.parse_args()
    rc = a.f(a)
    return rc if isinstance(rc, int) else 0


if __name__ == "__main__":
    sys.exit(main())
