"""
Exhaustive model check of the request fence.

Enumerates EVERY sequence of operations up to depth N over a small alphabet, runs the real
CLI, and asserts the two safety properties that the whole module exists to guarantee:

  SAFETY-1 (no stale render): an answer may only render if its generation is current.
  SAFETY-2 (no lost retry):   resending an identical prompt while it is still in flight
                              must NOT discard the in-flight answer.

Plus liveness: the generation counter never decreases.
"""
import itertools
import pathlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

CLI = str(pathlib.Path(__file__).resolve().parent.parent / "scripts" / "request_lifecycle.py")

# Small alphabet: two distinct prompts, plus lifecycle ops.
OPS = [("new", "A"), ("new", "B"), ("supersede", None), ("complete", "cur"), ("complete", "old")]


def run(home, args):
    return subprocess.run([sys.executable, CLI] + args, capture_output=True, text=True,
                          env=dict(os.environ, HOME=home), timeout=60)


def state(home):
    p = os.path.join(home, ".arena_turn", "lifecycle.json")
    if not os.path.exists(p):
        return {"generation": 0, "inflight": None, "history": []}
    return json.load(open(p))


def check_sequence(seq):
    home = tempfile.mkdtemp()
    try:
        last_gen = 0
        for op, arg in seq:
            before = state(home)
            if op == "new":
                run(home, ["new", arg])
            elif op == "supersede":
                run(home, ["supersede"])
            elif op == "complete":
                g = before["generation"] if arg == "cur" else max(0, before["generation"] - 1)
                run(home, ["complete", str(g)])

            after = state(home)

            # liveness: generation is monotonic
            if after["generation"] < last_gen:
                return f"generation decreased {last_gen} -> {after['generation']} at {op}/{arg}"
            last_gen = after["generation"]

            # SAFETY-1: only the current generation may render
            for g in range(0, after["generation"] + 2):
                r = run(home, ["check", str(g)])
                renders = "RENDER" in r.stdout
                if renders and g != after["generation"]:
                    return f"stale render: gen {g} rendered, current {after['generation']}"
                if not renders and g == after["generation"]:
                    return f"current gen {g} refused to render"

            # SAFETY-2: identical resend must not abort the in-flight generation
            if op == "new" and before.get("inflight") and \
               before["inflight"].get("status") == "running" and \
               before["inflight"].get("prompt") == arg:
                if after["generation"] != before["generation"]:
                    return (f"lost retry: resending {arg!r} bumped "
                            f"{before['generation']} -> {after['generation']}")
        return None
    finally:
        shutil.rmtree(home, ignore_errors=True)


def main():
    depth = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    total = 0
    for n in range(1, depth + 1):
        for seq in itertools.product(OPS, repeat=n):
            total += 1
            err = check_sequence(seq)
            if err:
                print("VIOLATION")
                print("  sequence:", " -> ".join(f"{o}({a})" for o, a in seq))
                print("  error   :", err)
                return 1
    print(f"OK — {total} sequences up to depth {depth}, no safety violation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
