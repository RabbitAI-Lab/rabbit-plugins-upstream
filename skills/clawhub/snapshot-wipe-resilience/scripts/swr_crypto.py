#!/usr/bin/env python3
"""
swr_crypto — hybrid post-quantum end-to-end encryption for swr manifests (v1.5.6).

WHAT THIS IS
  Authenticated hybrid public-key encryption combining a classical and a
  post-quantum KEM, so the payload stays confidential if *either* primitive
  survives. Same design class as TLS 1.3 X25519MLKEM768 and Signal's PQXDH —
  not a novel scheme. Novel crypto is how you get broken.

CIPHERSUITE  SWR-HYBRID-v1
  KEM-C   X25519            (RFC 7748)      classical ECDH, ephemeral
  KEM-PQ  ML-KEM-1024       (FIPS 203)      lattice KEM, NIST cat. 5
  KDF     HKDF-SHA-512      (RFC 5869)
  AEAD-like ChaCha20 + HMAC-SHA-512/256 encrypt-then-MAC construction
          (ChaCha20 is described in RFC 8439; this is NOT RFC 8439
           ChaCha20-Poly1305, and the composition has not had a formal audit)
  SIG     ML-DSA-87         (FIPS 204)      post-quantum sender auth, cat. 5

  Shared secret = HKDF(ss_x25519 || ss_mlkem || full transcript).
  Both KEM shared secrets contribute to the derived key; this is intended to
  provide hybrid protection, not a formal guarantee that either primitive can
  be broken without consequence. It is not a substitute for a reviewed
  protocol such as TLS or age.

WHY NOT "the #1 most secure encryption"
  No such thing exists. A one-time pad is information-theoretically secure but
  needs a truly random key as long as the message, shared in advance — which is
  the very problem E2E key agreement solves. What is achievable: NIST-standard
  PQ primitives at the highest category, hybridized with a battle-tested
  classical primitive, authenticated, with forward secrecy.

DEPENDENCIES  OpenSSL >= 3.5 (ML-KEM/ML-DSA) + Python stdlib. No pip packages.
"""

import argparse
import base64
import hashlib
import hmac
import json
import os
import secrets
import shutil
import struct
import subprocess
import sys
import tempfile
import time

HOME = os.path.expanduser("~")
SWR_DIR = os.path.join(HOME, ".swr")
# Trust metadata is fixed below the normal private state directory.  Do not
# let a hostile process environment redirect identity or peer files.
ID_DIR = os.path.join(SWR_DIR, "identity")
PEERS_DIR = os.path.join(SWR_DIR, "peers")

SUITE = "SWR-HYBRID-v1"
KDF_INFO = b"swr/hybrid/v1 x25519+mlkem1024 chacha20-hmacsha512256"
MAGIC = b"SWRE1"
MIN_OPENSSL = (3, 5)
MAX_ENVELOPE_B64 = 256 * 1024 * 1024
MAX_HEADER_BYTES = 64 * 1024
MAX_SIGNATURE_BYTES = 16 * 1024


def eprint(*a):
    print(*a, file=sys.stderr)


def die(msg, code=2):
    eprint(f"error: {msg}")
    sys.exit(code)


# ───────────────────────────────────────────────────────────── openssl shim

def ossl(args, inp=None, check=True):
    r = subprocess.run(["openssl", *args], input=inp,
                       capture_output=True, timeout=120)
    if check and r.returncode != 0:
        die(f"openssl {args[0]} failed: {r.stderr.decode()[:300]}")
    return r


def openssl_version():
    out = ossl(["version"]).stdout.decode()
    try:
        nums = out.split()[1].split(".")
        return (int(nums[0]), int(nums[1]))
    except Exception:
        return (0, 0)


def require_pq():
    if not shutil.which("openssl"):
        die("openssl not found — required for ML-KEM/ML-DSA")
    v = openssl_version()
    if v < MIN_OPENSSL:
        die(f"OpenSSL {v[0]}.{v[1]} lacks ML-KEM; need >= 3.5")
    if "ML-KEM-1024" not in ossl(["list", "-kem-algorithms"]).stdout.decode():
        die("this OpenSSL build has no ML-KEM-1024")


