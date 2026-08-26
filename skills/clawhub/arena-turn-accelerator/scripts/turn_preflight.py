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

v1.5.0 — any agent, any model:
  * --json emits ONE schema-versioned object bundling every stage, so agents
    other than the author's can consume preflight programmatically instead of
    scraping human text (each stage also stays runnable standalone).
  * --agent NAME isolates all per-session state (~/.arena_turn/agents/<name>/)
    so several agents sharing one machine cannot fence out or zombify each
    other. No flag = legacy shared dir = zero behaviour change.
  * --ctx-tokens N passes the model's real context window through to the
    hygiene stage, and --model M scopes the latency trend to that model.

Usage:
  turn_preflight.py --text "your prompt" [--turn N --chars N --latency F]
                    [--stakes low|normal|high] [--rapport cold|warm]
                    [--draft "your drafted reply"]        # audits YOUR text
                    [--json] [--agent NAME] [--model M] [--ctx-tokens N]
"""
import argparse, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def run(script, args, env=None):
    e = dict(os.environ)
    if env:
        e.update(env)
    return subprocess.run([sys.executable, os.path.join(HERE, script)] + args,
                          capture_output=True, text=True, timeout=60, env=e)


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
    ap.add_argument("--json", action="store_true", help="emit one machine-readable bundle")
    ap.add_argument("--agent", default=None,
                    help="isolate state per agent (~/.arena_turn/agents/<name>/)")
    ap.add_argument("--model", default="", help="model id serving this turn")
    ap.add_argument("--ctx-tokens", type=int, default=None,
                    help="model context window for scaled hygiene thresholds")
    a = ap.parse_args()

    env = {}
    if a.agent:
        env["ARENA_AGENT"] = a.agent

    # ── machine bundle path ────────────────────────────────────────────────
    if a.json:
        import prompt_compactor, spine, arbiter
        bundle = {"schema": "turn_preflight.v1", "agent": a.agent or
                  (env.get("ARENA_AGENT") or "default"), "text_chars": len(a.text)}

        c = prompt_compactor.compact(a.text)
        bundle["compaction"] = {k: c[k] for k in
                                ("compact", "chars_saved", "percent_saved", "est_tokens_compact",
                                 "lang_detected", "profile", "warnings")}

        rl = run("request_lifecycle.py", ["new", a.text[:200], "--json"], env)
        try:
            bundle["fence"] = json.loads(rl.stdout)
        except Exception:
            bundle["fence"] = {"raw": rl.stdout.strip()[:200]}

        if a.turn and a.chars:
            rec = ["record", "--turn", str(a.turn), "--chars", str(a.chars),
                   "--latency", str(a.latency)]
            if a.model:
                rec += ["--model", a.model]
            if a.ctx_tokens:
                rec += ["--ctx-tokens", str(a.ctx_tokens)]
            run("context_hygiene.py", rec, env)
        hy = run("context_hygiene.py", ["assess", "--json"] +
                 (["--ctx-tokens", str(a.ctx_tokens)] if a.ctx_tokens else []), env)
        try:
            bundle["hygiene"] = json.loads(hy.stdout)
        except Exception:
            bundle["hygiene"] = {"raw": hy.stdout.strip()[:200]}

        bundle["spine"] = spine.classify(a.text)
        g = spine.guard(a.text) if hasattr(spine, "guard") else ""
        bundle["spine_guard"] = g if isinstance(g, str) else str(g)
        bundle["arbiter"] = arbiter.decide(a.text, a.stakes, a.rapport,
                                           a.turns_since_strike, a.urgent)
        print(json.dumps(bundle, indent=2, ensure_ascii=False, default=str))
        return 0

    # ── human path (unchanged since v1.4) ──────────────────────────────────
    print("=" * 62); print("TURN PREFLIGHT"); print("=" * 62)

    print("\n[1/8] PROMPT COMPACTION")
    print(run("prompt_compactor.py", ["--text", a.text], env).stdout.rstrip())

    print("\n[2/8] REQUEST FENCE")
    print(run("request_lifecycle.py", ["new", a.text[:200]], env).stdout.rstrip())
    print("      chunks from an older generation are discarded, not rendered")

    print("\n[3/8] CONTEXT HEALTH")
    if a.turn and a.chars:
        rec = ["record", "--turn", str(a.turn), "--chars", str(a.chars),
               "--latency", str(a.latency)]
        if a.model:
            rec += ["--model", a.model]
        if a.ctx_tokens:
            rec += ["--ctx-tokens", str(a.ctx_tokens)]
        run("context_hygiene.py", rec, env)
    r = run("context_hygiene.py", ["assess"] +
            (["--ctx-tokens", str(a.ctx_tokens)] if a.ctx_tokens else []), env)
    print(r.stdout.rstrip() or "      (pass --turn/--chars to enable zombie detection)")

    print("\n[4/8] INTELLECTUAL SPINE (hold or fold?)")
    print(run("spine.py", ["classify", a.text], env).stdout.rstrip())
    g = run("spine.py", ["guard", a.text], env)
    if g.stdout.strip():
        print("  GUARD TO PREPEND:"); print("  " + g.stdout.strip())

    print("\n[5/8] DELIVERY REGISTER (in what voice?)")
    print(run("register.py", ["pick", a.text, "--stakes", a.stakes,
                              "--rapport", a.rapport], env).stdout.rstrip())
    if a.draft:
        print("\n  --- auditing your draft ---")
        print(run("register.py", ["check", a.draft], env).stdout.rstrip())

    print("\n[6/8] QUARRY (invent now? out of what?)")
    print(run("quarry.py", ["opening", a.text, "--turns-since-strike",
                            str(a.turns_since_strike)], env).stdout.rstrip())
    sd = run("quarry.py", ["seed", a.text], env).stdout.rstrip()
    if "REAL SEED (the thing" in sd:
        print("\n" + "\n".join(sd.split("\n")[2:8]))
    if a.draft:
        print("\n  --- auditing your draft for begging/hedging ---")
        print(run("quarry.py", ["check", a.draft], env).stdout.rstrip())

    print("\n[7/8] VERIFICATION RISK")
    print("      run: verification_triage.py --vpn yes --blocker strict --cookies blocked --tabs 6")
    print("      (only needed if CAPTCHAs are appearing)")

    print("\n[8/8] ARBITER — the single coherent instruction")
    print(run("arbiter.py", [a.text, "--stakes", a.stakes, "--rapport", a.rapport,
                             "--turns-since-strike", str(a.turns_since_strike)]
              + (["--urgent"] if a.urgent else []), env).stdout.rstrip())

    print("\n" + "=" * 62)
    print("Follow the ARBITER block — it already resolves conflicts between the modules above.")


if __name__ == "__main__":
    main()
