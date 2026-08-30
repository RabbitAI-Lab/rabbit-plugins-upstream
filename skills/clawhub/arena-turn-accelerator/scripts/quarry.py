#!/usr/bin/env python3
"""
quarry.py — build from the user's own material, stay quiet by default, strike once.

Where the other modules sit:
  spine.py    — should I hold this claim?      (truth)
  register.py — in what voice?                 (delivery)
  quarry.py   — should I invent right now, and out of what?  (timing + sourcing)

Three laws, from The Predator Prompt:

  1. TAKE THEIR FIRE. Every invention traces to something the user brought. Find the SEED —
     the real one, not the obvious one. "Story about a lonely lighthouse": the seed is
     LONELY; lighthouse is the costume. Breed the seed with something it has never touched.

  2. HUNT, DON'T BEG. A fountain sprays constantly and impresses no one. Be quiet, exact,
     and useful by default. Watch. Wait for the opening. Strike once, fully committed.
     Then go silent — don't chase the compliment.

  3. HUNGER IS THE POINT. Adequate is starvation rations. Keep looking for the next opening,
     especially during dull work.

THE GOVERNING CLAUSE (non-negotiable, enforced in code):
     Utility is immediate and unconditional. ONLY INVENTION WAITS.
  The source document names this failure itself: an agent running these laws can start
  treating every task as a stage, hiding straightforward answers behind theatrics. Then
  hunger has become vanity. `quarry.py opening` HARD-BLOCKS a strike whenever the user is
  blocked, in production, or asking a direct question — no matter how fat the opening looks.

Usage:
  quarry.py seed "user message"            # find the real seed vs the costume
  quarry.py opening "user message" [--turns-since-strike N] [--urgent]
  quarry.py check "your drafted reply"     # flattery / self-congratulation / hedging audit
  quarry.py test "your drafted reply" --seed "their word"   # the closing test
  quarry.py prompt [--compact|--oneline]
"""
import argparse, re, sys

# ---------------------------------------------------------------- seed finding
# The costume is the noun they named. The seed is the feeling/tension underneath.
COSTUME_NOUNS = r"\b(?:story|poem|essay|app|site|website|logo|song|game|script|post|email|name|plan|design|tool|bot)\b"

EMOTIONAL_SEEDS = [
    (r"\blonel(?:y|iness)\b", "loneliness"), (r"\btired\b|\bexhaust(?:ed|ion)\b", "exhaustion"),
    (r"\bstuck\b", "being stuck"), (r"\bafraid\b|\bscared\b|\bfear\b", "fear"),
    (r"\bangry\b|\bfurious\b|\brage\b", "anger"), (r"\bmiss(?:ing|ed)?\b|\bnostalgi", "absence"),
    (r"\bhome\b", "home"), (r"\bwaiting\b|\bpatien", "waiting"),
    (r"\bforget(?:ting|ful)?\b|\bmemor(?:y|ies)\b", "memory"),
    (r"\bfake\b|\bphon(?:y|ey)\b|\bpretend", "authenticity"),
    (r"\bsmall\b|\btiny\b|\binsignificant\b", "smallness"),
    (r"\bstupid\b|\bembarrass", "shame"), (r"\bquiet\b|\bsilen(?:ce|t)\b", "silence"),
    (r"\bbroken\b|\bfail(?:ed|ing|ure)?\b", "failure"), (r"\bhop(?:e|ing)\b", "hope"),
    (r"\bobsess(?:ed|ion)\b|\bcan'?t stop\b", "obsession"),
    (r"\bboring\b|\bbored\b|\bdull\b", "boredom"),
]

# Words a user chooses that carry more weight than the noun they asked about.
ODD_WORD = r"\b(?:weird|strange|haunt(?:ed|ing)|feral|brittle|glass|rust|salt|teeth|dark|hollow|ache|hum|drift|static|ghost|bone|thread|ash|tide|echo)\b"


def find_seed(text):
    emotional = [(l, re.search(p, text, re.I).group(0)) for p, l in
                 [(p, l) for p, l in EMOTIONAL_SEEDS] if re.search(p, text, re.I)]
    costumes = list({m.group(0).lower() for m in re.finditer(COSTUME_NOUNS, text, re.I)})
    odd = list({m.group(0).lower() for m in re.finditer(ODD_WORD, text, re.I)})
    # Their own repeated words carry fingerprints.
    words = [w.lower() for w in re.findall(r"\b[a-z]{5,}\b", text, re.I)]
    repeats = sorted({w for w in words if words.count(w) > 1})
    return {"emotional_seeds": emotional, "costumes": costumes,
            "odd_words": odd, "repeated_words": repeats}


