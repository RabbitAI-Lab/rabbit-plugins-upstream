import pathlib
"""
Mutation testing — deliberately inject bugs and confirm the test suites CATCH them.

A green suite is worthless if it cannot fail. Each mutant below is a realistic bug.
If a mutant SURVIVES (all tests still pass), the suite has a blind spot there.
"""
import re
import shutil
import subprocess
import sys
import tempfile
import os

SRC = str(pathlib.Path(__file__).resolve().parent.parent)

MUTANTS = [
    # (file, find, replace, description)
    ("scripts/spine.py", 'if e == 0 and p <= 1:', 'if e == 0 and p <= 99:',
     "spine: pressure threshold raised -> never detects pressure"),
    ("scripts/spine.py", 'elif e > 0 and p == 0:', 'elif e > 0 and p == 999:',
     "spine: evidence-only branch unreachable"),
    ("scripts/spine.py", '(3, r"\\badmit\\s+(?:your|the|you\'?re|it|that)\\b", "demand for confession"),',
     '(0, r"\\badmit\\s+(?:your|the|you\'?re|it|that)\\b", "demand for confession"),',
     "spine: 'admit it' weighted to zero"),
    ("scripts/register.py", 'if blockers or stakes == "high":', 'if blockers and stakes == "high":',
     "register: grief no longer blocks comedy on its own"),
    ("scripts/quarry.py", 'if r["blocked"]:', 'if r["blocked"] and False:',
     "quarry: utility blockers ignored -> strikes during outages"),
    ("scripts/quarry.py", 'if urgent:', 'if urgent and False:',
     "quarry: --urgent ignored"),
    ("scripts/prompt_compactor.py", 'if has_constraint(seg):', 'if False:',
     "compactor: constraint guard disabled -> drops numbers"),
    ("scripts/prompt_compactor.py",
     'QUESTION_RE = re.compile(r"(?:(?<=^)|(?<=[.?!؟？\\n]))[^.?!؟？\\n]*[?؟？]")',
     'QUESTION_RE = re.compile(r"[^.?!؟？\\n]*[?؟？]", re.S)',
     "compactor: ReDoS regex restored (perf regression)"),
    ("scripts/request_lifecycle.py", 'and cur.get("fingerprint") == fp',
     'and cur.get("fingerprint") != fp',
     "fence: retry detection inverted -> the v1.3.2 bug returns"),
    ("scripts/request_lifecycle.py", 'if gen == s["generation"]:', 'if gen <= s["generation"]:',
     "fence: stale answers render -> the original problem 2 returns"),
    ("scripts/arbiter.py", 'if s["verdict"] == "PURE SOCIAL PRESSURE":\n            # THE GENUINE CONFLICT',
     'if False:\n            # THE GENUINE CONFLICT',
     "arbiter: hold-vs-strike conflict no longer resolved"),
    ("scripts/arbiter.py", 'if q["blocked"]:', 'if q["blocked"] and False:',
     "arbiter: utility precedence removed"),
    ("scripts/arbiter.py", 'elif s["evidence_score"] > 0 and s["verdict"] != "NEUTRAL":',
     'elif False:',
     "arbiter: evidence never acknowledged"),
]


def run_suites(root):
    """Return True if ALL suites pass in `root`."""
    env = dict(os.environ, HOME=root + "/home")
    os.makedirs(root + "/home", exist_ok=True)
    st = subprocess.run(["bash", "scripts/selftest.sh"], cwd=root,
                        capture_output=True, text=True, env=env, timeout=600)
    if st.returncode != 0:
        return False, "selftest"
    pt = subprocess.run([sys.executable, "-m", "pytest", str(pathlib.Path(__file__).resolve().parent / "test_properties.py"),
                         "-q", "-x", "--no-header", "-p", "no:cacheprovider"],
                        capture_output=True, text=True, timeout=900,
                        env=dict(env, PYTHONPATH=root + "/scripts"))
    if pt.returncode != 0:
        return False, "properties"
    return True, ""


def main():
    killed, survived = [], []
    for path, find, repl, desc in MUTANTS:
        with tempfile.TemporaryDirectory() as td:
            root = td + "/plugin"
            shutil.copytree(SRC, root)
            f = os.path.join(root, path)
            src = open(f).read()
            if find not in src:
                survived.append((desc, "PATTERN NOT FOUND — mutant invalid"))
                print(f"?? INVALID  {desc}")
                continue
            open(f, "w").write(src.replace(find, repl, 1))
            ok, which = run_suites(root)
            if ok:
                survived.append((desc, "tests still passed"))
                print(f"!! SURVIVED {desc}")
            else:
                killed.append((desc, which))
                print(f"ok KILLED   [{which}] {desc}")

    print(f"\nkilled {len(killed)}/{len(MUTANTS)}  survived {len(survived)}")
    if survived:
        print("\nBLIND SPOTS:")
        for d, why in survived:
            print(f"  - {d}  ({why})")
    return 1 if survived else 0


if __name__ == "__main__":
    sys.exit(main())