def _securedir():
    """Prefer tmpfs so private key material never touches persistent storage."""
    for d in ("/dev/shm", "/run/user/%d" % os.getuid()):
        if os.path.isdir(d) and os.access(d, os.W_OK):
            return d
    return None


def _tmp(data, suffix=""):
    fd, p = tempfile.mkstemp(suffix=suffix, dir=_securedir())
    with os.fdopen(fd, "wb") as f:
        f.write(data)
    return p


def _shred(path):
    """Best-effort overwrite before unlink."""
    try:
        n = os.path.getsize(path)
        with open(path, "r+b", buffering=0) as f:
            f.write(b"\x00" * n)
            f.flush()
            os.fsync(f.fileno())
    except OSError:
        pass
    try:
        os.remove(path)
    except OSError:
        pass


def _private_dir(path):
    if os.path.islink(path):
        die(f"private directory {path} must not be a symlink")
    os.makedirs(path, mode=0o700, exist_ok=True)
    try:
        os.chmod(path, 0o700)
    except OSError:
        pass
    return path


def _private_file(path):
    if os.path.islink(path):
        die(f"private file {path} must not be a symlink")
    try:
        st = os.stat(path)
    except OSError:
        die(f"cannot stat private file {path}")
    if not os.path.isfile(path) or st.st_uid != os.getuid() or st.st_mode & 0o077:
        die(f"private file {path} is not a regular user-owned mode-600 file")


# ─────────────────────────────────────────────────────────────── KDF / AEAD

def hkdf(ikm, salt, info, length=64):
    """RFC 5869 HKDF-SHA512."""
    prk = hmac.new(salt or b"\x00" * 64, ikm, hashlib.sha512).digest()
    out, t, i = b"", b"", 1
    while len(out) < length:
        t = hmac.new(prk, t + info + bytes([i]), hashlib.sha512).digest()
        out += t
        i += 1
    return out[:length]


def chacha20(key, nonce12, data):
    """Stream cipher via OpenSSL (audited impl). counter||nonce = 16-byte IV."""
    iv = (b"\x00\x00\x00\x00" + nonce12).hex()
    return ossl(["enc", "-chacha20", "-K", key.hex(), "-iv", iv], inp=data).stdout


def _macdata(aad, nonce, ct):
    """Length-prefixed so AAD/nonce/ct boundaries cannot be shifted."""
    return (struct.pack(">Q", len(aad)) + aad +
            struct.pack(">Q", len(nonce)) + nonce +
            struct.pack(">Q", len(ct)) + ct)


def seal(key32, aad, plaintext):
    """Encrypt-then-MAC AEAD. Returns nonce||ct||tag."""
    ek = hkdf(key32, b"swr-aead-enc", b"enc", 32)
    mk = hkdf(key32, b"swr-aead-mac", b"mac", 32)
    nonce = secrets.token_bytes(12)
    ct = chacha20(ek, nonce, plaintext)
    tag = hmac.new(mk, _macdata(aad, nonce, ct), hashlib.sha512).digest()[:32]
    return nonce + ct + tag


def unseal(key32, aad, blob):
    if len(blob) < 12 + 32:
        die("ciphertext too short / truncated")
    nonce, ct, tag = blob[:12], blob[12:-32], blob[-32:]
    ek = hkdf(key32, b"swr-aead-enc", b"enc", 32)
    mk = hkdf(key32, b"swr-aead-mac", b"mac", 32)
    want = hmac.new(mk, _macdata(aad, nonce, ct), hashlib.sha512).digest()[:32]
    if not hmac.compare_digest(want, tag):
        die("AUTHENTICATION FAILED — ciphertext was modified, truncated, or the "
            "wrong key was used. Refusing to decrypt.", 3)
    return chacha20(ek, nonce, ct)


# ───────────────────────────────────────────────────────────────── identity

def _write_priv(path, data):
    old = os.umask(0o077)
    try:
        with open(path, "wb") as f:
            f.write(data)
    finally:
        os.umask(old)
    os.chmod(path, 0o600)