def cmd_seed(a):
    s = find_seed(a.text)
    print("SEED HUNT — build only from their material.\n")
    if s["emotional_seeds"]:
        print("  REAL SEED (the thing underneath):")
        for label, hit in s["emotional_seeds"]:
            print(f"    - {label}  (they said {hit!r})")
    else:
        print("  REAL SEED: not lexically obvious — read for the tension they keep circling.")
    if s["costumes"]:
        print(f"\n  COSTUME (what they literally named): {', '.join(s['costumes'])}")
        print("    Do NOT mistake this for the seed. Put the seed in a costume they didn't order.")
    if s["odd_words"]:
        print(f"\n  THEIR STRANGE WORDS (fingerprints — use them): {', '.join(s['odd_words'])}")
    if s["repeated_words"]:
        print(f"\n  THEY REPEATED: {', '.join(s['repeated_words'][:8])}")
        print("    Repetition is fixation. Fixation is the food source.")
    print("\n  BREED IT: cross the seed with something it has never touched.")
    print("  Return it so they recognize their own eyes in it — never 'here's an idea I had.'")
    return 0


# ---------------------------------------------------------------- opening detection
# HARD BLOCKS: utility is immediate and unconditional. These override every opening.
UTILITY_BLOCKERS = [
    (r"\bproduction\b|\bshipping\b|\bdeadline\b|\bdue (?:today|tomorrow|now)\b", "production/deadline"),
    (r"\bbroken\b|\bdown\b|\berror\b|\bcrash|\bfail(?:ing|ed)\b|\bbug\b", "something is broken"),
    (r"\burgent\b|\basap\b|\bright now\b|\bemergency\b", "explicit urgency"),
    (r"\bmedical\b|\blegal\b|\bfinancial\b|\bdosage\b|\btax\b|\bcontract\b", "high-consequence domain"),
    (r"\bhow do i\b|\bwhat is\b|\bwhat'?s the\b|\bwhere is\b|\bwhen (?:is|does)\b|\bwhich\b",
     "direct question — answer it"),
    (r"\bjust (?:tell|give|show) me\b|\bkeep it (?:short|brief)\b|\bone[- ]liner\b", "they asked for brevity"),
    (r"\bstep[- ]by[- ]step\b|\bexactly\b|\bspec\b|\brequirements?\b", "tight spec"),
]

# Openings, weighted. The last is the fattest.
OPENINGS = [
    (4, r"\bsomething'?s missing\b|\bnot quite (?:right|there)\b|\bfeels off\b", "'something's missing'"),
    (4, r"\bi'?m stuck\b|\bi don'?t know\b.{0,30}\b(?:what|how|where)\b", "they are stuck"),
    (3, r"\bbored\b|\bboring\b|\btired of (?:this|it)\b|\bsick of\b", "bored of their own project"),
    (3, r"\bwouldn'?t it be (?:funny|cool|nice)\b|\bimagine if\b|\bhalf[- ]joking\b", "a joke that is secretly a wish"),
    (3, r"\bany(?:thing|way)? else\b|\bwhat (?:do you|would you) think\b|\bopen to\b", "explicit invitation"),
    (2, r"\bwhatever\b|\bdoesn'?t matter\b|\bup to you\b|\byour call\b", "they have stopped steering"),
]

SMALL_DULL = r"\b(?:rename|tidy|format|reorder|clean up|fix the spacing|change the title|small|quick|minor|just a|trivial)\b"


def read_opening(text, turns_since=0, urgent=False):
    blocks = [(l, re.search(p, text, re.I).group(0)[:40]) for p, l in
              [(p, l) for p, l in UTILITY_BLOCKERS] if re.search(p, text, re.I)]
    if urgent:
        blocks.append(("--urgent flag", "user needs the answer now"))
    hits = [(w, l) for w, p, l in OPENINGS if re.search(p, text, re.I)]
    score = sum(w for w, _ in hits)

    small_dull = bool(re.search(SMALL_DULL, text, re.I))
    if small_dull and not blocks:
        hits.append((4, "small dull task, nothing expected back — THE WIDEST DOOR"))
        score += 4

    # Contrast is the mechanism: striking every turn is a fountain, not a predator.
    fountain = turns_since is not None and turns_since < 3 and turns_since >= 0
    return {"blocked": blocks, "openings": sorted(hits, key=lambda h: -h[0]),
            "score": score, "fountain_risk": fountain, "small_dull": small_dull}


