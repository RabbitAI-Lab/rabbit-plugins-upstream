#!/usr/bin/env python3
"""agentkey.py — LOCAL, offline, encrypted API-key vault for agents (v2.0.0).

No network. No telemetry. No update beacons. Everything runs on this machine,
key material enters via stdin or a 0600 file (never argv), ciphertext stays at
rest under ${AGENTKEY_HOME:-~/.agentkey} (0700), and the audit log is a
hash-chained JSONL that detects tampering.

Crypto (encrypt-then-MAC via system `openssl`, evidence: docs/evidence.md):
  ciphertext = AES-256-CBC(PBKDF2-SHA256(pass, salt, 600k), fresh salt, entry-json)
  tag        = HMAC-SHA256(SHA256(utf8(pass)||"agentkey-mac-v1"), "agentkey-v1"||ct)
Tag is verified BEFORE any decrypt attempt; wrong pass or edited bytes -> exit 4.

Commands:
  init                          create vault (0700) + audit log
  add NAME --provider P [--expires ISO] <key on stdin or --key-file 0600)
  get NAME [--fingerprint]      print key (or only its sha256 fingerprint)
  rotate NAME <new key stdin>   rotate; previous key kept in NAME.prev (decryptable)
  list [--json]                 redacted inventory (never key material)
  status [--json]               vault health (schema agentkey.status.v1)
  audit [--json] [--verify]     show / chain-verify audit log
  report [--json]               staleness report; rc 1 = stale(>90d) 2 = expired
Passphrase sources (first hit wins): --pass-file (0600 reqd) · $AGENTKEY_PASS ·
getpass on a tty. Absent everywhere -> exit 3. Empty passphrase refused.
Exit codes: 0 ok · 2 usage · 3 crypto/pass unavailable · 4 integrity · 5 not found · 6 refused.
"""
import base64, getpass, hashlib, hmac as hmac_lib, json, os, shutil, subprocess, sys, time, datetime

ITER = 600_000
CIPHER_CONST = "aes-256-cbc+pbkdf2-sha256"
VAULT_SCHEMA = "agentkey.entry.v1"


def home():
    return os.environ.get("AGENTKEY_HOME") or os.path.expanduser("~/.agentkey")


class AKError(Exception):
    def __init__(self, msg, rc):
        super().__init__(msg); self.rc = rc


def openssl_bin():
    over = os.environ.get("AGENTKEY_OPENSSL_BIN", "").strip()
    if over:
        return over if os.path.isfile(over) else None
    return shutil.which("openssl")


def need_openssl():
    if not openssl_bin():
        raise AKError("openssl binary not found — vault stays read-only; nothing stored (honest failure, never unencrypted noise)", 3)


def get_pass(a):
    if getattr(a, "pass_file", None):
        pf = a.pass_file
        mode = os.stat(pf).st_mode & 0o777
        if mode & 0o077:
            raise AKError(f"--pass-file {pf} has mode {oct(mode)} — chmod 600 required (refusing)", 3)
        with open(pf, "rb") as f:
            p = f.read()
    elif os.environ.get("AGENTKEY_PASS"):
        p = os.environ["AGENTKEY_PASS"].encode()
    elif sys.stdin.isatty():
        p = getpass.getpass("vault passphrase: ").encode()
    else:
        raise AKError("no passphrase available (set AGENTKEY_PASS or --pass-file; tty would prompt)", 3)
    if not p.strip():
        raise AKError("empty passphrase refused", 3)
    return p.rstrip(b"\n")


def _openssl_fd(argv_prefix, pass_bytes, data, decrypt=False):
    r, w = os.pipe()
    os.write(w, pass_bytes); os.close(w)
    argv = ([openssl_bin(), "enc"] + (["-d"] if decrypt else [])
            + ["-aes-256-cbc", "-pbkdf2", "-iter", str(ITER), "-salt", "-base64",
               "-pass", f"fd:{r}"])
    # scrub AGENTKEY_PASS from the cipher subprocess env — children must not
    # inherit the master passphrase (e.g. `ps -efww` reads env blocks on Linux)
    env = {k: v for k, v in os.environ.items() if k != "AGENTKEY_PASS"}
    p = subprocess.run(argv + argv_prefix, input=data, capture_output=True,
                       pass_fds=(r,), env=env)
    os.close(r)
    if p.returncode != 0:
        raise AKError("openssl cipher failed" + (" (decrypt: wrong pass or corrupt)" if decrypt else ""), 4)
    return p.stdout


def mac_key(pass_bytes):
    """Domain-separated raw 32-byte MAC key. Computation stays in-process:
    passing it to openssl argv would leak it via /proc/ps/auditd (fixed v2.0.0
    review finding)."""
    return hashlib.sha256(b"agentkey-mac-v1||" + pass_bytes).digest()