def genkey(alg, path):
    r = ossl(["genpkey", "-algorithm", alg, "-outform", "PEM"])
    _write_priv(path, r.stdout)
    return ossl(["pkey", "-in", path, "-pubout", "-outform", "PEM"]).stdout


def fingerprint(pubs):
    h = hashlib.sha512(b"".join(pubs)).digest()[:16]
    b = base64.b32encode(h).decode().rstrip("=").lower()
    return "-".join(b[i:i + 5] for i in range(0, 20, 5))


def cmd_keygen(a):
    require_pq()
    _private_dir(SWR_DIR)
    _private_dir(ID_DIR)
    if os.path.exists(os.path.join(ID_DIR, "id.json")) and not a.force:
        die("identity exists — use --force to replace (old ciphertexts become "
            "undecryptable)")
    x_pub = genkey("X25519", os.path.join(ID_DIR, "x25519.key"))
    k_pub = genkey("ML-KEM-1024", os.path.join(ID_DIR, "mlkem.key"))
    d_pub = genkey("ML-DSA-87", os.path.join(ID_DIR, "mldsa.key"))
    ident = {"suite": SUITE, "created": int(time.time()),
             "name": a.name or os.uname().nodename,
             "x25519": base64.b64encode(x_pub).decode(),
             "mlkem": base64.b64encode(k_pub).decode(),
             "mldsa": base64.b64encode(d_pub).decode()}
    ident["fingerprint"] = fingerprint([x_pub, k_pub, d_pub])
    idpath = os.path.join(ID_DIR, "id.json")
    with open(idpath, "w") as f:
        json.dump(ident, f, indent=2)
    os.chmod(idpath, 0o600)
    pubpath = os.path.join(SWR_DIR, "public-id.json")
    os.makedirs(SWR_DIR, exist_ok=True)
    with open(pubpath, "w") as f:
        json.dump(ident, f, indent=2)
    print(f"identity created  ({SUITE})")
    print(f"  fingerprint  {ident['fingerprint']}")
    print(f"  private keys {ID_DIR}/  (mode 600 — never share, never push)")
    print(f"  public id    {pubpath}")
    return 0