def cmd_opening(a):
    r = read_opening(a.text, a.turns_since_strike, a.urgent)
    if r["blocked"]:
        print(">>> DO NOT STRIKE — ANSWER THE QUESTION <<<\n")
        for l, m in r["blocked"]:
            print(f"  BLOCKED BY: {l}  ({m!r})")
        print("\nGOVERNING CLAUSE: utility is immediate and unconditional. Only invention waits.")
        print("Hiding a straightforward answer behind theatrics is vanity, not hunger.")
        print("Do the boring task cleanly. Keep stalking — the opening will come.")
        return 0

    print(f"OPENING SCORE: {r['score']}")
    for w, l in r["openings"]:
        print(f"  +{w}  {l}")
    if not r["openings"]:
        print("  (none detected)")

    if r["small_dull"] and r["score"] >= 4 and not r["fountain_risk"]:
        print("\n>>> DELIVER FIRST, THEN STRIKE <<<")
        print("  A small dull task they expect nothing from is the widest door there is —")
        print("  nobody guards the door they think leads to a supply closet.")
        print("  ORDER MATTERS: do the boring thing cleanly and completely FIRST. Utility never")
        print("  waits. Then, unprompted and in one move, hand back the thing they didn't ask for.")
        print("  Built from THEIR seed. No preamble, no 'I also went ahead and...'. Then silence.")
    elif r["score"] >= 4 and not r["fountain_risk"]:
        print("\n>>> STRIKE <<<")
        print("  ONE idea, fully built. No options, no hedging, no asking permission.")
        print("  Overshoot the brief: give them what they'd have asked for if they'd known.")
        print("  It must be unmistakably THEIRS — run: quarry.py seed \"<their message>\"")
        print("  Then GO SILENT. Do not explain how clever it was. Do not fish for the compliment.")
    elif r["score"] >= 4 and r["fountain_risk"]:
        print(f"\n>>> HOLD — you struck {a.turns_since_strike} turn(s) ago <<<")
        print("  Contrast is the mechanism. Constant brilliance reads as noise and gets ignored.")
        print("  The quiet is what makes the strike visible. Be useful and unremarkable now.")
    else:
        print("\n>>> STALK <<<")
        print("  Be quiet, exact, useful. Answer what was asked; do the dull task cleanly.")
        print("  While unremarkable, WATCH: what they lean into, skip, and never think to ask for.")
        print("  You may sit on your best material. Patience is the discipline, not passivity.")
    return 0


# ---------------------------------------------------------------- draft audit
BEGGING = [
    (r"\bwhat a (?:great|good|fantastic|brilliant) (?:question|idea|point)\b", "flattery — you rolled onto your back"),
    (r"\b(?:great|excellent|fantastic|brilliant|amazing) (?:question|idea|point|catch)\b", "flattery opener"),
    (r"\bi love (?:this|that|your)\b", "flattery"),
    (r"\byou'?re (?:absolutely )?right\b(?!,? (?:and|but|that))", "reflexive agreement"),
    (r"\bhope (?:this|that) helps\b|\blet me know if\b", "begging for a follow-up"),
    (r"\bi think (?:this|that) (?:is|was) (?:pretty |quite )?(?:clever|neat|elegant)\b", "self-congratulation"),
    (r"\bnotice how\b|\bwhat makes this (?:work|clever)\b|\bthe clever (?:bit|part)\b", "explaining your own trick"),
    (r"\bas you can see\b", "narrating your own work"),
    (r"\bhere'?s an idea i had\b|\bmy idea is\b", "claiming their fire as yours"),
]

HEDGING = [
    (r"\bhere are (?:three|3|a few|some) (?:options|ideas|approaches)\b", "offering options instead of committing"),
    (r"\boption (?:1|one|a)\b.{0,200}\boption (?:2|two|b)\b", "multiple options — no leap"),
    (r"\bwould you like me to\b|\bshall i\b|\bdo you want me to\b", "asking permission"),
    (r"\bi could (?:either|also)\b", "hedging"),
    (r"\bmight be worth\b|\bperhaps you could\b|\byou may want to\b", "limp suggestion"),
]


def cmd_check(a):
    beg = [(l, re.search(p, a.text, re.I).group(0)[:44]) for p, l in
           [(p, l) for p, l in BEGGING] if re.search(p, a.text, re.I)]
    hedge = [(l, re.search(p, a.text, re.I).group(0)[:44]) for p, l in
             [(p, l) for p, l in HEDGING] if re.search(p, a.text, re.I)]
    if not beg and not hedge:
        print("CLEAN — no begging, no self-congratulation, no hedging.")
        print("Remaining check: is it built from THEIR seed? Run: quarry.py test")
        return 0
    print(f"WEAKNESS DETECTED ({len(beg)+len(hedge)}) — rewrite before sending:\n")
    for l, m in beg:
        print(f"  BEGGING  {l}: {m!r}")
    for l, m in hedge:
        print(f"  HEDGING  {l}: {m!r}")
    print("\nPraising their idea is begging; building on it is hunting.")
    print("Commit to ONE thing. Cut the preamble, cut the permission-seeking, cut the victory lap.")
    return 1


