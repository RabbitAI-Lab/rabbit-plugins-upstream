#!/usr/bin/env python3
"""context_hygiene.py — detect and reverse late-conversation "zombie mode" before collapse.
Causes: quadratic attention cost (slower) + context dilution (goal buried under scrollback).
Usage: record --turn N --chars N --latency F | assess | brief | set-goal ... | reset
"""
import argparse, json, os, sys, time
STATE = os.path.expanduser("~/.arena_turn/context.json")
WATCH_TURNS, COMPACT_TURNS, RESET_TURNS = 25, 45, 70
WATCH_CHARS, COMPACT_CHARS, RESET_CHARS = 60_000, 140_000, 250_000

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

def zombie_score(s):
    if not s["samples"]: return 0, {}
    last = s["samples"][-1]; turns, chars = last.get("turn",0), last.get("chars",0)
    turn_c = min(100, turns/RESET_TURNS*100); size_c = min(100, chars/RESET_CHARS*100)
    lat_c = 0.0
    lats = [x["latency"] for x in s["samples"] if x.get("latency")]
    if len(lats) >= 4:
        h = len(lats)//2; early = sum(lats[:h])/h; late = sum(lats[h:])/(len(lats)-h)
        if early > 0: lat_c = min(100, max(0.0, (late/early - 1.0)*100))
    return round(0.35*turn_c + 0.35*size_c + 0.30*lat_c), {
        "turn_component": round(turn_c), "size_component": round(size_c), "latency_component": round(lat_c)}

def verdict(score, s):
    last = s["samples"][-1] if s["samples"] else {}
    turns, chars = last.get("turn",0), last.get("chars",0)
    if turns >= RESET_TURNS or chars >= RESET_CHARS or score >= 80:
        return "RESET", "Start a fresh context now and carry forward the brief."
    if turns >= COMPACT_TURNS or chars >= COMPACT_CHARS or score >= 55:
        return "COMPACT NOW", "Summarize and drop scrollback; re-anchor the goal at the top."
    if turns >= WATCH_TURNS or chars >= WATCH_CHARS or score >= 30:
        return "WATCH", "Schedule a compaction soon; keep replies tight."
    return "HEALTHY", "No action needed."

def cmd_record(a):
    s = load(); s["samples"].append({"turn":a.turn,"chars":a.chars,"latency":a.latency,"ts":time.time()})
    s["samples"] = s["samples"][-400:]; save(s)
    sc,_ = zombie_score(s); v,_ = verdict(sc,s)
    print(f"recorded turn={a.turn} chars={a.chars} latency={a.latency}s -> zombie={sc} {v}")

def cmd_assess(_a):
    s = load()
    if not s["samples"]: print("no samples yet — run `record` each turn"); return
    sc,parts = zombie_score(s); v,action = verdict(sc,s); last = s["samples"][-1]
    bar = "#"*(sc//5) + "."*(20-sc//5)
    print(f"ZOMBIE SCORE {sc}/100  [{bar}]")
    print(f"  turns={last.get('turn')}  chars={last.get('chars')}  last_latency={last.get('latency')}s")
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
    r.set_defaults(f=cmd_record)
    sub.add_parser("assess").set_defaults(f=cmd_assess)
    sub.add_parser("brief").set_defaults(f=cmd_brief)
    g = sub.add_parser("set-goal"); g.add_argument("goal",nargs="?",default="")
    for o in ("constraint","decision","open","artifact"): g.add_argument(f"--{o}",action="append")
    g.set_defaults(f=cmd_set)
    sub.add_parser("reset").set_defaults(f=lambda a:(save({"samples":[],"goal":"","constraints":[],
        "decisions":[],"open_items":[],"artifacts":[]}),print("reset")))
    a = ap.parse_args(); a.f(a)

if __name__ == "__main__": sys.exit(main() or 0)