def load_identity():
    p = os.path.join(ID_DIR, "id.json")
    if not os.path.exists(p):
        die("no identity — run: swr_crypto.py keygen")
    _private_file(p)
    for name in ("x25519.key", "mlkem.key", "mldsa.key"):
        _private_file(os.path.join(ID_DIR, name))
    try:
        ident = json.load(open(p, encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        die(f"identity is not valid JSON: {e}")
    if not isinstance(ident, dict) or ident.get("suite") != SUITE:
        die("identity has an unsupported suite")
    return ident


def _terminal_safe(text):
    """Keep QR output printable; never pass terminal control bytes through."""
    return "".join(ch for ch in text if ch == "\n" or ch.isprintable())


def cmd_export(a):
    ident = load_identity()
    if a.qr and shutil.which("qrencode"):
        blob = base64.b64encode(json.dumps(ident).encode()).decode()
        r = subprocess.run(["qrencode", "-t", "UTF8", blob],
                           capture_output=True, text=True, timeout=15)
        print(_terminal_safe(r.stdout))
    print(json.dumps(ident, indent=2))
    eprint(f"\nfingerprint: {ident['fingerprint']}  "
           f"<- verify this out-of-band before trusting")
    return 0


def _safe_peer_name(name):
    return (isinstance(name, str) and 1 <= len(name) <= 96 and
            all(c.isalnum() or c in "._+-" for c in name) and name not in (".", ".."))


def cmd_peer_add(a):
    _private_dir(PEERS_DIR)
    raw = open(a.file).read() if a.file else sys.stdin.read()
    try:
        peer = json.loads(raw)
    except json.JSONDecodeError:
        try:
            peer = json.loads(base64.b64decode(raw.strip()))
        except Exception:
            die("not a valid public id (expect JSON or base64 JSON)")
    for k in ("x25519", "mlkem", "mldsa"):
        if k not in peer:
            die(f"public id missing '{k}'")
        try:
            raw_k = base64.b64decode(peer[k], validate=True)
        except Exception:
            die(f"field '{k}' is not valid base64")
        if not raw_k.startswith(b"-----BEGIN PUBLIC KEY-----"):
            die(f"field '{k}' is not a PEM public key")
    # Parse each key with the expected algorithm: accepting garbage here
    # produced a raw OpenSSL error much later, at encrypt time.
    for k, want in (("x25519", "X25519"), ("mlkem", "ML-KEM-1024"),
                    ("mldsa", "ML-DSA-87")):
        f = _tmp(base64.b64decode(peer[k]), ".pem")
        try:
            r = ossl(["pkey", "-pubin", "-in", f, "-noout", "-text"], check=False)
            if r.returncode != 0:
                die(f"field '{k}' is not a parseable public key")
            txt = r.stdout.decode(errors="replace")
            if want.lower().replace("-", "") not in txt.lower().replace("-", ""):
                head = txt.splitlines()[0] if txt else "?"
                die(f"field '{k}' is the wrong algorithm "
                    f"(expected {want}, got: {head.strip()[:60]})")
        finally:
            _shred(f)
    fp = fingerprint([base64.b64decode(peer[k])
                      for k in ("x25519", "mlkem", "mldsa")])
    if peer.get("fingerprint") and peer["fingerprint"] != fp:
        die(f"FINGERPRINT MISMATCH: file says {peer['fingerprint']}, computed {fp}")
    peer["fingerprint"] = fp
    name = a.name or peer.get("name") or fp[:11]
    if not _safe_peer_name(name):
        die("peer name must contain only letters, numbers, '.', '_' '+' or '-' (max 96)")
    peerpath = os.path.join(PEERS_DIR, f"{name}.json")
    if os.path.lexists(peerpath):
        if os.path.islink(peerpath):
            die(f"refusing to replace symlinked peer file {peerpath}")
        if not a.force:
            die(f"peer '{name}' already exists; review fingerprints and use "
                "--force to replace it")
        try:
            with open(peerpath, encoding="utf-8") as f:
                old = json.load(f)
            atomic_json(peerpath + ".previous", old, 0o600)
            eprint(f"replacing peer '{name}': old fingerprint "
                   f"{old.get('fingerprint', '?')} -> new {fp}; "
                   f"backup {peerpath}.previous")
        except (OSError, json.JSONDecodeError) as ex:
            die(f"cannot preserve existing peer '{name}': {ex}")
    atomic_json(peerpath, peer, 0o600)
    print(f"added peer '{name}'\n  fingerprint {fp}")
    print("  VERIFY this fingerprint with the peer over a second channel "
          "(voice/in person) before sending secrets.")
    return 0


def cmd_peer_list(a):
    if not os.path.isdir(PEERS_DIR):
        print("no peers")
        return 0
    for fn in sorted(os.listdir(PEERS_DIR)):
        if not fn.endswith(".json"):
            continue
        try:
            with open(os.path.join(PEERS_DIR, fn), encoding="utf-8") as f:
                p = json.load(f)
            if not isinstance(p, dict):
                raise ValueError("not an object")
            print(f"  {fn[:-5]:<20} {p.get('fingerprint','?')}  {p.get('suite','?')}")
        except (OSError, json.JSONDecodeError, ValueError) as e:
            eprint(f"  {fn[:-5]:<20} invalid ({e})")
    return 0


def _validate_peer(peer):
    if not isinstance(peer, dict):
        die("peer is not a JSON object")
    try:
        pubs = [base64.b64decode(peer[k], validate=True)
                for k in ("x25519", "mlkem", "mldsa")]
    except Exception:
        die("peer contains invalid public-key encoding")
    if any(not p.startswith(b"-----BEGIN PUBLIC KEY-----") for p in pubs):
        die("peer contains a non-PEM public key")
    fp = fingerprint(pubs)
    if peer.get("fingerprint") != fp:
        die("peer fingerprint does not match its public keys")
    return peer


def load_peer(name):
    p = os.path.join(PEERS_DIR, f"{name}.json")
    source = p if os.path.exists(p) else name if os.path.exists(name) else None
    if not source:
        die(f"unknown peer '{name}' — add it: swr_crypto.py peer-add <file>")
    try:
        with open(source, encoding="utf-8") as f:
            peer = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        die(f"peer is not valid JSON: {e}")
    return _validate_peer(peer)


# ─────────────────────────────────────────────────────────────── encryption

def _encrypt_envelope(plaintext, peer, sign=True, aad_extra=b""):
    require_pq()
    tmps = []
    ephdir = tempfile.mkdtemp(dir=_securedir())
    try:
        # classical: ephemeral X25519 (forward secrecy)
        eph = os.path.join(ephdir, "eph.pem")
        ossl(["genpkey", "-algorithm", "X25519", "-out", eph])
        eph_pub = ossl(["pkey", "-in", eph, "-pubout", "-outform", "PEM"]).stdout
        peer_x = _tmp(base64.b64decode(peer["x25519"]), ".pem")
        tmps.append(peer_x)
        ss_c = ossl(["pkeyutl", "-derive", "-inkey", eph,
                     "-peerkey", peer_x]).stdout

        # post-quantum: ML-KEM-1024 encapsulation
        peer_k = _tmp(base64.b64decode(peer["mlkem"]), ".pem")
        ct_f, ss_f = _tmp(b""), _tmp(b"")
        tmps += [peer_k, ct_f, ss_f]
        ossl(["pkeyutl", "-encap", "-inkey", peer_k, "-pubin",
              "-secret", ss_f, "-out", ct_f])
        kem_ct = open(ct_f, "rb").read()
        ss_pq = open(ss_f, "rb").read()

        hdr = {"v": 1, "suite": SUITE, "to": peer["fingerprint"],
               "eph_x25519": base64.b64encode(eph_pub).decode(),
               "mlkem_ct": base64.b64encode(kem_ct).decode(),
               "ts": int(time.time())}
        if sign:
            ident = load_identity()
            hdr["from"] = ident["fingerprint"]
            hdr["from_mldsa"] = ident["mldsa"]
        hdr_b = json.dumps(hdr, sort_keys=True, separators=(",", ":")).encode()

        # transcript binding: every public value feeds the KDF
        transcript = hashlib.sha512(
            MAGIC + hdr_b + base64.b64decode(peer["x25519"]) +
            base64.b64decode(peer["mlkem"]) + aad_extra).digest()
        key = hkdf(ss_c + ss_pq, transcript, KDF_INFO, 32)
        body = seal(key, hdr_b + aad_extra, plaintext)

        env = {"hdr": base64.b64encode(hdr_b).decode(),
               "body": base64.b64encode(body).decode()}
        if sign:
            msg = _tmp(hdr_b + body)
            tmps.append(msg)
            sig = ossl(["pkeyutl", "-sign", "-rawin",
                        "-inkey", os.path.join(ID_DIR, "mldsa.key"),
                        "-in", msg]).stdout
            env["sig"] = base64.b64encode(sig).decode()
            env["sig_alg"] = "ML-DSA-87"
        return env
    finally:
        for t in tmps:
            _shred(t)
        shutil.rmtree(ephdir, ignore_errors=True)


def _parse_env(env):
    """Validate an envelope before touching crypto. Hostile input must produce
    a clean error, never a traceback or an unbounded allocation."""
    if not isinstance(env, dict):
        die("envelope is not a JSON object")
    for k in ("hdr", "body"):
        if k not in env:
            die(f"envelope missing required field '{k}'")
        if not isinstance(env[k], str):
            die(f"envelope field '{k}' must be a base64 string")
        if len(env[k]) > MAX_ENVELOPE_B64:
            die(f"envelope field '{k}' is too large")
    try:
        hdr_b = base64.b64decode(env["hdr"], validate=True)
        body = base64.b64decode(env["body"], validate=True)
    except Exception:
        die("envelope is not valid base64 — file is corrupt or not an swr message")
    if len(hdr_b) > MAX_HEADER_BYTES:
        die("envelope header is too large")
    try:
        hdr = json.loads(hdr_b)
    except (UnicodeDecodeError, json.JSONDecodeError):
        die("envelope header is not valid JSON")
    if not isinstance(hdr, dict):
        die("envelope header is not an object")
    for k in ("eph_x25519", "mlkem_ct"):
        if not isinstance(hdr.get(k), str):
            die(f"envelope header field '{k}' is missing or not a string")
        try:
            value = base64.b64decode(hdr[k], validate=True)
        except Exception:
            die(f"envelope header field '{k}' is not valid base64")
        if not value:
            die(f"envelope header field '{k}' is empty")
        if k == "mlkem_ct" and len(value) != 1568:
            die(f"ML-KEM-1024 ciphertext has wrong size ({len(value)} bytes)")
        if k == "eph_x25519" and len(value) > 1024:
            die("X25519 ephemeral public key is too large")
    if not isinstance(hdr.get("suite"), str) or not isinstance(hdr.get("to"), str):
        die("envelope header is missing suite or recipient")
    if "from" in hdr and not isinstance(hdr["from"], str):
        die("envelope sender fingerprint is not a string")
    if "from_mldsa" in hdr:
        if not isinstance(hdr["from_mldsa"], str):
            die("envelope sender key is not a string")
        try:
            base64.b64decode(hdr["from_mldsa"], validate=True)
        except Exception:
            die("envelope sender key is not valid base64")
    sig = env.get("sig")
    if sig is not None:
        if env.get("sig_alg") != "ML-DSA-87" or not isinstance(sig, str):
            die("unsupported or malformed envelope signature")
        if len(sig) > MAX_SIGNATURE_BYTES * 2:
            die("envelope signature is too large")
        try:
            if not base64.b64decode(sig, validate=True):
                raise ValueError
        except Exception:
            die("envelope signature is not valid base64")
    return hdr_b, body, hdr


def _decrypt_envelope(env, expect_from=None, aad_extra=b""):
    require_pq()
    ident = load_identity()
    hdr_b, body, hdr = _parse_env(env)
    if hdr.get("suite") != SUITE:
        die(f"unsupported suite {hdr.get('suite')!r}")
    if hdr.get("to") != ident["fingerprint"]:
        die(f"not addressed to this identity (to={hdr.get('to')}, "
            f"me={ident['fingerprint']})")

    # A header that claims a sender REQUIRES a signature: refuse the downgrade.
    claims_sender = bool(hdr.get("from") or hdr.get("from_mldsa"))
    if claims_sender and not env.get("sig"):
        die("SIGNATURE STRIPPED — header claims sender "
            f"{hdr.get('from', '?')} but no signature is present. "
            "Refusing: this is a downgrade attack.", 3)

    sender = None
    if env.get("sig"):
        pk = hdr.get("from_mldsa")
        if not pk:
            die("signature present but no sender key in header")
        pkf = _tmp(base64.b64decode(pk), ".pem")
        msgf = _tmp(hdr_b + body)
        sigf = _tmp(base64.b64decode(env["sig"]))
        try:
            r = ossl(["pkeyutl", "-verify", "-rawin", "-inkey", pkf, "-pubin",
                      "-in", msgf, "-sigfile", sigf], check=False)
            if r.returncode != 0:
                die("ML-DSA SIGNATURE INVALID — message forged or tampered", 3)
        finally:
            for f in (pkf, msgf, sigf):
                _shred(f)
        sender = hdr.get("from")
        known, known_fp = None, None
        if os.path.isdir(PEERS_DIR):
            for fn in os.listdir(PEERS_DIR):
                if not fn.endswith(".json"):
                    continue
                try:
                    with open(os.path.join(PEERS_DIR, fn), encoding="utf-8") as f:
                        p = json.load(f)
                except (OSError, json.JSONDecodeError):
                    continue
                if isinstance(p, dict) and p.get("mldsa") == pk:
                    known, known_fp = fn[:-5], p.get("fingerprint")
                    break
        if known and known_fp and sender != known_fp:
            die("sender fingerprint does not match the known peer key", 3)
        if expect_from:
            if not known or not known_fp:
                die("--from requires a known peer signing key", 3)
            if sender != known_fp or expect_from not in (known, known_fp):
                die(f"sender mismatch: expected {expect_from}, got {sender}", 3)
        elif not known:
            eprint(f"!! signature valid but sender {sender} is not a known peer")
    elif expect_from:
        die("--from given but message is unsigned", 3)

    tmps = []
    try:
        eph_pub = _tmp(base64.b64decode(hdr["eph_x25519"]), ".pem")
        tmps.append(eph_pub)
        ss_c = ossl(["pkeyutl", "-derive",
                     "-inkey", os.path.join(ID_DIR, "x25519.key"),
                     "-peerkey", eph_pub]).stdout
        ctf = _tmp(base64.b64decode(hdr["mlkem_ct"]))
        ssf = _tmp(b"")
        tmps += [ctf, ssf]
        ossl(["pkeyutl", "-decap", "-inkey", os.path.join(ID_DIR, "mlkem.key"),
              "-secret", ssf, "-in", ctf])
        ss_pq = open(ssf, "rb").read()
        transcript = hashlib.sha512(
            MAGIC + hdr_b + base64.b64decode(ident["x25519"]) +
            base64.b64decode(ident["mlkem"]) + aad_extra).digest()
        key = hkdf(ss_c + ss_pq, transcript, KDF_INFO, 32)
        return unseal(key, hdr_b + aad_extra, body), hdr, sender
    finally:
        for t in tmps:
            _shred(t)


# ───────────────────────────────────────────────────────────────── commands

def cmd_selftest(a):
    require_pq()
    print(f"ciphersuite: {SUITE}")
    print(f"openssl:     {'.'.join(map(str, openssl_version()))}")
    ok = True

    def t(name, cond):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'}  {name}")
        ok = ok and cond

    tmp = tempfile.mkdtemp()
    global ID_DIR, PEERS_DIR
    oid, opd = ID_DIR, PEERS_DIR
    try:
        ID_DIR = os.path.join(tmp, "id")
        PEERS_DIR = os.path.join(tmp, "peers")
        os.makedirs(ID_DIR)
        os.makedirs(PEERS_DIR)
        a_x = genkey("X25519", os.path.join(ID_DIR, "x25519.key"))
        a_k = genkey("ML-KEM-1024", os.path.join(ID_DIR, "mlkem.key"))
        a_d = genkey("ML-DSA-87", os.path.join(ID_DIR, "mldsa.key"))
        me = {"suite": SUITE, "name": "self",
              "x25519": base64.b64encode(a_x).decode(),
              "mlkem": base64.b64encode(a_k).decode(),
              "mldsa": base64.b64encode(a_d).decode()}
        me["fingerprint"] = fingerprint([a_x, a_k, a_d])
        idpath = os.path.join(ID_DIR, "id.json")
        with open(idpath, "w") as f:
            json.dump(me, f)
        os.chmod(idpath, 0o600)
        _private_dir(PEERS_DIR)
        with open(os.path.join(PEERS_DIR, "self.json"), "w") as f:
            json.dump(me, f)

        msg = b"swr hybrid pq test " + secrets.token_bytes(64)
        env = _encrypt_envelope(msg, me)
        t("encrypt produces envelope", set(env) >= {"hdr", "body", "sig"})
        pt, hdr, sender = _decrypt_envelope(env)
        t("round-trip plaintext matches", pt == msg)
        t("sender authenticated", sender == me["fingerprint"])
        t("ML-KEM ciphertext present (1568B)",
          len(base64.b64decode(json.loads(
              base64.b64decode(env["hdr"]))["mlkem_ct"])) == 1568)

        def isolated(payload):
            return subprocess.run(
                [sys.executable, __file__, "_isolated_decrypt", ID_DIR, PEERS_DIR],
                input=json.dumps(payload).encode(), capture_output=True).returncode

        t("isolated decrypt accepts valid envelope", isolated(env) == 0)

        bad = dict(env)
        b = bytearray(base64.b64decode(env["body"]))
        b[len(b) // 2] ^= 0xFF
        bad["body"] = base64.b64encode(bytes(b)).decode()
        t("tampered ciphertext rejected", isolated(bad) != 0)

        bad2 = dict(env)
        h = json.loads(base64.b64decode(env["hdr"]))
        h["ts"] = 1
        bad2["hdr"] = base64.b64encode(
            json.dumps(h, sort_keys=True, separators=(",", ":")).encode()).decode()
        t("tampered header rejected", isolated(bad2) != 0)

        ID2 = os.path.join(tmp, "id2")
        os.makedirs(ID2)
        b_x = genkey("X25519", os.path.join(ID2, "x25519.key"))
        b_k = genkey("ML-KEM-1024", os.path.join(ID2, "mlkem.key"))
        b_d = genkey("ML-DSA-87", os.path.join(ID2, "mldsa.key"))
        other = {"suite": SUITE, "name": "other",
                 "x25519": base64.b64encode(b_x).decode(),
                 "mlkem": base64.b64encode(b_k).decode(),
                 "mldsa": base64.b64encode(b_d).decode()}
        other["fingerprint"] = fingerprint([b_x, b_k, b_d])
        with open(os.path.join(ID2, "id.json"), "w") as f:
            json.dump(other, f)
        os.chmod(os.path.join(ID2, "id.json"), 0o600)
        t("wrong-recipient message rejected",
          isolated(_encrypt_envelope(b"for other only", other)) != 0)

        # An unknown signing key must not be able to claim the fingerprint of
        # a trusted peer when the caller explicitly requires that peer.
        old_id_dir = ID_DIR
        ID_DIR = ID2
        forged_sender = _encrypt_envelope(b"forged sender", me)
        ID_DIR = old_id_dir
        try:
            _decrypt_envelope(forged_sender, expect_from=me["fingerprint"])
        except SystemExit:
            t("unknown sender cannot satisfy --from", True)
        else:
            t("unknown sender cannot satisfy --from", False)

        strip = {k: v for k, v in env.items() if k not in ("sig", "sig_alg")}
        t("signature stripping rejected", isolated(strip) != 0)

        e1 = json.loads(base64.b64decode(_encrypt_envelope(b"x", me)["hdr"]))
        e2 = json.loads(base64.b64decode(_encrypt_envelope(b"x", me)["hdr"]))
        t("ephemeral key differs per message", e1["eph_x25519"] != e2["eph_x25519"])
        t("KEM ciphertext differs per message", e1["mlkem_ct"] != e2["mlkem_ct"])
    finally:
        ID_DIR, PEERS_DIR = oid, opd
        shutil.rmtree(tmp, ignore_errors=True)
    print(f"\n{'ALL PASS' if ok else 'FAILURES PRESENT'}")
    return 0 if ok else 1


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "_isolated_decrypt":
        global ID_DIR, PEERS_DIR
        if len(sys.argv) == 4:
            ID_DIR = os.path.abspath(sys.argv[2])
            PEERS_DIR = os.path.abspath(sys.argv[3])
        elif len(sys.argv) != 2:
            die("isolated decrypt expects identity and peer directories")
        try:
            env = json.loads(sys.stdin.read())
        except json.JSONDecodeError:
            die("not valid JSON")
        _decrypt_envelope(env)
        return 0

    p = argparse.ArgumentParser(prog="swr_crypto", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    s = p.add_subparsers(dest="cmd", required=True)
    q = s.add_parser("keygen")
    q.add_argument("--name"); q.add_argument("--force", action="store_true")
    q = s.add_parser("export"); q.add_argument("--qr", action="store_true")
    q = s.add_parser("peer-add")
    q.add_argument("file", nargs="?"); q.add_argument("--name")
    q.add_argument("--force", action="store_true",
                   help="replace an existing peer after reviewing old/new fingerprints")
    s.add_parser("peer-list")
    s.add_parser("selftest")

    a = p.parse_args()
    return {"keygen": cmd_keygen, "export": cmd_export, "peer-add": cmd_peer_add,
            "peer-list": cmd_peer_list, "selftest": cmd_selftest}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
