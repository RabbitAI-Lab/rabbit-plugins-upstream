#!/usr/bin/env python3
"""
context_hygiene.py — detect and reverse late-conversation "zombie mode" before collapse.
Causes: quadratic attention cost (slower) + context dilution (goal buried under scrollback).

v1.5.0 — any model:
  * --ctx-tokens N scales the char/turn thresholds to the model's real context
    window (a 8k-token model must not wait for 60k chars of scrollback before
    WATCH fires; a 1M-token model must not panic at 70 turns). Floors keep
    tiny windows from triggering on turn 1.
  * record --model M tags each sample; the latency trend is computed only
    within the CURRENT model run, because a router switching models mid-chat
    changes baseline latency and would otherwise poison the trend (apples:
    local 0.5B, oranges: cloud flagship).
  * assess --json emits a schema-versioned object for any agent to consume.

Usage: record --turn N --chars N [--latency F] [--model M] [--ctx-tokens N]
       | assess [--ctx-tokens N] [--json] | brief | set-goal ... | reset
"""
import argparse, json, os, sys, time

try:
    import agent_state
    STATE = agent_state.state_path("context.json")
except ImportError:
    STATE = os.path.expanduser("~/.arena_turn/context.json")

# Baseline thresholds, calibrated for a ~128k-token context window
# (chars ≈ 4×tokens; 60k chars ≈ 15k tokens of scrollback etc.).
WATCH_TURNS, COMPACT_TURNS, RESET_TURNS = 25, 45, 70
WATCH_CHARS, COMPACT_CHARS, RESET_CHARS = 60_000, 140_000, 250_000
BASE_CTX_TOKENS = 128_000
SCHEMA = "context_hygiene.v1"

# A window below ~8k or above ~2M is a caller error, not a model size.
MIN_CTX_TOKENS, MAX_CTX_TOKENS = 4_096, 2_000_000


def thresholds(ctx_tokens=None, state=None):
    """Scale thresholds to the model's context window, with floors.

    ratio = ctx / 128k, clamped to [1/8, 8] so absurd inputs cannot zero out
    or blow up the thresholds. Char thresholds scale linearly (context is
    measured in chars) but keep a floor (5k/12k/20k): a tiny window still
    deserves a small grace period, not 'RESET' on the first message. Turn
    thresholds scale with sqrt(ratio) — conversation length tolerance grows
    with context but sublinearly (human patience does not 8x on a big model)
    — floored at 5/8/12 so an 8k model is not flagged 'WATCH' on turn 2.
    """
    state = state or {}
    ctx = ctx_tokens or state.get("ctx_tokens") or BASE_CTX_TOKENS
    try:
        ctx = int(ctx)
    except (TypeError, ValueError):
        ctx = BASE_CTX_TOKENS
    ctx = max(MIN_CTX_TOKENS, min(MAX_CTX_TOKENS, ctx))
    ratio = ctx / BASE_CTX_TOKENS
    ratio = max(1 / 8, min(8, ratio))
    r = ratio ** 0.5
    return {
        "ctx_tokens": ctx, "ratio": round(ratio, 3),
        "watch_turns": max(5, round(WATCH_TURNS * r)),
        "compact_turns": max(8, round(COMPACT_TURNS * r)),
        "reset_turns": max(12, round(RESET_TURNS * r)),
        "watch_chars": max(5_000, round(WATCH_CHARS * ratio)),
        "compact_chars": max(12_000, round(COMPACT_CHARS * ratio)),
        "reset_chars": max(20_000, round(RESET_CHARS * ratio)),
    }


def load():
    if os.path.exists(STATE):
        try: return json.load(open(STATE))
        except Exception: pass
    return {"samples": [], "goal": "", "constraints": [], "decisions": [], "open_items": [], "artifacts": []}

def save(s):
    """Atomically persist state.

    BUG FIXED: every process previously wrote to the SAME `STATE + ".tmp"` path, so two
    concurrent writers interleaved bytes into one temp file and os.replace() published the
    mangled result — 10 parallel writers reliably produced invalid JSON. The temp file must
    be unique per process, flushed, and fsynced before the rename.
    """
    d = os.path.dirname(STATE)
    os.makedirs(d, exist_ok=True)
    tmp = f"{STATE}.{os.getpid()}.tmp"
    try:
        with open(tmp, "w") as fh:
            json.dump(s, fh, indent=2)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, STATE)
    finally:
        if os.path.exists(tmp):
            try:
                os.unlink(tmp)
            except OSError:
                pass


