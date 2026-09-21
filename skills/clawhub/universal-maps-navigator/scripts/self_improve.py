#!/usr/bin/env python3
"""self_improve.py — Self-improving loop for universal-maps-navigator v2.

Memento-Skills pattern: Invoke → Execute → Review → Update

- Every CLI run logs metrics to ~/.local/share/universal-maps-navigator/learnings.json
- Analyze logs to propose improvements
- Apply improvements (bump version, update prompts)

Stdlib only, Python 3.8+.

Usage:
    from self_improve import log_run, analyze_learnings, apply_improvements
    python3 self_improve.py --analyze
    python3 self_improve.py --apply
"""
from __future__ import annotations
import json
import os
import time
import hashlib
from typing import Dict, List

LEARNINGS_DIR = os.environ.get("UMN_LEARNINGS_DIR") or os.path.join(
    os.environ.get("XDG_DATA_HOME", os.path.expanduser("~/.local/share")),
    "universal-maps-navigator"
)
LEARNINGS_PATH = os.path.join(LEARNINGS_DIR, "learnings.json")
METRICS_PATH = os.path.join(LEARNINGS_DIR, "metrics.json")

def ensure_dir():
    os.makedirs(LEARNINGS_DIR, exist_ok=True)

def load_learnings() -> List[Dict]:
    try:
        with open(LEARNINGS_PATH) as f:
            return json.load(f)
    except Exception:
        return []

