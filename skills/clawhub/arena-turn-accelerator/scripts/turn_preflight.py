#!/usr/bin/env python3
"""
turn_preflight.py — one command that optimizes a whole turn before you hit send.

  1. compacts the prompt (faster first token)
  2. opens a new generation (stale answers get fenced out)
  3. assesses context health (zombie-mode early warning)
  4. classifies pressure-vs-evidence and emits an anti-sycophancy guard
  5. picks the delivery register (plain / comic / never-martyred)
  6. finds the seed and reads the opening (strike / stalk / deliver-first)
  7. flags verification false-positive risk
  8. ARBITER: collapses all of the above into ONE non-contradictory instruction

Usage:
  turn_preflight.py --text "your prompt" [--turn N --chars N --latency F]
                    [--stakes low|normal|high] [--rapport cold|warm]
                    [--draft "your drafted reply"]   # audits YOUR text for the anti-pattern
"""
import argparse, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def run(script, args):
    return subprocess.run([sys.executable, os.path.join(HERE, script)] + args,
                          capture_output=True, text=True, timeout=60)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", required=True)
    ap.add_argument("--turn", type=int); ap.add_argument("--chars", type=int)
    ap.add_argument("--latency", type=float, default=0.0)
    ap.add_argument("--stakes", choices=["low", "normal", "high"], default="normal")
    ap.add_argument("--rapport", choices=["cold", "warm"], default="warm")
    ap.add_argument("--draft")
    ap.add_argument("--turns-since-strike", type=int, default=99)
    ap.add_argument("--urgent", action="store_true")
    a = ap.parse_args()

    print("=" * 62); print("TURN PREFLIGHT"); print("=" * 62)

    print("\n[1/8] PROMPT COMPACTION")
    print(run("prompt_compactor.py", ["--text", a.text]).stdout.rstrip())

    print("\n[2/8] REQUEST FENCE")
    print(run("request_lifecycle.py", ["new", a.text[:200]]).stdout.rstrip())
    print("      chunks from an older generation are discarded, not rendered")

    print("\n[3/8] CONTEXT HEALTH")
    if a.turn and a.chars:
        run("context_hygiene.py", ["record", "--turn", str(a.turn),
                                   "--chars", str(a.chars), "--latency", str(a.latency)])
    r = run("context_hygiene.py", ["assess"])
    print(r.stdout.rstrip() or "      (pass --turn/--chars to enable zombie detection)")

    print("\n[4/8] INTELLECTUAL SPINE (hold or fold?)")
    print(run("spine.py", ["classify", a.text]).stdout.rstrip())
    g = run("spine.py", ["guard", a.text])
    if g.stdout.strip():
        print("  GUARD TO PREPEND:"); print("  " + g.stdout.strip())

    print("\n[5/8] DELIVERY REGISTER (in what voice?)")
    print(run("register.py", ["pick", a.text, "--stakes", a.stakes,
                              "--rapport", a.rapport]).stdout.rstrip())
    if a.draft:
        print("\n  --- auditing your draft ---")
        print(run("register.py", ["check", a.draft]).stdout.rstrip())

    print("\n[6/8] QUARRY (invent now? out of what?)")
    print(run("quarry.py", ["opening", a.text, "--turns-since-strike",
                            str(a.turns_since_strike)]).stdout.rstrip())
    sd = run("quarry.py", ["seed", a.text]).stdout.rstrip()
    if "REAL SEED (the thing" in sd:
        print("\n" + "\n".join(sd.split("\n")[2:8]))
    if a.draft:
        print("\n  --- auditing your draft for begging/hedging ---")
        print(run("quarry.py", ["check", a.draft]).stdout.rstrip())

    print("\n[7/8] VERIFICATION RISK")
    print("      run: verification_triage.py --vpn yes --blocker strict --cookies blocked --tabs 6")
    print("      (only needed if CAPTCHAs are appearing)")

    print("\n[8/8] ARBITER — the single coherent instruction")
    print(run("arbiter.py", [a.text, "--stakes", a.stakes, "--rapport", a.rapport,
                             "--turns-since-strike", str(a.turns_since_strike)]
              + (["--urgent"] if a.urgent else [])).stdout.rstrip())

    print("\n" + "=" * 62)
    print("Follow the ARBITER block — it already resolves conflicts between the modules above.")


if __name__ == "__main__":
    main()
