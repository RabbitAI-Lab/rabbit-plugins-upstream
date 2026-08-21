#!/usr/bin/env python3
"""
post_critic.py: heuristic reach-scorer for a draft X post.

Mirrors the *value system* of X's open-sourced For You ranking algorithm
(home-mixer/params/param.rs): it estimates a plausible action profile for a
draft from simple text heuristics, then scores it with the REAL weight table.

This is a writing aid, NOT a simulator of X's ML model. X never sees your raw
text. It conditions on embeddings, engagement counts, and graph features. Use
this to reason about *which actions your wording invites* and to catch
negative-signal risks, not to predict actual reach.

Usage:
    python post_critic.py "your draft text"
    python post_critic.py < draft.txt
    echo "draft" | python post_critic.py

No dependencies; standard library only.
"""

import re
import sys

# Make output ASCII-safe on Windows consoles (cp1252) while allowing UTF-8.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# --- The real weight table (param.rs defaults, 2026-08 snapshot) -------------
# Positive heads people can take on a post, with their ranking weights.
WEIGHTS = {
    "copy_link_share": 20.0,
    "reply": 5.0,
    "quote": 5.0,
    "dm_share": 5.0,
    "follow_author": 4.0,
    "share": 2.0,
    "retweet": 1.0,
    "favorite": 0.5,
    "click": 0.4,
    "open_link": 0.2,
    "video_open": 0.05,
    "dwell_unit": 0.004,   # per unit of continuous dwell
    # negatives
    "not_interested": -43.2,
    "block": -31.2,
    "mute": -58.8,
    "report": -234.0,
    "not_dwelled": -0.02,
}

MAX_TWEET_LEN = 280

# --- Heuristic signal detectors ----------------------------------------------

QUESTION_RE = re.compile(r"\?")
URL_RE = re.compile(r"https?://|www\.", re.I)
HASHTAG_RE = re.compile(r"#\w+")
MENTION_RE = re.compile(r"@\w+")
ALLCAPS_RUN_RE = re.compile(r"\b[A-Z]{4,}\b")

ENGAGEMENT_BAIT = [
    r"\blike (?:if|and)\b", r"\bretweet (?:if|and|to)\b", r"\bfollow (?:me )?(?:for|back)\b",
    r"\bcomment\b.*\bbelow\b", r"\breply (?:with )?[\"']?go[\"']?\b",
    r"\btag (?:a|someone|3|three)\b", r"\bfollow for follow\b", r"\bf4f\b",
    r"\bdrop a\b.*\bif\b", r"\bwho else\b.*\?$",
]
BAIT_RE = re.compile("|".join(ENGAGEMENT_BAIT), re.I)

RAGE_MARKERS = [
    r"\bunpopular opinion\b", r"\bhot take\b", r"\bnobody (?:is )?talking about\b",
    r"\bdelete this\b", r"\bratio\b", r"\bcope\b", r"\btriggered\b",
    r"\bwake up\b", r"\bthey don'?t want you to know\b",
]
RAGE_RE = re.compile("|".join(RAGE_MARKERS), re.I)

FORWARD_MARKERS = [
    r"\bhere'?s how\b", r"\bstep[- ]by[- ]step\b", r"\ba thread\b", r"\bguide\b",
    r"\bbookmark this\b", r"\bsave this\b", r"\bcheat ?sheet\b", r"\btl;?dr\b",
    r"\bthe (?:complete|ultimate|only)\b", r"\bexplained\b", r"\btemplate\b",
]
FORWARD_RE = re.compile("|".join(FORWARD_MARKERS), re.I)

SLUR_LITE_RISK = [  # crude NSFW/abusive risk flags, directional only
    r"\bnsfw\b", r"\bonlyfans\b", r"\bxxx\b", r"\b18\+\b", r"\bgore\b",
]
NSFW_RE = re.compile("|".join(SLUR_LITE_RISK), re.I)


def clamp(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, x))


