#!/usr/bin/env python3
"""Engram recall battery — large-scale, adversarial, self-mining.

Goes beyond engram-eval.py's 10 golden queries: mines ~100 ground-truth
cases from the DB itself plus hand-written adversarial/paraphrase/negative
sets, scores per class, and dumps failures for diagnosis.

Classes:
  name_partial   informative words from a node's name → that node must return
  prop_value     distinctive prop value (email/domain/status) → owning node
  content_probe  rare words from a node's content → source node
  paraphrase     same intent, different words (hand-written)
  adversarial    confusables, superseded chains, episodic bleed, typos, Dutch
  negative       things NOT in the engram → must not confabulate confident hits

Usage:
  python3 scripts/engram-battery.py --mine          # show mined cases only
  python3 scripts/engram-battery.py --run [--label X] [--limit N]
  python3 scripts/engram-battery.py --diff A B      # compare two saved runs

Exit code: 0 when the run completed, 1 when the engine failed to run at all
(non-zero exit or a traceback on any case). A low score is not an error; a
dead engine is.
"""
import argparse
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
from collections import Counter, defaultdict

# Engram: load paths from config
try:
    import bpconfig
    _cfg = bpconfig.load_config()
    WS = _cfg["workspace"]
    DB = _cfg["db_path"]
    BQ = ['python3', os.path.join(_cfg["engram_dir"], "bq.py")]
    RESULTS_DIR = _cfg["logs_dir"]
except Exception:
    WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    DB = os.path.join(WS, 'engram', 'engram.db')
    BQ = ['python3', os.path.join(WS, 'engram', 'bq.py')]
    RESULTS_DIR = os.path.join(WS, 'logs')

STOP = set('''the a an and or of to in for with on at from by is are was were be been this that it as
about into over after before not no vs their his her its our your all any each which what when where
how why can will just also more most other some such only own same so than too very s t d ll re ve
een de het en van voor met op um die der und'''.split())

KNOWLEDGE_TYPES = ('project', 'decision', 'rule', 'knowledge', 'concept', 'person',
                   'organization', 'business', 'product', 'finding', 'lesson', 'fact',
                   'task', 'contact', 'workflow', 'config')

# ---------- hand-written sets ----------
# Hand-written probe sets are workspace-specific. Add your own paraphrase
# probes (query, expected-name regex) and adversarial probes
# (query, must_match, must_not_match_in_top, note) for the content that
# matters in YOUR workspace. Fresh installs are verified by
# engram-seed-battery.py, which generates cases from migrated content.
PARAPHRASE = []
ADVERSARIAL = []
NEGATIVE = [
    "tesla stock trading strategy details",
    "kubernetes cluster admin password",
    "wedding planning for cousin marta",
]

# ---------- prospective-memory (intention) class ----------
# Arms one distinctive intention, then routes 5 messages through msgctx:
# 3 that must surface the ⏰ INTENTION line, 2 that must NOT. Cleaned up after.
INTENTION_TRIGGER = "when Zephyr replies about the flux capacitor shipment"
INTENTION_ACTION = "resume the warehouse audit thread"
INTENTION_NODE_NAME = f"intention: {INTENTION_TRIGGER}"
INTENTION_CASES = [
    # (message, should_fire)
    ("Zephyr just replied about the flux capacitor", True),
    ("any word from Zephyr on the shipment yet?", True),
    ("can you pull the flux capacitor shipment status please", True),
    ("what's the weather in Amsterdam tomorrow", False),
    ("remind me to buy groceries and fresh milk", False),
]


# An abstain is a result the engine chose to give. Silence is not one.
ABSTAIN = re.compile(
    r"no confident match|no results for|found 0 node|nothing (?:found|stored|on that)",
    re.IGNORECASE,
)


def _last_error_line(stderr):
    lines = [ln.strip() for ln in (stderr or '').splitlines() if ln.strip()]
    return lines[-1] if lines else 'no stderr'


