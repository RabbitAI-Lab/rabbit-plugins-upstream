#!/usr/bin/env python3
"""
swr_paste — off-box manifest sync for snapshot-wipe-resilience (v1.4.1).

The manifest is itself workspace state: when the sandbox wipes, the very file
that knows how to rebuild everything can vanish too. This pushes it to paste
hosts and pulls it back from a short URL.

SECURITY MODEL
  * Encryption is ON BY DEFAULT when an identity exists (hybrid PQ to yourself);
    publishing in the clear requires --plaintext-ok.
  * Redaction (secrets -> ${ENV_VAR}) protects unencrypted pushes. It is skipped
    for encrypted payloads, because rewriting the body would invalidate the
    manifest signature.
  * Pushed manifests keep their signatures. swr.py REFUSES to execute recipes
    from a manifest whose signature does not verify, so a hijacked paste cannot
    run code on your box.
"""

import argparse
import base64
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zlib

try:
    import swr_crypto as _pq
except Exception:
    _pq = None

HOME = os.path.expanduser("~")
SWR_DIR = os.path.join(HOME, ".swr")
DEFAULT_MANIFEST = os.path.join(SWR_DIR, "manifest.json")
PIN_FILE = os.path.join(SWR_DIR, "remote.json")
UA = "swr-snapshot-wipe-resilience/1.4.1"
PAYLOAD_MAX = 64 * 1024 * 1024

