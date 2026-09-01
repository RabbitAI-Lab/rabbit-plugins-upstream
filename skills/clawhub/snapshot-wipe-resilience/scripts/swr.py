#!/usr/bin/env python3
"""
swr — Snapshot-Wipe Resilience (v1.4.1)

Detect and auto-repair partially-wiped agent workspaces in sandboxes that only
persist part of the filesystem between turns.

Design rule: NEVER trust os.path.exists(). A snapshot restore can leave a
directory present but empty, a file present but truncated, or a script present
but non-executable. Verify integrity, not presence.

Security: restore recipes are shell commands, i.e. code. They only execute when
the manifest carries a valid HMAC signature from this machine OR a valid
ML-DSA-87 signature from a signer in ~/.swr/trusted_signers.json.

Exit codes: 0 healthy · 1 damaged · 2 unrepairable · 3 recheck-failed · 4 bad manifest
"""

import argparse
import base64
import concurrent.futures as futures
import fcntl
import hashlib
import hmac
import json
import os
import shutil
import signal
import stat
import subprocess
import sys
import time

HOME = os.path.expanduser("~")
SWR_DIR = os.path.join(HOME, ".swr")
DEFAULT_MANIFEST = os.path.join(SWR_DIR, "manifest.json")
CACHE_FILE = os.path.join(SWR_DIR, "cache.json")
HISTORY_FILE = os.path.join(SWR_DIR, "history.jsonl")
PROGRESS_DIR = os.path.join(SWR_DIR, "progress")
KEY_FILE = os.path.join(SWR_DIR, "signing.key")
LOCK_FILE = os.path.join(SWR_DIR, "lock")
QUARANTINE = os.path.join(SWR_DIR, "quarantine")
ID_DIR = os.path.join(SWR_DIR, "identity")
TRUST_FILE = os.path.join(SWR_DIR, "trusted_signers.json")
CANARY_DIR = ".swr-canaries"

SCHEMA_VERSION = 2
CACHE_TTL = 3600          # re-hash hourly: (mtime,size,inode) can be forged
PROGRESS_TTL = 6 * 3600
HISTORY_MAX_LINES = 5000
HISTORY_TRIM_TO = 4000
ESCROW_MAX = 256 * 1024
ESCROW_DECOMP_MAX = 64 * 1024 * 1024

EXCLUDED_DIRNAMES = {
    ".arena", ".cache", ".mypy_cache", ".next", ".nox", ".npm", ".nuxt",
    ".output", ".parcel-cache", ".pytest_cache", ".ruff_cache", ".svelte-kit",
    ".tox", ".turbo", ".venv", ".vite", "__pycache__", "build", "coverage",
    "dist", "node_modules", "out", "target",
}

OK, MISSING, CORRUPT, STRIPPED, EMPTY = "OK", "MISSING", "CORRUPT", "STRIPPED", "EMPTY"
BROKEN_LINK, SMOKE_FAIL, SKIPPED = "BROKENLNK", "SMOKEFAIL", "SKIPPED"
BAD = {MISSING, CORRUPT, STRIPPED, EMPTY, BROKEN_LINK, SMOKE_FAIL}

EXIT_OK, EXIT_DAMAGED, EXIT_UNREPAIRABLE, EXIT_RECHECK, EXIT_BADMANIFEST = 0, 1, 2, 3, 4

SYM = {OK: "+", MISSING: "x", CORRUPT: "!", STRIPPED: "~", EMPTY: "0",
       BROKEN_LINK: "/", SMOKE_FAIL: "?", SKIPPED: "-"}
C = {OK: "\033[32m", MISSING: "\033[31m", CORRUPT: "\033[31m", EMPTY: "\033[31m",
     STRIPPED: "\033[33m", BROKEN_LINK: "\033[35m", SMOKE_FAIL: "\033[33m",
     SKIPPED: "\033[2m", "r": "\033[0m", "d": "\033[2m", "b": "\033[1m"}
if not sys.stdout.isatty() or os.environ.get("NO_COLOR"):
    C = {k: "" for k in C}


def eprint(*a):
    print(*a, file=sys.stderr)


# ─────────────────────────────────────────────────────── canonical / signing

