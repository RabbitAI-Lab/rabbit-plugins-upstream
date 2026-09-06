#!/usr/bin/env python3
"""prompt_cache.py — disk-backed SHA256 response cache (stdlib only).

usage: prompt_cache.py get <model> <n> <prompt> [sig]      # hit: print cached text, rc 0
                                                            # miss: rc 1
       prompt_cache.py put <model> <n> <prompt> <text> [sig]
       prompt_cache.py stats                                # human readable
`sig` ties an entry to the model artifact (e.g. "size-mtime"); a replaced or
re-downloaded model changes sig -> stale entries simply miss. Never raises.
Cache dir: $SELFHEAL_HOME/cache (default ~/.selfheal/cache, mode 0700).
CONSENT: `put` writes only when SELFHEAL_MODE=fix; otherwise it is a no-op
(check mode persists nothing, no matter who calls this tool directly).
"""
import hashlib, json, os, sys, time

HOME = os.environ.get("SELFHEAL_HOME", os.path.expanduser("~/.selfheal"))
CDIR = os.path.join(HOME, "cache")
MAX_ENTRIES, TTL = 256, 7 * 24 * 3600


def key(model, n, prompt, sig=""):
    h = hashlib.sha256()
    for part in (model, str(n), prompt, sig):
        h.update(part.encode("utf-8", "surrogatepass")); h.update(b"\0")
    return h.hexdigest()


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "stats"
    if cmd == "get":
        model, n, prompt = sys.argv[2], sys.argv[3], sys.argv[4]
        sig = sys.argv[5] if len(sys.argv) > 5 else ""
        p = os.path.join(CDIR, key(model, n, prompt, sig) + ".json")
        try:
            d = json.load(open(p))
            if time.time() - d["ts"] > TTL:
                raise ValueError("expired")
            sys.stdout.write(d["text"])
            return 0
        except Exception:
            return 1
    if cmd == "put":
        if os.environ.get("SELFHEAL_MODE", "check") != "fix":
            print("prompt_cache: put suppressed (SELFHEAL_MODE!=fix)", file=sys.stderr)
            return 0
        model, n, prompt, text = sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
        sig = sys.argv[6] if len(sys.argv) > 6 else ""
        os.makedirs(CDIR, mode=0o700, exist_ok=True)  # writes create dirs only after consent
        entries = []
        for f in os.listdir(CDIR):
            if f.endswith(".json"):
                fp = os.path.join(CDIR, f)
                try:
                    entries.append((os.path.getmtime(fp), fp))
                except OSError:
                    pass
        if len(entries) >= MAX_ENTRIES:  # evict oldest ~10%
            entries.sort()
            for _, fp in entries[: max(1, len(entries) // 10)]:
                try:
                    os.remove(fp)
                except OSError:
                    pass
        json.dump({"ts": time.time(), "text": text},
                  open(os.path.join(CDIR, key(model, n, prompt, sig) + ".json"), "w"))
        return 0
    if cmd == "stats":
        try:
            files = [f for f in os.listdir(CDIR) if f.endswith(".json")]
        except OSError:
            files = []
        print(f"entries={len(files)} dir={CDIR} ttl_s={TTL} max={MAX_ENTRIES}")
        return 0
    print(__doc__)
    return 64


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(1)  # cache failure must never crash inference