def engine_failure(stderr, code):
    """Return why the engine is broken, or None when it ran.

    A non-zero exit or a traceback is a broken engine, not a retrieval miss.
    Scoring one as the other is how a crash ships to users looking like a
    mediocre hit rate.
    """
    if code != 0:
        return f"engine exited {code}: {_last_error_line(stderr)}"
    if 'Traceback (most recent call last)' in (stderr or ''):
        return f"engine traceback: {_last_error_line(stderr)}"
    return None


def run_msgctx(message):
    """Returns (stdout, stderr, returncode). Streams are kept apart on purpose."""
    try:
        r = subprocess.run(BQ + ['msgctx', message],
                           capture_output=True, text=True, timeout=60, cwd=WS)
        return (r.stdout or ''), (r.stderr or ''), r.returncode
    except subprocess.TimeoutExpired:
        return '', 'msgctx timed out after 60s', 124
    except Exception as exc:
        return '', f'could not run the engine: {exc}', 126


def run_intention_class():
    """Returns (n, hit, failures, broken). Arms a test intention, exercises
    msgctx, then deletes the test node so the live engram is left untouched."""
    failures = []
    broken = []
    n = hit = 0
    # cleanup any stale copy first, then arm fresh
    subprocess.run(BQ + ['delete', '--name', INTENTION_NODE_NAME], capture_output=True, text=True, cwd=WS)
    arm = subprocess.run(BQ + ['intend', INTENTION_TRIGGER, INTENTION_ACTION],
                         capture_output=True, text=True, cwd=WS)
    armed_ok = 'Armed' in (arm.stdout + arm.stderr) or 'Stored' in (arm.stdout + arm.stderr)
    try:
        for msg, should_fire in INTENTION_CASES:
            out, err, code = run_msgctx(msg)
            dead = engine_failure(err, code)
            fired = '⏰ INTENTION' in out
            ok = (not dead) and armed_ok and (fired == should_fire)
            n += 1
            hit += ok
            mark = '✅' if ok else ('💥' if dead else '❌')
            print(f"  {mark} [{'intention':13}] {msg[:60]!r} "
                  f"(fire={fired}, want={should_fire})"
                  + (f" — {dead}" if dead else ""))
            if not ok:
                failures.append({'class': 'intention', 'query': msg,
                                 'expect': f'fire={should_fire}',
                                 'node_id': None, 'tokens': len(out) // 4,
                                 'error': dead, 'out_head': (out or err)[:400]})
                if dead:
                    broken.append(f"intention {msg[:50]!r}: {dead}")
    finally:
        subprocess.run(BQ + ['delete', '--name', INTENTION_NODE_NAME], capture_output=True, text=True, cwd=WS)
    return n, hit, failures, broken


def informative_words(text, k=3):
    words = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z0-9_-]{3,}", text)]
    return [w for w in words if w not in STOP][:k]


