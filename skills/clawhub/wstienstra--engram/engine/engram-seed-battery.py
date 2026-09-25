#!/usr/bin/env python3
"""
engram-seed-battery.py — Seeded mini-battery for install verification.

Generates 20 recall cases FROM the migrated content in Engram, plus 3
negative controls (things NOT in the engram).

The bar is 90% of the mined positives plus 3/3 negatives. A negative control
passes only when the engine ran and said in words that it has nothing — an
empty result is a broken engine, not an abstain. Any non-zero exit or traceback
fails the whole run, whatever the score looks like.

Usage:
  python3 engram/engram-seed-battery.py
"""

import math
import os
import re
import subprocess
import sys
import sqlite3
from collections import Counter

try:
    import bpconfig
    _cfg = bpconfig.load_config()
    WORKSPACE = _cfg["workspace"]
    DB_PATH = _cfg["db_path"]
    BQ_CLI = os.path.join(_cfg["engram_dir"], "bq.py")
    ENGRAM_CLI = os.path.join(_cfg["engram_dir"], "engram.py")
except Exception:
    ENGRAM_DIR = os.path.dirname(os.path.abspath(__file__))
    WORKSPACE = os.path.dirname(ENGRAM_DIR)
    DB_PATH = os.path.join(ENGRAM_DIR, "engram.db")
    BQ_CLI = os.path.join(ENGRAM_DIR, "bq.py")
    ENGRAM_CLI = os.path.join(ENGRAM_DIR, "engram.py")

STOP = set('''the a an and or of to in for with on at from by is are was were be been this that it as
about into over after before not no vs their his her its our your all any each which what when where
how why can will just also more most other some such only own same so than too very s t d ll re ve
een de het en van voor met op um die der und'''.split())


# An abstain is a result, not a silence. The engine says one of these when it
# has nothing worth reporting; anything else on a negative control is a hit.
ABSTAIN = re.compile(
    r"no confident match|no results for|found 0 node|nothing (?:found|stored|on that)",
    re.IGNORECASE,
)

# A match the engine is willing to stand behind. Used only on negative controls.
CONFIDENT = re.compile(r"== DIRECT ==|== RELATED ==|exact match", re.IGNORECASE)


def run_recall(query):
    """Run one recall. Returns (stdout, stderr, returncode).

    Nothing is swallowed. A crash must look like a crash to the caller, because
    a battery that reads a dead engine as a quiet one is worse than no battery.
    """
    cmd = [sys.executable, ENGRAM_CLI, "recall", query, "--limit", "5"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60,
                           cwd=WORKSPACE)
        return r.stdout, r.stderr, r.returncode
    except subprocess.TimeoutExpired:
        return "", "recall timed out after 60s", 124
    except Exception as exc:
        return "", f"could not run the engine: {exc}", 126


def engine_failure(stderr, code):
    """Return why the engine is broken, or None when it ran.

    Broken means broken: a non-zero exit, or a traceback on stderr even when the
    exit code lies. This is not a retrieval miss and must never be scored as one.
    """
    if code != 0:
        return f"engine exited {code}: {_last_error_line(stderr)}"
    if "Traceback (most recent call last)" in (stderr or ""):
        return f"engine traceback: {_last_error_line(stderr)}"
    return None


def _last_error_line(stderr):
    lines = [ln.strip() for ln in (stderr or "").splitlines() if ln.strip()]
    return lines[-1] if lines else "no stderr"


def mine_cases_from_db():
    """Mine recall cases from the DB content."""
    if not os.path.isfile(DB_PATH):
        return []

    conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    cases = []

    nodes = conn.execute(
        "SELECT id, name, type, content FROM nodes ORDER BY id LIMIT 50"
    ).fetchall()

    for node in nodes:
        name = node["name"] or ""
        content = node["content"] or ""
        ntype = node["type"] or ""

        # Skip very short names
        if len(name) < 5:
            continue

        # Create a query from distinctive words in the name
        words = [w for w in re.findall(r'\w+', name.lower()) if w not in STOP and len(w) > 3]
        if words:
            query = " ".join(words[:3])
            cases.append({
                "query": query,
                "must_match": re.escape(name[:30]),
                "type": "name_partial",
                "node_name": name,
            })

        # Create a query from distinctive content words
        content_words = [w for w in re.findall(r'\w+', content.lower()) if w not in STOP and len(w) > 4]
        if content_words:
            # Pick a few distinctive ones
            query = " ".join(content_words[:3])
            cases.append({
                "query": query,
                "must_match": re.escape(name[:30]),
                "type": "content_probe",
                "node_name": name,
            })

        if len(cases) >= 30:
            break

    conn.close()
    return cases[:20]  # Exactly 20


