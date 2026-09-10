#!/usr/bin/env python3
"""turn_report.py — rolling self-improvement stats (v2.0.0). READ-ONLY.

Aggregates the per-agent, per-model history that context_hygiene.py records
and turns it into numbers an agent can act on: latency baseline + trend,
transcript growth, current zombie verdict. Adaptive baselines come from THIS
machine's own measurements — never hardcoded guesses from another box.

Usage: turn_report.py [--agent NAME] [--ctx-tokens N] [--json]
Exit codes mirror the verdict: 0 HEALTHY · 1 WATCH · 2 COMPACT NOW · 3 RESET.
"""
import json, os, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import agent_state, context_hygiene  # noqa: E402

try:
    import utf8io
except ImportError:  # pragma: no cover
    import os as _os, sys as _sys
    _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
    import utf8io
utf8io.utf8_io()

RC = {"HEALTHY": 0, "WATCH": 1, "COMPACT NOW": 2, "RESET": 3}


def report(ctx_tokens=None):
    s = context_hygiene.load()
    th = context_hygiene.thresholds(ctx_tokens, s)
    samples = s.get("samples", [])
    out = {"schema": "turn_report.v1",
           "agent": os.environ.get("ARENA_AGENT", "default"),
           "samples_total": len(samples)}
    if not samples:
        out.update({"verdict": "HEALTHY",
                    "note": "no recorded turns yet — run turn_preflight with --turn/--chars/--latency"})
        return out

    lat = [x["latency"] for x in samples if x.get("latency")]
    chars = [x["chars"] for x in samples if x.get("chars")]
    model_run, cur_model = context_hygiene._current_model_run(s)  # trend scoped to current model

    def ema(xs, a=0.3):
        e = None
        for v in xs:
            e = v if e is None else a * v + (1 - a) * e
        return e

    if lat:
        med = statistics.median(lat)
        e = ema(lat)
        recent = statistics.median(lat[-3:]) if len(lat) >= 3 else med
        out["latency_s"] = {"median": round(med, 2), "ema": round(e, 2),
                            "recent3": round(recent, 2),
                            "trend_pct": round((recent / med - 1) * 100, 1) if med else 0.0}
    if chars:
        budget = max(1, int(th.get("reset_chars") or 1))
        out["chars"] = {"last": chars[-1], "median": statistics.median(chars),
                        "budget_reset": th["reset_chars"],
                        "pct_of_reset_budget": round(chars[-1] / budget * 100, 1)}
    score, comp = context_hygiene.zombie_score(s, th)
    v, action = context_hygiene.verdict(score, s, th)
    out["zombie"] = {"score": score, "components": comp, "verdict": v, "action": action}
    out["verdict"] = v
    out["model_run_samples"] = len(model_run)
    out["model"] = cur_model
    return out


def main():
    agent = None; ctx = None; as_json = False
    argv = sys.argv[1:]
    i = 0
    while i < len(argv):
        if argv[i] == "--agent" and i + 1 < len(argv):
            agent = argv[i + 1]
            os.environ["ARENA_AGENT"] = agent
            # BUG FIXED (v2.1.1, found by the ClawHub security scanner):
            # context_hygiene binds its STATE path at IMPORT time (line 16 above),
            # which happens before this loop runs. Setting the environment variable
            # here was therefore too late: `--agent alice` kept reading the DEFAULT
            # agent's context.json while labelling the output agent="alice" — it
            # reported one agent's data under another agent's name, the exact
            # cross-agent contamination this skill exists to prevent. Rebind the
            # already-imported module's STATE to the requested agent.
            context_hygiene.STATE = agent_state.state_path("context.json", agent)
            i += 2
        elif argv[i] == "--ctx-tokens" and i + 1 < len(argv):
            ctx = int(argv[i + 1]); i += 2
        elif argv[i] == "--json":
            as_json = True; i += 1
        else:
            print(__doc__); return 2
    r = report(ctx)
    if as_json:
        print(json.dumps(r, indent=2, ensure_ascii=False, default=str))
    else:
        print(f"verdict: {r['verdict']}   (samples={r['samples_total']}, agent={r['agent']})")
        if "latency_s" in r:
            t = r["latency_s"]; print(f"latency: median {t['median']}s · ema {t['ema']}s · trend {t['trend_pct']}%")
        if "chars" in r:
            c = r["chars"]; print(f"transcript: {c['last']} chars ({c['pct_of_reset_budget']}% of reset budget)")
        if "zombie" in r:
            print(f"zombie: {r['zombie']['score']}/100 → {r['zombie']['action']}")
    return RC.get(r["verdict"], 0)


if __name__ == "__main__":
    sys.exit(main())