class _Lock:
    """Advisory lock so read-modify-write cycles don't lose updates.

    Falls back to a no-op if fcntl is unavailable (Windows); the atomic save above still
    guarantees the file is never corrupt, only that a concurrent update may be overwritten.
    """

    def __init__(self):
        self.path = STATE + ".lock"
        self.fh = None

    def __enter__(self):
        try:
            import fcntl
            os.makedirs(os.path.dirname(STATE), exist_ok=True)
            self.fh = open(self.path, "w")
            fcntl.flock(self.fh.fileno(), fcntl.LOCK_EX)
        except Exception:
            self.fh = None
        return self

    def __exit__(self, *exc):
        if self.fh:
            try:
                import fcntl
                fcntl.flock(self.fh.fileno(), fcntl.LOCK_UN)
            finally:
                self.fh.close()
        return False

def _current_model_run(s):
    """Samples belonging to the most recent model (model-switch aware trend).

    If a router switched models mid-session, latency baselines from the old
    model are noise for the new one. The zombie *size* components stay global
    (scrollback is scrollback whichever model reads it); only the latency
    trend is scoped to the current model's samples.
    """
    last_model = (s["samples"][-1].get("model") if s["samples"] else None) or "default"
    run = []
    for x in reversed(s["samples"]):
        if (x.get("model") or "default") != last_model:
            break
        run.append(x)
    return list(reversed(run)), last_model

def zombie_score(s, th=None):
    th = th or thresholds(state=s)
    if not s["samples"]: return 0, {}
    last = s["samples"][-1]; turns, chars = last.get("turn",0), last.get("chars",0)
    turn_c = min(100, turns/th["reset_turns"]*100); size_c = min(100, chars/th["reset_chars"]*100)
    lat_c = 0.0
    run, _ = _current_model_run(s)
    lats = [x["latency"] for x in run if x.get("latency")]
    if len(lats) >= 4:
        h = len(lats)//2; early = sum(lats[:h])/h; late = sum(lats[h:])/(len(lats)-h)
        if early > 0: lat_c = min(100, max(0.0, (late/early - 1.0)*100))
    return round(0.35*turn_c + 0.35*size_c + 0.30*lat_c), {
        "turn_component": round(turn_c), "size_component": round(size_c), "latency_component": round(lat_c)}

def verdict(score, s, th=None):
    th = th or thresholds(state=s)
    last = s["samples"][-1] if s["samples"] else {}
    turns, chars = last.get("turn",0), last.get("chars",0)
    if turns >= th["reset_turns"] or chars >= th["reset_chars"] or score >= 80:
        return "RESET", "Start a fresh context now and carry forward the brief."
    if turns >= th["compact_turns"] or chars >= th["compact_chars"] or score >= 55:
        return "COMPACT NOW", "Summarize and drop scrollback; re-anchor the goal at the top."
    if turns >= th["watch_turns"] or chars >= th["watch_chars"] or score >= 30:
        return "WATCH", "Schedule a compaction soon; keep replies tight."
    return "HEALTHY", "No action needed."

def cmd_record(a):
    with _Lock():
        s = load()
        s["samples"].append({"turn":a.turn,"chars":a.chars,"latency":a.latency,
                             "model":a.model or "","ts":time.time()})
        s["samples"] = s["samples"][-400:]
        if a.ctx_tokens:
            s["ctx_tokens"] = a.ctx_tokens
        save(s)
    th = thresholds(a.ctx_tokens, s)
    sc,_ = zombie_score(s, th); v,_ = verdict(sc,s,th)
    print(f"recorded turn={a.turn} chars={a.chars} latency={a.latency}s "
          f"model={a.model or 'default'} ctx={th['ctx_tokens']} -> zombie={sc} {v}")