def tag_of(pass_bytes, mac_input):
    return base64.b64encode(
        hmac_lib.new(mac_key(pass_bytes), mac_input, hashlib.sha256).digest()).decode()


def _mac_input(blob):
    """Authenticate the FULL blob (metadata + ct), not just ct — a mutated
    cipher name or iteration count must invalidate the entry too."""
    return (b"agentkey-v1"
            + b"|v=" + str(blob.get("v", "")).encode()
            + b"|cipher=" + blob.get("cipher", "").encode()
            + b"|iter=" + str(blob.get("iter", "")).encode()
            + b"|ct=" + blob.get("ct", "").encode())


def encrypt_entry(pass_bytes, obj):
    raw = json.dumps(obj, ensure_ascii=False, separators=(",", ":")).encode()
    ct = _openssl_fd([], pass_bytes, raw)
    blob = {"v": 1, "cipher": CIPHER_CONST, "iter": ITER,
            "ct": ct.decode().strip()}
    blob["tag"] = tag_of(pass_bytes, _mac_input(blob))
    return blob


def decrypt_entry(pass_bytes, blob):
    if (not isinstance(blob.get("ct"), str) or not blob["ct"].strip()
            or blob.get("cipher") != CIPHER_CONST
            or blob.get("iter") != ITER or blob.get("v") != 1):
        raise AKError("malformed v1 vault entry (cipher/iter/ct) — refusing", 4)
    expect = tag_of(pass_bytes, _mac_input(blob))
    got = blob.get("tag", "")
    if not got or not hmac_eq(expect, got):
        raise AKError("integrity tag mismatch — passphrase wrong or vault entry tampered (refusing to decrypt)", 4)
    ct = blob["ct"].encode() + b"\n"
    raw = _openssl_fd([], pass_bytes, ct, decrypt=True)
    return json.loads(raw.decode())


def hmac_eq(a, b):
    return hmac_lib.compare_digest(str(a), str(b))


def _hmac_eq_fallback(a, b):
    a, b = str(a), str(b)
    if len(a) != len(b):
        return False
    acc = 0
    for x, y in zip(a, b):
        acc |= ord(x) ^ ord(y)
    return acc == 0


def fingerprint(key_bytes):
    return hashlib.sha256(key_bytes).hexdigest()[:16]


def path_of(name, prev=False):
    return os.path.join(home(), "vault", name + (".prev.enc.json" if prev else ".enc.json"))


def read_secret(a):
    if getattr(a, "key_file", None):
        kf = a.key_file
        if os.stat(kf).st_mode & 0o777 != 0o600:
            raise AKError(f"--key-file {kf} must be mode 600 (refusing)", 6)
        with open(kf, "rb") as f:
            return f.read().strip()
    if sys.stdin.isatty():
        return getpass.getpass("key: ").encode().strip()
    return sys.stdin.buffer.read().strip()


def ensure_vault(init=False):
    vdir = os.path.join(home(), "vault")
    if init:
        os.makedirs(vdir, mode=0o700, exist_ok=True)
        try:
            os.chmod(vdir, 0o700); os.chmod(home(), 0o700)
        except OSError:
            pass
    if not os.path.isdir(vdir):
        raise AKError("vault not initialized — run: agentkey.py init", 5)


AUDIT = lambda: os.path.join(home(), "audit.jsonl")


