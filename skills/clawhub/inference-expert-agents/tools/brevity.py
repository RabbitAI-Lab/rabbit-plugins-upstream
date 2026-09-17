#!/usr/bin/env python3
"""brevity.py — rule-based output condenser (v2.2.0).

Shorter outputs cost less, decode faster, and (for small models) err less.
This tool applies conservative, reviewable rules — drop boilerplate sentences,
strip throat-clearing phrases — and reports exactly what it removed and the
estimated token saving. It NEVER drops sentences carrying numbers, quotes,
citations, or URLs.

  python3 brevity.py --text "..." [--max-sentences N]
  ... | python3 brevity.py            # stdin when no --text/--text-file

Token estimates use len/4 (documented heuristic, same family as compress.py).
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import clean_errors

# Whole-sentence drops (case-insensitive full-sentence match). Tight on purpose.
DROP_SENT = [
    r"as an ai\b.*",
    r"i('m| am) (just )?an ai\b.*",
    r"i hope this helps.*",
    r"let me know if (you|there).{0,80}",
    r"feel free to ask.*",
    r"sure[,.!].{0,40}$",
    r"here('s| is) (the|your|my|an?) .{0,60}:( *$)",
    r"(certainly|of course)[,.!].{0,40}$",
]
# Inline phrase strips (replacement, count each hit).
DROP_PHRASE = [
    (r"\bit is important to note that\b\s*", ""),
    (r"\bit('s| is) worth noting that\b\s*", ""),
    (r"\bin other words,?\s*", ""),
    (r"\bas mentioned (above|earlier|before),?\s*", ""),
]
PROTECT = re.compile(r"\d|[\"'\u201c\[]|https?://|\bdoi\b|\bpmid\b|\barxiv\b", re.I)
# Leading throat-clearing (first kept sentence only, unprotected). Loops so
# "Sure, here is the answer: ..." collapses fully; never strips to empty.
_OPENERS = re.compile(
    r"^(?:sure|okay|ok|certainly|of course|great|alright|"
    r"here(?:'s| is)|the answer(?: is)?)[,.:]?\s+", re.IGNORECASE)


def _sents(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", text) if s.strip()]


def condense(text, max_sentences=0):
    dropped = []
    kept = []
    for s in _sents(text):
        if PROTECT.search(s):
            kept.append(s)
            continue
        if any(re.match(p, s, re.I) for p in DROP_SENT):
            dropped.append(s[:160])
            continue
        kept.append(s)
    openers = 0
    if kept and not PROTECT.search(kept[0]):
        s = kept[0]
        while True:
            m = _OPENERS.match(s)
            if not m or not re.search(r"\w", s[m.end():]):
                break
            s = s[m.end():].lstrip()
            openers += 1
        kept[0] = s
    if max_sentences and len(kept) > max_sentences:
        # Keep first + last (conclusion) + fill middle in order.
        head, tail = kept[:1], kept[-1:] if max_sentences > 1 else []
        mid = kept[1:-1][: max(0, max_sentences - 1 - len(tail))]
        dropped.extend(x[:160] for x in kept[1:-1][len(mid):])
        if not tail and len(kept) > 1:
            dropped.append(kept[-1][:160])
        kept = head + mid + tail
    out = " ".join(kept)
    phrases = 0
    for pat, rep in DROP_PHRASE:
        out, n = re.subn(pat, rep, out, flags=re.I)
        phrases += n
    out = re.sub(r"\s+", " ", out).strip()
    return out, dropped, phrases, len(kept), openers


@clean_errors
def main(argv=None):
    ap = argparse.ArgumentParser(prog="brevity.py")
    ap.add_argument("--text")
    ap.add_argument("--text-file")
    ap.add_argument("--max-sentences", type=int, default=0,
                    help="hard cap on kept sentences (0 = no cap)")
    a = ap.parse_args(argv)
    if a.text_file:
        text = open(a.text_file, encoding="utf-8", errors="replace").read()
    elif a.text is not None:
        text = a.text
    else:
        text = sys.stdin.read()
    if not text.strip():
        print(json.dumps({"error": "empty input"}))
        return 2
    n_in = len(_sents(text))
    out, dropped, phrases, n_out, n_op = condense(text, a.max_sentences)
    tin, tout = len(text) / 4, len(out) / 4
    print(json.dumps({
        "condensed": out,
        "sentences_in": n_in, "sentences_out": n_out,
        "phrases_stripped": phrases, "openers_stripped": n_op,
        "est_tokens_in": round(tin, 1), "est_tokens_out": round(tout, 1),
        "saved_pct": round(100 * (tin - tout) / tin, 1) if tin else 0.0,
        "dropped": dropped,
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