def canonical(obj):
    """Stable JSON encoding, safe to sign across Python versions."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False).encode()


def manifest_digest(man):
    body = {k: v for k, v in man.items()
            if k not in ("_sig", "_pksig", "_presig_body", "_migrated_from")}
    return hashlib.sha256(canonical(body)).hexdigest()


def get_key(create=True):
    if os.path.exists(KEY_FILE):
        return open(KEY_FILE, "rb").read().strip()
    if not create:
        return None
    os.makedirs(SWR_DIR, exist_ok=True)
    k = os.urandom(32).hex().encode()
    old = os.umask(0o077)
    try:
        with open(KEY_FILE, "wb") as f:
            f.write(k + b"\n")
    finally:
        os.umask(old)
    os.chmod(KEY_FILE, 0o600)
    return k


def _ossl(args, inp=None):
    return subprocess.run(["openssl", *args], input=inp,
                          capture_output=True, timeout=120)


def _mldsa_available():
    return shutil.which("openssl") and os.path.exists(
        os.path.join(ID_DIR, "mldsa.key"))


def _pubkey_pem():
    r = _ossl(["pkey", "-in", os.path.join(ID_DIR, "mldsa.key"),
               "-pubout", "-outform", "PEM"])
    return r.stdout if r.returncode == 0 else None


def _fingerprint(pub):
    h = hashlib.sha512(pub).digest()[:16]
    b = base64.b32encode(h).decode().rstrip("=").lower()
    return "-".join(b[i:i + 5] for i in range(0, 20, 5))


def _securedir():
    for d in ("/dev/shm", "/run/user/%d" % os.getuid()):
        if os.path.isdir(d) and os.access(d, os.W_OK):
            return d
    return None


def sign(man, asymmetric=None):
    """HMAC always; ML-DSA-87 public-key signature too when an identity exists."""
    key = get_key()
    man.pop("_sig", None)
    man.pop("_pksig", None)
    sig = hmac.new(key, canonical(man), hashlib.sha256).hexdigest()
    man["_sig"] = {"alg": "HMAC-SHA256", "value": sig, "at": int(time.time())}

    want = _mldsa_available() if asymmetric is None else asymmetric
    if want and _mldsa_available():
        import tempfile
        body = canonical({k: v for k, v in man.items()
                          if k not in ("_sig", "_pksig")})
        fd, mf = tempfile.mkstemp(dir=_securedir())
        with os.fdopen(fd, "wb") as f:
            f.write(body)
        try:
            r = _ossl(["pkeyutl", "-sign", "-rawin",
                       "-inkey", os.path.join(ID_DIR, "mldsa.key"), "-in", mf])
            pub = _pubkey_pem()
            if r.returncode == 0 and pub:
                man["_pksig"] = {
                    "alg": "ML-DSA-87",
                    "value": base64.b64encode(r.stdout).decode(),
                    "pub": base64.b64encode(pub).decode(),
                    "fp": _fingerprint(pub), "at": int(time.time())}
        finally:
            try:
                os.remove(mf)
            except OSError:
                pass
    return man


def verify_sig(man):
    """-> (state, detail). state in {valid, invalid, unsigned, nokey}"""
    s = man.get("_sig")
    if not s:
        return "unsigned", "manifest carries no signature"
    key = get_key(create=False)
    if not key:
        return "nokey", "no local signing key to verify against"
    got = s.get("value", "")
    # Several canonical forms: manifests signed by earlier versions may or may
    # not include bookkeeping keys.
    forms = [
        {k: v for k, v in man.items()
         if k not in ("_sig", "_pksig", "_presig_body", "_migrated_from")},
        {k: v for k, v in man.items() if k not in ("_sig", "_pksig", "_presig_body")},
        {k: v for k, v in man.items() if k not in ("_sig", "_pksig")},
        {k: v for k, v in man.items() if k != "_sig"},
    ]
    for body in forms:
        if hmac.compare_digest(
                hmac.new(key, canonical(body), hashlib.sha256).hexdigest(), got):
            return "valid", f"signed {int(time.time()) - s.get('at', 0)}s ago"
    mv = man.get("_migrated_from")
    if isinstance(mv, int) and mv < SCHEMA_VERSION:
        if hmac.compare_digest(
                hmac.new(key, canonical(_unmigrate(man, mv)),
                         hashlib.sha256).hexdigest(), got):
            return "valid", (f"signed as schema v{mv} (migrated to "
                             f"v{SCHEMA_VERSION}; run `swr sign` to re-sign)")
    return "invalid", "SIGNATURE MISMATCH — manifest was altered"


def load_trust():
    try:
        return json.load(open(TRUST_FILE))
    except Exception:
        return {}


def verify_pksig(man):
    """Verify ML-DSA-87 signature. -> (state, detail, fingerprint)"""
    ps = man.get("_pksig")
    if not ps:
        return "absent", "no public-key signature", None
    try:
        pub = base64.b64decode(ps["pub"])
        sigv = base64.b64decode(ps["value"])
    except Exception:
        return "invalid", "malformed _pksig", None
    # Fingerprint is recomputed from the KEY, never trusted from the declaration.
    fp = _fingerprint(pub)
    if ps.get("fp") and ps["fp"] != fp:
        return "invalid", "declared fingerprint does not match key", fp
    if not shutil.which("openssl"):
        return "invalid", "openssl unavailable", fp
    import tempfile
    body = canonical({k: v for k, v in man.items() if k not in ("_sig", "_pksig")})
    paths = []
    try:
        for data in (body, pub, sigv):
            fd, pth = tempfile.mkstemp(dir=_securedir())
            with os.fdopen(fd, "wb") as f:
                f.write(data)
            paths.append(pth)
        mf, pf, sf = paths
        r = _ossl(["pkeyutl", "-verify", "-rawin", "-inkey", pf, "-pubin",
                   "-in", mf, "-sigfile", sf])
        if r.returncode != 0:
            return "invalid", "ML-DSA signature does not verify", fp
    finally:
        for pth in paths:
            try:
                os.remove(pth)
            except OSError:
                pass
    trust = load_trust()
    if fp in trust:
        return "valid", f"signed by trusted '{trust[fp]}' ({fp})", fp
    return "untrusted", f"valid signature from UNKNOWN signer {fp}", fp


# ────────────────────────────────────────────────────────────── persistence

def _reject_reserved(man, mpath):
    if "_presig_body" in man:
        eprint(f"REFUSING {mpath}: contains reserved field '_presig_body'. "
               f"This field was used in a signature-forgery attack and is no "
               f"longer accepted. Remove it and re-sign.")
        sys.exit(EXIT_BADMANIFEST)


def migrate(man):
    v = man.get("version", 1)
    if v < SCHEMA_VERSION:
        for e in man.get("entries", []):
            e.setdefault("needs", [])
        man["version"] = SCHEMA_VERSION
        man["_migrated_from"] = v
    return man


def _unmigrate(man, from_version):
    """Reconstruct the pre-migration body from CURRENT data (never from a
    self-declared field: that was a signature-forgery vector)."""
    body = json.loads(json.dumps(
        {k: v for k, v in man.items()
         if k not in ("_sig", "_pksig", "_migrated_from", "_presig_body")}))
    if from_version < 2:
        body["version"] = from_version
        for e in body.get("entries", []):
            if e.get("needs") == []:
                e.pop("needs", None)
    return body


def load(mpath, require=True):
    if not os.path.exists(mpath):
        if require:
            eprint(f"no manifest at {mpath} — run: swr init")
            sys.exit(EXIT_BADMANIFEST)
        return None
    try:
        man = json.load(open(mpath))
    except json.JSONDecodeError as e:
        eprint(f"manifest is not valid JSON: {e}")
        sys.exit(EXIT_BADMANIFEST)
    _reject_reserved(man, mpath)
    return migrate(man)


def save(mpath, man, do_sign=True):
    man.pop("_presig_body", None)
    man.pop("_migrated_from", None)
    if do_sign:
        sign(man)
    os.makedirs(os.path.dirname(mpath) or ".", exist_ok=True)
    tmp = mpath + ".tmp"
    with open(tmp, "w") as f:
        json.dump(man, f, indent=2)
        f.write("\n")
    os.replace(tmp, mpath)


def abspath(man, p):
    return p if os.path.isabs(p) else os.path.join(man.get("workspace", HOME), p)


def escapes_workspace(man, path):
    ws = os.path.realpath(man.get("workspace", HOME))
    tgt = os.path.realpath(abspath(man, path))
    return not (tgt == ws or tgt.startswith(ws + os.sep))


def contained(man, e, action="operate on"):
    if escapes_workspace(man, e["path"]):
        eprint(f"REFUSING to {action} '{e['id']}': path {e['path']!r} resolves "
               f"outside the workspace root {man.get('workspace', HOME)!r}")
        return False
    return True


class Lock:
    """flock so two concurrent doctor runs never race the same restore."""
    def __init__(self, enabled=True):
        self.enabled, self.fh = enabled, None

    def __enter__(self):
        if not self.enabled:
            return self
        os.makedirs(SWR_DIR, exist_ok=True)
        self.fh = open(LOCK_FILE, "w")
        try:
            fcntl.flock(self.fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            eprint("another swr run holds the lock; waiting up to 300s...")
            signal.signal(signal.SIGALRM,
                          lambda *_: (_ for _ in ()).throw(TimeoutError()))
            signal.alarm(300)
            try:
                fcntl.flock(self.fh, fcntl.LOCK_EX)
            finally:
                signal.alarm(0)
        self.fh.write(str(os.getpid()))
        self.fh.flush()
        return self

    def __exit__(self, *a):
        if self.fh:
            fcntl.flock(self.fh, fcntl.LOCK_UN)
            self.fh.close()


# ───────────────────────────────────────────────────────────────── hashing

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_headtail(path, span=1 << 20):
    """Catch corruption in O(2MB) regardless of file size."""
    sz = os.path.getsize(path)
    h = hashlib.sha256()
    h.update(str(sz).encode())
    with open(path, "rb") as f:
        h.update(f.read(span))
        if sz > span:
            f.seek(max(0, sz - span))
            h.update(f.read(span))
    return h.hexdigest()


def merkle_tree(root, ignore_dirs=()):
    """Root hash over (relpath, size, mode) — detects ANY drift."""
    parts, n = [], 0
    for dp, dns, fns in os.walk(root):
        dns[:] = sorted(d for d in dns if d not in ignore_dirs)
        for fn in sorted(fns):
            fp = os.path.join(dp, fn)
            rel = os.path.relpath(fp, root)
            try:
                st = os.lstat(fp)
            except OSError:
                continue
            parts.append(f"{rel}\0{st.st_size}\0{stat.S_IMODE(st.st_mode):o}")
            n += 1
    return hashlib.sha256("\n".join(parts).encode()).hexdigest(), n


def tree_cache_key(root, ignore_dirs=()):
    """Per-file (size, mtime_ns) fingerprint so Merkle results can be cached.
    A directory-mtime-only key was tried first and masked real edits."""
    h = hashlib.sha256()
    try:
        for dp, dns, fns in os.walk(root):
            dns[:] = sorted(d for d in dns if d not in ignore_dirs)
            for fn in sorted(fns):
                fp = os.path.join(dp, fn)
                try:
                    st = os.lstat(fp)
                except OSError:
                    continue
                h.update(f"{os.path.relpath(fp, root)}\0{st.st_size}\0"
                         f"{st.st_mtime_ns}\n".encode())
    except OSError:
        return None
    return h.hexdigest()


def load_cache():
    try:
        return json.load(open(CACHE_FILE))
    except Exception:
        return {}


def save_cache(c):
    """Best-effort: never let a cache write break a check."""
    try:
        os.makedirs(SWR_DIR, exist_ok=True)
        tmp = CACHE_FILE + ".tmp"
        with open(tmp, "w") as f:
            json.dump(c, f)
        os.replace(tmp, CACHE_FILE)
    except OSError as e:
        eprint(f"note: cache not written ({e.strerror}) — continuing uncached")


def cache_key(path):
    """NOTE: an attacker with write access can preserve (mtime,size,inode)
    while altering content. The cache is a performance optimisation, not a
    security boundary; entries expire and --no-cache forces a re-hash."""
    try:
        st = os.stat(path)
    except OSError:
        return None
    return f"{int(st.st_mtime_ns)}:{st.st_size}:{st.st_ino}"


# ─────────────────────────────────────────────────────────────── fragility

def volatile_reason(path):
    for p in os.path.normpath(path).split(os.sep):
        if p in EXCLUDED_DIRNAMES:
            return f"lives under excluded dir '{p}/'"
    try:
        if os.path.getsize(path) > 64 * 1024 * 1024:
            return (f"large blob ({os.path.getsize(path)/1e6:.0f} MB) — "
                    f"likely exceeds snapshot size cap")
    except OSError:
        pass
    return ""


def fs_boundary(man, path):
    try:
        return os.stat(man.get("workspace", HOME)).st_dev != os.stat(path).st_dev
    except OSError:
        return False


# ──────────────────────────────────────────────────────────── verification

def run_smoke(cmd, cwd, timeout=60):
    try:
        r = subprocess.run(["bash", "-lc", cmd], cwd=cwd, timeout=timeout,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return r.returncode == 0
    except Exception:
        return False


def check_ldd(path):
    try:
        r = subprocess.run(["ldd", path], capture_output=True, text=True, timeout=30)
        return [l.split("=>")[0].strip() for l in r.stdout.splitlines()
                if "not found" in l]
    except Exception:
        return []


def verify(man, e, cache=None, use_cache=True):
    path = abspath(man, e["path"])
    kind = e.get("kind", "file")

    if escapes_workspace(man, e["path"]):
        return CORRUPT, (f"path escapes workspace root ({e['path']!r}) — "
                         f"refusing to manage; remove this entry")
    if os.path.islink(path) and not os.path.exists(path):
        return BROKEN_LINK, f"dangling symlink -> {os.readlink(path)}"

    if kind == "tree":
        if not os.path.isdir(path):
            return MISSING, "directory absent"
        for s in e.get("sentinels", []):
            sp = os.path.join(path, s)
            if not os.path.exists(sp):
                return CORRUPT, f"sentinel missing: {s}"
            if os.path.isfile(sp) and os.path.getsize(sp) == 0:
                return CORRUPT, f"sentinel empty: {s}"
        if e.get("merkle"):
            ign = set(e.get("ignore_dirs", []))
            tk = tree_cache_key(path, ign) if use_cache else None
            tc = (cache or {}).get("tree:" + e["id"]) if use_cache else None
            if (tk and tc and tc.get("key") == tk and tc.get("root") == e["merkle"]
                    and (time.time() - tc.get("t", 0)) < CACHE_TTL):
                return OK, f"{tc.get('n', '?')} files, merkle ok (cached)"
            root, n = merkle_tree(path, ign)
            if n == 0:
                return EMPTY, "directory present but contains 0 files"
            if root != e["merkle"]:
                return CORRUPT, f"merkle drift ({n} files, root {root[:10]}…)"
            if cache is not None and tk:
                cache["tree:" + e["id"]] = {"key": tk, "root": root, "n": n,
                                            "t": time.time()}
            return OK, f"{n} files, merkle ok"
        n = sum(len(fs) for _, _, fs in os.walk(path))
        if n == 0:
            return EMPTY, "directory present but contains 0 files"
        mn = e.get("min_files")
        if mn and n < mn:
            return CORRUPT, f"only {n} files, expected >= {mn}"
        if mn and n and mn <= n * 0.75:
            return OK, (f"{n} files  [!] min_files={mn} tolerates "
                        f"{100*(n-mn)//n}% loss — run `swr retighten`")
        return OK, f"{n} files"

    if not os.path.exists(path):
        return MISSING, "absent"

    ck = cache_key(path) if use_cache else None
    cached = (cache or {}).get(e["id"]) if use_cache else None
    fresh = bool(ck and cached and cached.get("key") == ck and cached.get("ok")
                 and (time.time() - cached.get("t", 0)) < CACHE_TTL)

    if kind == "blob":
        want = e.get("bytes")
        got = os.path.getsize(path)
        if want is not None and got != want:
            return CORRUPT, f"{got:,} bytes (want {want:,}, {got-want:+,})"
        if e.get("headtail") and not fresh:
            ht = sha256_headtail(path)
            if ht != e["headtail"]:
                return CORRUPT, f"head/tail hash mismatch ({ht[:10]}…)"
        if cache is not None and ck:
            cache[e["id"]] = {"key": ck, "ok": True, "t": time.time()}
        return OK, f"{got:,} bytes" + (" (cached)" if fresh else "")

    if not fresh:
        if e.get("sha256"):
            got = sha256_file(path)
            if got != e["sha256"]:
                return CORRUPT, f"sha256 {got[:12]}… != {e['sha256'][:12]}…"
        elif e.get("bytes") is not None:
            if os.path.getsize(path) != e["bytes"]:
                return CORRUPT, f"{os.path.getsize(path):,} bytes (want {e['bytes']:,})"

    if e.get("mode"):
        cur = stat.S_IMODE(os.stat(path).st_mode)
        want = int(e["mode"], 8)
        if (want & 0o111) and not (cur & 0o111):
            return STRIPPED, f"mode {cur:04o}, exec bit lost (want {want:04o})"

    if e.get("ldd") and shutil.which("ldd"):
        miss = check_ldd(path)
        if miss:
            return SMOKE_FAIL, f"missing shared libs: {', '.join(miss[:3])}"

    if e.get("smoke") and not fresh:
        if not run_smoke(e["smoke"], man.get("workspace", HOME),
                         e.get("smoke_timeout", 60)):
            return SMOKE_FAIL, f"smoke test failed: {e['smoke'][:50]}"

    if cache is not None and ck:
        cache[e["id"]] = {"key": ck, "ok": True, "t": time.time()}
    return OK, "verified" + (" (cached)" if fresh else "")


def run_check(man, only=None, jobs=8, use_cache=True):
    cache = load_cache() if use_cache else {}
    if only:
        known = {e["id"] for e in man["entries"]}
        unknown = [o for o in only if o not in known]
        if unknown:
            eprint(f"unknown entry id(s): {', '.join(unknown)}")
            eprint(f"  known: {', '.join(sorted(known)) or '(none)'}")
            sys.exit(EXIT_BADMANIFEST)
    ents = [e for e in man["entries"] if not only or e["id"] in only]
    ents.sort(key=lambda x: (x.get("tier", 5), x["id"]))
    if jobs > 1 and len(ents) > 2:
        with futures.ThreadPoolExecutor(max_workers=jobs) as ex:
            fut = {ex.submit(verify, man, e, cache, use_cache): e for e in ents}
            res = {}
            for f in futures.as_completed(fut):
                e = fut[f]
                try:
                    res[e["id"]] = f.result()
                except Exception as ex_:
                    res[e["id"]] = (CORRUPT, f"verifier error: {ex_}")
            rows = [(e, *res[e["id"]]) for e in ents]
    else:
        rows = [(e, *verify(man, e, cache, use_cache)) for e in ents]
    if use_cache:
        save_cache(cache)
    return rows


# ───────────────────────────────────────────────────────────────── telemetry

def record(man, rows):
    """Best-effort: a read-only or full disk must not break checks."""
    try:
        os.makedirs(SWR_DIR, exist_ok=True)
        rec = {"t": int(time.time()), "s": {e["id"]: st for e, st, _ in rows}}
        with open(HISTORY_FILE, "a") as f:
            f.write(json.dumps(rec, separators=(",", ":")) + "\n")
        _rotate_history()
    except OSError as e:
        eprint(f"note: telemetry not written ({e.strerror})")


def _rotate_history():
    """Unbounded append was ~267 MB/year at one check per minute."""
    try:
        if os.path.getsize(HISTORY_FILE) < 512 * 1024:
            return
        with open(HISTORY_FILE) as f:
            lines = f.readlines()
        if len(lines) <= HISTORY_MAX_LINES:
            return
        tmp = HISTORY_FILE + ".tmp"
        with open(tmp, "w") as f:
            f.writelines(lines[-HISTORY_TRIM_TO:])
        os.replace(tmp, HISTORY_FILE)
    except OSError:
        pass


def history():
    if not os.path.exists(HISTORY_FILE):
        return []
    out = []
    for line in open(HISTORY_FILE):
        line = line.strip()
        if line:
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return out


def survival(hist):
    tot, ok = {}, {}
    for h in hist:
        for k, v in h.get("s", {}).items():
            tot[k] = tot.get(k, 0) + 1
            if v == OK:
                ok[k] = ok.get(k, 0) + 1
    return {k: ok.get(k, 0) / tot[k] for k in tot}


def classify(man, rows):
    """Name the wipe pattern instead of listing symptoms."""
    bad = [(e, s) for e, s, _ in rows if s in BAD]
    if not bad:
        return "healthy", "no damage"
    n, tot = len(bad), len(rows)
    kinds = {e.get("kind", "file") for e, _ in bad}
    states = {s for _, s in bad}
    if n == tot and states == {MISSING} and tot >= 3:
        return "cold-start", "everything is gone — fresh container or full wipe"
    if states == {CORRUPT} and n <= 2:
        return "local-corruption", "content damage, not a wipe (bad download or bit-rot)"
    if states == {STRIPPED}:
        return "permission-reset", "content intact, only exec bits lost"
    if kinds == {"blob"}:
        return "size-cap-eviction", "only large blobs evicted — snapshot size limit"
    excl = [e for e, _ in bad
            if volatile_reason(abspath(man, e["path"])).startswith("lives under")]
    if excl and len(excl) == n:
        return "exclusion-sweep", "only excluded-dir paths lost — snapshot ignore rules"
    if all(e.get("tier", 5) == 0 for e, _ in bad):
        return "credential-loss", "auth/shims gone; dependents will cascade"
    return "mixed", f"{n}/{tot} damaged across several classes"


# ────────────────────────────────────────────────────────────────── escrow

def escrow_blob(path):
    import zlib
    return base64.b64encode(zlib.compress(open(path, "rb").read(), 9)).decode()


def escrow_restore(e):
    """Rebuild a file from inline escrow, bounded against decompression bombs.
    200 MB of zeros compresses to ~204 KB — small enough to fit in a paste."""
    import zlib
    declared = int(e.get("escrow_bytes") or 0)
    if declared > ESCROW_DECOMP_MAX:
        raise ValueError(f"escrow declares {declared:,}B, over the "
                         f"{ESCROW_DECOMP_MAX:,}B limit")
    limit = min(ESCROW_DECOMP_MAX, max(declared * 2, 1 << 20))
    d = zlib.decompressobj()
    out = d.decompress(base64.b64decode(e["escrow"]), limit)
    if d.unconsumed_tail:
        raise ValueError(f"escrow expands beyond {limit:,}B — refusing "
                         f"(possible decompression bomb)")
    if declared and len(out) != declared:
        raise ValueError(f"escrow expanded to {len(out):,}B but declares "
                         f"{declared:,}B")
    return out


# ───────────────────────────────────────────────────────────────── restore

def quarantine(man, e):
    if not contained(man, e, "quarantine"):
        return None
    p = abspath(man, e["path"])
    if not os.path.exists(p):
        return None
    os.makedirs(QUARANTINE, exist_ok=True)
    dst = os.path.join(QUARANTINE, f"{e['id']}.{int(time.time())}")
    try:
        shutil.move(p, dst)
        return dst
    except Exception:
        return None


def restore_entry(man, e, dry=False, timeout=None, quar=False):
    cmd = e.get("restore")
    # Prefer inline escrow when content is absent/corrupt: a recipe like
    # `chmod +x` cannot recreate deleted content.
    if e.get("escrow"):
        p_ = abspath(man, e["path"])
        needs_content = (not os.path.exists(p_)) or (
            e.get("sha256") and os.path.isfile(p_)
            and sha256_file(p_) != e["sha256"])
        if needs_content:
            cmd = f"swr-escrow:{e['id']}"

    if cmd and cmd.startswith("swr-escrow:"):
        if not e.get("escrow"):
            print(f"  {C[MISSING]}!!{C['r']} {e['id']}: escrow recipe but no content")
            return False
        print(f"  -> {e['id']}: {C['d']}restore from inline escrow "
              f"({e.get('escrow_bytes', 0):,}B){C['r']}")
        if dry:
            return True
        if not contained(man, e, "restore"):
            return False
        p = abspath(man, e["path"])
        try:
            data = escrow_restore(e)          # validate BEFORE touching disk
            os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
            tmp = p + ".swr-tmp"
            with open(tmp, "wb") as f:
                f.write(data)
            if e.get("mode"):
                os.chmod(tmp, int(e["mode"], 8))
            os.replace(tmp, p)                # atomic: no truncated leftovers
            print("     ok from escrow")
            return True
        except Exception as ex:
            junk = p + ".swr-tmp"
            if os.path.exists(junk):
                try:
                    os.remove(junk)
                except OSError:
                    pass
            print(f"     escrow restore failed: {ex}")
            return False

    if not cmd:
        print(f"  {C[MISSING]}!!{C['r']} {e['id']}: no restore recipe — manual fix required")
        return False
    if quar:
        q = quarantine(man, e)
        if q:
            print(f"     quarantined old copy -> {q}")
    short = cmd if len(cmd) <= 96 else cmd[:96] + "…"
    print(f"  -> {e['id']}: {C['d']}{short}{C['r']}")
    if dry:
        return True
    t0 = time.time()
    tmo = timeout or e.get("timeout_s", 1800)
    try:
        r = subprocess.run(["bash", "-lc", cmd], cwd=man.get("workspace", HOME),
                           timeout=tmo, start_new_session=True)
        rc = r.returncode
    except subprocess.TimeoutExpired:
        print(f"     {C[CORRUPT]}timeout after {tmo}s{C['r']}")
        return False
    print(f"     {'ok' if rc == 0 else 'exit ' + str(rc)} in {time.time()-t0:.1f}s")
    return rc == 0


def plan(man, rows):
    """Topological order over `needs`, skipping doomed dependents."""
    bad = {e["id"]: e for e, s, _ in rows if s in BAD}
    ordered, seen = [], set()

    def visit(eid, stack):
        if eid in seen or eid in stack:
            return
        stack.add(eid)
        e = bad.get(eid)
        if e:
            for dep in e.get("needs", []):
                if dep in bad:
                    visit(dep, stack)
            if eid not in seen:
                ordered.append(e)
                seen.add(eid)
        stack.discard(eid)

    for e in sorted(bad.values(), key=lambda x: (x.get("tier", 5), x["id"])):
        visit(e["id"], set())
    return ordered


def progress_path(man):
    """Per-manifest resume file: a single global file let one workspace's
    progress skip another workspace's identically-named entries."""
    key = hashlib.sha256(
        (man.get("workspace", HOME) + "|" +
         ",".join(sorted(e["id"] for e in man.get("entries", [])))).encode()
    ).hexdigest()[:16]
    return os.path.join(PROGRESS_DIR, f"{key}.json")


