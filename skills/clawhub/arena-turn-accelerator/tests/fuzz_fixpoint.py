#!/usr/bin/env python3
"""Fixpoint fuzz for prompt_compactor (v1.5.0 regression).

Runs N random inputs over a multilingual adversarial alphabet and asserts
compact(compact(x)) == compact(x) for every one. The v1.4 single-pass pipeline
failed this 159/4000 times; the v1.5 fixpoint-by-construction pipeline must
fail 0.
"""
import random, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
from prompt_compactor import selfcheck  # noqa: E402

def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 500
    random.seed(3)
    alpha = list("abc?!؟0: \n.,سلاممرسی لطفا»«\"`'`_;") + ["می‌کنم", "hello", "please", "?؟"]
    bad = 0
    for i in range(n):
        t = "".join(random.choice(alpha) for _ in range(random.randint(0, 90)))
        ok, _d = selfcheck(t)
        if not ok:
            bad += 1
            print(f"FAIL {t!r}")
    print(f"{n - bad}/{n} fixpoint clean")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