def cmd_assess(a):
    s = load()
    th = thresholds(a.ctx_tokens, s)
    if not s["samples"]:
        if a.json:
            print(json.dumps({"schema": SCHEMA, "samples": 0, "thresholds": th,
                              "zombie_score": 0, "verdict": "HEALTHY",
                              "action": "no samples yet — run `record` each turn"}))
        else:
            print("no samples yet — run `record` each turn")
        return
    sc,parts = zombie_score(s, th); v,action = verdict(sc,s,th); last = s["samples"][-1]
    run, cur_model = _current_model_run(s)
    if a.json:
        print(json.dumps({
            "schema": SCHEMA, "zombie_score": sc, "components": parts, "verdict": v,
            "action": action, "thresholds": th, "model": cur_model,
            "turn": last.get("turn"), "chars": last.get("chars"),
            "latency_last_s": last.get("latency"),
            "samples_total": len(s["samples"]), "samples_current_model": len(run),
        }, indent=2))
        return
    bar = "#"*(sc//5) + "."*(20-sc//5)
    print(f"ZOMBIE SCORE {sc}/100  [{bar}]")
    print(f"  turns={last.get('turn')}  chars={last.get('chars')}  last_latency={last.get('latency')}s")
    print(f"  model={cur_model}  ctx_tokens={th['ctx_tokens']} (ratio {th['ratio']})")
    print(f"  thresholds: watch {th['watch_turns']}t/{th['watch_chars']:,}c  "
          f"compact {th['compact_turns']}t/{th['compact_chars']:,}c  reset {th['reset_turns']}t/{th['reset_chars']:,}c")
    print(f"  components: {parts}")
    print(f"VERDICT: {v}\nACTION:  {action}")
    if v in ("COMPACT NOW","RESET"):
        print("\nRun: python3 context_hygiene.py brief > CARRY_FORWARD.md")
        print("Then open a fresh chat and paste the brief as the FIRST message.")

def cmd_brief(_a):
    s = load(); out = ["# Carry-Forward Brief","","## Goal", s["goal"] or "_(set with set-goal)_",""]
    if s["constraints"]: out += ["## Hard constraints"]+[f"- {c}" for c in s["constraints"]]+[""]
    if s["decisions"]: out += ["## Decisions already made (do not relitigate)"]+[f"- {d}" for d in s["decisions"]]+[""]
    if s["open_items"]: out += ["## Open items"]+[f"- [ ] {o}" for o in s["open_items"]]+[""]
    if s["artifacts"]: out += ["## Artifacts"]+[f"- `{p}`" for p in s["artifacts"]]+[""]
    out += ["## Instruction to the fresh agent",
            "Resume from the state above. Do not re-derive prior decisions. Answer first, elaborate after."]
    print("\n".join(out))

def cmd_set(a):
    with _Lock():
        s = load()
        if a.goal: s["goal"] = a.goal
        for k,dest in (("constraint","constraints"),("decision","decisions"),("open","open_items"),("artifact","artifacts")):
            for v in (getattr(a,k) or []):
                if v not in s[dest]: s[dest].append(v)
        save(s)
    print(f"goal={s['goal']!r} constraints={len(s['constraints'])} decisions={len(s['decisions'])} "
          f"open={len(s['open_items'])} artifacts={len(s['artifacts'])}")

def main():
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("record"); r.add_argument("--turn",type=int,required=True)
    r.add_argument("--chars",type=int,required=True); r.add_argument("--latency",type=float,default=0.0)
    r.add_argument("--model",default="",help="model id serving this turn (trend is per-model)")
    r.add_argument("--ctx-tokens",type=int,default=None,help="model context window; persists in state")
    r.set_defaults(f=cmd_record)
    a2 = sub.add_parser("assess"); a2.add_argument("--ctx-tokens",type=int,default=None)
    a2.add_argument("--json",action="store_true"); a2.set_defaults(f=cmd_assess)
    sub.add_parser("brief").set_defaults(f=cmd_brief)
    g = sub.add_parser("set-goal"); g.add_argument("goal",nargs="?",default="")
    for o in ("constraint","decision","open","artifact"): g.add_argument(f"--{o}",action="append")
    g.set_defaults(f=cmd_set)
    sub.add_parser("reset").set_defaults(f=lambda a:(save({"samples":[],"goal":"","constraints":[],
        "decisions":[],"open_items":[],"artifacts":[]}),print("reset")))
    a = ap.parse_args(); a.f(a)

if __name__ == "__main__": sys.exit(main() or 0)