def check_case(case):
    """Positive case. Returns (passed, detail, broken)."""
    out, err, code = run_recall(case["query"])
    broken = engine_failure(err, code)
    if broken:
        return False, broken, True
    if not out.strip():
        return False, "the engine printed nothing at all", True
    if re.search(case["must_match"], out, re.IGNORECASE):
        return True, "found", False
    return False, f"not found in results for '{case['query']}'", False


def check_negative(query):
    """Negative control. Returns (passed, detail, broken).

    A pass needs two things: the engine ran, and it said out loud that it has
    nothing. Silence is not an abstain — silence is what a dead engine produces.
    """
    out, err, code = run_recall(query)
    broken = engine_failure(err, code)
    if broken:
        return False, broken, True
    if not out.strip():
        return False, "the engine printed nothing at all — silence is not an abstain", True
    if ABSTAIN.search(out):
        return True, "explicit abstain", False
    if CONFIDENT.search(out):
        return False, "confident match on a question with no answer", False
    return False, "no abstain and no match — unreadable result", False


def main():
    print("Engram Seeded Mini-Battery")
    print("=" * 50)

    # Mine cases from migrated content
    cases = mine_cases_from_db()

    if len(cases) < 20:
        print(f"WARNING: Only mined {len(cases)} cases (need 20). Using what we have.")

    # Run positive cases
    passed = 0
    failed = 0
    failures = []
    broken = []

    print(f"\nPositive cases ({len(cases)}):")
    for i, case in enumerate(cases, 1):
        ok, detail, is_broken = check_case(case)
        status = "✅" if ok else ("💥" if is_broken else "❌")
        print(f"  {status} [{case['type']}] '{case['query']}' → {case['node_name'][:40]} ({detail})")
        if ok:
            passed += 1
        else:
            failed += 1
            failures.append(f"  Case {i}: '{case['query']}' expected '{case['node_name'][:40]}' — {detail}")
            if is_broken:
                broken.append(f"  Case {i}: '{case['query']}' — {detail}")

    # Negative controls
    negatives = [
        "tesla stock trading strategy details",
        "kubernetes cluster admin password",
        "wedding planning for cousin marta",
    ]

    print(f"\nNegative controls ({len(negatives)}):")
    neg_passed = 0
    for q in negatives:
        ok, detail, is_broken = check_negative(q)
        status = "✅" if ok else ("💥" if is_broken else "❌")
        print(f"  {status} '{q}' ({detail})")
        if ok:
            neg_passed += 1
        else:
            failures.append(f"  Negative: '{q}' — {detail}")
            if is_broken:
                broken.append(f"  Negative: '{q}' — {detail}")

    # Summary
    total = len(cases) + len(negatives)
    total_passed = passed + neg_passed
    print(f"\n{'=' * 50}")
    print(f"Results: {total_passed}/{total} passed")
    print(f"  Positive: {passed}/{len(cases)}")
    print(f"  Negative: {neg_passed}/{len(negatives)}")

    if failures:
        print(f"\nFailures:")
        for f in failures:
            print(f)

    # A broken engine is not a bad score, it is no score. Say so and stop,
    # before any percentage gets a chance to look reassuring.
    if broken:
        print(f"\n💥 ENGINE BROKEN — {len(broken)} case(s) could not run:")
        for b in broken[:5]:
            print(b)
        if len(broken) > 5:
            print(f"  ... and {len(broken) - 5} more")
        print("\n❌ BATTERY FAILED (the engine did not run; these results mean nothing)")
        sys.exit(1)

    # Gate: >=90% of mined positive cases (min 3 cases) + 3/3 negative.
    # Rate-based, not absolute: small workspaces mine fewer than 20 cases
    # and must still be able to pass at a high hit rate. Rounded up, because
    # int() let 10/12 print as "≥90%" — a gate that rounds in its own favour
    # is the same dishonesty as a battery that scores a crash as a pass.
    min_needed = max(3, math.ceil(len(cases) * 0.9))
    if len(cases) >= 3 and passed >= min_needed and neg_passed == 3:
        pct = passed * 100 // max(len(cases), 1)
        print(f"\n✅ BATTERY PASSED ({passed}/{len(cases)} positive = {pct}% ≥90% + 3/3 negative)")
        sys.exit(0)
    else:
        if len(cases) < 3:
            print("\n❌ BATTERY FAILED (fewer than 3 minable cases — workspace too sparse to verify)")
        else:
            print(f"\n❌ BATTERY FAILED ({passed}/{len(cases)} positive, need ≥{min_needed}; negatives {neg_passed}/3)")
        sys.exit(1)


if __name__ == "__main__":
    main()