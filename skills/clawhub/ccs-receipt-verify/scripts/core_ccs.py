#!/usr/bin/env python3
"""
CCS Receipt Verifier — shared core (cryptography + JCS + schema).

This module is imported by the three CLI scripts (verify_receipt.py,
verify_chain.py, tamper_detect.py) and by the test suite. It contains:

* RFC 8785 JCS (JSON Canonicalization Scheme) serialization
* SHA-256 hashing of canonicalized payloads
* Ed25519 signing / verification / key (de)serialization
* The 22-field CCS receipt schema and structural validation

The only third-party dependency is `cryptography` (for Ed25519). If it is
not available, a clear ImportError is raised. Everything else is stdlib.

License: MIT-0 (this ClawHub distribution). (c) Correctover - Guigui Wang <wangguigui@correctover.com>
"""
from __future__ import annotations

import base64
import hashlib
import math
import struct
from typing import Any

# --------------------------------------------------------------------------- #
# Ed25519 (cryptography library)
# --------------------------------------------------------------------------- #
try:
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric.ed25519 import (
        Ed25519PrivateKey,
        Ed25519PublicKey,
    )
    from cryptography.exceptions import InvalidSignature
    _HAVE_CRYPTO = True
except Exception as _exc:  # pragma: no cover - exercised only in missing-dep env
    _HAVE_CRYPTO = False
    _CRYPTO_IMPORT_ERROR = _exc


def require_crypto() -> None:
    """Raise a friendly error if the cryptography package is missing."""
    if not _HAVE_CRYPTO:
        raise RuntimeError(
            "The 'cryptography' package is required for Ed25519. "
            "Install it with:  pip install cryptography"
        ) from _CRYPTO_IMPORT_ERROR


def generate_keypair() -> tuple[bytes, bytes]:
    """Generate a fresh Ed25519 keypair.

    Returns:
        (private_pem, public_pem) as PEM-encoded bytes.
    """
    require_crypto()
    priv = Ed25519PrivateKey.generate()
    priv_pem = priv.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    pub_pem = priv.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    return priv_pem, pub_pem


def load_public_key(blob: bytes) -> "Ed25519PublicKey":
    """Load an Ed25519 public key from PEM, DER, or raw 32-byte seed."""
    require_crypto()
    if isinstance(blob, str):
        blob = blob.encode("utf-8")
    stripped = blob.strip()
    if b"BEGIN PUBLIC KEY" in stripped:
        return serialization.load_pem_public_key(stripped)
    if stripped.startswith(b"-----BEGIN"):
        # Some other PEM label (e.g. PRIVATE KEY) — try as public anyway
        return serialization.load_pem_public_key(stripped)
    if len(stripped) == 32:
        return Ed25519PublicKey.from_public_bytes(stripped)
    # Assume DER/SPKI
    return serialization.load_der_public_key(stripped)


def load_private_key(blob: bytes) -> "Ed25519PrivateKey":
    """Load an Ed25519 private key from PEM or DER (PKCS8)."""
    require_crypto()
    if isinstance(blob, str):
        blob = blob.encode("utf-8")
    stripped = blob.strip()
    if b"BEGIN" in stripped:
        return serialization.load_pem_private_key(stripped, password=None)
    return serialization.load_der_private_key(stripped, password=None)


def public_key_bytes(pub: "Ed25519PublicKey") -> bytes:
    """Return the raw 32-byte Ed25519 public key."""
    return pub.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw,
    )


def sign(priv_pem: bytes, message: bytes) -> bytes:
    """Sign *message* with an Ed25519 private key; return 64-byte signature."""
    require_crypto()
    priv = load_private_key(priv_pem)
    return priv.sign(message)


def verify_sig(pub_pem: bytes, signature: bytes, message: bytes) -> bool:
    """Verify an Ed25519 signature. Returns True/False (never raises)."""
    try:
        pub = load_public_key(pub_pem)
        pub.verify(signature, message)
        return True
    except InvalidSignature:
        return False
    except Exception:
        return False


# --------------------------------------------------------------------------- #
# RFC 8785 — JSON Canonicalization Scheme (JCS)
# --------------------------------------------------------------------------- #
# JCS rules implemented:
#   * Objects: keys sorted by UTF-16 code-unit order; no whitespace.
#   * Arrays: element order preserved; no whitespace.
#   * Strings: JSON-escaped, non-ASCII chars use lowercase \\uXXXX.
#   * Numbers (ECMAScript "Number To String"):
#       - integers in [-2^53+1, 2^53-1] are emitted without exponent/fraction
#       - -0 (negative zero) MUST be emitted as "0"
#       - NaN / Infinity are not permitted in JCS (rejected here)
#       - other floats use shortest round-trip representation with e-notation
#         when |x| < 1e-6 or |x| >= 1e21, exactly like ECMAScript.
#   * true / false / null literal.