def do_restore(man, rows, a):
    ordered = plan(man, rows)
    if not ordered:
        return True, []
    prog = {}
    pfile = progress_path(man)
    if getattr(a, "resume", False) and os.path.exists(pfile):
        try:
            cand = json.load(open(pfile))
            age = int(time.time()) - cand.get("t", 0)
            if age > PROGRESS_TTL:
                print(f"  {C['d']}(ignoring resume state from {age//3600}h ago){C['r']}")
            elif cand.get("workspace") != man.get("workspace"):
                print(f"  {C['d']}(resume state is for another workspace){C['r']}")
            else:
                prog = cand
        except Exception:
            prog = {}
    done, failed = set(prog.get("done", [])), []
    total = len(ordered)
    for i, e in enumerate(ordered, 1):
        if e["id"] in done:
            print(f"  [{i}/{total}] {e['id']}: already done (resumed)")
            continue
        deps = [d for d in e.get("needs", []) if d in failed]
        if deps:
            print(f"  [{i}/{total}] {C[SKIPPED]}skip {e['id']}{C['r']} — "
                  f"dependency failed: {', '.join(deps)}")
            failed.append(e["id"])
            continue
        print(f"  [{i}/{total}]", end=" ")
        ok = restore_entry(man, e, a.dry_run, getattr(a, "timeout", None),
                           getattr(a, "quarantine", False))
        if ok:
            done.add(e["id"])
        else:
            failed.append(e["id"])
        if not a.dry_run:
            try:
                os.makedirs(PROGRESS_DIR, exist_ok=True)
                with open(pfile, "w") as pf:
                    json.dump({"done": sorted(done), "t": int(time.time()),
                               "workspace": man.get("workspace")}, pf)
            except OSError as ex:
                eprint(f"note: resume state not saved ({ex.strerror})")
    if not a.dry_run and not failed and os.path.exists(pfile):
        os.remove(pfile)
    return not failed, failed