def mine_cases(db, per_class=35):
    cases = []  # (cls, query, expect_regex, flags, node_id)
    # doc frequency for informativeness
    df = Counter()
    names = db.execute(f"""SELECT id, name FROM nodes WHERE type IN {KNOWLEDGE_TYPES}
        AND length(name) > 20 AND props NOT LIKE '%superseded_by%'""").fetchall()
    for _, nm in names:
        for w in set(informative_words(nm, 10)):
            df[w] += 1
    rare = lambda w: df[w] <= max(3, len(names) // 50)

    # name_partial
    step = max(1, len(names) // per_class)
    for nid, nm in names[::step][:per_class]:
        ws = [w for w in informative_words(nm, 8) if rare(w)][:3]
        if len(ws) < 2:
            continue
        expect = re.escape(nm[:38])
        cases.append(("name_partial", " ".join(ws), expect, [], nid))

    # prop_value
    rows = db.execute(f"""SELECT id, name, props FROM nodes WHERE type IN {KNOWLEDGE_TYPES}
        AND props LIKE '%@%' AND props NOT LIKE '%superseded_by%' LIMIT 400""").fetchall()
    step = max(1, len(rows) // per_class)
    for nid, nm, props in rows[::step][:per_class]:
        m = re.search(r'[\w.+-]+@[\w.-]+\.\w+', props or '')
        owner_emails = {e.lower() for e in bpconfig.get('owner_emails', [])}
        if not m or m.group(0).lower() in owner_emails:
            continue
        cases.append(("prop_value", m.group(0), re.escape(nm[:38]), [], nid))

    # content_probe
    rows = db.execute(f"""SELECT id, name, content FROM nodes WHERE type IN {KNOWLEDGE_TYPES}
        AND length(content) > 250 AND props NOT LIKE '%superseded_by%' LIMIT 600""").fetchall()
    step = max(1, len(rows) // per_class)
    for nid, nm, content in rows[::step][:per_class]:
        ws = [w for w in informative_words(content, 20) if rare(w)][:4]
        if len(ws) < 3:
            continue
        cases.append(("content_probe", " ".join(ws), re.escape(nm[:38]), [], nid))
    return cases


def run_recall(query, flags=()):
    """Returns (stdout, stderr, returncode, elapsed_seconds)."""
    t0 = time.time()
    try:
        r = subprocess.run(BQ + ['recall', query, '--compact', '--budget', '400'] + list(flags),
                           capture_output=True, text=True, timeout=60, cwd=WS)
        return (r.stdout or ''), (r.stderr or ''), r.returncode, time.time() - t0
    except subprocess.TimeoutExpired:
        return '', 'recall timed out after 60s', 124, 60.0
    except Exception as exc:
        return '', f'could not run the engine: {exc}', 126, time.time() - t0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mine', action='store_true')
    ap.add_argument('--run', action='store_true')
    ap.add_argument('--label', default=time.strftime('%Y%m%d-%H%M'))
    ap.add_argument('--limit', type=int, default=0, help='cap cases per class')
    ap.add_argument('--diff', nargs=2, metavar=('A', 'B'))
    args = ap.parse_args()

    if args.diff:
        a = json.load(open(f'{RESULTS_DIR}/battery-{args.diff[0]}.json'))
        b = json.load(open(f'{RESULTS_DIR}/battery-{args.diff[1]}.json'))
        print(f"{'class':14} {args.diff[0]:>12} {args.diff[1]:>12}")
        for cls in sorted(set(a['by_class']) | set(b['by_class'])):
            ra, rb = a['by_class'].get(cls, {}), b['by_class'].get(cls, {})
            print(f"{cls:14} {ra.get('hit', 0)}/{ra.get('n', 0):>3}        {rb.get('hit', 0)}/{rb.get('n', 0):>3}")
        print(f"{'avg tokens':14} {a.get('avg_tokens', '?'):>12} {b.get('avg_tokens', '?'):>12}")
        print(f"{'avg ms':14} {a.get('avg_ms', '?'):>12} {b.get('avg_ms', '?'):>12}")
        return

    db = sqlite3.connect(DB)
    cases = mine_cases(db)
    db.close()
    for q, e in PARAPHRASE:
        cases.append(("paraphrase", q, e, [], None))
    for q, e, nn, note in ADVERSARIAL:
        cases.append(("adversarial", q, e, [], None))
    for q in NEGATIVE:
        cases.append(("negative", q, None, [], None))

    if args.limit:
        by = defaultdict(list)
        for c in cases:
            by[c[0]].append(c)
        cases = [c for cls in by for c in by[cls][:args.limit]]

    if args.mine and not args.run:
        for cls, q, e, fl, nid in cases:
            print(f"[{cls:13}] {q!r}  → expect /{(e or 'NO-HIT')[:50]}/")
        print(f"\n{len(cases)} cases total")
        return

    if not args.run:
        print("use --mine or --run"); return

    stats = defaultdict(lambda: {'n': 0, 'hit': 0})
    failures, broken, tok_sum, ms_sum = [], [], 0, 0
    adv_notes = {q: (nn, note) for q, e, nn, note in ADVERSARIAL}
    for i, (cls, q, expect, flags, nid) in enumerate(cases):
        out, err, code, el = run_recall(q, flags)
        tokens = len(out) // 4
        tok_sum += tokens; ms_sum += el * 1000
        dead = engine_failure(err, code)
        if dead:
            # Not a miss. The engine did not answer, so this case has no score.
            hit = False
        elif cls == 'negative':
            # Pass only when the engine ran and said, in words, that it has
            # nothing. An empty stdout is a symptom, not an abstain.
            if not out.strip():
                dead = 'the engine printed nothing at all'
                hit = False
            else:
                hit = bool(ABSTAIN.search(out)) and '== DIRECT ==' not in out
        else:
            hit = bool(re.search(expect, out, re.I))
            nn, _ = adv_notes.get(q, (None, None))
            if hit and nn and re.search(nn, out, re.M):
                hit = False
        stats[cls]['n'] += 1
        stats[cls]['hit'] += hit
        if not hit:
            failures.append({'class': cls, 'query': q, 'expect': expect,
                             'node_id': nid, 'tokens': tokens,
                             'error': dead, 'out_head': (out or err)[:400]})
            if dead:
                broken.append(f"[{cls}] {q[:50]!r}: {dead}")
        mark = '✅' if hit else ('💥' if dead else '❌')
        print(f"  {mark} [{cls:13}] {q[:60]!r}" + (f" — {dead}" if dead else ""))

    # prospective-memory (intention) class — stateful, runs through msgctx
    if not args.limit or args.limit >= 1:
        i_n, i_hit, i_fail, i_broken = run_intention_class()
        stats['intention']['n'] += i_n
        stats['intention']['hit'] += i_hit
        failures.extend(i_fail)
        broken.extend(i_broken)

    n = sum(s['n'] for s in stats.values())
    print(f"\n{'='*52}\nBATTERY RESULTS ({args.label})\n{'='*52}")
    for cls, s in sorted(stats.items()):
        print(f"  {cls:14} {s['hit']:3}/{s['n']:3}  ({s['hit']*100//max(s['n'],1)}%)")
    total_hit = sum(s['hit'] for s in stats.values())
    print(f"  {'TOTAL':14} {total_hit:3}/{n:3}  ({total_hit*100//max(n,1)}%)")
    rn = len(cases)  # recall-path cases only (intention runs via msgctx)
    print(f"  avg tokens/recall: {tok_sum//max(rn,1)} | avg latency: {int(ms_sum/max(rn,1))}ms")

    result = {'label': args.label, 'total': n, 'hit': total_hit,
              'by_class': {k: dict(v) for k, v in stats.items()},
              'broken': len(broken), 'broken_detail': broken[:20],
              'avg_tokens': tok_sum // max(rn, 1), 'avg_ms': int(ms_sum / max(rn, 1))}
    with open(f'{RESULTS_DIR}/battery-{args.label}.json', 'w') as f:
        json.dump(result, f, indent=1)
    with open(f'{RESULTS_DIR}/battery-{args.label}-failures.jsonl', 'w') as f:
        for x in failures:
            f.write(json.dumps(x) + '\n')
    print(f"\nSaved: logs/battery-{args.label}.json (+failures.jsonl, {len(failures)} misses)")

    # A broken engine ends the run. No percentage from a program that did not
    # run is worth reading, and a battery that hides that is worse than none.
    if broken:
        print(f"\n💥 ENGINE BROKEN — {len(broken)} case(s) could not run:")
        for b in broken[:5]:
            print(f"  {b}")
        if len(broken) > 5:
            print(f"  ... and {len(broken) - 5} more")
        print("❌ BATTERY FAILED (the engine did not run; these results mean nothing)")
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
