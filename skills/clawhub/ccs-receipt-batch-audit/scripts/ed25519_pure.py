#!/usr/bin/env python3
"""ed25519_pure.py — minimal, stdlib-only Ed25519 signature verification.

Used as a fallback when the `cryptography` package is unavailable (e.g. the
FC custom runtime ships bare Python). RFC 8032 verification only (no signing;
the service never holds private keys). Accepts raw 32-byte keys, RFC 8410
SPKI DER, or PEM text/base64.

Implementation notes
--------------------
* Curve arithmetic uses projective twisted-Edwards coordinates with the
  unified addition formula add-2008-hwcd-3 (a = -1) from the EFD. Point
  additions need no field inversion; equality is checked by cross-multiplying
  Z coordinates. This keeps verification to ~tens of milliseconds per
  signature on bare CPython (vs ~300+ ms with affine coordinates), so a
  200-receipt batch stays well inside a 30 s function timeout.
* Precomputed 2^i·P tables: the base-point table is built once at import;
  per-public-key tables (decode + subgroup check + table) are cached.
* Subgroup membership of both A and R is enforced (l·P == identity), exactly
  like the RFC 8032 reference implementation.
"""
from __future__ import annotations

import base64
import hashlib
import threading

q = 2 ** 255 - 19
l = 2 ** 252 + 27742317777372353535851937790883648493

_IDENT = (0, 1, 1)  # projective identity (X:Y:Z) = (0:1:1)
_KEY_CACHE_MAX = 16
_key_cache: dict[bytes, tuple] = {}
_key_cache_lock = threading.Lock()


def _H(m: bytes) -> bytes:
    return hashlib.sha512(m).digest()


def _inv(x: int) -> int:
    return pow(x, q - 2, q)