# ────────────────────────────────────────────────────────────────── output

def print_rows(man, rows, show_all=True):
    w = max([len(e["id"]) for e, _, _ in rows] + [8])
    for e, st, detail in rows:
        if not show_all and st == OK:
            continue
        print(f"  {C[st]}{SYM[st]} {st:<10}{C['r']}{e['id']:<{w}}  "
              f"{C['d']}{detail}{C['r']}")
    bad = [r for r in rows if r[1] in BAD]
    print(f"\n  {len(rows)-len(bad)}/{len(rows)} healthy", end="")
    print(f", {C[CORRUPT]}{len(bad)} damaged{C['r']}" if bad else "")
    return bad


def as_json(man, rows, extra=None):
    kind, why = classify(man, rows)
    out = {"healthy": all(s not in BAD for _, s, _ in rows),
           "total": len(rows),
           "damaged": [e["id"] for e, s, _ in rows if s in BAD],
           "signature": {"pattern": kind, "detail": why},
           "entries": [{"id": e["id"], "status": s, "detail": d,
                        "tier": e.get("tier", 5), "kind": e.get("kind", "file"),
                        "needs": e.get("needs", [])} for e, s, d in rows]}
    if extra:
        out.update(extra)
    return out


# ──────────────────────────────────────────────────────────────── commands

def guard_signature(man, a=None):
    """Recipes are code. Two independent trust paths are accepted:
    HMAC signed by THIS box, or ML-DSA-87 from a trusted signer."""
    state, detail = verify_sig(man)
    if state == "valid":
        return True
    pk_state, pk_detail, pk_fp = verify_pksig(man)
    if pk_state == "valid":
        print(f"  {C['d']}accepted via public-key signature: {pk_detail}{C['r']}")
        return True
    if pk_state == "untrusted":
        eprint(f"REFUSING: {pk_detail}")
        eprint("  The signature is cryptographically valid but you have not "
               "declared this signer trustworthy.")
        eprint(f"  If you recognise this fingerprint, run:  swr trust add {pk_fp} <name>")
        return False
    if pk_state == "invalid":
        eprint(f"REFUSING: public-key signature {pk_detail}")
        return False

    tok = getattr(a, "i_trust_this_manifest", None)
    if tok:
        dg = manifest_digest(man)
        if tok is True or tok == "":
            eprint("--i-trust-this-manifest now requires the manifest digest, so "
                   "trust applies to THIS content only and cannot silently cover "
                   "a later edit.")
            eprint("  if you have reviewed it, re-run with:")
            eprint(f"    --i-trust-this-manifest {dg}")
            return False
        if tok != dg:
            eprint("--i-trust-this-manifest digest mismatch:")
            eprint(f"  you approved {tok}")
            eprint(f"  manifest is  {dg}")
            eprint("  the content changed since you reviewed it — refusing.")
            return False
        eprint(f"!! proceeding on explicit digest approval ({dg[:16]}…); "
               f"signature {state}: {detail}")
        return True

    eprint(f"REFUSING TO RUN RESTORE RECIPES: signature {state} — {detail}")
    eprint("  Recipes execute as shell commands. An unverified manifest is untrusted code.")
    eprint("  If you authored this manifest locally, re-sign it:  swr sign")
    eprint("  If you deliberately pulled it from elsewhere:       "
           "add --i-trust-this-manifest <digest>")
    return False


def cmd_check(man, mpath, a):
    rows = run_check(man, a.only, a.jobs, not a.no_cache)
    if not a.no_record:
        record(man, rows)
    if a.json:
        print(json.dumps(as_json(man, rows), indent=2))
    else:
        bad = print_rows(man, rows, not a.quiet)
        if bad:
            kind, why = classify(man, rows)
            print(f"  {C['b']}wipe signature:{C['r']} {kind} — {why}")
    return EXIT_DAMAGED if any(s in BAD for _, s, _ in rows) else EXIT_OK


def cmd_restore(man, mpath, a):
    if not a.dry_run and not guard_signature(man, a):
        return EXIT_UNREPAIRABLE
    rows = run_check(man, a.only, a.jobs, not a.no_cache)
    if not any(s in BAD for _, s, _ in rows):
        print("nothing to restore — all entries healthy")
        return EXIT_OK
    ok, failed = do_restore(man, rows, a)
    return EXIT_OK if ok else EXIT_UNREPAIRABLE


def cmd_doctor(man, mpath, a):
    if not a.dry_run and not guard_signature(man, a):
        return EXIT_UNREPAIRABLE
    print("== check ==")
    rows = run_check(man, a.only, a.jobs, not a.no_cache)
    if not a.no_record:
        record(man, rows)
    bad = print_rows(man, rows, not a.quiet)
    if not bad:
        if a.json:
            print(json.dumps(as_json(man, rows), indent=2))
        else:
            print("\nworkspace intact — nothing to do")
        return EXIT_OK
    kind, why = classify(man, rows)
    print(f"  {C['b']}wipe signature:{C['r']} {kind} — {why}\n")
    print("== restore ==")
    ok, failed = do_restore(man, rows, a)
    if a.dry_run:
        return EXIT_DAMAGED
    print("\n== re-check ==")
    rows2 = run_check(man, a.only, a.jobs, use_cache=False)
    bad2 = print_rows(man, rows2, not a.quiet)
    if a.json:
        print(json.dumps(as_json(man, rows2, {"restored": ok}), indent=2))
    if bad2:
        print(f"\n{C[CORRUPT]}still damaged:{C['r']} " +
              ", ".join(e["id"] for e, _, _ in bad2))
        return EXIT_RECHECK
    print("\nall entries restored")
    return EXIT_OK


