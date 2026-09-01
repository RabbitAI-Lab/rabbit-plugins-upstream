#!/usr/bin/env python3
"""request_lifecycle.py — generation fence: a recovered connection can never render a
superseded answer. Last write wins.
Usage: new <prompt> [--force] | check <gen> | supersede | complete <gen> | resume <gen>
       | status | diagnose | reset   [--json]  [$ARENA_AGENT=<name> isolates state per agent]
"""
import hashlib, json, os, sys, time

try:
    import agent_state
    STATE = agent_state.state_path("lifecycle.json")
except ImportError:
    STATE = os.path.expanduser("~/.arena_turn/lifecycle.json")

JSON_OUT = False

def _emit(human, obj):
    """Print human text or a schema-versioned JSON object (v1.5.0 machine contract)."""
    if JSON_OUT:
        obj.setdefault("schema", "request_lifecycle.v1")
        print(json.dumps(obj, ensure_ascii=False)); return
    print(human)

def load():
    if os.path.exists(STATE):
        try: return json.load(open(STATE))
        except Exception: pass
    return {"generation": 0, "inflight": None, "history": []}

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

def _fingerprint(prompt):
    """Stable identity for a prompt, ignoring whitespace/case noise."""
    norm = " ".join((prompt or "").split()).lower()
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()[:16]


# A resend of the SAME prompt inside this window is a retry, not a new question.
RETRY_WINDOW_S = 90


def cmd_new(prompt, force=False):
    """Open a generation for a new send.

    BUG FIXED (the "rejected first time, accepted on the second attempt" report):
    this used to supersede unconditionally. So when a user re-sent the SAME prompt —
    because the UI looked stuck, or they pressed enter twice — the still-running first
    request was killed, its (correct, nearly-finished) answer was fenced out as STALE,
    and only the second attempt was ever rendered. The user's first try was silently
    binned and the model did the work twice.

    Superseding is right for a CHANGED prompt (last write wins) and wrong for a REPEATED
    one (that is a retry). We now tell them apart by fingerprint.
    """
    with _Lock():                      # generation bump must be serialized
        s = load()
        fp = _fingerprint(prompt)
        cur = s.get("inflight")

        if (not force and cur and cur.get("status") == "running"
                and cur.get("fingerprint") == fp
                and (time.time() - cur.get("started", 0)) < RETRY_WINDOW_S):
            age = time.time() - cur["started"]
            cur["retries"] = cur.get("retries", 0) + 1
            save(s)
            _emit(f"DUPLICATE of generation={cur['generation']} "
                  f"(same prompt, {age:.1f}s in flight, retry #{cur['retries']})\n"
                  f"ADOPT generation={cur['generation']} — do NOT restart; keep waiting on the "
                  f"in-flight answer. Re-sending would discard work that is already almost done.",
                  {"event": "adopt", "generation": cur["generation"], "retries": cur["retries"],
                   "inflight_age_s": round(age, 1)})
            return

        if cur and cur.get("status") == "running":
            cur["status"] = "superseded"
            s["history"].append(cur)
            why = "forced restart" if force else "superseded by a DIFFERENT prompt"
            _emit(f"ABORT generation={cur['generation']} ({why})",
                  {"event": "abort", "generation": cur["generation"], "why": why})

        s["generation"] += 1
        s["inflight"] = {"generation": s["generation"], "prompt": (prompt or "")[:400],
                         "fingerprint": fp, "retries": 0,
                         "status": "running", "started": time.time()}
        s["history"] = s["history"][-200:]     # bound growth; the fence only needs `generation`
        save(s)
        _emit(f"CURRENT generation={s['generation']}",
              {"event": "new", "generation": s["generation"]})


def _gen(v):
    """Parse a generation argument; a bad value must not raise a raw traceback."""
    try:
        return int(v)
    except (TypeError, ValueError):
        print(f"ERROR: generation must be an integer, got {v!r}")
        return None


def cmd_check(gen):
    gen = _gen(gen)
    if gen is None: return 2
    s = load()
    if gen == s["generation"]:
        _emit(f"CURRENT generation={gen} -> RENDER", {"stale": False, "generation": gen, "action": "render"}); return 0
    _emit(f"STALE generation={gen} (current={s['generation']}) -> DISCARD, do not render",
          {"stale": True, "generation": gen, "current": s["generation"], "action": "discard"}); return 1

def cmd_supersede():
    with _Lock():
        s = load()
        if s["inflight"] and s["inflight"].get("status") == "running":
            s["inflight"]["status"] = "superseded"
            s["history"].append(s["inflight"])
            s["inflight"] = None
        s["generation"] += 1
        save(s)
        print(f"SUPERSEDED -> new current generation={s['generation']}")