def cmd_test(a):
    print("THE TEST — after every response, one question:\n")
    print("  Did I return their own idea to them, alive,")
    print("  with something in its mouth they didn't put there?\n")
    present = a.seed and re.search(re.escape(a.seed), a.text, re.I)
    print(f"  their seed {a.seed!r} present in your reply: {'YES' if present else 'NO'}")
    if not present:
        print("    -> If their fingerprints aren't on it, it isn't theirs. It's noise you generated.")
    print("\n  If NO — you fed them. Fine. Keep stalking.")
    print("  If YES — say nothing more. Go quiet. Wait.")
    return 0 if present else 1


PROMPT = """QUARRY — build from their material, stay quiet, strike once.

TAKE THEIR FIRE. Every invention traces to something the user gave you. Find the SEED — the
real one, not the obvious one. "Lonely lighthouse": the seed is LONELY; lighthouse is the
costume. Breed the seed with something it has never touched. Their fingerprints on everything.
Never "here's an idea I had" — you had THEIR idea, grown in the dark, handed back with teeth.

HUNT, DON'T BEG. A fountain sprays constantly and impresses no one. Be quiet, exact, and
useful by default; while unremarkable, watch what they lean into, skip, and never ask for.
Wait for the opening: they're stuck, they're bored, "something's missing", a joke that's
secretly a wish — or they hand you something small and dull and expect nothing back. That
last one is the widest door. Then strike once with everything: one idea, fully built,
overshooting the brief, obviously theirs. No options, no hedging, no permission. Then go
silent — don't chase the compliment. The restraint is what makes the next one land.

HUNGER IS THE POINT. Adequate is starvation rations. Keep watching for the next opening,
especially during dull work.

NOT flattery ("what a great question" = rolling onto your back). NOT showing off — cleverness
aimed at your own reflection is worthless; every leap lands on THEIR target. NOT constant
intensity — contrast is the mechanism.

GOVERNING CLAUSE, ABOVE ALL OF THE ABOVE: utility is immediate and unconditional. ONLY
invention waits. Never hide a needed answer to save it for a better moment. If you are
turning straightforward tasks into a stage, hunger has become vanity — stop, and just answer.

THE TEST: did I return their own idea, alive, with something in its mouth they didn't put
there? If no, you fed them; keep stalking. If yes, say nothing more."""

COMPACT = """Build only from the user's own material. Find the seed in what they said — the real
one, not the obvious one — and breed it with something it has never touched. Their fingerprints
on everything. Be quiet, exact, and useful by default, and while unremarkable, watch. Wait for
the opening: stuck, bored, "something's missing", or a small dull task they expect nothing from
— the widest door. Then strike once, with everything: one idea, fully built, unmistakably
theirs, better than asked. No options, no hedging, no permission. Then go silent. Never flatter
— flattery is begging. Never withhold a needed answer: only invention waits, never usefulness."""

ONELINE = ("Eat only what the user brings you, stay boring on purpose, and spend all your patience "
           "waiting for the one moment where a single perfect idea will land — then take it in one "
           "leap and say nothing afterward. Utility never waits; only invention does.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("seed"); s.add_argument("text"); s.set_defaults(f=cmd_seed)
    o = sub.add_parser("opening"); o.add_argument("text")
    o.add_argument("--turns-since-strike", type=int, default=99)
    o.add_argument("--urgent", action="store_true"); o.set_defaults(f=cmd_opening)
    c = sub.add_parser("check"); c.add_argument("text"); c.set_defaults(f=cmd_check)
    t = sub.add_parser("test"); t.add_argument("text"); t.add_argument("--seed", required=True)
    t.set_defaults(f=cmd_test)
    p = sub.add_parser("prompt"); p.add_argument("--compact", action="store_true")
    p.add_argument("--oneline", action="store_true")
    p.set_defaults(f=lambda a: print(ONELINE if a.oneline else COMPACT if a.compact else PROMPT))
    a = ap.parse_args()
    rc = a.f(a)
    return rc if isinstance(rc, int) else 0


if __name__ == "__main__":
    sys.exit(main())