def audit(action, name, provider, fp, detail=""):
    ensure_vault()
    entries = audit_read()
    prev = entries[-1]["hash"] if entries else "0" * 64
    rec = {"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "action": action, "name": name, "provider": provider,
           "fp": fp, "actor": os.environ.get("AGENTKEY_ACTOR", "skill-agentkey"),
           "detail": detail, "prev": prev}
    rec["hash"] = hashlib.sha256(
        json.dumps(rec, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    with open(AUDIT(), "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    os.chmod(AUDIT(), 0o600)                    # beat umask (review C1)


def audit_read():
    if not os.path.exists(AUDIT()):
        return []
    out = []
    with open(AUDIT(), encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if ln:
                out.append(json.loads(ln))
    return out


def audit_verify():
    bad = []
    prev = "0" * 64
    for i, rec in enumerate(audit_read()):
        h = rec.pop("hash", None)
        calc = hashlib.sha256(
            json.dumps(rec, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
        if rec.get("prev") != prev or calc != h:
            bad.append(i)
        prev = h or prev
    return bad


def days_old(ts):
    try:
        t = datetime.datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
        if t.tzinfo is None:
            t = t.replace(tzinfo=datetime.timezone.utc)   # naive ISO date -> treat as UTC
        return (datetime.datetime.now(datetime.timezone.utc) - t).total_seconds() / 86400
    except Exception:
        return None


def load_meta_list():
    vdir = os.path.join(home(), "vault")
    out = {}
    if os.path.isdir(vdir):
        for fn in sorted(os.listdir(vdir)):
            if fn.endswith(".enc.json") and not fn.endswith(".prev.enc.json"):
                name = fn[:-len(".enc.json")]
                out[name] = os.path.join(vdir, fn)
    return out


def cmd_init(a):
    need_openssl()
    ensure_vault(init=True)
    if not os.path.exists(AUDIT()):
        open(AUDIT(), "a").close(); os.chmod(AUDIT(), 0o600)
    audit("init", "-", "-", "-", "vault initialized")
    print(json.dumps({"schema": "agentkey.status.v1", "vault": home(),
                      "initialized": True, "encrypted": True}, indent=2))
    return 0


def cmd_add(a):
    need_openssl()
    pw = get_pass(a); ensure_vault()
    if not a.name or "/" in a.name or a.name.startswith(".") or len(a.name) > 64:
        raise AKError("bad name (1–64 chars, no slash, no leading dot)", 2)
    if os.path.exists(path_of(a.name)):
        raise AKError(f"{a.name!r} already exists — use rotate", 6)
    key = read_secret(a)
    if not key:
        raise AKError("empty key refused", 6)
    now_iso = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    obj = {**{"schema": VAULT_SCHEMA, "name": a.name, "provider": a.provider or "",
              "created": now_iso, "rotated": now_iso, "rotations": 0,
              "expires": a.expires}, "key": key.decode("utf-8", errors="strict") if is_utf8(key) else key.hex()}
    if not is_utf8(key):
        obj["encoding"] = "hex"
    blob = encrypt_entry(pw, obj)
    with open(path_of(a.name), "w", encoding="utf-8") as f:
        json.dump(blob, f, ensure_ascii=False, indent=1)
    os.chmod(path_of(a.name), 0o600)
    audit("add", a.name, obj["provider"], fingerprint(key))
    print(json.dumps({"schema": "agentkey.status.v1", "added": a.name,
                      "fp": fingerprint(key), "encrypted": True}, indent=2))
    return 0


def is_utf8(b):
    try:
        b.decode(); return True
    except UnicodeDecodeError:
        return False


def cmd_get(a):
    pw = get_pass(a); ensure_vault()
    pth = path_of(a.name)
    if not os.path.exists(pth):
        raise AKError(f"no such key: {a.name!r}", 5)
    obj = decrypt_entry(pw, json.load(open(pth)))
    key = (bytes.fromhex(obj["key"]) if obj.get("encoding") == "hex"
           else obj["key"].encode())
    if a.fingerprint:
        print(json.dumps({"name": a.name, "fp": fingerprint(key)}, indent=2))
    else:
        sys.stdout.write(key.decode("utf-8", errors="replace") + "\n")
    audit("get", a.name, obj.get("provider", ""), fingerprint(key),
          "fingerprint-only" if a.fingerprint else "revealed")
    return 0


def cmd_rotate(a):
    need_openssl()
    pw = get_pass(a); ensure_vault()
    pth = path_of(a.name)
    if not os.path.exists(pth):
        raise AKError(f"no such key: {a.name!r}", 5)
    obj = decrypt_entry(pw, json.load(open(pth)))
    new = read_secret(a)
    if not new:
        raise AKError("empty key refused", 6)
    old_key = (bytes.fromhex(obj["key"]) if obj.get("encoding") == "hex" else obj["key"].encode())
    prev_obj = dict(obj); prev_obj["kept_as"] = "prev"; prev_obj["rotations"] = obj.get("rotations", 0)
    prev_obj["retired"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with open(path_of(a.name, prev=True), "w", encoding="utf-8") as f:
        json.dump(encrypt_entry(pw, prev_obj), f, ensure_ascii=False, indent=1)
    os.chmod(path_of(a.name, prev=True), 0o600)
    obj["key"] = new.decode() if is_utf8(new) else new.hex()
    if not is_utf8(new):
        obj["encoding"] = "hex"
    elif "encoding" in obj:
        obj.pop("encoding")
    obj["rotations"] = obj.get("rotations", 0) + 1
    obj["rotated"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    if a.expires is not None:
        obj["expires"] = a.expires
    with open(pth, "w", encoding="utf-8") as f:
        json.dump(encrypt_entry(pw, obj), f, ensure_ascii=False, indent=1)
    os.chmod(pth, 0o600)
    audit("rotate", a.name, obj.get("provider", ""), fingerprint(new),
          f"rotations={obj['rotations']}")
    print(json.dumps({"schema": "agentkey.status.v1", "rotated": a.name,
                      "rotations": obj["rotations"], "new_fp": fingerprint(new),
                      "prev_kept": True}, indent=2))
    return 0


def cmd_list(a):
    pw = get_pass(a); ensure_vault()
    rows = []
    for name, p in load_meta_list().items():
        try:
            obj = decrypt_entry(pw, json.load(open(p)))
            key = (bytes.fromhex(obj["key"]) if obj.get("encoding") == "hex" else obj["key"].encode())
            rows.append({"name": name, "provider": obj.get("provider", ""),
                         "fp": fingerprint(key),
                         "created": obj.get("created"), "rotated": obj.get("rotated"),
                         "rotations": obj.get("rotations", 0), "expires": obj.get("expires"),
                         "age_days": round(days_old(obj.get("rotated")) or -1, 1),
                         "has_prev": os.path.exists(path_of(name, prev=True))})
        except AKError:
            rows.append({"name": name, "error": "integrity/unreadable"})
    out = {"schema": "agentkey.list.v1", "count": len(rows), "entries": rows}
    if a.json:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        for r in rows:
            print(f"{r.get('name','?')}: provider={r.get('provider','?')} fp={r.get('fp','-')} "
                  f"rotations={r.get('rotations','-')} age_d={r.get('age_days','-')} expires={r.get('expires','-')}"
                  + (" [ERROR]" if r.get("error") else ""))
    return 0


def cmd_status(a):
    need_openssl()
    ensure_vault()
    entries = load_meta_list()
    bad = audit_verify()
    ap = AUDIT()
    mode_ok = True
    if os.path.exists(ap):
        mode_ok = (os.stat(ap).st_mode & 0o077) == 0
        if not mode_ok:
            os.chmod(ap, 0o600)
    out = {"schema": "agentkey.status.v1", "vault": home(),
           "openssl": openssl_bin() is not None, "iter": ITER,
           "keys": len(entries), "audit_entries": len(audit_read()),
           "audit_mode_hardened": mode_ok,
           "audit_integrity": "ok" if not bad else f"TAMPER lines {bad}"}
    print(json.dumps(out, indent=2))
    return 0 if not bad else 4


def cmd_audit(a):
    ensure_vault()
    rows = audit_read()
    if a.verify:
        bad = audit_verify()
        print(json.dumps({"schema": "agentkey.audit.v1", "chain_ok": not bad,
                          "entries": len(rows), "bad_lines": bad}, indent=2))
        return 0 if not bad else 4
    if a.json:
        print(json.dumps({"schema": "agentkey.audit.v1", "entries": rows}, indent=2, ensure_ascii=False))
    else:
        for r in rows:
            print(f"{r['ts']} {r['action']:<7} {r['name']:<16} fp={r['fp']} {r['detail']}")
    return 0


def cmd_report(a):
    pw = get_pass(a); ensure_vault()
    stale, expired, ok_names = [], [], []
    for name, p in load_meta_list().items():
        try:
            obj = decrypt_entry(pw, json.load(open(p)))
        except AKError:
            continue
        exp = obj.get("expires")
        if exp and days_old(exp) > 0:
            expired.append(name); continue
        age = days_old(obj.get("rotated"))
        if age is not None and age > 90:
            stale.append(name)
        else:
            ok_names.append(name)
    verdict = "EXPIRED KEYS PRESENT" if expired else ("STALE KEYS (>90d)" if stale else "ALL KEYS FRESH")
    out = {"schema": "agentkey.report.v1", "verdict": verdict,
           "stale": stale, "expired": expired, "fresh": ok_names,
           "threshold_stale_days": 90}
    print(json.dumps(out, indent=2))
    return 2 if expired else (1 if stale else 0)


def main():
    import argparse
    ap = argparse.ArgumentParser(prog="agentkey.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pass-file", help="file holding the vault passphrase (MUST be mode 600)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init")
    p = sub.add_parser("add"); p.add_argument("name"); p.add_argument("--provider", default="")
    p.add_argument("--expires", default=None, help="ISO date, e.g. 2027-01-01")
    p.add_argument("--key-file", help="read key from a 0600 file instead of stdin")
    p = sub.add_parser("get"); p.add_argument("name"); p.add_argument("--fingerprint", action="store_true")
    p = sub.add_parser("rotate"); p.add_argument("name"); p.add_argument("--expires", default=None)
    p = sub.add_parser("list"); p.add_argument("--json", action="store_true")
    sub.add_parser("status")
    p = sub.add_parser("audit"); p.add_argument("--json", action="store_true"); p.add_argument("--verify", action="store_true")
    p = sub.add_parser("report"); p.add_argument("--json", action="store_true")
    a = ap.parse_args()
    try:
        return {"init": cmd_init, "add": cmd_add, "get": cmd_get, "rotate": cmd_rotate,
                "list": cmd_list, "status": cmd_status, "audit": cmd_audit,
                "report": cmd_report}[a.cmd](a)
    except AKError as e:
        print(f"agentkey: {e}", file=sys.stderr)
        return e.rc
    except BrokenPipeError:
        return 0


if __name__ == "__main__":
    sys.exit(main())