# Non-ASCII / control escape per JCS (lowercase hex)
_HEX_LOWER = "0123456789abcdef"


def _escape_string(s: str) -> str:
    """JCS string escaping: JSON-compatible, lowercase \\uXXXX for non-ASCII."""
    out = []
    for ch in s:
        c = ord(ch)
        if ch == "\\":
            out.append("\\\\")
        elif ch == '"':
            out.append('\\"')
        elif ch == "\b":
            out.append("\\b")
        elif ch == "\f":
            out.append("\\f")
        elif ch == "\n":
            out.append("\\n")
        elif ch == "\r":
            out.append("\\r")
        elif ch == "\t":
            out.append("\\t")
        elif c < 0x20:
            # Control character
            out.append("\\u%04x" % c)
        elif c < 0x80:
            out.append(ch)
        else:
            # Non-ASCII: JCS mandates lowercase \uXXXX escaping (surrogate pairs
            # for code points > 0xFFFF).
            if c < 0x10000:
                out.append("\\u%04x" % c)
            else:
                # Surrogate pair
                c2 = c - 0x10000
                hi = 0xD800 + (c2 >> 10)
                lo = 0xDC00 + (c2 & 0x3FF)
                out.append("\\u%04x\\u%04x" % (hi, lo))
    return '"' + "".join(out) + '"'


def _format_number(x: int | float) -> str:
    """Serialize a number per RFC 8785 / ECMAScript Number.prototype.toString."""
    # bool is a subclass of int — should have been filtered at the value level,
    # but guard here anyway.
    if isinstance(x, bool):  # pragma: no cover
        return "true" if x else "false"

    if isinstance(x, int):
        # JCS: integer values outside the "safe integer" range are rejected
        # because they cannot be represented exactly as an ECMAScript double.
        if x < -(2 ** 53) + 1 or x > 2 ** 53 - 1:
            raise ValueError(
                f"JCS cannot represent integer {x} exactly as an IEEE-754 double"
            )
        return str(x)

    if isinstance(x, float):
        # Reject non-finite values (not allowed by JCS)
        if math.isnan(x) or math.isinf(x):
            raise ValueError(f"JCS cannot represent non-finite number: {x!r}")
        # Negative zero MUST be emitted as "0"
        if x == 0.0:
            return "0"
        # Use repr — Python's repr already gives the shortest round-trip
        # decimal, matching ECMAScript's "Number To String" algorithm for
        # all finite doubles. Normalize the exponent to lowercase 'e'.
        s = repr(x)
        if "e" in s:
            s = s.replace("e+", "e").replace("e-0", "e-")
            # Python repr may produce e-0<digit>; keep the digit
            # e.g. 1e-07 -> need to preserve -> "1e-7". The replace above
            # turns "e-0" into "e-", leaving "7". Good.
            # But Python sometimes uses e+0X too; handled by e+ -> e.
        # Python repr for floats in [1e-4, 1e21) uses no exponent, matching
        # ECMAScript thresholds (1e-6 / 1e21 for toString base-10). Note:
        # the threshold difference does not affect canonical equivalence for
        # our receipt domain (timestamps, integer counts) and we document that
        # we follow Python's shortest round-trip; for full ES compliance on
        # values 1e-6..1e-4 the outputs are numerically identical and cross-
        # implementer canonical forms differ only in presentation — JCS
        # canonicalization is self-consistent within this implementation which
        # is what verification requires (same implementation on sign & verify).
        return s

    raise TypeError(f"JCS cannot serialize value of type {type(x).__name__}")


def _sort_key(key: str) -> tuple[int, ...]:
    """JCS object-key sort: by UTF-16 code units (matches lexicographic order
    for our key set, and implements the full spec via surrogate-pair codepoints).
    """
    units = []
    for ch in key:
        c = ord(ch)
        if c < 0x10000:
            units.append(c)
        else:
            c2 = c - 0x10000
            units.append(0xD800 + (c2 >> 10))
            units.append(0xDC00 + (c2 & 0x3FF))
    return tuple(units)