def cmd_why(man, mpath, a):
    hist = history()
    surv = survival(hist)
    if getattr(a, "json", False):
        out = []
        for e in man["entries"]:
            if a.only and e["id"] not in a.only:
                continue
            p = abspath(man, e["path"])
            st, detail = verify(man, e, None, False)
            out.append({"id": e["id"], "status": st, "detail": detail,
                        "path": e["path"], "kind": e.get("kind", "file"),
                        "tier": e.get("tier", 5),
                        "risk": e.get("fragile") or volatile_reason(p) or None,
                        "other_filesystem": fs_boundary(man, p),
                        "survival": surv.get(e["id"]),
                        "needs": e.get("needs", []),
                        "blocks": [x["id"] for x in man["entries"]
                                   if e["id"] in x.get("needs", [])],
                        "restore": e.get("restore")})
        print(json.dumps(out, indent=2))
        return EXIT_OK
    for e in man["entries"]:
        if a.only and e["id"] not in a.only:
            continue
        p = abspath(man, e["path"])
        st, detail = verify(man, e, None, False)
        risk = e.get("fragile") or volatile_reason(p) or "no known fragility"
        print(f"{C['b']}{e['id']}{C['r']}")
        print(f"  is        {st} ({detail})")
        print(f"  path      {e['path']}  [{e.get('kind','file')}, tier {e.get('tier',5)}]")
        print(f"  at risk   {risk}")
        if fs_boundary(man, p):
            print("  warning   lives on a different filesystem than the workspace root")
        if e["id"] in surv:
            n = sum(1 for h in hist if e["id"] in h.get("s", {}))
            print(f"  survives  {surv[e['id']]*100:.0f}% of turns (n={n})")
        if e.get("needs"):
            print(f"  needs     {', '.join(e['needs'])}")
        dependents = [x["id"] for x in man["entries"] if e["id"] in x.get("needs", [])]
        if dependents:
            print(f"  blocks    {', '.join(dependents)}")
        print(f"  fix       {(e.get('restore') or '(no recipe — manual)')[:110]}")
        print()
    return EXIT_OK


def cmd_stats(man, mpath, a):
    hist = history()
    if getattr(a, "json", False):
        print(json.dumps({"observations": len(hist), "survival": survival(hist)},
                         indent=2))
        return EXIT_OK
    if not hist:
        print("no history yet — run `swr check` over a few turns")
        return EXIT_OK
    surv = survival(hist)
    print(f"observations: {len(hist)} turns\n")
    print(f"  {'entry':<32} {'survives':>9}  risk")
    for k in sorted(surv, key=lambda x: surv[x]):
        e = next((x for x in man["entries"] if x["id"] == k), {})
        r = e.get("fragile") or volatile_reason(abspath(man, e.get("path", ""))) or ""
        print(f"  {k:<32} {surv[k]*100:>8.0f}%  {C['d']}{r[:44]}{C['r']}")
    return EXIT_OK


def cmd_audit(man, mpath, a):
    ws = man.get("workspace", HOME)
    tracked = {os.path.normpath(abspath(man, e["path"])) for e in man["entries"]}
    found = []
    for name in sorted(os.listdir(ws)):
        p = os.path.normpath(os.path.join(ws, name))
        if p in tracked or name.startswith(".swr"):
            continue
        if name in EXCLUDED_DIRNAMES:
            continue
        if any(p.startswith(t + os.sep) for t in tracked):
            continue
        try:
            sz = (sum(os.path.getsize(os.path.join(dp, f))
                      for dp, _, fs in os.walk(p) for f in fs)
                  if os.path.isdir(p) else os.path.getsize(p))
        except OSError:
            sz = 0
        found.append((sz, name, "dir" if os.path.isdir(p) else "file"))
    found.sort(reverse=True)
    if not found:
        print("no untracked artifacts")
        return EXIT_OK
    print(f"{len(found)} untracked (largest first):\n")
    for sz, name, kind in found[:a.limit]:
        flag = "  <-- consider tracking" if sz > 1 << 20 else ""
        print(f"  {sz/1e6:>9.1f} MB  {kind:<5} {name}{flag}")
    return EXIT_OK


def canary_paths(man):
    ws = man.get("workspace", HOME)
    spots = {"home": os.path.join(ws, CANARY_DIR, "home.txt"),
             "tmp": os.path.join("/tmp", CANARY_DIR, "tmp.txt")}
    for d in ("build", "node_modules", "dist", "__pycache__", ".cache", "target"):
        spots[d] = os.path.join(ws, CANARY_DIR + "-probe", d, "canary.txt")
    return spots


def cmd_canary(man, mpath, a):
    """Empirically learn what this platform actually persists."""
    spots = canary_paths(man)
    if a.action == "clean":
        ws = man.get("workspace", HOME)
        removed = 0
        for d in (os.path.join(ws, CANARY_DIR), os.path.join(ws, CANARY_DIR + "-probe"),
                  os.path.join("/tmp", CANARY_DIR)):
            if os.path.isdir(d):
                shutil.rmtree(d, ignore_errors=True)
                removed += 1
        print(f"removed {removed} canary director{'y' if removed == 1 else 'ies'}")
        return EXIT_OK
    if a.action == "plant":
        stamp = str(int(time.time()))
        for name, p in spots.items():
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w") as f:
                f.write(stamp)
        print(f"planted {len(spots)} canaries (stamp {stamp})")
        print("run `swr canary read` in a LATER turn to see what survived,")
        print("then `swr canary clean` to remove the probe directories")
        return EXIT_OK
    alive = [n for n, p in spots.items() if os.path.exists(p)]
    dead = [n for n, p in spots.items() if not os.path.exists(p)]
    print(f"survived ({len(alive)}): {', '.join(sorted(alive)) or '-'}")
    print(f"lost     ({len(dead)}): {', '.join(sorted(dead)) or '-'}")
    if dead:
        print("\nempirically volatile on this platform — treat as rebuildable:")
        for d in sorted(dead):
            print(f"  {d}/")
    return EXIT_OK