def estimate_profile(text):
    """Return an estimated probability for each action head from text heuristics."""
    t = text.strip()
    low = t.lower()
    words = re.findall(r"\w+", t)
    n_words = len(words)

    has_question = bool(QUESTION_RE.search(t))
    has_url = bool(URL_RE.search(t))
    n_hashtags = len(HASHTAG_RE.findall(t))
    n_mentions = len(MENTION_RE.findall(t))
    is_bait = bool(BAIT_RE.search(low))
    is_rage = bool(RAGE_RE.search(low))
    is_forwardable = bool(FORWARD_RE.search(low))
    nsfw_risk = bool(NSFW_RE.search(low))
    allcaps = len(ALLCAPS_RUN_RE.findall(t))
    is_thread = bool(re.search(r"\b(?:thread|1/|🧵)\b", low)) or n_words > 60

    # Hook strength: first ~10 words. Short punchy or question-led = stronger.
    first = " ".join(words[:10]).lower()
    hook = 0.5
    if has_question and t.index("?") < 120:
        hook += 0.15
    if re.search(r"^(how|why|what|the|stop|never|most people|here'?s)", first):
        hook += 0.15
    if n_words > 0 and n_words <= 25:
        hook += 0.1
    if allcaps >= 2:
        hook -= 0.1
    if n_hashtags >= 3:
        hook -= 0.15
    hook = clamp(hook)

    # Base positive propensities (small; these are rare events per impression).
    p = {
        "favorite": 0.03,
        "reply": 0.004,
        "quote": 0.001,
        "retweet": 0.004,
        "share": 0.002,
        "dm_share": 0.001,
        "copy_link_share": 0.0005,
        "follow_author": 0.001,
        "click": 0.02 if has_url else 0.008,
        "open_link": 0.01 if has_url else 0.0,
        "video_open": 0.0,
        "dwell_unit": 2.0 + (n_words / 20.0),  # rough dwell "units"
    }

    # Wording effects on high-value actions.
    if has_question:
        p["reply"] *= 2.2
    if is_forwardable:
        p["copy_link_share"] *= 4.0
        p["dm_share"] *= 3.0
        p["favorite"] *= 1.3
    if is_thread:
        p["dwell_unit"] *= 1.6
        p["follow_author"] *= 1.8
    # Hook lifts everything a bit (survives the scroll).
    lift = 0.7 + 0.6 * hook
    for k in ("favorite", "reply", "retweet", "share", "copy_link_share", "dm_share", "quote"):
        p[k] *= lift

    # Negative propensities. These are rare per-impression events on X; a clean
    # post should net positive, so baselines are low and only bad patterns spike
    # them. (Report/mute/not_interested carry huge weights, so small changes in
    # these probabilities move the score a lot, which is the real dynamic.)
    neg = {
        "not_interested": 0.0010,
        "block": 0.0002,
        "mute": 0.0003,
        "report": 0.00005,
        "not_dwelled": clamp(0.45 - 0.4 * hook, 0.03, 0.7),
    }
    if is_bait:
        neg["not_interested"] *= 4.0
        neg["mute"] *= 3.0
    if is_rage:
        neg["not_interested"] *= 3.0
        neg["block"] *= 3.0
        neg["mute"] *= 2.5
        neg["report"] *= 2.0
    if nsfw_risk:
        neg["report"] *= 2.0
    if n_hashtags >= 4:
        neg["not_interested"] *= 1.5

    p.update(neg)
    # Clamp probabilities.
    for k in p:
        if k != "dwell_unit":
            p[k] = clamp(p[k])
    return p, {
        "n_words": n_words, "hook": hook, "has_question": has_question,
        "has_url": has_url, "n_hashtags": n_hashtags, "n_mentions": n_mentions,
        "is_bait": is_bait, "is_rage": is_rage, "is_forwardable": is_forwardable,
        "nsfw_risk": nsfw_risk, "is_thread": is_thread, "allcaps": allcaps,
    }


def score(profile):
    total = 0.0
    contrib = {}
    for action, prob in profile.items():
        w = WEIGHTS.get("dwell_unit") if action == "dwell_unit" else WEIGHTS.get(action)
        if w is None:
            continue
        c = w * prob
        contrib[action] = c
        total += c
    return total, contrib


def bar(x, width=24, lo=-1.0, hi=1.0):
    frac = clamp((x - lo) / (hi - lo))
    fill = int(frac * width)
    return "[" + "#" * fill + "-" * (width - fill) + "]"


def verdict_for(total):
    # Thresholds are calibrated to this heuristic's compressed scale (per-
    # impression probabilities are tiny), not to raw production score units.
    return ("strong" if total >= 0.15 else
            "ok" if total >= 0.03 else
            "weak" if total >= -0.05 else "NEGATIVE (likely suppressed)")