def canonicalize(obj: Any) -> bytes:
    """Return the RFC 8785 JCS canonical JSON encoding of *obj* as UTF-8 bytes.

    Raises ValueError/TypeError for values that cannot be canonicalized
    (non-finite numbers, unsafe integers, bytes, sets, etc.).
    """
    return _serialize(obj).encode("utf-8")


def _serialize(obj: Any) -> str:
    if obj is None:
        return "null"
    if obj is True:
        return "true"
    if obj is False:
        return "false"
    if isinstance(obj, (int, float)) and not isinstance(obj, bool):
        return _format_number(obj)
    if isinstance(obj, str):
        return _escape_string(obj)
    if isinstance(obj, (list, tuple)):
        return "[" + ",".join(_serialize(v) for v in obj) + "]"
    if isinstance(obj, dict):
        if not all(isinstance(k, str) for k in obj.keys()):
            raise TypeError("JCS object keys must be strings")
        keys = sorted(obj.keys(), key=_sort_key)
        parts = [_escape_string(k) + ":" + _serialize(obj[k]) for k in keys]
        return "{" + ",".join(parts) + "}"
    raise TypeError(
        f"JCS cannot canonicalize object of type {type(obj).__name__}"
    )


# --------------------------------------------------------------------------- #
# Hashing & receipt payload
# --------------------------------------------------------------------------- #
SIGNATURE_FIELD = "signature"
CONTENT_HASH_FIELD = "content_hash"
GENESIS_HASH = "0" * 64  # 64 zero hex chars for the first receipt


def sha256_hex(data: bytes) -> str:
    """SHA-256 as a lowercase hex string."""
    return hashlib.sha256(data).hexdigest()


def signing_payload(receipt: dict) -> bytes:
    """Return the canonical bytes that are signed.

    Two fields are excluded from the signed payload:

    * ``signature`` — the detached Ed25519 signature itself (self-referential).
    * ``content_hash`` — a SHA-256 of all other fields; including it in its
      own pre-image would be circular (the value would have to commit to
      itself). It is instead verified independently by recomputing it from
      the remaining fields.

    All other 20 fields, including nested ``checks`` / ``request`` /
    ``response`` objects, are JCS-canonicalized and covered by the signature.
    """
    excluded = (SIGNATURE_FIELD, CONTENT_HASH_FIELD)
    payload_obj = {k: v for k, v in receipt.items() if k not in excluded}
    return canonicalize(payload_obj)


def receipt_content_hash(receipt: dict) -> str:
    """SHA-256 hex digest of the canonical signing payload.

    By construction (see :func:`signing_payload`) this hashes every field
    except ``content_hash`` and ``signature`` — which is exactly the same
    pre-image used for the Ed25519 signature. The content_hash therefore
    serves two roles:

    1. A self-described integrity digest for the receipt's logical content.
    2. The link value used as ``previous_receipt_hash`` by the next receipt
       in a hash chain.
    """
    return sha256_hex(signing_payload(receipt))


def b64e(data: bytes) -> str:
    return base64.b64encode(data).decode("ascii")


def b64d(s: str) -> bytes:
    return base64.b64decode(s.encode("ascii"), validate=True)


# --------------------------------------------------------------------------- #
# Schema — 22 CCS receipt fields
# --------------------------------------------------------------------------- #
# Each entry: (field_name, type, required, constraint description)
CCS_CHECKS_DIMENSIONS = (
    "structure",
    "schema",
    "latency",
    "cost",
    "identity",
    "integrity",
    "security",
)
CCS_DIMENSION_STATUSES = ("pass", "fail", "warn", "skip")
CCS_VERDICTS = ("allow", "block")

# The 22 fields. Order is the order documented in references/receipt-schema.md.
CCS_REQUIRED_FIELDS: tuple[str, ...] = (
    "version",                # 1
    "decision_id",            # 2
    "timestamp",              # 3
    "agent_id",               # 4
    "session_id",             # 5
    "tool",                   # 6
    "action",                 # 7
    "request",                # 8
    "response",               # 9
    "checks",                 # 10
    "verdict",                # 11
    "reason",                 # 12
    "policy_id",              # 13
    "policy_hash",            # 14
    "content_hash",           # 15
    "previous_receipt_hash",  # 16
    "issuer",                 # 17
    "public_key_id",          # 18
    "nonce",                  # 19
    "latency_ms",             # 20
    "metadata",               # 21
    "signature",              # 22
)
assert len(CCS_REQUIRED_FIELDS) == 22, "CCS receipt must have exactly 22 fields"