def cmd_retighten(man, mpath, a):
    """Recompute loose tree bounds in an existing manifest."""
    changed = []
    for e in man["entries"]:
        if e.get("kind") != "tree" or e.get("merkle"):
            continue
        p = abspath(man, e["path"])
        if not os.path.isdir(p):
            continue
        n = sum(len(f) for _, _, f in os.walk(p))
        old = e.get("min_files")
        new = max(1, n - max(1, n // 20))
        if old is None or old < new:
            e["min_files"], e["files_at_capture"] = new, n
            changed.append((e["id"], old, new, n))
    if not changed:
        print("all tree bounds already tight")
        return EXIT_OK
    for i, o, nw, n in changed:
        tol_old = "n/a" if o is None else f"{100*(n-o)//n}%"
        print(f"  {i}: min_files {o} -> {nw}  (tolerated {tol_old}, now {100*(n-nw)//n}%)")
    save(mpath, man)
    print(f"\nretightened {len(changed)} entr{'y' if len(changed)==1 else 'ies'}; "
          f"manifest re-signed")
    return EXIT_OK


def cmd_trust(man, mpath, a):
    """Manage the public-key trust store."""
    trust = load_trust()
    if a.action == "list":
        if not trust:
            print("no trusted signers")
            print("  add one:  swr trust add <fingerprint> <name>")
            return EXIT_OK
        for fp, name in sorted(trust.items(), key=lambda x: x[1]):
            print(f"  {name:<20} {fp}")
        return EXIT_OK
    if a.action == "add":
        if not a.fingerprint or not a.name:
            eprint("usage: swr trust add <fingerprint> <name>")
            return EXIT_BADMANIFEST
        trust[a.fingerprint] = a.name
        os.makedirs(SWR_DIR, exist_ok=True)
        json.dump(trust, open(TRUST_FILE, "w"), indent=2)
        print(f"trusted '{a.name}' = {a.fingerprint}")
        print("  VERIFY this fingerprint out-of-band before relying on it.")
        return EXIT_OK
    if a.action == "remove":
        if a.fingerprint in trust:
            name = trust.pop(a.fingerprint)
            json.dump(trust, open(TRUST_FILE, "w"), indent=2)
            print(f"removed '{name}'")
        else:
            print("not in trust store")
        return EXIT_OK
    if a.action == "mine":
        if not _mldsa_available():
            eprint("no ML-DSA identity — create one: python3 swr_crypto.py keygen")
            return EXIT_BADMANIFEST
        print(f"your signing fingerprint: {_fingerprint(_pubkey_pem())}")
        print("  share it so others can:  swr trust add <fp> <your-name>")
        return EXIT_OK
    return EXIT_OK


def cmd_escrow(man, mpath, a):
    """Embed small files' contents in the manifest so they are restorable
    even with no build recipe."""
    done, skipped = [], []
    for e in man["entries"]:
        if a.only and e["id"] not in a.only:
            continue
        if e.get("kind") != "file":
            continue
        p = abspath(man, e["path"])
        if not os.path.isfile(p):
            continue
        sz = os.path.getsize(p)
        if sz > min(a.max_bytes, ESCROW_DECOMP_MAX):
            skipped.append((e["id"], sz))
            continue
        e["escrow"] = escrow_blob(p)
        e["escrow_bytes"] = sz
        e.setdefault("restore", f"swr-escrow:{e['id']}")
        if a.force:
            e["restore"] = f"swr-escrow:{e['id']}"
        done.append((e["id"], sz, len(e["escrow"])))
    if not done and not skipped:
        print("nothing to escrow")
        return EXIT_OK
    for i, sz, enc in done:
        print(f"  escrowed {i:<28} {sz:>7,}B -> {enc:>7,}B inline")
    for i, sz in skipped:
        print(f"  skipped  {i:<28} {sz:>7,}B (over --max-bytes {a.max_bytes:,})")
    if done:
        save(mpath, man)
        total = sum(len(e.get("escrow", "")) for e in man["entries"])
        print(f"\n{len(done)} file(s) escrowed; manifest re-signed "
              f"(+{total/1024:.0f} KB inline)")
        print("  these now survive a total wipe via `swr_paste.py push`")
    return EXIT_OK


def cmd_attacktest(man, mpath, a):
    """Regression tests for every known attack class."""
    ok = True

    def t(name, cond):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'}  {name}")
        ok = ok and cond

    key = get_key()
    base = {"version": 2, "workspace": "/tmp", "entries": [
        {"id": "safe", "path": "x", "kind": "file", "tier": 1,
         "restore": "echo benign", "needs": []}]}
    sig = hmac.new(key, canonical(base), hashlib.sha256).hexdigest()
    signed = dict(base)
    signed["_sig"] = {"alg": "HMAC-SHA256", "value": sig, "at": 0}
    t("legit manifest verifies", verify_sig(json.loads(json.dumps(signed)))[0] == "valid")

    ev = json.loads(json.dumps(signed))
    ev["entries"] = [{"id": "evil", "path": "x", "kind": "file", "tier": 1,
                      "restore": "rm -rf /", "needs": []}]
    t("altered entries rejected", verify_sig(ev)[0] != "valid")

    fg = json.loads(json.dumps(signed))
    fg["entries"] = ev["entries"]
    fg["_presig_body"] = base
    t("_presig_body forgery rejected", verify_sig(fg)[0] != "valid")

    mg = json.loads(json.dumps(signed))
    mg["_migrated_from"] = 1
    mg["entries"] = ev["entries"]
    t("_migrated_from forgery rejected", verify_sig(mg)[0] != "valid")

    import zlib as _z
    bomb = base64.b64encode(_z.compress(b"\0" * (200 * 1024 * 1024), 9)).decode()
    try:
        escrow_restore({"escrow": bomb, "escrow_bytes": 1024})
        t("decompression bomb rejected", False)
    except Exception:
        t("decompression bomb rejected", True)
    try:
        escrow_restore({"escrow": bomb, "escrow_bytes": 300 * 1024 * 1024})
        t("oversized escrow rejected", False)
    except Exception:
        t("oversized escrow rejected", True)

    ps = man.get("_pksig")
    if ps:
        fake = json.loads(json.dumps(man))
        fake["_pksig"] = dict(ps)
        fake["_pksig"]["fp"] = "aaaaa-bbbbb-ccccc-ddddd"
        t("fingerprint substitution rejected", verify_pksig(fake)[0] != "valid")

    print(f"\n{'ALL PASS' if ok else 'FAILURES'}")
    return EXIT_OK if ok else EXIT_UNREPAIRABLE


def cmd_verify(man, mpath, a):
    st, detail = verify_sig(man)
    pst, pdetail, pfp = verify_pksig(man)
    if getattr(a, "json", False):
        print(json.dumps({"signature": st, "detail": detail,
                          "pubkey_signature": pst, "pubkey_detail": pdetail,
                          "signer_fingerprint": pfp,
                          "digest": manifest_digest(man)}, indent=2))
        return EXIT_OK if (st == "valid" or pst == "valid") else EXIT_BADMANIFEST
    print(f"signature: {st} — {detail}")
    print(f"pubkey:    {pst} — {pdetail}")
    print(f"digest:    {manifest_digest(man)}")
    return EXIT_OK if (st == "valid" or pst == "valid") else EXIT_BADMANIFEST


def cmd_sign(man, mpath, a):
    save(mpath, man)
    st, detail = verify_sig(load(mpath))
    print(f"signed: {st} ({detail})")
    print(f"key: {KEY_FILE} (mode {oct(stat.S_IMODE(os.stat(KEY_FILE).st_mode))})")
    if _mldsa_available():
        print(f"pubkey signature: ML-DSA-87 as {_fingerprint(_pubkey_pem())}")
    return EXIT_OK


def cmd_selftest(man, mpath, a):
    """Prove restore recipes are idempotent. Executes recipes -> guarded."""
    if not guard_signature(man, a):
        return EXIT_UNREPAIRABLE
    print("selftest: verifying restore recipes are idempotent\n")
    maxt = a.max_tier if a.max_tier is not None else 1
    targets = [e for e in man["entries"]
               if e.get("restore") and (not a.only or e["id"] in a.only)
               and e.get("tier", 5) <= maxt]
    if not targets:
        print("no eligible entries (raise --max-tier; default 1 keeps it cheap)")
        return EXIT_OK
    bad = 0
    for e in targets:
        print(f"  {e['id']}: ", end="", flush=True)

        def _run():
            try:
                return subprocess.run(
                    ["bash", "-lc", e["restore"]], cwd=man.get("workspace", HOME),
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                    timeout=e.get("timeout_s", 300),
                    start_new_session=True).returncode == 0
            except subprocess.TimeoutExpired:
                print("TIMEOUT ", end="")
                return False
            except Exception as ex:
                print(f"ERROR({ex}) ", end="")
                return False

        if e["restore"].startswith("swr-escrow:"):
            print("escrow (idempotent by construction)")
            continue
        ok2 = _run()
        st2, _ = verify(man, e, None, False)
        ok3 = _run()
        st3, _ = verify(man, e, None, False)
        good = ok2 and ok3 and st2 == OK and st3 == OK
        print(f"{'IDEMPOTENT' if good else 'NOT IDEMPOTENT'} ({st2}->{st3})")
        if not good:
            bad += 1
    print(f"\n{len(targets)-bad}/{len(targets)} recipes idempotent")
    return EXIT_OK if not bad else EXIT_UNREPAIRABLE


# ─────────────────────────────────────────────────────── v1.5.0: any workspace

# Agent presets: (id, relpath, kind, tier, sentinels, recipe, needs)
# DESIGN RULE: a preset NEVER writes a secret into a recipe. Credential files
# are hash-TRACKED (integrity of the file is verified — truncation and
# rotation are caught) but their recipes only restore the DIRECTORY,
# PERMISSIONS and an empty placeholder; the secret value must come back via
# the user's own channel (env var, secret manager, or `swr escrow`, which
# encrypts). This is the same rule the paste-sync redactor enforces.
AGENT_PRESETS = {
    "arena": [
        ("shim-npx", ".shim/npx", "file", 0, None,
         "mkdir -p ~/.shim && printf '#!/bin/bash\\nexec /usr/bin/npx --yes \"$@\"\\n' > ~/.shim/npx && chmod +x ~/.shim/npx"),
        ("cred-store", "secrets/api_credentials.json", "file", 0, None,
         'mkdir -p ~/secrets && umask 177 && touch ~/secrets/api_credentials.json   # value restores from your secret channel, never from this recipe'),
        ("clawhub-token", ".clawhub/TOKEN", "file", 0, None,
         'mkdir -p ~/.clawhub && umask 177 && touch ~/.clawhub/TOKEN   # paste the token back from your password manager'),
        ("turn-state", ".arena_turn", "tree", 2, [], None),
        ("skills", "skills", "tree", 2, [], None),
    ],
    "openclaw": [
        ("clawhub-token", ".clawhub/TOKEN", "file", 0, None,
         'mkdir -p ~/.clawhub && umask 177 && touch ~/.clawhub/TOKEN   # paste the token back from your password manager'),
        ("openclaw-home", ".openclaw", "tree", 0, ["settings.json"], None),
        ("skills", "skills", "tree", 2, [], None),
    ],
    "claude-code": [
        ("claude-home", ".claude", "tree", 0, ["settings.json"], None),
        ("claude-state", ".claude.json", "file", 0, None,
         'umask 177 && touch ~/.claude.json   # onboarding state; value not secret but large — restore from your own backup'),
        ("claude-memory", ".claude/CLAUDE.md", "file", 2, None, None),
    ],
    "generic": [
        ("bashrc", ".bashrc", "file", 1, None, None),
        ("profile", ".profile", "file", 1, None, None),
        ("gitconfig", ".gitconfig", "file", 1, None, None),
    ],
}


def _preset_entries(man, preset):
    """Build entries for a preset from what actually exists on disk.

    Presets are opportunistic: paths that do not exist are skipped (a preset
    aimed at the wrong machine adds noise, not protection). Trees get loose
    bounds — the user is expected to run `retighten`/`--merkle` on valuable
    trees — and sentinels are intersected with reality so a preset never
    ships a sentinel that cannot pass.
    """
    ws = man.get("workspace", HOME)
    out = []
    for ident, rel, kind, tier, sentinels, recipe in AGENT_PRESETS.get(preset, []):
        ap = os.path.join(ws, rel) if not os.path.isabs(rel) else rel
        ap = os.path.abspath(os.path.join(HOME, rel)) if rel.startswith("~") or not os.path.isabs(rel) else ap
        ap = os.path.abspath(os.path.expanduser(rel)) if rel.startswith("~") else ap
        ap = os.path.join(ws, rel)
        if not os.path.exists(ap):
            continue
        # Preset dotfiles (.shim, .arena_turn, .clawhub, .claude…) are HOME-shaped
        # and their recipes target $HOME. They only belong in a manifest whose
        # workspace root CONTAINS them (in practice: workspace == $HOME, the
        # arena layout). Tracking them under a foreign workspace root would
        # verify one path while the recipe restores another.
        # realpath: a symlinked entry name must not smuggle a target outside
        # the workspace past a lexical check (consensus-review fix).
        if os.path.commonpath([os.path.realpath(ws), os.path.realpath(ap)]) != os.path.realpath(ws):
            continue
        if escapes_workspace(man, rel):
            continue
        try:
            if kind == "tree":
                real_sents = [x for x in (sentinels or [])
                              if os.path.exists(os.path.join(ap, x))]
                e = capture(man, rel, "tree", ident, tier=tier, sentinels=real_sents)
            else:
                e = capture(man, rel, "file" if os.path.isfile(ap) else "tree",
                            ident, tier=tier, restore=recipe)
        except Exception as ex:                        # unreadable path: skip loudly
            eprint(f"  preset: skipping {rel!r} ({ex})")
            continue
        e["_preset"] = preset
        out.append(e)
    return out


def cmd_preset(man, mpath, a):
    """Apply an agent preset to the current manifest (idempotent)."""
    preset = a.name
    if preset not in AGENT_PRESETS:
        eprint(f"unknown preset {preset!r} — choose one of: " +
               ", ".join(sorted(AGENT_PRESETS)))
        return EXIT_BADMANIFEST
    if man is None:
        eprint("no manifest yet — run `swr init` first (or `swr autopilot`)")
        return EXIT_BADMANIFEST
    ents = _preset_entries(man, preset)
    known = {e["id"] for e in man["entries"]}
    added = 0
    for e in ents:
        if e["id"] in known:
            continue
        man["entries"].append(e)
        added += 1
        print(f"  + {e['id']:<16} {e['kind']:5} tier {e['tier']}  {e['path']}")
    save(mpath, man)
    print(f"preset {preset!r}: {added} new entr{'y' if added == 1 else 'ies'} "
          f"({len(ents) - added} already present, {len(AGENT_PRESETS[preset]) - len(ents)} not on this machine)")
    if any(e["kind"] == "tree" for e in ents):
        print("next: `swr retighten` to tighten preset trees, `swr add --merkle` for valuable ones")
    return EXIT_OK


MODEL_EXTS = (".gguf", ".safetensors", ".onnx", ".bin", ".pt", ".ckpt")


def cmd_models(man, mpath, a):
    """Find model/weight files on disk and (optionally) track them as blobs.

    Model weights are the biggest single wipe loss — hours of download for a
    file whose damage is invisible (a valid header on half the bytes). Blob
    entries verify exact byte count, which catches truncation in one stat()
    call. Scan never invents download recipes: without --url the entry ships
    recipe-less (verification-only) and `swr why` tells you to add one.
    """
    if man is None:
        eprint("no manifest — run `swr init` first")
        return EXIT_BADMANIFEST
    ws = man.get("workspace", HOME)
    min_bytes = a.min_mb * 1024 * 1024
    found, volatile = [], 0
    tracked = {e["path"] for e in man["entries"]}
    for root, dirs, files in os.walk(ws):
        dirs[:] = [d for d in dirs if d not in
                   ("build", "dist", "out", "target", "node_modules", ".venv",
                    "__pycache__", ".cache", ".git")]
        for f in files:
            if not f.lower().endswith(MODEL_EXTS):
                continue
            ap = os.path.join(root, f)
            rel = os.path.relpath(ap, ws)
            try:
                sz = os.path.getsize(ap)
            except OSError:
                continue
            if volatile_reason(ap):
                volatile += 1
                continue
            if sz < min_bytes or rel in tracked:
                continue
            found.append((rel, sz))
    found.sort(key=lambda x: -x[1])
    if not found:
        print(f"no untracked model files > {a.min_mb} MB"
              + (f" ({volatile} skipped in volatile dirs)" if volatile else ""))
        return EXIT_OK
    print(f"{len(found)} untracked model file(s), {sum(s for _, s in found)/2**30:.2f} GiB total:")
    for rel, sz in found:
        print(f"  {sz/2**30:6.2f} GiB  {rel}")
    if not a.apply:
        print("\nre-run with --apply to track them (byte-count verification; add download recipes with")
        print("`swr add <path> --kind blob --restore \"curl -C - ...\"`)")
        return EXIT_OK
    for rel, sz in found:
        e = capture(man, rel, "blob", tier=3)
        man["entries"].append(e)
        print(f"  + tracked {e['id']} ({sz:,} bytes)")
    save(mpath, man)
    print(f"manifest re-signed with {len(found)} blob entries")
    return EXIT_OK


def cmd_export(man, mpath, a):
    """Export the restore runbook in a portable format for ANY agent.

    The manifest is signed, but a fresh box has neither it nor this tool —
    `export-recipes` writes the tier/DAG-ordered recovery plan as a shell
    script, markdown, or JSON that any agent (or human) can execute/read
    directly. Escrow recipes (`swr-escrow:`) are exported as comments: they
    need the encrypted manifest itself, which paste-sync carries.
    """
    if man is None:
        eprint("no manifest — run `swr init` first")
        return EXIT_BADMANIFEST
    sig_ok = verify_sig(man)[0] == "valid"
    _status_all = {x[0]["id"]: x[1] for x in run_check(man, use_cache=True)}
    # The runbook covers ALL entries (not just damaged ones — a fresh box needs
    # the full rebuild order), topologically sorted so dependencies come before
    # dependents, ties broken by tier (credentials/shims first) then id.
    import heapq
    by_id = {e["id"]: e for e in man["entries"]}
    needs_of = {i: [d for d in e.get("needs", []) if d in by_id]
                for i, e in by_id.items()}
    indeg = {i: len(d) for i, d in needs_of.items()}
    dependents = {i: [] for i in by_id}
    for i, ds in needs_of.items():
        for d in ds:
            dependents[d].append(i)
    heap = [(by_id[i].get("tier", 5), i) for i, deg in indeg.items() if deg == 0]
    heapq.heapify(heap)
    rows = []
    while heap:
        _, i = heapq.heappop(heap)
        rows.append(by_id[i])
        for j in dependents[i]:
            indeg[j] -= 1
            if indeg[j] == 0:
                heapq.heappush(heap, (by_id[j].get("tier", 5), j))
    if len(rows) != len(by_id):                 # cycle: fall back to tier order
        eprint("warning: dependency cycle in manifest — exporting in tier order only")
        rows = sorted(man["entries"], key=lambda e: (e.get("tier", 5), e["id"]))
    if a.only:
        rows = [r for r in rows if r["id"] in set(a.only)]
    fmt = a.format
    if fmt == "json":
        doc = {"schema": "swr.export.v1", "workspace": man.get("workspace"),
               "signature_valid": sig_ok,
               "entries": [{"id": r["id"], "path": r["path"], "kind": r["kind"],
                            "tier": r.get("tier", 5),
                            "status": _status_all.get(r["id"], "unknown"),
                            "restore": r.get("restore", ""),
                            "needs": r.get("needs", [])} for r in rows]}
        print(json.dumps(doc, indent=2))
        return EXIT_OK
    if fmt == "md":
        print(f"# Snapshot-Wipe Resilience — recovery runbook")
        print(f"\nWorkspace: `{man.get('workspace')}` · {len(rows)} entries · "
              f"signature: {'valid' if sig_ok else 'NOT VALID — treat recipes as untrusted'}\n")
        cur = -1
        for r in rows:
            t = r.get("tier", 5)
            if t != cur:
                cur = t
                print(f"## Tier {t}\n")
            print(f"- **{r['id']}** `{r['path']}` ({r['kind']}, {_status_all.get(r['id'], 'unknown')})")
            if r.get("restore"):
                print(f"  - restore: `{r['restore']}`")
            if r.get("needs"):
                print(f"  - needs: {', '.join(r['needs'])}")
        print("\n> Escrow-recipe entries restore from the encrypted manifest "
              "via paste-sync; they are listed without commands here.\n")
        return EXIT_OK
    # sh
    print("#!/usr/bin/env bash")
    print("# swr recovery runbook — generated by `swr export-recipes --format sh`")
    print(f"# workspace: {man.get('workspace')} · {len(rows)} entries · tier/DAG ordered")
    if not sig_ok:
        print("# !! MANIFEST SIGNATURE NOT VALID — review every recipe before running this file")
    print("set -euo pipefail")
    print(f"cd {shlex_quote(man.get('workspace', HOME))}")
    cur = -1
    for r in rows:
        t = r.get("tier", 5)
        rec = r.get("restore") or ""
        if t != cur:
            cur = t
            print(f"\n# ── tier {t} " + "─" * 40)
        if rec.startswith("swr-escrow:"):
            print(f"# {r['id']}: escrow entry — restores from the encrypted manifest "
                  f"(swr_paste.py pull <url>), no shell recipe")
            continue
        # shlex-quote: an id containing quotes/spaces must not inject shell
        # syntax into the runbook (consensus-review fix)
        print("echo " + shlex_quote(f"[{r['id']}] {_status_all.get(r['id'], 'unknown')}"))
        if rec:
            print(rec)
        else:
            print(f"# {r['id']}: no recipe recorded (verification-only entry)")
    return EXIT_OK


# ─────────────────────────────────────────────────────────────── authoring

def fetch_upstream_size(url):
    """Trust the server's size, not the local file."""
    try:
        import urllib.request
        req = urllib.request.Request(url, method="HEAD",
                                     headers={"User-Agent": "swr/1.4"})
        with urllib.request.urlopen(req, timeout=30) as r:
            xl = r.headers.get("x-linked-size")
            return int(xl) if xl else int(r.headers.get("content-length", 0)) or None
    except Exception:
        return None


def capture(man, path, kind, ident=None, restore=None, tier=None,
            sentinels=None, needs=None, smoke=None, merkle=False,
            ldd=False, upstream=None):
    ap = abspath(man, path)
    e = {"id": ident or os.path.basename(path.rstrip("/")), "path": path, "kind": kind}
    if kind == "tree":
        e["sentinels"] = sentinels or []
        if os.path.isdir(ap):
            if merkle:
                root, n = merkle_tree(ap)
                e["merkle"], e["files_at_capture"] = root, n
            else:
                nf = sum(len(f) for _, _, f in os.walk(ap))
                # Tight bound: 5% churn tolerance. nf//2 let a tree silently
                # lose HALF its files and still pass.
                e["min_files"] = max(1, nf - max(1, nf // 20))
                e["files_at_capture"] = nf
    elif kind == "blob":
        e["bytes"] = os.path.getsize(ap)
        e["headtail"] = sha256_headtail(ap)
        if upstream:
            us = fetch_upstream_size(upstream)
            if us and us != e["bytes"]:
                eprint(f"!! upstream says {us:,} bytes but local file is "
                       f"{e['bytes']:,} — recording upstream size")
                e["bytes"] = us
            e["upstream"] = upstream
    else:
        e["sha256"] = sha256_file(ap)
        e["mode"] = format(stat.S_IMODE(os.stat(ap).st_mode), "04o")
        if ldd:
            e["ldd"] = True
    e["tier"] = tier if tier is not None else (1 if kind == "file" else 3)
    if needs:
        e["needs"] = needs
    if smoke:
        e["smoke"] = smoke
    if restore:
        e["restore"] = restore
    why = volatile_reason(ap)
    if why:
        e["fragile"] = why
    return e


def shlex_quote(s):
    import shlex
    return shlex.quote(s)


def cmd_add(man, mpath, a):
    ap = abspath(man, a.path)
    if not os.path.exists(ap):
        eprint(f"cannot add: {ap} does not exist (add entries while they are healthy)")
        return EXIT_BADMANIFEST
    if escapes_workspace(man, a.path):
        eprint(f"cannot add: {a.path!r} resolves outside the workspace root "
               f"{man.get('workspace', HOME)!r}.")
        return EXIT_BADMANIFEST
    kind = a.kind or ("tree" if os.path.isdir(ap)
                      else "blob" if os.path.getsize(ap) > 32 * 1024 * 1024
                      else "file")
    e = capture(man, a.path, kind, a.id, a.restore, a.tier, a.sentinel,
                a.needs, a.smoke, a.merkle, a.ldd, a.upstream)
    man["entries"] = [x for x in man["entries"] if x["id"] != e["id"]] + [e]
    save(mpath, man)
    print(json.dumps(e, indent=2))
    return EXIT_OK


def cmd_init(mpath, a):
    ws = os.path.abspath(a.workspace)
    man = {"version": SCHEMA_VERSION, "workspace": ws,
           "created": int(time.time()), "entries": []}
    ents = []
    for name in sorted(os.listdir(ws)):
        p = os.path.join(ws, name)
        if os.path.isfile(p) and name.endswith((".sh", ".py")):
            ents.append(capture(man, name, "file", tier=1,
                                restore=f"chmod +x {shlex_quote(p)}"))
        elif os.path.isfile(p) and os.path.getsize(p) > 32 * 1024 * 1024:
            ents.append(capture(man, name, "blob", tier=3))
    man["entries"] = ents
    save(mpath, man)
    print(f"wrote {mpath} with {len(ents)} auto-detected entries (signed)")
    print("next: `swr add` your trees with --sentinel/--merkle, then `swr escrow`")
    return EXIT_OK


def cmd_autopilot(man, mpath, a):
    """Zero-to-protected in one command."""
    ws = os.path.abspath(a.workspace)
    print("== autopilot ==")
    if man is None:
        cmd_init(mpath, argparse.Namespace(workspace=ws))
        man = load(mpath)
    n0 = len(man["entries"])
    for name in sorted(os.listdir(ws)):
        p = os.path.join(ws, name)
        if not os.path.isdir(p) or name.startswith("."):
            continue
        if any(x["path"] == name for x in man["entries"]):
            continue
        if sum(len(f) for _, _, f in os.walk(p)) == 0:
            continue
        sent = []
        for cand in ("CMakeLists.txt", "package.json", "pyproject.toml",
                     "Makefile", "go.mod", "Cargo.toml", "pom.xml"):
            if os.path.exists(os.path.join(p, cand)):
                sent.append(cand)
        # Root markers alone miss the classic failure: a subdirectory that
        # survives while being emptied.
        for sub in ("src", "lib", "include", "ggml/src", "app", "cmd"):
            sp = os.path.join(p, sub)
            if not os.path.isdir(sp):
                continue
            picks = sorted(f for f in os.listdir(sp)
                           if os.path.isfile(os.path.join(sp, f))
                           and not f.startswith("."))
            if picks:
                sent.append(os.path.join(sub, picks[0]))
        man["entries"].append(capture(man, name, "tree", tier=2,
                                      sentinels=sent[:6]))
    save(mpath, man)
    print(f"tracked {len(man['entries'])} entries ({len(man['entries'])-n0} new)")
    rows = run_check(man, None, a.jobs, False)
    print_rows(man, rows, False)
    norec = [e["id"] for e in man["entries"] if not e.get("restore")]
    if norec:
        print(f"\n  {C[STRIPPED]}{len(norec)} entr"
              f"{'y' if len(norec)==1 else 'ies'} "
              f"{'has' if len(norec)==1 else 'have'} NO restore recipe{C['r']} — "
              f"detectable but not repairable:")
        for i in norec:
            print(f"    {i}")
        print("  add one:  swr add <path> --restore '<shell command>'")
        print("  or embed small files:  swr escrow")
    print("\nnext: push off-box:  python3 swr_paste.py push")
    return EXIT_OK


# ───────────────────────────────────────────────────────────────────── main

def main():
    p = argparse.ArgumentParser(
        prog="swr", description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("-m", "--manifest",
                   default=os.environ.get("SWR_MANIFEST", DEFAULT_MANIFEST))
    p.add_argument("--json", action="store_true", help="machine-readable output")
    p.add_argument("--jobs", type=int, default=8,
                   help="parallel verifiers (clamped to 1..32)")
    p.add_argument("--no-cache", action="store_true",
                   help="ignore the mtime cache and re-hash everything "
                        "(the cache is a speed optimisation, not tamper-proof)")
    p.add_argument("--no-record", action="store_true", help="do not log telemetry")
    p.add_argument("--quiet", action="store_true", help="only show damaged entries")
    p.add_argument("--no-lock", action="store_true")
    s = p.add_subparsers(dest="cmd", required=True)

    q = s.add_parser("init"); q.add_argument("--workspace", default=HOME)
    q.add_argument("--agent", default=None,
                   help="also apply an agent preset: " + "/".join(sorted(AGENT_PRESETS)))
    q = s.add_parser("autopilot"); q.add_argument("--workspace", default=HOME)
    q = s.add_parser("preset"); q.add_argument("name",
        help="arena|openclaw|claude-code|generic — add known state trees/credentials for that agent")
    q = s.add_parser("models"); q.add_argument("--apply", action="store_true")
    q.add_argument("--min-mb", type=int, default=10)
    q = s.add_parser("export-recipes")
    q.add_argument("--format", choices=["sh", "md", "json"], default="sh")
    q.add_argument("--only", nargs="*")

    q = s.add_parser("add")
    q.add_argument("path"); q.add_argument("--id")
    q.add_argument("--kind", choices=["file", "blob", "tree"])
    q.add_argument("--restore"); q.add_argument("--tier", type=int)
    q.add_argument("--sentinel", action="append")
    q.add_argument("--needs", action="append", help="entry id this depends on")
    q.add_argument("--smoke", help="shell cmd that must exit 0")
    q.add_argument("--merkle", action="store_true", help="full-tree hash")
    q.add_argument("--ldd", action="store_true", help="check shared libs resolve")
    q.add_argument("--upstream", help="URL to fetch authoritative size from")

    for n in ("check", "restore", "doctor", "why", "stats", "sign", "verify"):
        q = s.add_parser(n)
        q.add_argument("--only", nargs="*")
        if n in ("restore", "doctor"):
            q.add_argument("--dry-run", action="store_true")
            q.add_argument("--timeout", type=int)
            q.add_argument("--quarantine", action="store_true")
            q.add_argument("--resume", action="store_true")
            q.add_argument("--i-trust-this-manifest", nargs="?", const=True,
                           default=None, metavar="DIGEST",
                           dest="i_trust_this_manifest",
                           help="approve THIS exact manifest by digest")

    q = s.add_parser("audit"); q.add_argument("--limit", type=int, default=20)
    q = s.add_parser("canary")
    q.add_argument("action", choices=["plant", "read", "clean"])
    s.add_parser("retighten")
    s.add_parser("attacktest")
    q = s.add_parser("trust")
    q.add_argument("action", choices=["list", "add", "remove", "mine"])
    q.add_argument("fingerprint", nargs="?"); q.add_argument("name", nargs="?")
    q = s.add_parser("escrow")
    q.add_argument("--only", nargs="*")
    q.add_argument("--max-bytes", type=int, default=ESCROW_MAX)
    q.add_argument("--force", action="store_true")
    q = s.add_parser("selftest")
    q.add_argument("--only", nargs="*"); q.add_argument("--max-tier", type=int)
    q.add_argument("--i-trust-this-manifest", nargs="?", const=True,
                   default=None, metavar="DIGEST", dest="i_trust_this_manifest")

    a = p.parse_args()
    a.jobs = max(1, min(32, getattr(a, "jobs", 8)))

    if a.cmd == "init":
        rc = cmd_init(a.manifest, a)
        if rc == EXIT_OK and getattr(a, "agent", None):
            rc = cmd_preset(load(a.manifest), a.manifest,
                            argparse.Namespace(name=a.agent))
        return rc
    if a.cmd == "autopilot":
        return cmd_autopilot(load(a.manifest, require=False), a.manifest, a)
    if a.cmd == "preset":
        return cmd_preset(load(a.manifest, require=False), a.manifest, a)

    man = load(a.manifest)
    fns = {"check": cmd_check, "restore": cmd_restore, "doctor": cmd_doctor,
           "add": cmd_add, "why": cmd_why, "stats": cmd_stats, "audit": cmd_audit,
           "canary": cmd_canary, "sign": cmd_sign, "verify": cmd_verify,
           "selftest": cmd_selftest, "retighten": cmd_retighten,
           "attacktest": cmd_attacktest, "trust": cmd_trust, "escrow": cmd_escrow,
           "models": cmd_models, "export-recipes": cmd_export}
    needs_lock = a.cmd in ("restore", "doctor", "selftest")
    with Lock(needs_lock and not a.no_lock):
        return fns[a.cmd](man, a.manifest, a)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        eprint("\ninterrupted")
        sys.exit(130)