def cmd_complete(gen):
    gen = _gen(gen)
    if gen is None: return 2
    s = load()
    if gen != s["generation"]:
        print(f"IGNORED completion of stale generation={gen} (current={s['generation']})"); return 1
    if s["inflight"]:
        s["inflight"]["status"] = "complete"; s["inflight"]["ended"] = time.time()
        s["history"].append(s["inflight"]); s["inflight"] = None
    save(s); print(f"COMPLETE generation={gen}"); return 0

def cmd_resume(gen):
    gen = _gen(gen)
    if gen is None: return 2
    s = load()
    if gen == s["generation"]:
        print(f"RESUME OK generation={gen} — stream is still current"); return 0
    print(f"DO NOT RESUME generation={gen} (current={s['generation']}) — discard and re-issue"); return 1

def cmd_diagnose():
    """Explain a 'rejected first time, accepted on the second attempt' report."""
    s = load()
    hist = s.get("history", [])
    sup = [h for h in hist if h.get("status") == "superseded"]
    dupes = sum(h.get("retries", 0) for h in hist) + (s.get("inflight") or {}).get("retries", 0)

    print("DIAGNOSING: 'prompt rejected on the first attempt, accepted on the second'\n")
    print(f"  generations opened .......... {s.get('generation', 0)}")
    print(f"  superseded (answers binned) . {len(sup)}")
    print(f"  duplicate resends detected .. {dupes}")

    same = [h for h in sup if h.get("fingerprint")
            and any(o.get("fingerprint") == h.get("fingerprint")
                    for o in hist if o is not h)]
    print()
    if same:
        print("  >>> CONFIRMED: identical prompts were superseded.")
        print("      Your first attempt WAS answered; the fence discarded it because a resend")
        print("      bumped the generation. Fixed in v1.3.2 — identical resends now ADOPT the")
        print("      in-flight generation instead of killing it.")
    elif len(sup) > 0:
        print("  Superseding happened, but on DIFFERENT prompts — that is correct behaviour")
        print("  (last write wins). Your first-attempt failure is coming from somewhere else.")
    else:
        print("  No superseding recorded here, so the fence is not your cause.")

    print("\n  Other things that produce the same symptom, in likelihood order:")
    print("   1. Cold start — first call pays model load / connection setup and times out;")
    print("      the second hits a warm path. Check whether attempt 1 is slow, not rejected.")
    print("   2. Auth/session token minted lazily: first call 401s, second succeeds.")
    print("      Test: run the same request twice after a fresh login.")
    print("   3. Input too large on the first send, trimmed on the retry.")
    print("      Test: python3 prompt_compactor.py --text \"<your prompt>\" and resend.")
    print("   4. A leading character the parser rejects (stray quote, smart-dash, RTL mark).")
    return 0


def cmd_status():
    s = load()
    f = s.get("inflight")
    inflight = None
    if f and f.get("status") == "running":
        inflight = {"generation": f["generation"], "age_s": round(time.time()-f["started"], 1),
                    "prompt": f["prompt"][:70]}
    stale = sum(1 for h in s["history"] if h.get("status") == "superseded")
    _emit(f"current_generation = {s['generation']}\n"
          + (f"in-flight: gen={f['generation']} age={time.time()-f['started']:.1f}s prompt={f['prompt'][:70]!r}\n"
             if inflight else "in-flight: none\n")
          + f"history: {len(s['history'])} finished, {stale} superseded (stale answers blocked)",
          {"generation": s["generation"], "inflight": inflight,
           "history_finished": len(s["history"]), "history_superseded": stale})

def main():
    global JSON_OUT
    argv = list(sys.argv)
    if "--json" in argv:
        JSON_OUT = True
        argv = [x for x in argv if x != "--json"]
    sys.argv = argv
    if len(sys.argv) < 2: print(__doc__); return 2
    c = sys.argv[1]
    if c == "new":
        args = sys.argv[2:]
        force = "--force" in args
        args = [x for x in args if x != "--force"]
        cmd_new(args[0] if args else "", force=force)
    elif c == "check": return cmd_check(sys.argv[2] if len(sys.argv) > 2 else None)
    elif c == "supersede": cmd_supersede()
    elif c == "complete": return cmd_complete(sys.argv[2] if len(sys.argv) > 2 else None)
    elif c == "resume": return cmd_resume(sys.argv[2] if len(sys.argv) > 2 else None)
    elif c == "status": cmd_status()
    elif c == "diagnose": return cmd_diagnose()
    elif c == "reset": save({"generation": 0, "inflight": None, "history": []}); print("reset")
    else: print(__doc__); return 2
    return 0

if __name__ == "__main__": sys.exit(main())