def build_flags(text, feat):
    flags = []
    if feat["hook"] < 0.5:
        flags.append("Weak hook: first words may lose the scroll test (not_dwelled penalty).")
    if not feat["has_question"] and not feat["is_forwardable"]:
        flags.append("No clear reply or forward trigger; targets only low-value likes (0.5). "
                     "Add a real question (reply=5) or make it forward-worthy (copy-link=20).")
    if feat["is_bait"]:
        flags.append("Engagement-bait pattern: risks not_interested/mute and SPAM_HIGH_RECALL "
                     "(OON-only drop). Replace with genuine prompting.")
    if feat["is_rage"]:
        flags.append("Rage/controversy markers: inflate blocks/reports vs likes (agatha ratio), "
                     "the chain that silently caps stranger reach. Report weight is -234.")
    if feat["nsfw_risk"]:
        flags.append("Possible NSFW/adult markers: risk NSFW labels (OON-only drop) and a Grox "
                     "re-scan at 128+ favs.")
    if feat["has_url"]:
        flags.append("Contains a link: link opens are low value (0.2) and carry MALICIOUS_URL "
                     "risk. Put the value in the post, and vet the domain.")
    if feat["n_hashtags"] >= 3:
        flags.append(f"{feat['n_hashtags']} hashtags: reads as spammy and weakens the hook.")
    if len(text) > MAX_TWEET_LEN:
        flags.append(f"Over 280 chars ({len(text)}): will be truncated unless you're on a "
                     "long-post tier.")
    if feat["is_forwardable"]:
        flags.append("[+] Forward-worthy framing detected. Targets the 20x copy-link share. Good.")
    if feat["has_question"]:
        flags.append("[+] Question present. Targets reply weight (5.0). Good.")
    if feat["is_thread"]:
        flags.append("[+] Thread/long-form. Accumulates weighted dwell time and follows.")
    return flags


def report(text):
    """Print the full single-draft report. Returns the score."""
    profile, feat = estimate_profile(text)
    total, contrib = score(profile)

    print("=" * 60)
    print("X POST CRITIC - heuristic reach score (directional, not a model)")
    print("=" * 60)
    print(f"\nDraft ({feat['n_words']} words, {len(text)} chars"
          + ("  (!) over 280!" if len(text) > MAX_TWEET_LEN else "") + "):")
    print("  " + (text[:200] + ("..." if len(text) > 200 else "")))

    print(f"\nEstimated weighted score: {total:+.3f}  {bar(total)}")
    print(f"Verdict: {verdict_for(total)}")

    # Top contributors.
    pos = sorted([(k, v) for k, v in contrib.items() if v > 0], key=lambda x: -x[1])[:5]
    negs = sorted([(k, v) for k, v in contrib.items() if v < 0], key=lambda x: x[1])[:5]
    print("\nTop positive drivers:")
    for k, v in pos:
        print(f"  +{v:6.3f}  {k}")
    print("Top negative drivers:")
    for k, v in negs:
        print(f"  {v:7.3f}  {k}")

    print("\nFlags:")
    for f in build_flags(text, feat):
        print(f"  - {f}")

    print("\nReminder: X's model does not read your text; it conditions on embeddings,")
    print("engagement counts, graph, and freshness. This score reflects which ACTIONS")
    print("your wording invites. See references/ for the real mechanics.")
    return total


def compare(drafts):
    """Score several drafts and rank them."""
    scored = []
    for i, d in enumerate(drafts, 1):
        profile, feat = estimate_profile(d)
        total, _ = score(profile)
        scored.append((i, total, d, feat))

    print("=" * 60)
    print(f"X POST CRITIC - comparing {len(drafts)} drafts")
    print("=" * 60)
    for i, total, d, feat in scored:
        snippet = d[:70].replace("\n", " ") + ("..." if len(d) > 70 else "")
        print(f"\n[{i}] {total:+.3f}  {bar(total)}  ({verdict_for(total)})")
        print(f"    {snippet}")
        key_flags = [f for f in build_flags(d, feat)
                     if not f.startswith("[+]")][:2]
        for f in key_flags:
            print(f"      - {f}")

    winner = max(scored, key=lambda s: s[1])
    print(f"\n>>> Strongest: draft [{winner[0]}] at {winner[1]:+.3f}")
    print("\nReminder: heuristic writing aid, not a model of X's ranker. "
          "See references/ for mechanics.")
    return 0


HELP = """post_critic.py: heuristic reach-scorer for a draft X post.

Usage:
  python post_critic.py "your draft text"
  python post_critic.py < draft.txt
  python post_critic.py --compare "draft A" "draft B" ["draft C" ...]
  python post_critic.py --compare < drafts.txt   # drafts separated by a line of '==='
"""


def main():
    args = sys.argv[1:]

    if args and args[0] in ("-h", "--help"):
        print(HELP)
        return 0

    if args and args[0] == "--compare":
        rest = args[1:]
        if len(rest) >= 2:
            drafts = [d.strip() for d in rest if d.strip()]
        else:
            # Read from stdin, split on a line that is only '===' or '---'.
            raw = sys.stdin.read()
            drafts = [d.strip() for d in re.split(r"(?m)^\s*[=-]{3,}\s*$", raw) if d.strip()]
        if len(drafts) < 2:
            print("--compare needs at least 2 drafts "
                  "(as args, or on stdin separated by a line of '===').")
            return 1
        return compare(drafts)

    if args:
        text = " ".join(args)
    else:
        text = sys.stdin.read()
    text = text.strip()
    if not text:
        print(HELP)
        return 1

    report(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