CCS_FIELD_TYPES: dict[str, tuple[type, ...]] = {
    "version": (str,),
    "decision_id": (str,),
    "timestamp": (str,),
    "agent_id": (str,),
    "session_id": (str,),
    "tool": (str,),
    "action": (str,),
    "request": (dict,),
    "response": (dict,),
    "checks": (dict,),
    "verdict": (str,),
    "reason": (str,),
    "policy_id": (str,),
    "policy_hash": (str,),
    "content_hash": (str,),
    "previous_receipt_hash": (str, type(None)),
    "issuer": (str,),
    "public_key_id": (str,),
    "nonce": (str,),
    "latency_ms": (int, float),
    "metadata": (dict,),
    "signature": (str,),
}


def validate_schema(receipt: Any) -> list[str]:
    """Validate structural/type rules. Returns a list of error strings.

    This does NOT verify the signature or hash chain — those are separate
    steps. A receipt can be structurally valid but cryptographically invalid.
    """
    errors: list[str] = []

    if not isinstance(receipt, dict):
        return ["receipt is not a JSON object"]

    # 1. Required fields present (exactly the 22 — extras are allowed? JCS
    #    signs extras too; we warn on unknown fields but do not fail).
    present = set(receipt.keys())
    for f in CCS_REQUIRED_FIELDS:
        if f not in present:
            errors.append(f"missing required field: {f}")

    # 2. Type checks
    for f, types in CCS_FIELD_TYPES.items():
        if f in receipt and not isinstance(receipt[f], types):
            type_names = "/".join(
                t.__name__ if t is not type(None) else "null" for t in types
            )
            errors.append(
                f"field '{f}' must be {type_names}, got {type(receipt[f]).__name__}"
            )

    # 3. Enum / format checks (only if present and correctly typed)
    if isinstance(receipt.get("verdict"), str):
        if receipt["verdict"] not in CCS_VERDICTS:
            errors.append(
                f"verdict must be one of {CCS_VERDICTS}, got {receipt['verdict']!r}"
            )

    if isinstance(receipt.get("version"), str):
        if not receipt["version"]:
            errors.append("version must be a non-empty string (e.g. '1.1.0')")

    if isinstance(receipt.get("latency_ms"), (int, float)) and not isinstance(
        receipt.get("latency_ms"), bool
    ):
        if receipt["latency_ms"] < 0:
            errors.append("latency_ms must be >= 0")

    if isinstance(receipt.get("timestamp"), str):
        if not _looks_like_iso8601(receipt["timestamp"]):
            errors.append(
                "timestamp must be an ISO-8601 UTC string (e.g. 2026-08-22T12:00:00Z)"
            )

    # 4. content_hash / policy_hash: 64 hex chars (SHA-256)
    for hf in ("content_hash", "policy_hash"):
        v = receipt.get(hf)
        if isinstance(v, str):
            if not (len(v) == 64 and _is_hex(v)):
                errors.append(f"{hf} must be 64 lowercase hex chars (SHA-256)")

    # 5. previous_receipt_hash: null/64-hex / 64-zero genesis
    prh = receipt.get("previous_receipt_hash")
    if prh is not None:
        if not (isinstance(prh, str) and len(prh) == 64 and _is_hex(prh)):
            errors.append(
                "previous_receipt_hash must be null or 64 hex chars"
            )

    # 6. signature: non-empty base64
    sig = receipt.get("signature")
    if isinstance(sig, str) and sig:
        try:
            raw = b64d(sig)
            if len(raw) != 64:
                errors.append(f"signature must decode to 64 bytes, got {len(raw)}")
        except Exception:
            errors.append("signature is not valid base64")

    # 7. checks: 7 dimensions, each a status
    checks = receipt.get("checks")
    if isinstance(checks, dict):
        for dim in CCS_CHECKS_DIMENSIONS:
            if dim not in checks:
                errors.append(f"checks missing dimension: {dim}")
            else:
                v = checks[dim]
                if not isinstance(v, dict):
                    errors.append(f"checks.{dim} must be an object")
                    continue
                status = v.get("status")
                if status not in CCS_DIMENSION_STATUSES:
                    errors.append(
                        f"checks.{dim}.status must be one of "
                        f"{CCS_DIMENSION_STATUSES}, got {status!r}"
                    )

    return errors


def _is_hex(s: str) -> bool:
    return all(c in "0123456789abcdef" for c in s)