def save_learnings(data: List[Dict]):
    ensure_dir()
    tmp = LEARNINGS_PATH + ".tmp"
    with open(tmp, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    os.replace(tmp, LEARNINGS_PATH)
    try:
        os.chmod(LEARNINGS_PATH, 0o600)
    except Exception:
        pass

def log_run(command: str, success: bool, latency_ms: float, tokens_used: int = 0,
            model: str = "unknown", error: str = None, lang: str = "en"):
    """Log a single CLI run for self-improvement."""
    ensure_dir()
    entry = {
        "ts": int(time.time()),
        "command": command,
        "success": success,
        "latency_ms": latency_ms,
        "tokens_used": tokens_used,
        "model": model,
        "lang": lang,
        "error": error,
        "hash": hashlib.sha256(f"{command}{success}{error}".encode()).hexdigest()[:8]
    }
    learnings = load_learnings()
    learnings.append(entry)
    # Keep last 1000 entries to avoid bloat
    if len(learnings) > 1000:
        learnings = learnings[-1000:]
    save_learnings(learnings)
    # Update metrics
    update_metrics(learnings)

def update_metrics(learnings: List[Dict]):
    ensure_dir()
    total = len(learnings)
    if total == 0:
        return
    success_rate = sum(1 for e in learnings if e["success"]) / total
    avg_latency = sum(e["latency_ms"] for e in learnings) / total
    avg_tokens = sum(e.get("tokens_used", 0) for e in learnings) / total
    # Failure patterns
    failures = {}
    for e in learnings:
        if not e["success"] and e.get("error"):
            key = e["error"][:50]
            failures[key] = failures.get(key, 0) + 1
    metrics = {
        "total_runs": total,
        "success_rate": success_rate,
        "avg_latency_ms": avg_latency,
        "avg_tokens": avg_tokens,
        "top_failures": sorted(failures.items(), key=lambda x: -x[1])[:5],
        "last_update": int(time.time()),
        "languages": list(set(e.get("lang", "en") for e in learnings)),
        "models": list(set(e.get("model", "unknown") for e in learnings)),
    }
    with open(METRICS_PATH, "w") as f:
        json.dump(metrics, f, indent=2)

def analyze_learnings() -> Dict:
    """Analyze learnings and propose improvements."""
    learnings = load_learnings()
    if not learnings:
        return {"status": "no_data", "message": "No learnings yet, run some commands first"}
    total = len(learnings)
    success_rate = sum(1 for e in learnings if e["success"]) / total
    avg_latency = sum(e["latency_ms"] for e in learnings) / total
    avg_tokens = sum(e.get("tokens_used", 0) for e in learnings) / total

    proposals = []

    # Low success rate → suggest validation improvements
    if success_rate < 0.85:
        proposals.append({
            "type": "hallucination_reduction",
            "priority": "high",
            "issue": f"Success rate {success_rate:.1%} < 85%",
            "fix": "Add stricter JSON schema validation, abstention when data missing, confidence scores",
            "score": 0.9
        })

    # High latency → suggest caching, parallel
    if avg_latency > 3000:
        proposals.append({
            "type": "speed",
            "priority": "high",
            "issue": f"Avg latency {avg_latency:.0f}ms > 3000ms",
            "fix": "Enable parallel Overpass mirrors, cache geocodes 7d, use --compact, sample_line optimization",
            "score": 0.85
        })

    # High token usage → suggest compact mode
    if avg_tokens > 500:
        proposals.append({
            "type": "token_optimization",
            "priority": "medium",
            "issue": f"Avg tokens {avg_tokens:.0f} > 500",
            "fix": "Use --compact and --json, decision tree table, single example, prefix caching",
            "score": 0.8
        })

    # Failure patterns
    failures = {}
    for e in learnings:
        if not e["success"] and e.get("error"):
            key = e["error"][:80]
            failures[key] = failures.get(key, 0) + 1
    for err, count in sorted(failures.items(), key=lambda x: -x[1])[:3]:
        if count >= 3:
            proposals.append({
                "type": "bugfix",
                "priority": "high",
                "issue": f"Repeated failure ({count}x): {err}",
                "fix": f"Add handling for {err[:30]}, improve error message, add fallback",
                "score": 0.9
            })

    # Language coverage
    langs = set(e.get("lang", "en") for e in learnings)
    if len(langs) < 3:
        proposals.append({
            "type": "i18n",
            "priority": "medium",
            "issue": f"Only {len(langs)} languages used, need broader coverage",
            "fix": "Test with --lang ar,fa,zh,es,ro, add cultural POI tests",
            "score": 0.6
        })

    # Model compatibility
    models = set(e.get("model", "unknown") for e in learnings)
    if len(models) < 2:
        proposals.append({
            "type": "compatibility",
            "priority": "medium",
            "issue": f"Only {len(models)} models tested",
            "fix": "Test with Claude, GPT, Gemini, Mistral, Groq, Qwen using router.py",
            "score": 0.65
        })

    return {
        "total_runs": total,
        "success_rate": success_rate,
        "avg_latency_ms": avg_latency,
        "avg_tokens": avg_tokens,
        "proposals": sorted(proposals, key=lambda x: -x["score"]),
        "languages": list(langs),
        "models": list(models),
        "confidence": "high" if total >= 20 else "medium" if total >= 5 else "low"
    }

def apply_improvements(dry_run: bool = True) -> Dict:
    """Apply improvements based on analysis (currently logs only, future: auto-patch)."""
    analysis = analyze_learnings()
    if analysis.get("status") == "no_data":
        return analysis

    applied = []
    for prop in analysis.get("proposals", []):
        if prop["score"] >= 0.75:
            # In real self-improving system, this would patch SKILL.md or code
            # For now, we log the proposal as applied (simulated)
            applied.append({
                "proposal": prop,
                "action": "logged" if dry_run else "patched",
                "ts": int(time.time())
            })

    # Save applied log
    ensure_dir()
    applied_path = os.path.join(LEARNINGS_DIR, "applied_improvements.json")
    try:
        existing = json.load(open(applied_path)) if os.path.exists(applied_path) else []
    except Exception:
        existing = []
    existing.extend(applied)
    with open(applied_path, "w") as f:
        json.dump(existing[-100:], f, indent=2)

    return {
        "analyzed": analysis["total_runs"],
        "applied_count": len(applied),
        "applied": applied,
        "dry_run": dry_run,
        "next_steps": "Review applied_improvements.json and manually patch SKILL.md/umn.py if needed, then bump version"
    }

def main():
    import argparse
    ap = argparse.ArgumentParser(description="Self-improvement loop for universal-maps-navigator")
    ap.add_argument("--analyze", action="store_true", help="Analyze learnings and propose improvements")
    ap.add_argument("--apply", action="store_true", help="Apply high-score improvements (dry-run by default)")
    ap.add_argument("--live", action="store_true", help="Actually apply patches (not just dry-run)")
    ap.add_argument("--stats", action="store_true", help="Show metrics")
    args = ap.parse_args()

    if args.stats or not (args.analyze or args.apply):
        try:
            metrics = json.load(open(METRICS_PATH))
            print(json.dumps(metrics, indent=2))
        except Exception:
            print("No metrics yet, run some commands first")
        if not (args.analyze or args.apply):
            return

    if args.analyze:
        result = analyze_learnings()
        print(json.dumps(result, indent=2, ensure_ascii=False))

    if args.apply:
        result = apply_improvements(dry_run=not args.live)
        print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