SECRET_PATTERNS = [
    (re.compile(r"\bclh_[A-Za-z0-9_\-]{20,}"),            "CLAWHUB_TOKEN"),
    (re.compile(r"\bclaw_sk_[A-Za-z0-9]{20,}"),           "CLAWARENA_API_KEY"),
    (re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}"),         "GITHUB_TOKEN"),
    (re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_\-]{20,}"),   "OPENAI_API_KEY"),
    (re.compile(r"\bhf_[A-Za-z0-9]{30,}"),                "HF_TOKEN"),
    (re.compile(r"\bxox[baprs]-[A-Za-z0-9\-]{10,}"),      "SLACK_TOKEN"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"),                 "AWS_ACCESS_KEY_ID"),
    (re.compile(r"\bAIza[0-9A-Za-z_\-]{35}"),             "GOOGLE_API_KEY"),
    (re.compile(r"\bglpat-[A-Za-z0-9_\-]{20,}"),          "GITLAB_TOKEN"),
    (re.compile(r"\bdop_v1_[a-f0-9]{64}"),                "DIGITALOCEAN_TOKEN"),
    (re.compile(r"\bnpm_[A-Za-z0-9]{36}"),                "NPM_TOKEN"),
    (re.compile(r"\b[A-Za-z0-9_\-]{20,}\.[A-Za-z0-9_\-]{20,}\.[A-Za-z0-9_\-]{20,}\b"),
     "JWT_TOKEN"),
]
URL_CRED = re.compile(r"\b([a-z][a-z0-9+.\-]*://)([^/\s:@]+):([^/\s@]{4,})@")
PEM_BLOCK = re.compile(
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----", re.S)
ENV_ASSIGN = re.compile(r"\b([A-Z][A-Z0-9_]{2,})\s*=\s*['\"]?([A-Za-z0-9_\-/+=.]{16,})['\"]?")


def eprint(*a):
    print(*a, file=sys.stderr)


def shannon(s):
    if not s:
        return 0.0
    freq = {c: s.count(c) / len(s) for c in set(s)}
    return -sum(p * math.log2(p) for p in freq.values())


def redact(text, paranoid=False):
    """-> (clean, [(var, preview)], [suspicious])"""
    found, suspicious = [], []
    for m in PEM_BLOCK.findall(text):
        found.append(("PRIVATE_KEY_PEM", "-----BEGIN…KEY-----"))
        text = text.replace(m, "${PRIVATE_KEY_PEM}")

    def _url(m):
        found.append(("URL_PASSWORD", f"{m.group(1)}{m.group(2)}:****@"))
        return f"{m.group(1)}{m.group(2)}:${{URL_PASSWORD}}@"
    text = URL_CRED.sub(_url, text)

    for pat, var in SECRET_PATTERNS:
        for m in sorted(set(pat.findall(text)), key=len, reverse=True):
            if not isinstance(m, str):
                continue
            found.append((var, f"{m[:8]}…{m[-4:]}"))
            text = text.replace(m, "${%s}" % var)

    for var, val in ENV_ASSIGN.findall(text):
        if "${" in val or val.startswith("http"):
            continue
        if len(val) >= 20 and shannon(val) >= 4.0:
            suspicious.append((var, f"{val[:6]}…{val[-4:]}", round(shannon(val), 2)))
            if paranoid:
                text = text.replace(val, "${%s}" % var)
                found.append((var, f"{val[:6]}…{val[-4:]}"))
    return text, found, suspicious


def diff(a, b):
    import difflib
    return "\n".join(difflib.unified_diff(a.splitlines(), b.splitlines(),
                                          "local", "to-upload", lineterm="", n=1))


# ───────────────────────────────────────────────────────────────── transport

def _open(req, retries=3):
    delay = 2
    for i in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                return r.read().decode("utf-8", "replace").strip()
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and i < retries:
                ra = e.headers.get("Retry-After")
                w = int(ra) if (ra or "").isdigit() else delay
                eprint(f"  http {e.code}, retry in {w}s ({i+1}/{retries})")
                time.sleep(w)
                delay = min(delay * 2, 30)
                continue
            body = ""
            try:
                body = e.read().decode("utf-8", "replace")[:200]
            except Exception:
                pass
            raise RuntimeError(f"HTTP {e.code} {e.reason}"
                               f"{': ' + body if body else ''}") from None
        except urllib.error.URLError as e:
            if i < retries:
                time.sleep(delay)
                delay = min(delay * 2, 30)
                continue
            raise RuntimeError(f"network unreachable: {e.reason}") from None
    raise RuntimeError("retries exhausted")


def post(url, data=None, headers=None, method=None):
    return _open(urllib.request.Request(
        url, data=data, method=method,
        headers={"User-Agent": UA, **(headers or {})}))


def fetch(url):
    return post(url)


# ────────────────────────────────────────────────────────────────── backends

def up_pastebin(text, name, expire, private):
    key = os.environ.get("PASTEBIN_API_KEY")
    if not key:
        raise RuntimeError("PASTEBIN_API_KEY not set")
    body = {"api_dev_key": key, "api_option": "paste", "api_paste_code": text,
            "api_paste_name": name, "api_paste_format": "json",
            "api_paste_private": "1", "api_paste_expire_date": expire or "1W"}
    uk = os.environ.get("PASTEBIN_USER_KEY")
    if uk:
        body["api_user_key"] = uk
        if private:
            body["api_paste_private"] = "2"
    out = post("https://pastebin.com/api/api_post.php",
               urllib.parse.urlencode(body).encode())
    if not out.startswith("http"):
        raise RuntimeError(f"pastebin: {out}")
    return out


def raw_pastebin(u):
    return f"https://pastebin.com/raw/{u.rstrip('/').split('/')[-1]}"


def up_dpaste(text, name, expire, private):
    days = {"10M": 1, "1H": 1, "1D": 1, "1W": 7, "2W": 14, "1M": 30, "N": 365}
    return post("https://dpaste.com/api/v2/", urllib.parse.urlencode({
        "content": text, "syntax": "json", "title": name,
        "expiry_days": days.get(expire or "1W", 7)}).encode())


def raw_dpaste(u):
    return u.rstrip("/") + ".txt"


def up_pasters(text, name, expire, private):
    return post("https://paste.rs/", text.encode())


def raw_pasters(u):
    return u


BACKENDS = {
    "pastebin": (up_pastebin, raw_pastebin, "needs PASTEBIN_API_KEY"),
    "dpaste":   (up_dpaste,   raw_dpaste,   "keyless"),
    "pasters":  (up_pasters,  raw_pasters,  "keyless"),
}
ORDER = ["pastebin", "dpaste", "pasters"]


def available():
    return ORDER if os.environ.get("PASTEBIN_API_KEY") else ORDER[1:]


WORDS = ("amber anchor bishop cargo cobalt copper delta ember falcon garnet "
         "harbor indigo jasper kernel lumen mosaic nectar onyx pilot quartz "
         "raven summit tundra umber vector walnut xenon yonder zephyr basalt "
         "cedar dune").split()


def mnemonic(s, n=4):
    h = hashlib.sha256(s.encode()).digest()
    return "-".join(WORDS[b % len(WORDS)] for b in h[:n])


def qr(data):
    if shutil.which("qrencode"):
        try:
            return subprocess.run(["qrencode", "-t", "ANSIUTF8", data],
                                  capture_output=True, text=True,
                                  timeout=15).stdout
        except Exception:
            pass
    return None


# ─────────────────────────────────────────────────────────── payload wrapping

def wrap(text, compress, encrypt_to, pq_to=None, no_sign=False):
    """pq_to -> hybrid post-quantum E2E (X25519+ML-KEM-1024, ML-DSA-87 signed)."""
    meta = {"swr": 1, "enc": None, "z": False}
    body = text
    if pq_to:
        if _pq is None:
            raise RuntimeError("swr_crypto.py not importable — cannot use --pq-to")
        if compress:
            body = base64.b64encode(zlib.compress(text.encode(), 9)).decode()
            meta["z"] = True
        peer = _pq.load_peer(pq_to)
        env = _pq.encrypt(body.encode(), peer, sign=not no_sign)
        meta["enc"] = "swr-hybrid-v1"
        meta["to"] = peer["fingerprint"]
        meta["body"] = json.dumps(env, separators=(",", ":"))
        return json.dumps(meta, separators=(",", ":"))
    if encrypt_to:
        if not shutil.which("age"):
            raise RuntimeError("age not installed — cannot encrypt")
        r = subprocess.run(["age", "-r", encrypt_to, "-a"],
                           input=text.encode(), capture_output=True, timeout=60)
        if r.returncode:
            raise RuntimeError(f"age failed: {r.stderr.decode()[:200]}")
        meta["enc"] = "age"
        meta["body"] = r.stdout.decode()
        return json.dumps(meta, separators=(",", ":"))
    if compress:
        meta["z"] = True
        meta["body"] = base64.b64encode(zlib.compress(text.encode(), 9)).decode()
        return json.dumps(meta, separators=(",", ":"))
    return text


def _bounded_decompress(b64):
    """Decompress with a hard cap: a paste payload is attacker-supplied."""
    raw = base64.b64decode(b64)
    d = zlib.decompressobj()
    out = d.decompress(raw, PAYLOAD_MAX)
    if d.unconsumed_tail:
        raise RuntimeError(f"payload expands beyond {PAYLOAD_MAX:,}B — "
                           f"refusing (possible decompression bomb)")
    return out.decode()


def unwrap(raw, identity=None, expect_from=None):
    try:
        o = json.loads(raw)
    except json.JSONDecodeError:
        return raw
    if not isinstance(o, dict) or o.get("swr") != 1 or "body" not in o:
        return raw
    if o.get("enc") == "swr-hybrid-v1":
        if _pq is None:
            raise RuntimeError("payload is hybrid-PQ encrypted but swr_crypto.py "
                               "is not importable")
        pt, hdr, sender = _pq.decrypt(json.loads(o["body"]), expect_from)
        inner = pt.decode()
        if o.get("z"):
            inner = _bounded_decompress(inner)
        eprint(f"  decrypted: {hdr['suite']} from "
               f"{sender or 'ANONYMOUS (unsigned)'}")
        return inner
    if o.get("enc") == "age":
        if not shutil.which("age"):
            raise RuntimeError("payload is age-encrypted but `age` is not installed")
        cmd = ["age", "-d"] + (["-i", identity] if identity else [])
        r = subprocess.run(cmd, input=o["body"].encode(),
                           capture_output=True, timeout=60)
        if r.returncode:
            raise RuntimeError(f"age decrypt failed: {r.stderr.decode()[:200]}")
        return r.stdout.decode()
    if o.get("z"):
        return _bounded_decompress(o["body"])
    return raw


EXPIRY_SECONDS = {"10M": 600, "1H": 3600, "1D": 86400, "1W": 604800,
                  "2W": 1209600, "1M": 2592000, "N": None}


# ─────────────────────────────────────────────────────────────────  commands

def cmd_push(a):
    if not os.path.exists(a.manifest):
        sys.exit(f"no manifest at {a.manifest}")
    raw = open(a.manifest).read()
    try:
        man = json.loads(raw)
    except json.JSONDecodeError as e:
        sys.exit(f"manifest is not valid JSON: {e}")

    if not man.get("_sig"):
        eprint("!! manifest is UNSIGNED — a puller will refuse to run its recipes.")
        eprint("   sign it first:  python3 swr.py sign")
        if not a.allow_unsigned:
            sys.exit("refusing to push unsigned manifest (use --allow-unsigned)")

    # Validate encryption options BEFORE the dry-run exit.
    if a.pq_to and a.encrypt_to:
        sys.exit("--pq-to and --encrypt-to are mutually exclusive; pick one")

    # Default to encryption when an identity exists: a public paste is public.
    if (not a.pq_to and not a.encrypt_to and not a.plaintext_ok
            and _pq is not None):
        try:
            _pq.require_pq()
            has_id = os.path.exists(os.path.join(_pq.ID_DIR, "id.json"))
        except SystemExit:
            has_id = False
        if has_id:
            ident = json.load(open(os.path.join(_pq.ID_DIR, "id.json")))
            self_peer = os.path.join(_pq.PEERS_DIR, "self.json")
            if not os.path.exists(self_peer):
                os.makedirs(_pq.PEERS_DIR, exist_ok=True)
                json.dump(ident, open(self_peer, "w"), indent=2)
            a.pq_to = "self"
            eprint("note: encrypting to your own identity by default (hybrid PQ). "
                   "Use --plaintext-ok to publish unencrypted, or --pq-to <peer>.")

    if a.pq_to:
        if _pq is None:
            sys.exit("--pq-to requires swr_crypto.py alongside this script")
        try:
            _pq.require_pq()
        except SystemExit:
            sys.exit("--pq-to needs OpenSSL >= 3.5 with ML-KEM support")
        pfile = os.path.join(_pq.PEERS_DIR, f"{a.pq_to}.json")
        if not os.path.exists(pfile) and not os.path.exists(a.pq_to):
            known = (sorted(f[:-5] for f in os.listdir(_pq.PEERS_DIR))
                     if os.path.isdir(_pq.PEERS_DIR) else [])
            sys.exit(f"unknown peer '{a.pq_to}'. Known peers: "
                     f"{', '.join(known) if known else '(none)'}\n"
                     f"  add one:  python3 swr_crypto.py peer-add <their.pub> "
                     f"--name <name>")
    if a.encrypt_to and not shutil.which("age"):
        sys.exit("--encrypt-to requires `age` (not installed); "
                 "use --pq-to for built-in hybrid PQ encryption")

    # Encrypted payloads do not need redaction, and redacting would rewrite the
    # signed bytes so the recovered manifest could no longer verify or restore.
    if (a.pq_to or a.encrypt_to) and not a.force_redact:
        a.no_redact = True

    if a.no_redact:
        text, found, susp = raw, [], []
        if not a.pq_to and not a.encrypt_to:
            eprint("!! --no-redact with NO encryption: secrets will be PUBLIC")
    else:
        text, found, susp = redact(raw, a.paranoid)

    if found:
        print("redacted before upload:")
        for var, prev in sorted(set(found)):
            print(f"  {prev}  ->  ${{{var}}}")
    if susp:
        print("\nhigh-entropy strings (possible unknown secrets):")
        for var, prev, ent in susp:
            print(f"  {var}={prev}  entropy {ent}" +
                  ("  [redacted]" if a.paranoid else "  [NOT redacted]"))
        if not a.paranoid and a.strict:
            sys.exit("--strict: refusing to push with unrecognised high-entropy strings")
    if a.show_diff and not a.no_redact:
        d = diff(raw, text)
        print("\n--- redaction diff ---")
        print(d if d.strip() else "(no changes)")
        print("--- end diff ---")
    if a.dry_run:
        extra = (f", hybrid-PQ encrypted to '{a.pq_to}'" if a.pq_to else
                 f", age-encrypted to {a.encrypt_to}" if a.encrypt_to else "")
        print(f"\ndry-run: would upload {len(text)} bytes{extra}, not sending")
        return 0

    digest = hashlib.sha256(text.encode()).hexdigest()
    try:
        payload = wrap(text, a.compress, a.encrypt_to, a.pq_to, a.pq_no_sign)
    except RuntimeError as e:
        sys.exit(f"encryption failed: {e}")
    payload_digest = hashlib.sha256(payload.encode()).hexdigest()
    if a.pq_to:
        print(f"\nhybrid PQ encrypted -> {a.pq_to}  "
              f"({len(text)} -> {len(payload)} bytes)")
        print("  X25519 + ML-KEM-1024, ChaCha20+HMAC-SHA512/256"
              + ("" if a.pq_no_sign else ", signed ML-DSA-87"))
    elif a.compress:
        print(f"\ncompressed {len(text)} -> {len(payload)} bytes "
              f"({100*len(payload)/max(1,len(text)):.0f}%)")

    targets = [a.backend] if a.backend else available()
    results, errs = [], []
    for name in targets:
        up, rawf, _ = BACKENDS[name]
        try:
            url = up(payload, a.title, a.expire, not a.public)
            rec = {"backend": name, "url": url, "raw": rawf(url)}
            if a.verify:
                got = fetch(rec["raw"])
                # Compare the transport payload, not plaintext: we may have
                # encrypted to a peer whose private key we do not hold.
                if got.strip() != payload.strip() and \
                        hashlib.sha256(got.encode()).hexdigest() != payload_digest:
                    errs.append(f"{name}: round-trip payload mismatch")
                    continue
                rec["verified"] = True
            results.append(rec)
            print(f"\npushed via {name}\n  url  {url}\n  raw  {rec['raw']}"
                  + ("\n  round-trip verified" if a.verify else ""))
            if not a.mirror:
                break
        except Exception as e:
            errs.append(f"{name}: {e}")
            eprint(f"  {name} failed: {e}")
    if not results:
        sys.exit("all backends failed:\n  " + "\n  ".join(errs))

    ttl = EXPIRY_SECONDS.get(a.expire or "1W")
    pin = {"pushed_at": int(time.time()),
           "expires_at": int(time.time()) + ttl if ttl else None,
           "sha256": digest, "payload_sha256": payload_digest,
           "bytes": len(text), "redacted": bool(found),
           "encrypted": "swr-hybrid-v1" if a.pq_to else bool(a.encrypt_to),
           "pq_to": a.pq_to or None,
           "compressed": bool(a.compress and not a.pq_to and not a.encrypt_to),
           "signed": bool(man.get("_sig")),
           "mnemonic": mnemonic(results[0]["raw"]),
           "replicas": results}
    os.makedirs(SWR_DIR, exist_ok=True)
    json.dump(pin, open(PIN_FILE, "w"), indent=2)

    print(f"\n  recovery code: {pin['mnemonic']}   (sha256 {digest[:12]}…)")
    if a.qr:
        img = qr(results[0]["raw"])
        print(img if img else "  (install `qrencode` for QR output)")
    print(f"\nrecover with:\n  python3 swr_paste.py pull {results[0]['raw']}")
    if found:
        print("\nset these before restoring:")
        for v in sorted({v for v, _ in found}):
            print(f"  export {v}=...")
    return 0


def cmd_pull(a):
    if not a.url.startswith("http"):
        sys.exit("pass the raw URL (e.g. https://dpaste.com/XXXX.txt)")
    try:
        raw = fetch(a.url)
    except RuntimeError as e:
        msg = str(e)
        if "404" in msg or "410" in msg:
            hint = ("paste not found — it may have expired, or the URL is wrong. "
                    "Check `swr_paste.py status` for a mirror.")
        elif "429" in msg:
            hint = "rate-limited — wait a minute, or pull from a mirror."
        else:
            hint = "check connectivity, or pull from a mirror."
        sys.exit(f"fetch failed: {msg}\n  hint: {hint}")
    try:
        text = unwrap(raw, a.identity, a.pq_from)
    except RuntimeError as e:
        sys.exit(str(e))

    got = hashlib.sha256(text.encode()).hexdigest()
    raw_digest = hashlib.sha256(raw.encode()).hexdigest()
    if a.sha256 and got != a.sha256 and raw_digest != a.sha256:
        sys.exit(f"HASH MISMATCH\n  expected {a.sha256}\n  got      {got}\n"
                 f"  refusing to write — content was altered in transit or at rest")

    try:
        man = json.loads(text)
    except json.JSONDecodeError:
        sys.exit(f"fetched content is not JSON (got {text[:80]!r})")

    if a.expand:
        missing = []

        def sub(m):
            v = os.environ.get(m.group(1))
            if v is None:
                missing.append(m.group(1))
                return m.group(0)
            return v
        text = re.sub(r"\$\{([A-Z_][A-Z0-9_]*)\}", sub, text)
        if missing:
            eprint(f"!! unset, left as placeholders: {', '.join(sorted(set(missing)))}")
        man = json.loads(text)

    dest = a.out or a.manifest
    if os.path.exists(dest) and not a.force:
        sys.exit(f"{dest} exists — use --force to overwrite")
    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    with open(dest, "w") as f:
        json.dump(man, f, indent=2)
        f.write("\n")
    print(f"pulled {len(man.get('entries', []))} entries -> {dest}")
    print(f"  sha256 {got[:16]}…  mnemonic {mnemonic(a.url)}")
    if man.get("_sig"):
        print("  manifest is signed — swr.py will verify before running recipes")
    else:
        print("  !! UNSIGNED — swr.py will refuse to run its recipes")
    print("next: python3 swr.py doctor")
    return 0


def cmd_status(a):
    if not os.path.exists(PIN_FILE):
        print("no remote copy pinned — run: swr_paste.py push")
        return 1
    pin = json.load(open(PIN_FILE))
    print(json.dumps(pin, indent=2))
    if pin.get("expires_at"):
        left = pin["expires_at"] - int(time.time())
        if left < 0:
            print(f"\n!! EXPIRED {-left//3600}h ago — re-push now")
            return 1
        print(f"\nexpires in {left//3600}h {(left%3600)//60}m"
              + ("   <-- renew soon" if left < 86400 else ""))
    ok = 0
    for r in pin.get("replicas", []):
        try:
            raw_live = fetch(r["raw"])
            pd = pin.get("payload_sha256")
            if pd:
                good = hashlib.sha256(raw_live.encode()).hexdigest() == pd
            else:
                good = hashlib.sha256(
                    unwrap(raw_live, a.identity).encode()).hexdigest() == pin.get("sha256")
            print(f"  {r['backend']:<9} {'hash OK' if good else 'HASH DRIFT'}  {r['raw']}")
            ok += good
        except Exception as e:
            print(f"  {r['backend']:<9} unreachable: {e}")
    print(f"\n{ok}/{len(pin.get('replicas', []))} replicas healthy")
    return 0 if ok else 1


def cmd_backends(a):
    print("backend   status   notes")
    for n in ORDER:
        _, _, note = BACKENDS[n]
        st = "ready" if (n != "pastebin" or os.environ.get("PASTEBIN_API_KEY")) else "no key"
        print(f"  {n:<9} {st:<8} {note}")
    print(f"\nauto order: {' -> '.join(available())}")
    print(f"age (encryption): {'available' if shutil.which('age') else 'not installed'}")
    if _pq:
        try:
            _pq.require_pq()
            ok = "available (X25519+ML-KEM-1024, ML-DSA-87)"
        except SystemExit:
            ok = "openssl too old (need >= 3.5)"
    else:
        ok = "swr_crypto.py not importable"
    print(f"hybrid PQ E2E:    {ok}")
    print(f"qrencode:         {'available' if shutil.which('qrencode') else 'not installed'}")
    return 0


def main():
    p = argparse.ArgumentParser(prog="swr_paste", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("-m", "--manifest",
                   default=os.environ.get("SWR_MANIFEST", DEFAULT_MANIFEST))
    p.add_argument("--identity", help="age identity file for decryption")
    s = p.add_subparsers(dest="cmd", required=True)

    q = s.add_parser("push")
    q.add_argument("--backend", choices=list(BACKENDS))
    q.add_argument("--mirror", action="store_true", help="push to ALL backends")
    q.add_argument("--expire", default="1W", help="10M 1H 1D 1W 2W 1M N")
    q.add_argument("--title", default="swr-manifest")
    q.add_argument("--public", action="store_true")
    q.add_argument("--no-redact", action="store_true")
    q.add_argument("--force-redact", action="store_true",
                   help="redact even when encrypting (breaks manifest signature)")
    q.add_argument("--plaintext-ok", action="store_true",
                   help="publish WITHOUT encryption (redaction only)")
    q.add_argument("--paranoid", action="store_true",
                   help="also redact high-entropy strings")
    q.add_argument("--strict", action="store_true")
    q.add_argument("--show-diff", action="store_true")
    q.add_argument("--dry-run", action="store_true")
    q.add_argument("--compress", action="store_true")
    q.add_argument("--encrypt-to", help="age recipient (public key)")
    q.add_argument("--pq-to", help="peer name/file -> hybrid PQ E2E encryption")
    q.add_argument("--pq-no-sign", action="store_true")
    q.add_argument("--verify", action="store_true", default=True)
    q.add_argument("--no-verify", dest="verify", action="store_false")
    q.add_argument("--qr", action="store_true")
    q.add_argument("--allow-unsigned", action="store_true")

    q = s.add_parser("pull")
    q.add_argument("url"); q.add_argument("--out")
    q.add_argument("--force", action="store_true")
    q.add_argument("--expand", action="store_true")
    q.add_argument("--sha256", help="required content hash (fail closed)")
    q.add_argument("--pq-from", help="require this signed PQ sender")

    s.add_parser("status")
    s.add_parser("backends")

    a = p.parse_args()
    return {"push": cmd_push, "pull": cmd_pull,
            "status": cmd_status, "backends": cmd_backends}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