d = -121665 * _inv(121666) % q
I = pow(2, (q - 1) // 4, q)


def _xrecover(y: int) -> int:
    xx = (y * y - 1) * _inv(d * y * y + 1) % q
    x = pow(xx, (q + 3) // 8, q)
    if (x * x - xx) % q != 0:
        x = (x * I) % q
    if x % 2 != 0:
        x = q - x
    return x


By = 4 * _inv(5) % q
Bx = _xrecover(By)


# --------------------------------------------------------------------------- #
# Projective twisted-Edwards arithmetic (a = -1), formula add-2008-hwcd-3
# --------------------------------------------------------------------------- #
def _padd(P, Q):
    X1, Y1, Z1 = P
    X2, Y2, Z2 = Q
    A = (Z1 * Z2) % q
    B = (A * A) % q
    C = (X1 * X2) % q
    D = (Y1 * Y2) % q
    E = (d * C * D) % q
    F = (B - E) % q
    G = (B + E) % q
    X3 = (A * F * ((X1 + Y1) * (X2 + Y2) - C - D)) % q
    Y3 = (A * G * (D + C)) % q
    Z3 = (F * G) % q
    return (X3, Y3, Z3)


def _ptable(P):
    """Return [P, 2P, 4P, ..., 2^255 P] in projective coordinates."""
    tab = [P]
    for _ in range(255):
        tab.append(_padd(tab[-1], tab[-1]))
    return tab


def _tmul(table, k):
    """Scalar multiply using a precomputed 2^i·P table."""
    R = _IDENT
    for i in range(256):
        if (k >> i) & 1:
            R = _padd(R, table[i])
    return R


def _is_identity(P) -> bool:
    X, Y, Z = P
    return X % q == 0 and (Y - Z) % q == 0


def _peq(P, Q) -> bool:
    X1, Y1, Z1 = P
    X2, Y2, Z2 = Q
    return (X1 * Z2 - X2 * Z1) % q == 0 and (Y1 * Z2 - Y2 * Z1) % q == 0


# Base point table, built once at import (256 projective doublings).
_B_TAB = _ptable((Bx % q, By % q, 1))


def _bit(h: bytes, i: int) -> int:
    return (h[i // 8] >> (i % 8)) & 1


def _decode_affine(s: bytes):
    """Decode 32 compressed bytes -> affine (x, y) on the curve, or None.

    Does NOT perform the subgroup check (callers do it projectively).
    """
    y = int.from_bytes(s, "little") & ((1 << 255) - 1)
    x = _xrecover(y)
    if (x & 1) != _bit(s, 255):
        x = q - x
    return (x, y)


def _key_entry(raw: bytes):
    """Return cached (A_projective, A_table) for a raw 32-byte key, or None."""
    with _key_cache_lock:
        entry = _key_cache.get(raw)
    if entry is not None:
        return entry
    aff = _decode_affine(raw)
    if aff is None:
        return None
    A = (aff[0], aff[1], 1)
    tab = _ptable(A)
    # subgroup check: l·A must be the identity
    if not _is_identity(_tmul(tab, l)):
        return None
    entry = (A, tab)
    with _key_cache_lock:
        _key_cache[raw] = entry
        if len(_key_cache) > _KEY_CACHE_MAX:
            # drop the oldest entries (dict preserves insertion order)
            for old in list(_key_cache)[:len(_key_cache) - _KEY_CACHE_MAX]:
                _key_cache.pop(old, None)
    return entry


def verify(public_key, signature: bytes, message: bytes) -> bool:
    """Verify an Ed25519 signature. Never raises — returns True/False."""
    try:
        if not isinstance(signature, (bytes, bytearray)) or len(signature) != 64:
            return False
        signature = bytes(signature)
        if not isinstance(message, (bytes, bytearray)):
            return False
        raw = _extract_raw_key(public_key)
        if raw is None or len(raw) != 32:
            return False

        entry = _key_entry(raw)
        if entry is None:
            return False
        _, a_tab = entry

        r_aff = _decode_affine(signature[:32])
        if r_aff is None:
            return False
        R = (r_aff[0], r_aff[1], 1)
        # subgroup check on R
        r_tab = _ptable(R)
        if not _is_identity(_tmul(r_tab, l)):
            return False

        s = int.from_bytes(signature[32:], "little")
        if s >= l:
            return False
        h = int.from_bytes(_H(signature[:32] + raw + bytes(message)), "little")

        sB = _tmul(_B_TAB, s)
        hA = _tmul(a_tab, h % l)  # l·A == identity, so reducing h mod l is sound
        lhs = _padd(R, hA)
        return _peq(lhs, sB)
    except Exception:
        return False


def _extract_raw_key(blob):
    """Extract the 32-byte raw Ed25519 key from raw / DER(SPKI) / PEM."""
    if isinstance(blob, str):
        s = blob.strip()
        if "BEGIN" in s:
            try:
                b64 = "".join(
                    line for line in s.splitlines()
                    if not line.startswith("-----")
                )
                der = base64.b64decode(b64)
                return _raw_from_der(der)
            except Exception:
                return None
        try:
            blob = base64.b64decode(s, validate=True)
        except Exception:
            blob = s.encode()
    if not isinstance(blob, (bytes, bytearray)):
        return None
    blob = bytes(blob)
    if len(blob) == 32:
        return blob
    if b"BEGIN" in blob:
        try:
            b64 = b"".join(
                line for line in blob.splitlines()
                if not line.startswith(b"-----")
            )
            blob = base64.b64decode(b64)
        except Exception:
            return None
    return _raw_from_der(blob)


def _raw_from_der(der: bytes):
    """Parse a minimal RFC 8410 Ed25519 SPKI DER key -> 32 raw bytes."""
    try:
        oid = bytes([0x06, 0x03, 0x2B, 0x65, 0x70])  # OID 1.3.101.112
        idx = der.find(oid)
        if idx < 0:
            return None
        rest = der[idx + len(oid):]
        bs = rest.find(b"\x03")  # BIT STRING
        if bs < 0:
            return None
        j = bs + 1
        length = rest[j]
        j += 1
        if length & 0x80:
            n = length & 0x7F
            length = int.from_bytes(rest[j:j + n], "big")
            j += n
        if rest[j] != 0x00:
            return None
        key = rest[j + 1: j + length]
        if len(key) == 32:
            return key
    except Exception:
        return None
    return None
