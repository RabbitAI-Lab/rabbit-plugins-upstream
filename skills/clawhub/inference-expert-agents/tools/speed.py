#!/usr/bin/env python3
"""speed.py — token-generation throughput toolkit (v2.1).

measure      tok/s from tokens+seconds, with honest sanity bands
plan         prioritized serving-config levers (local or API) with evidence-based gains
parallelize  how to run self-consistency samples without serial latency

A skill cannot make a server faster, but it can (a) never be the bottleneck
(terse contracts, compression), (b) measure, and (c) prescribe the right levers.
Stdlib-only, read-only.
"""
import argparse, json, sys

LOCAL_LEVERS = [
    {"lever": "EAGLE-2 speculative decoding", "gain": "2-3x", "cost": "~1-2% extra params",
     "note": "2026 default for production serving; provably exact output"},
    {"lever": "Medusa decoding heads", "gain": "2.2-3.6x", "cost": "head fine-tune",
     "note": "no separate draft model needed (arXiv:2401.10774)"},
    {"lever": "vanilla speculative decoding", "gain": "1.5-2x", "cost": "draft model, same tokenizer",
     "note": "provably exact; acceptance 70-90% with well-matched pairs"},
    {"lever": "continuous batching", "gain": "5-10x throughput", "cost": "+latency per request",
     "note": "vLLM; batching 32 requests cuts per-token cost ~85%"},
    {"lever": "INT4 weight quantization (AWQ/GPTQ)", "gain": "-75% cost/mem", "quality": "1-2% degradation",
     "note": "INT8 if quality-critical (-50% cost, <1% loss)"},
    {"lever": "prefix/prompt caching", "gain": "skips re-prefill of shared prefixes",
     "note": "huge for the skill's fixed doctrine prefix — keep the system prompt byte-stable"},
    {"lever": "PagedAttention", "gain": "KV waste 60-80% -> <4%; ~10x concurrency"},
    {"lever": "constrained decoding (grammar)", "gain": "neutral or +20% on JSON outputs",
     "note": "guarantees schema conformance for machine-readable modes"},
]

API_LEVERS = [
    {"lever": "batched n>1 sampling", "gain": "N self-consistency samples in ONE request",
     "note": "one queue hop instead of N; often half the wall-time of serial calls"},
    {"lever": "provider prompt caching", "gain": "cached-prefix reads are cheap+fast",
     "note": "keep the skill's stable instructions as a byte-stable prefix"},
    {"lever": "route by difficulty (cascade.py)", "gain": "cheap tiers for L0/L1 queries",
     "note": "FrugalGPT: matched quality at up to 96% lower cost"},
    {"lever": "stream + early exit", "gain": "perceived latency; abort at conf floor",
     "note": "deliberate.py abort_floor stops doomed generations early"},
]

def band(tps):
    if tps >= 200: return "very fast (optimized stack or very small model)"
    if tps >= 80: return "healthy local/server range"
    if tps >= 25: return "typical API range"
    if tps >= 5: return "slow — check network, max_tokens, batching"
    return "very slow — something is wrong (throttle, cold start, or CPU-only)"

# v2.1.2: shared clean-error contract — never traceback ({"error":...} + exit 2)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _common import clean_errors


@clean_errors
def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("measure")
    m.add_argument("--tokens", type=int, default=None)
    m.add_argument("--seconds", type=float, default=None)
    m.add_argument("--samples-file", default=None,
                    help="JSON array [{tokens, seconds}, ...] for aggregate bands")
    p = sub.add_parser("plan")
    p.add_argument("--deployment", choices=["local", "api"], required=True)
    p.add_argument("--goal", choices=["speed", "cost", "both"], default="both")
    z = sub.add_parser("parallelize")
    z.add_argument("--samples", type=int, default=5)
    a = ap.parse_args()
    if a.cmd == "measure":
        if a.samples_file:
            try:
                samples = json.load(open(a.samples_file, encoding="utf-8"))
                vals = sorted(s["tokens"] / s["seconds"] for s in samples)
                assert vals and all(v > 0 for v in vals)
            except Exception as e:
                print(json.dumps({"error": f"bad samples file: {e}"})); return 2
            n = len(vals)
            p50 = vals[n // 2]
            print(json.dumps({"n": n, "mean_tps": round(sum(vals) / n, 1),
                              "p50_tps": round(p50, 1),
                              "min_tps": round(vals[0], 1), "max_tps": round(vals[-1], 1),
                              "assessment": band(p50),
                              "hint": "log tok/s per rung in ladder_trace latency_s fields"},
                             indent=2))
            return 0
        if not a.tokens or not a.seconds or a.tokens <= 0 or a.seconds <= 0:
            print(json.dumps({"error": "tokens/seconds must be positive"})); return 2
        tps = a.tokens / a.seconds
        print(json.dumps({"tokens_per_second": round(tps, 1),
                          "tokens": a.tokens, "seconds": a.seconds,
                          "assessment": band(tps),
                          "hint": "log tok/s per rung in ladder_trace latency_s fields"}, indent=2))
        return 0
    if a.cmd == "parallelize":
        n = max(2, a.samples)
        print(json.dumps({
            "samples": n,
            "preferred": f"single request with n={n} (provider sampling parameter) — one queue hop",
            "fallback": f"{n} concurrent requests (threads) if n>1 unsupported",
            "never": "serial sequential calls for independent samples",
            "note": "self-consistency samples are independent by definition — parallelism is free accuracy",
        }, indent=2)); return 0
    levers = LOCAL_LEVERS if a.deployment == "local" else API_LEVERS
    if a.goal == "speed":
        levers = [l for l in levers if "throughput" in json.dumps(l) or "x" in l.get("gain", "")]
    print(json.dumps({
        "deployment": a.deployment, "goal": a.goal,
        "levers": levers,
        "first_move": ("enable prefix caching + keep skill doctrine byte-stable"
                       if a.deployment == "api" else
                       "enable continuous batching, then EAGLE-2/Medusa, then INT4"),
        "measure_after": "speed.py measure --tokens N --seconds S; A/B via eval_regression",
    }, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