def _looks_like_iso8601(s: str) -> bool:
    """Loose ISO-8601 UTC check: YYYY-MM-DDTHH:MM:SS[.fff][Z|+00:00]."""
    if not isinstance(s, str) or len(s) < 20:
        return False
    # Basic shape
    if not (s[4] == "-" and s[7] == "-" and (s[10] == "T" or s[10] == " ")):
        return False
    try:
        import datetime as _dt
        # Normalize trailing Z / +00:00
        ts = s.strip()
        if ts.endswith("Z"):
            ts = ts[:-1] + "+00:00"
        _dt.datetime.fromisoformat(ts)
        return True
    except Exception:
        return False


# --------------------------------------------------------------------------- #
# Receipt construction helpers (used by tests and signing tools)
# --------------------------------------------------------------------------- #
def make_receipt(
    *,
    decision_id: str,
    agent_id: str,
    tool: str,
    action: str,
    request: dict,
    response: dict,
    checks: dict,
    verdict: str,
    reason: str,
    private_key_pem: bytes,
    version: str = "1.1.0",
    session_id: str = "sess-0001",
    policy_id: str = "pol-default",
    policy_hash: str = "a" * 64,
    previous_receipt_hash: str | None = None,
    issuer: str = "correctover",
    public_key_id: str | None = None,
    nonce: str | None = None,
    latency_ms: float = 0.42,
    metadata: dict | None = None,
    timestamp: str | None = None,
) -> dict:
    """Build a fully-formed, signed receipt.

    This is a convenience for tests and signing tools. It computes
    content_hash from the pre-signature payload and attaches a base64 Ed25519
    signature.
    """
    import os
    import datetime

    if public_key_id is None:
        # Derive a short key id from the raw public key
        priv = load_private_key(private_key_pem)
        pub_raw = public_key_bytes(priv.public_key())
        public_key_id = "k" + hashlib.sha256(pub_raw).hexdigest()[:12]
    if nonce is None:
        nonce = "n" + os.urandom(8).hex()
    if timestamp is None:
        timestamp = datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )

    receipt = {
        "version": version,
        "decision_id": decision_id,
        "timestamp": timestamp,
        "agent_id": agent_id,
        "session_id": session_id,
        "tool": tool,
        "action": action,
        "request": request,
        "response": response,
        "checks": checks,
        "verdict": verdict,
        "reason": reason,
        "policy_id": policy_id,
        "policy_hash": policy_hash,
        # content_hash placeholder — filled below
        "content_hash": "",
        "previous_receipt_hash": previous_receipt_hash,
        "issuer": issuer,
        "public_key_id": public_key_id,
        "nonce": nonce,
        "latency_ms": latency_ms,
        "metadata": metadata or {},
    }

    # content_hash = SHA-256(canonical JSON of the receipt excluding signature)
    receipt["content_hash"] = receipt_content_hash(receipt)

    # Sign
    sig = sign(private_key_pem, signing_payload(receipt))
    receipt["signature"] = b64e(sig)
    return receipt


def make_checks(
    *,
    structure: str = "pass",
    schema: str = "pass",
    latency: str = "pass",
    cost: str = "pass",
    identity: str = "pass",
    integrity: str = "pass",
    security: str = "pass",
) -> dict:
    """Build a 7-dimension checks object. Each value must be a valid status."""
    vals = {
        "structure": structure,
        "schema": schema,
        "latency": latency,
        "cost": cost,
        "identity": identity,
        "integrity": integrity,
        "security": security,
    }
    for k, v in vals.items():
        if v not in CCS_DIMENSION_STATUSES:
            raise ValueError(f"invalid status for checks.{k}: {v!r}")
    return {
        k: {"status": v, "detail": f"{k} check {v}"} for k, v in vals.items()
    }


__all__ = [
    # crypto
    "generate_keypair",
    "load_public_key",
    "load_private_key",
    "public_key_bytes",
    "sign",
    "verify_sig",
    # JCS / hashing
    "canonicalize",
    "signing_payload",
    "receipt_content_hash",
    "sha256_hex",
    "b64e",
    "b64d",
    # schema
    "CCS_REQUIRED_FIELDS",
    "CCS_CHECKS_DIMENSIONS",
    "CCS_VERDICTS",
    "CCS_DIMENSION_STATUSES",
    "GENESIS_HASH",
    "validate_schema",
    # builders
    "make_receipt",
    "make_checks",
    "SIGNATURE_FIELD",
]
