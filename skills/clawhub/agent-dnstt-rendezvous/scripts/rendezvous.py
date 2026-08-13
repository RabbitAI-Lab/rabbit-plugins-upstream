#!/usr/bin/env python3
"""Authorization-gated DNSTT rendezvous planner for cooperating agents.

The planner never starts a tunnel, changes DNS/firewalls, scans resolvers,
downloads binaries, or reads a private key. It creates short-lived connection
cards and deterministic command plans for explicitly authorized infrastructure.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import hmac
import ipaddress
import json
import os
import re
import secrets
import shlex
import stat
import sys
import tempfile
import unicodedata
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

VERSION = "1.1.2"
SCHEMA = "agent-dnstt-rendezvous/v1"
STATUS_SCHEMA = "agent-dnstt-status/v1"
CARD_CANON = "canonical-json-v1"
MAX_CARD_BYTES = 64 * 1024
MAX_STATUS_BYTES = 16 * 1024
MAX_PUBLIC_KEY_BYTES = 4096
MAX_JSON_DEPTH = 16
MAX_JSON_NODES = 512
MAX_TEXT = 512
MAX_STATUS_MESSAGE = 500
MAX_HMAC_SECRET_BYTES = 4096
MAX_OUTPUT_BYTES = 1024 * 1024
CLOCK_SKEW = dt.timedelta(minutes=5)
MIN_CARD_TTL = dt.timedelta(minutes=5)
MAX_CARD_TTL = dt.timedelta(hours=24)

AGENT_RE = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9._-]{0,63}$")
ENV_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
BINARY_RE = re.compile(
    r"^(?:[A-Za-z0-9_+.-]+|(?:/|\./|\.\./)[A-Za-z0-9_+./ -]+|"
    r"[A-Za-z]:\\[A-Za-z0-9_+.\\ /-]+)$"
)
DOMAIN_RE = re.compile(
    r"^(?=.{1,253}\.?$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+"
    r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.?$",
    re.IGNORECASE,
)
HOST_RE = re.compile(
    r"^(?=.{1,253}\.?$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)*"
    r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.?$",
    re.IGNORECASE,
)
HEX_KEY_RE = re.compile(r"^[0-9a-fA-F]{64}$")
HEX64_RE = re.compile(r"^[0-9a-f]{64}$")
HEX32_RE = re.compile(r"^[0-9a-f]{32}$")
FINGERPRINT_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
STATES = ("planned", "authorized", "configured", "reachable", "connected", "verified", "closed", "failed")
ROLES = ("client", "server", "observer")
ALLOWED_TRANSITIONS = {
    "planned": {"authorized", "failed", "closed"},
    "authorized": {"configured", "failed", "closed"},
    "configured": {"reachable", "failed", "closed"},
    "reachable": {"connected", "failed", "closed"},
    "connected": {"verified", "failed", "closed"},
    "verified": {"closed", "failed"},
    "failed": {"planned", "closed"},
    "closed": set(),
}
CARD_FIELDS = {
    "schema",
    "canonicalization",
    "role",
    "server_agent_id",
    "tunnel_domain",
    "server_public_key",
    "server_key_fingerprint",
    "server_listener",
    "upstream_service",
    "authorization_ref",
    "purpose",
    "issued_at",
    "expires_at",
    "nonce",
    "constraints",
    "card_id",
    "coordination_hmac_sha256",
}
STATUS_FIELDS = {
    "schema",
    "card_id",
    "agent_id",
    "role",
    "state",
    "observed_at",
    "message",
    "previous_status_id",
    "transition_verified",
    "safe_to_share",
    "contains_private_key",
    "status_id",
    "coordination_hmac_sha256",
}
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----", re.IGNORECASE),
    re.compile(r"\b(?:github_pat_|ghp_|gho_|glpat-|clh_|claw_sk_|sk-[A-Za-z0-9_-]{12})[A-Za-z0-9_-]*"),
    re.compile(r"(?i)\b(?:password|passwd|secret|token|api[_ -]?key|private[_ -]?key)\s*[:=]\s*\S+"),
    re.compile(r"\b[A-Za-z0-9+/]{48,}={0,2}\b"),
)
DEBUG_ENABLED = False


class RendezvousError(ValueError):
    def __init__(self, message: str, *, code: str = "invalid_input", hint: str | None = None):
        super().__init__(message)
        self.code = code
        self.hint = hint

    def as_dict(self) -> dict[str, Any]:
        value: dict[str, Any] = {"ok": False, "error": {"code": self.code, "message": str(self)}}
        if self.hint:
            value["error"]["hint"] = self.hint
        return value


def debug_event(event: str, **fields: Any) -> None:
    """Emit bounded, secret-free JSON diagnostics to stderr."""
    if not DEBUG_ENABLED:
        return
    safe: dict[str, Any] = {"event": event, "at": iso(utcnow())}
    sensitive_tokens = ("secret", "token", "password", "private", "public_key", "hmac", "credential", "message")
    for key, value in fields.items():
        lowered = key.lower()
        if any(token in lowered for token in sensitive_tokens):
            continue
        if isinstance(value, str):
            if contains_secret(value):
                continue
            safe[key] = value[:160]
        elif isinstance(value, (int, bool)) or value is None:
            safe[key] = value
    print(json.dumps(safe, sort_keys=True, ensure_ascii=False), file=sys.stderr)


def utcnow() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)  # noqa: UP017 - keep Python 3.10 support


def iso(value: dt.datetime) -> str:
    return value.astimezone(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")  # noqa: UP017 - Python 3.10


def parse_time(value: str) -> dt.datetime:
    if not isinstance(value, str) or len(value) > 40:
        raise RendezvousError("timestamp must be a short ISO-8601 string", code="invalid_timestamp")
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))  # noqa: FURB162 - Python 3.10
    except ValueError as exc:
        raise RendezvousError(f"invalid timestamp: {value}", code="invalid_timestamp") from exc
    if parsed.tzinfo is None:
        raise RendezvousError("timestamp must include a timezone", code="invalid_timestamp")
    return parsed.astimezone(dt.timezone.utc)  # noqa: UP017 - keep Python 3.10 support


def validate_json_value(value: Any, *, depth: int = 0, nodes: list[int] | None = None) -> None:
    if nodes is None:
        nodes = [0]
    nodes[0] += 1
    if nodes[0] > MAX_JSON_NODES:
        raise RendezvousError("JSON contains too many values", code="json_too_complex")
    if depth > MAX_JSON_DEPTH:
        raise RendezvousError("JSON nesting is too deep", code="json_too_deep")
    if value is None or isinstance(value, (bool, int)):
        return
    if isinstance(value, float):
        raise RendezvousError("floating-point values are not allowed in signed JSON", code="json_float_forbidden")
    if isinstance(value, str):
        if len(value) > MAX_CARD_BYTES:
            raise RendezvousError("JSON string is too long", code="json_string_too_long")
        if any(ord(char) < 32 or ord(char) == 127 or 0xD800 <= ord(char) <= 0xDFFF for char in value):
            raise RendezvousError("JSON strings must not contain control or surrogate code points", code="json_unsafe_string")
        if unicodedata.normalize("NFC", value) != value:
            raise RendezvousError("JSON strings must use Unicode NFC normalization", code="json_not_nfc")
        return
    if isinstance(value, list):
        for item in value:
            validate_json_value(item, depth=depth + 1, nodes=nodes)
        return
    if isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str):
                raise RendezvousError("JSON object keys must be strings", code="json_key_type")
            if any(ord(char) < 32 or ord(char) == 127 or 0xD800 <= ord(char) <= 0xDFFF for char in key):
                raise RendezvousError("JSON keys contain unsafe code points", code="json_unsafe_string")
            if unicodedata.normalize("NFC", key) != key:
                raise RendezvousError("JSON keys must use Unicode NFC normalization", code="json_not_nfc")
            validate_json_value(item, depth=depth + 1, nodes=nodes)
        return
    raise RendezvousError(f"unsupported JSON value type: {type(value).__name__}", code="json_type_forbidden")


def canonical(value: Any) -> bytes:
    """Versioned deterministic JSON for this schema (not a claim of full RFC 8785)."""
    validate_json_value(value)
    try:
        text = json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        )
    except (TypeError, ValueError, UnicodeError) as exc:
        raise RendezvousError(f"cannot canonicalize JSON: {exc}", code="canonicalization_failed") from exc
    return text.encode("utf-8")


def reject_duplicate_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise RendezvousError(f"duplicate JSON key: {key}", code="duplicate_json_key")
        result[key] = value
    return result


def reject_json_constant(value: str) -> None:
    raise RendezvousError(f"non-finite JSON number is forbidden: {value}", code="json_nonfinite")


def read_bounded_regular(path: Path, *, maximum: int, label: str) -> bytes:
    path = path.expanduser()
    try:
        lst = path.lstat()
    except OSError as exc:
        raise RendezvousError(f"cannot stat {label}: {exc}", code="file_unavailable") from exc
    if stat.S_ISLNK(lst.st_mode):
        raise RendezvousError(f"{label} must not be a symlink", code="symlink_forbidden")
    if not stat.S_ISREG(lst.st_mode):
        raise RendezvousError(f"{label} must be a regular file", code="not_regular_file")
    if lst.st_size > maximum:
        raise RendezvousError(f"{label} exceeds {maximum} bytes", code="file_too_large")
    # O_NONBLOCK prevents a lstat/open swap to a FIFO or device from hanging
    # before fstat can reject the changed file type.
    flags = (
        os.O_RDONLY
        | getattr(os, "O_CLOEXEC", 0)
        | getattr(os, "O_NOFOLLOW", 0)
        | getattr(os, "O_NONBLOCK", 0)
    )
    try:
        fd = os.open(path, flags)
    except OSError as exc:
        raise RendezvousError(f"cannot open {label}: {exc}", code="file_unavailable") from exc
    try:
        current = os.fstat(fd)
        if not stat.S_ISREG(current.st_mode):
            raise RendezvousError(f"{label} changed type while opening", code="file_race_detected")
        if current.st_size > maximum:
            raise RendezvousError(f"{label} exceeds {maximum} bytes", code="file_too_large")
        chunks: list[bytes] = []
        remaining = maximum + 1
        while remaining > 0:
            chunk = os.read(fd, min(65536, remaining))
            if not chunk:
                break
            chunks.append(chunk)
            remaining -= len(chunk)
        data = b"".join(chunks)
        if len(data) > maximum:
            raise RendezvousError(f"{label} exceeds {maximum} bytes", code="file_too_large")
        return data
    finally:
        os.close(fd)


def load_json_object(path: Path, *, maximum: int, label: str) -> dict[str, Any]:
    data = read_bounded_regular(path, maximum=maximum, label=label)
    try:
        text = data.decode("utf-8", errors="strict")
        value = json.loads(
            text,
            object_pairs_hook=reject_duplicate_pairs,
            parse_constant=reject_json_constant,
        )
    except RendezvousError:
        raise
    except UnicodeDecodeError as exc:
        raise RendezvousError(f"{label} is not UTF-8", code="invalid_utf8") from exc
    except (json.JSONDecodeError, RecursionError, ValueError) as exc:
        raise RendezvousError(f"{label} is not valid bounded JSON: {exc}", code="invalid_json") from exc
    if not isinstance(value, dict):
        raise RendezvousError(f"{label} root must be a JSON object", code="json_root_type")
    validate_json_value(value)
    return value


def validate_safe_text(value: Any, *, label: str, maximum: int = MAX_TEXT, allow_empty: bool = False) -> str:
    if not isinstance(value, str):
        raise RendezvousError(f"{label} must be text", code="invalid_text")
    text = unicodedata.normalize("NFC", value.strip())
    if not text and not allow_empty:
        raise RendezvousError(f"{label} is required", code="missing_text")
    if len(text) > maximum:
        raise RendezvousError(f"{label} exceeds {maximum} characters", code="text_too_long")
    if any(ord(char) < 32 or ord(char) == 127 for char in text):
        raise RendezvousError(f"{label} contains control characters", code="control_character")
    return text


def contains_secret(text: str) -> bool:
    return any(pattern.search(text) for pattern in SECRET_PATTERNS)


def validate_public_text(value: Any, *, label: str, maximum: int) -> str:
    text = validate_safe_text(value, label=label, maximum=maximum)
    if contains_secret(text):
        raise RendezvousError(
            f"{label} looks like it contains a credential or private key",
            code="sensitive_public_text",
            hint="use an opaque non-secret reference instead",
        )
    return text


def validate_status_message(value: Any) -> str:
    text = validate_safe_text(value, label="status message", maximum=MAX_STATUS_MESSAGE, allow_empty=True)
    if contains_secret(text):
        raise RendezvousError(
            "status message looks like it contains a credential or private key",
            code="sensitive_status_message",
            hint="replace sensitive material with a non-secret observation",
        )
    return text


def normalize_domain(value: str) -> str:
    domain = validate_safe_text(value, label="domain", maximum=253).lower().rstrip(".")
    if not DOMAIN_RE.fullmatch(domain):
        raise RendezvousError("domain must be a valid delegated DNS name", code="invalid_domain")
    if domain.endswith((".local", ".localhost", ".invalid")):
        raise RendezvousError("mDNS/localhost/invalid suffixes cannot be DNSTT zones", code="invalid_domain")
    return domain


def validate_hostname(host: str, *, label: str) -> str:
    host = host.strip()
    try:
        return str(ipaddress.ip_address(host))
    except ValueError:
        if re.fullmatch(r"[0-9.]+", host):
            raise RendezvousError(f"{label} resembles an invalid IP address", code="invalid_endpoint")
        candidate = host.lower().rstrip(".")
        if not HOST_RE.fullmatch(candidate):
            raise RendezvousError(f"{label} host is invalid", code="invalid_endpoint")
        return candidate


def parse_endpoint(value: str, *, label: str, allow_hostnames: bool = True) -> tuple[str, int]:
    value = validate_safe_text(value, label=label, maximum=320)
    if value.startswith("["):
        end = value.find("]")
        if end < 0 or end + 1 >= len(value) or value[end + 1] != ":":
            raise RendezvousError(f"{label} must be [IPv6]:port", code="invalid_endpoint")
        host, port_text = value[1:end], value[end + 2 :]
    else:
        if value.count(":") != 1:
            raise RendezvousError(f"{label} must be host:port (IPv6 uses [addr]:port)", code="invalid_endpoint")
        host, port_text = value.rsplit(":", 1)
    host = host.strip()
    if not host:
        raise RendezvousError(f"{label} host is required", code="invalid_endpoint")
    try:
        port = int(port_text)
    except ValueError as exc:
        raise RendezvousError(f"{label} port must be an integer", code="invalid_endpoint") from exc
    if not 1 <= port <= 65535:
        raise RendezvousError(f"{label} port must be between 1 and 65535", code="invalid_endpoint")
    try:
        normalized = str(ipaddress.ip_address(host))
    except ValueError:
        if not allow_hostnames:
            raise RendezvousError(f"{label} requires an IP address", code="invalid_endpoint")
        normalized = validate_hostname(host, label=label)
    return normalized, port


def endpoint_text(host: str, port: int) -> str:
    return f"[{host}]:{port}" if ":" in host else f"{host}:{port}"


def normalize_endpoint(value: str, *, label: str) -> str:
    return endpoint_text(*parse_endpoint(value, label=label))


def is_loopback(host: str) -> bool:
    if host.lower() == "localhost":
        return True
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


def read_public_key(path: Path) -> str:
    data = read_bounded_regular(path, maximum=MAX_PUBLIC_KEY_BYTES, label="public-key file")
    try:
        text = data.decode("utf-8", errors="strict").strip()
    except UnicodeDecodeError as exc:
        raise RendezvousError("public-key file must be UTF-8 text", code="invalid_public_key") from exc
    candidates: list[str] = re.findall(r"(?<![0-9a-fA-F])[0-9a-fA-F]{64}(?![0-9a-fA-F])", text)
    if len(candidates) != 1:
        raise RendezvousError("public-key file must contain exactly one 64-hex DNSTT key", code="invalid_public_key")
    return candidates[0].lower()


def key_fingerprint(public_key: str) -> str:
    if not isinstance(public_key, str) or not HEX_KEY_RE.fullmatch(public_key):
        raise RendezvousError("DNSTT public key must be exactly 64 hexadecimal characters", code="invalid_public_key")
    return "sha256:" + hashlib.sha256(bytes.fromhex(public_key)).hexdigest()


def grouped_fingerprint(value: str) -> str:
    if not FINGERPRINT_RE.fullmatch(value):
        raise RendezvousError("fingerprint must use sha256:<64 lowercase hex>", code="invalid_fingerprint")
    raw = value.removeprefix("sha256:")
    return "sha256:" + ":".join(raw[i : i + 8] for i in range(0, len(raw), 8))


def validate_hmac_key(secret: bytes | None) -> bytes | None:
    if secret is None:
        return None
    if not isinstance(secret, bytes):
        raise RendezvousError("coordination HMAC secret must be bytes", code="invalid_hmac_secret")
    if len(secret) < 32:
        raise RendezvousError("coordination HMAC secret must be at least 32 bytes", code="weak_hmac_secret")
    if len(secret) > MAX_HMAC_SECRET_BYTES:
        raise RendezvousError("coordination HMAC secret is unreasonably large", code="hmac_secret_too_large")
    return secret


def hmac_secret(env_name: str | None) -> bytes | None:
    if not env_name:
        return None
    if not ENV_RE.fullmatch(env_name):
        raise RendezvousError("HMAC environment variable name is invalid", code="invalid_env_name")
    value = os.environ.get(env_name)
    if value is None:
        raise RendezvousError(f"environment variable {env_name!r} is not set", code="missing_hmac_secret")
    return validate_hmac_key(value.encode("utf-8"))


def sign_object(value: dict[str, Any], *, id_field: str, secret: bytes | None) -> dict[str, Any]:
    secret = validate_hmac_key(secret)
    unsigned = dict(value)
    unsigned.pop("coordination_hmac_sha256", None)
    unsigned.pop(id_field, None)
    object_id = hashlib.sha256(canonical(unsigned)).hexdigest()
    signed = {**unsigned, id_field: object_id}
    if secret is not None:
        signed["coordination_hmac_sha256"] = hmac.new(secret, canonical(signed), hashlib.sha256).hexdigest()
    return signed


def sign_card(card: dict[str, Any], secret: bytes | None) -> dict[str, Any]:
    return sign_object(card, id_field="card_id", secret=secret)


def verify_object_signature(
    value: dict[str, Any],
    *,
    id_field: str,
    secret: bytes | None,
    require_hmac: bool,
) -> tuple[str, bool]:
    secret = validate_hmac_key(secret)
    unsigned = dict(value)
    supplied_hmac = unsigned.pop("coordination_hmac_sha256", None)
    supplied_id = unsigned.pop(id_field, None)
    if not isinstance(supplied_id, str) or not HEX64_RE.fullmatch(supplied_id):
        raise RendezvousError(f"{id_field} must be 64 lowercase hex", code="invalid_object_id")
    actual_id = hashlib.sha256(canonical(unsigned)).hexdigest()
    if not hmac.compare_digest(supplied_id, actual_id):
        raise RendezvousError(f"{id_field} mismatch; object may have been edited", code="object_id_mismatch")
    if supplied_hmac is None:
        if require_hmac:
            raise RendezvousError(
                "authenticated card/status required for this operation",
                code="hmac_required",
                hint="supply --hmac-env or explicitly use --allow-unsigned-card for an authorized offline workflow",
            )
        if secret is not None:
            raise RendezvousError("coordination secret supplied but object has no HMAC", code="unexpected_hmac_secret")
        return supplied_id, False
    if not isinstance(supplied_hmac, str) or not HEX64_RE.fullmatch(supplied_hmac):
        raise RendezvousError("coordination HMAC must be 64 lowercase hex", code="invalid_hmac")
    if secret is None:
        raise RendezvousError("HMAC-authenticated object requires --hmac-env", code="missing_hmac_secret")
    expected = hmac.new(secret, canonical({**unsigned, id_field: supplied_id}), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(supplied_hmac, expected):
        raise RendezvousError("coordination HMAC mismatch", code="hmac_mismatch")
    return supplied_id, True


def validate_constraints(value: Any) -> dict[str, bool]:
    expected = {
        "authorized_infrastructure_only",
        "client_listener_loopback_only",
        "no_private_key_in_card",
        "no_automatic_execution",
        "no_resolver_scanning",
        "upstream_loopback_only",
    }
    if not isinstance(value, dict) or set(value) != expected:
        raise RendezvousError("card constraints are missing, unknown, or malformed", code="invalid_constraints")
    if any(not isinstance(item, bool) for item in value.values()):
        raise RendezvousError("card constraints must be booleans", code="invalid_constraints")
    required_true = expected - {"upstream_loopback_only", "client_listener_loopback_only"}
    if any(value[name] is not True for name in required_true):
        raise RendezvousError("mandatory safety constraints must be true", code="invalid_constraints")
    return value


def verify_card(
    card: dict[str, Any],
    *,
    expected_fingerprint: str | None,
    secret: bytes | None,
    allow_expired: bool = False,
    require_hmac: bool = False,
) -> dict[str, Any]:
    unknown = sorted(set(card) - CARD_FIELDS)
    missing = sorted((CARD_FIELDS - {"coordination_hmac_sha256"}) - set(card))
    if missing:
        raise RendezvousError("card missing fields: " + ", ".join(missing), code="card_missing_fields")
    if unknown:
        raise RendezvousError("card has unknown fields: " + ", ".join(unknown), code="card_unknown_fields")
    if card["schema"] != SCHEMA or card["canonicalization"] != CARD_CANON or card["role"] != "dnstt-server":
        raise RendezvousError("unsupported card schema, canonicalization, or role", code="unsupported_schema")
    agent_id = validate_safe_text(card["server_agent_id"], label="server_agent_id", maximum=64)
    if not AGENT_RE.fullmatch(agent_id):
        raise RendezvousError("invalid server_agent_id", code="invalid_agent_id")
    domain = normalize_domain(card["tunnel_domain"])
    public_key = str(card["server_public_key"]).lower()
    calculated_fp = key_fingerprint(public_key)
    if card["server_key_fingerprint"] != calculated_fp:
        raise RendezvousError("card public key and fingerprint do not match", code="fingerprint_mismatch")
    if expected_fingerprint is not None:
        expected = str(expected_fingerprint).lower()
        if not FINGERPRINT_RE.fullmatch(expected):
            raise RendezvousError("expected fingerprint must be sha256:<64 lowercase hex>", code="invalid_fingerprint")
        if not hmac.compare_digest(expected, calculated_fp):
            raise RendezvousError("out-of-band server fingerprint mismatch", code="fingerprint_mismatch")
    listener = normalize_endpoint(card["server_listener"], label="server listener")
    upstream = normalize_endpoint(card["upstream_service"], label="upstream service")
    if listener != card["server_listener"] or upstream != card["upstream_service"]:
        raise RendezvousError("card endpoints must use canonical host:port spelling", code="noncanonical_endpoint")
    upstream_host, _ = parse_endpoint(upstream, label="upstream service")
    constraints = validate_constraints(card["constraints"])
    if constraints["upstream_loopback_only"] and not is_loopback(upstream_host):
        raise RendezvousError("card claims loopback-only upstream but endpoint is not loopback", code="constraint_mismatch")
    authorization_ref = validate_public_text(card["authorization_ref"], label="authorization_ref", maximum=128)
    purpose = validate_public_text(card["purpose"], label="purpose", maximum=256)
    nonce = card["nonce"]
    if not isinstance(nonce, str) or not HEX32_RE.fullmatch(nonce):
        raise RendezvousError("nonce must be 32 lowercase hex", code="invalid_nonce")
    issued = parse_time(card["issued_at"])
    expires = parse_time(card["expires_at"])
    now = utcnow()
    ttl = expires - issued
    if not MIN_CARD_TTL <= ttl <= MAX_CARD_TTL:
        raise RendezvousError("card lifetime must be between 5 minutes and 24 hours", code="invalid_card_ttl")
    if issued > now + CLOCK_SKEW:
        raise RendezvousError("card issue time is too far in the future", code="future_card")
    if not allow_expired and now >= expires:
        raise RendezvousError("rendezvous card has expired", code="expired_card")
    card_id, authenticated = verify_object_signature(
        card,
        id_field="card_id",
        secret=secret,
        require_hmac=require_hmac,
    )
    debug_event("card_verified", card_id=card_id, hmac_authenticated=authenticated)
    return {
        "card_id": card_id,
        "domain": domain,
        "fingerprint": calculated_fp,
        "fingerprint_display": grouped_fingerprint(calculated_fp),
        "authorization_ref": authorization_ref,
        "purpose": purpose,
        "issued_at": iso(issued),
        "expires_at": iso(expires),
        "expired": now >= expires,
        "hmac_authenticated": authenticated,
    }


def load_card(path: Path) -> dict[str, Any]:
    return load_json_object(path, maximum=MAX_CARD_BYTES, label="rendezvous card")


def atomic_write(path: Path, data: bytes, *, force: bool, mode: int = 0o600) -> None:
    path = path.expanduser()
    parent = path.parent if str(path.parent) else Path(".")
    parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    if path.exists() or path.is_symlink():
        if path.is_symlink():
            raise RendezvousError("refusing to replace output symlink", code="output_symlink")
        if not force:
            raise RendezvousError("output already exists; pass --force-output to replace it", code="output_exists")
        if not path.is_file():
            raise RendezvousError("output target is not a regular file", code="output_not_regular")
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(parent))
    temp_path = Path(temp_name)
    try:
        os.fchmod(fd, mode)
        view = memoryview(data)
        while view:
            written = os.write(fd, view)
            if written <= 0:
                raise OSError("short write")
            view = view[written:]
        os.fsync(fd)
        os.close(fd)
        fd = -1
        if path.is_symlink():
            raise RendezvousError("output became a symlink during write", code="output_race_detected")
        os.replace(temp_path, path)
        try:
            dir_flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_CLOEXEC", 0)
            dir_fd = os.open(parent, dir_flags)
            try:
                os.fsync(dir_fd)
            finally:
                os.close(dir_fd)
        except OSError:
            pass
    finally:
        if fd >= 0:
            os.close(fd)
        try:
            temp_path.unlink()
        except FileNotFoundError:
            pass


def write_json(value: Any, output: str | None, *, force: bool = False) -> None:
    validate_json_value(value)
    text = json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
    data = text.encode("utf-8")
    if len(data) > MAX_OUTPUT_BYTES:
        raise RendezvousError("JSON output exceeds the 1 MiB safety limit", code="output_too_large")
    if output:
        path = Path(output)
        atomic_write(path, data, force=force)
        debug_event("output_written", bytes=len(data), filename=path.name)
        print(str(path.expanduser()))
    else:
        sys.stdout.write(text)


def require_authorized(args: argparse.Namespace) -> None:
    if not getattr(args, "ack_authorized", False):
        raise RendezvousError("refusing operational plan without --ack-authorized", code="authorization_ack_required")


def safe_path_arg(value: str, *, label: str) -> str:
    text = validate_safe_text(value, label=label, maximum=4096)
    return str(Path(text).expanduser().resolve(strict=False))


def safe_binary(value: str, *, label: str) -> str:
    text = validate_safe_text(value, label=label, maximum=4096)
    if text.startswith("-") or not BINARY_RE.fullmatch(text):
        raise RendezvousError(
            f"{label} must be a simple command name or safe filesystem path",
            code="invalid_binary",
        )
    return text


def keygen_target(value: str, *, label: str) -> str:
    path = Path(validate_safe_text(value, label=label, maximum=4096)).expanduser()
    if path.is_symlink():
        raise RendezvousError(f"{label} must not be a symlink", code="keygen_target_symlink")
    if path.exists():
        raise RendezvousError(
            f"{label} already exists; refusing a plan that could overwrite key material",
            code="keygen_target_exists",
        )
    return str(path.resolve(strict=False))


def command_plan(
    command: list[str],
    *,
    plan_kind: str,
    notes: list[str],
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    stable = {"plan_kind": plan_kind, "command_argv": command, "notes": notes, **(extra or {})}
    plan_id = hashlib.sha256(canonical(stable)).hexdigest()
    return {
        "schema": "agent-dnstt-plan/v1",
        "plan_id": plan_id,
        "plan_kind": plan_kind,
        "generated_at": iso(utcnow()),
        "execute_automatically": False,
        "command_argv": command,
        "shell_preview": shlex.join(command),
        "operator_review_required": True,
        "notes": notes,
        **(extra or {}),
    }


def operational_require_hmac(args: argparse.Namespace) -> bool:
    return not getattr(args, "allow_unsigned_card", False)


def cmd_server_card(args: argparse.Namespace) -> None:
    require_authorized(args)
    agent_id = validate_safe_text(args.agent_id, label="agent-id", maximum=64)
    if not AGENT_RE.fullmatch(agent_id):
        raise RendezvousError("agent-id must be 1-64 safe identifier characters", code="invalid_agent_id")
    domain = normalize_domain(args.domain)
    public_key = read_public_key(Path(args.pubkey_file))
    listen = endpoint_text(*parse_endpoint(args.listen, label="server listener"))
    upstream_host, upstream_port = parse_endpoint(args.upstream, label="upstream service")
    upstream = endpoint_text(upstream_host, upstream_port)
    if not is_loopback(upstream_host) and not args.allow_nonloopback_upstream:
        raise RendezvousError("upstream must be loopback unless explicit override is reviewed", code="nonloopback_upstream")
    authorization_ref = validate_public_text(args.authorization_ref, label="authorization-ref", maximum=128)
    purpose = validate_public_text(args.purpose, label="purpose", maximum=256)
    secret = hmac_secret(args.hmac_env)
    now = utcnow()
    expires = now + dt.timedelta(minutes=args.expires_minutes)
    card = {
        "schema": SCHEMA,
        "canonicalization": CARD_CANON,
        "role": "dnstt-server",
        "server_agent_id": agent_id,
        "tunnel_domain": domain,
        "server_public_key": public_key,
        "server_key_fingerprint": key_fingerprint(public_key),
        "server_listener": listen,
        "upstream_service": upstream,
        "authorization_ref": authorization_ref,
        "purpose": purpose,
        "issued_at": iso(now),
        "expires_at": iso(expires),
        "nonce": secrets.token_hex(16),
        "constraints": {
            "authorized_infrastructure_only": True,
            "client_listener_loopback_only": not args.allow_lan_client_listener,
            "no_private_key_in_card": True,
            "no_automatic_execution": True,
            "no_resolver_scanning": True,
            "upstream_loopback_only": is_loopback(upstream_host),
        },
    }
    signed = sign_card(card, secret)
    debug_event("card_created", card_id=signed["card_id"], hmac_authenticated=secret is not None)
    write_json(signed, args.output, force=args.force_output)


def cmd_verify(args: argparse.Namespace) -> None:
    card = load_card(Path(args.card))
    result = verify_card(
        card,
        expected_fingerprint=args.expected_fingerprint,
        secret=hmac_secret(args.hmac_env),
        allow_expired=args.allow_expired,
        require_hmac=args.require_hmac,
    )
    write_json({"valid": True, **result}, args.output, force=args.force_output)


def cmd_keygen_plan(args: argparse.Namespace) -> None:
    require_authorized(args)
    private_target = keygen_target(args.privkey_file, label="private-key path")
    public_target = keygen_target(args.pubkey_file, label="public-key path")
    if private_target == public_target:
        raise RendezvousError("private and public key paths must differ", code="keygen_target_collision")
    command = [
        safe_binary(args.dnstt_server, label="dnstt-server binary"),
        "-gen-key",
        "-privkey-file",
        private_target,
        "-pubkey-file",
        public_target,
    ]
    write_json(
        command_plan(
            command,
            plan_kind="keygen",
            notes=[
                "Run once on the authorized server host.",
                "Set the private key file to mode 0600 immediately after generation.",
                "Share only the public key and its out-of-band fingerprint.",
            ],
        ),
        args.output,
        force=args.force_output,
    )


def inspect_private_key(path: Path) -> dict[str, Any]:
    path = path.expanduser()
    try:
        info = path.lstat()
    except OSError as exc:
        raise RendezvousError(f"cannot stat private-key file: {exc}", code="private_key_unavailable") from exc
    if stat.S_ISLNK(info.st_mode):
        raise RendezvousError("private-key file must not be a symlink", code="private_key_symlink")
    if not stat.S_ISREG(info.st_mode):
        raise RendezvousError("private-key path must be a regular file", code="private_key_not_regular")
    mode = stat.S_IMODE(info.st_mode)
    if mode & 0o077:
        raise RendezvousError(f"private-key permissions must be 0600 or stricter (current {mode:04o})", code="private_key_permissions")
    if info.st_size <= 0 or info.st_size > MAX_PUBLIC_KEY_BYTES:
        raise RendezvousError("private-key file size is implausible", code="private_key_size")
    if hasattr(os, "geteuid") and info.st_uid != os.geteuid():
        raise RendezvousError("private-key file must be owned by the current user", code="private_key_owner")
    return {"path": str(path.resolve(strict=False)), "mode": f"{mode:04o}", "size": info.st_size}


def cmd_server_plan(args: argparse.Namespace) -> None:
    require_authorized(args)
    card = load_card(Path(args.card))
    verification = verify_card(
        card,
        expected_fingerprint=None,
        secret=hmac_secret(args.hmac_env),
        require_hmac=operational_require_hmac(args),
    )
    private_key = inspect_private_key(Path(args.privkey_file))
    command = [
        safe_binary(args.dnstt_server, label="dnstt-server binary"),
        "-udp",
        card["server_listener"],
        "-privkey-file",
        private_key["path"],
        card["tunnel_domain"],
        card["upstream_service"],
    ]
    write_json(
        command_plan(
            command,
            plan_kind="server",
            notes=[
                "This plan does not change firewall or DNS records.",
                "Keep the upstream service access-controlled.",
                "Recheck private-key path, owner, and mode immediately before manual execution.",
            ],
            extra={"verified_card": verification, "private_key_metadata": private_key},
        ),
        args.output,
        force=args.force_output,
    )


def validate_resolver(transport: str, resolver: str) -> str:
    resolver = validate_safe_text(resolver, label="resolver", maximum=2048)
    if transport == "doh":
        if any(char.isspace() for char in resolver):
            raise RendezvousError("DoH URL must not contain whitespace", code="invalid_doh_url")
        parsed = urlsplit(resolver)
        if parsed.scheme.lower() != "https" or not parsed.hostname:
            raise RendezvousError("DoH resolver must be an https:// URL", code="invalid_doh_url")
        if parsed.username is not None or parsed.password is not None:
            raise RendezvousError("DoH URL must not contain credentials", code="doh_userinfo_forbidden")
        if parsed.fragment or parsed.query:
            raise RendezvousError("DoH URL must not contain query or fragment data", code="doh_url_metadata_forbidden")
        host = validate_hostname(parsed.hostname, label="DoH resolver")
        try:
            port = parsed.port
        except ValueError as exc:
            raise RendezvousError("DoH resolver port is invalid", code="invalid_doh_url") from exc
        if port is not None and not 1 <= port <= 65535:
            raise RendezvousError("DoH resolver port is invalid", code="invalid_doh_url")
        host_text = f"[{host}]" if ":" in host else host
        netloc = host_text + (f":{port}" if port is not None else "")
        path = parsed.path or "/dns-query"
        if not path.startswith("/") or "//" in path:
            raise RendezvousError("DoH URL path is invalid", code="invalid_doh_url")
        return urlunsplit(("https", netloc, path, "", ""))
    host, port = parse_endpoint(resolver, label=f"{transport.upper()} resolver")
    return endpoint_text(host, port)


def cmd_client_plan(args: argparse.Namespace) -> None:
    require_authorized(args)
    card = load_card(Path(args.card))
    verification = verify_card(
        card,
        expected_fingerprint=args.expected_fingerprint,
        secret=hmac_secret(args.hmac_env),
        require_hmac=operational_require_hmac(args),
    )
    local_host, local_port = parse_endpoint(args.local_listen, label="client listener")
    if not is_loopback(local_host):
        if card["constraints"]["client_listener_loopback_only"]:
            raise RendezvousError("signed card requires a loopback client listener", code="constraint_mismatch")
        if not args.allow_lan_listener:
            raise RendezvousError("non-loopback client listener requires explicit local approval", code="nonloopback_client")
    resolver = validate_resolver(args.transport, args.resolver)
    transport_flag = {"udp": "-udp", "doh": "-doh", "dot": "-dot"}[args.transport]
    public_key_path = safe_path_arg(args.pubkey_file, label="public-key path")
    command = [
        safe_binary(args.dnstt_client, label="dnstt-client binary"),
        transport_flag,
        resolver,
        "-pubkey-file",
        public_key_path,
        card["tunnel_domain"],
        endpoint_text(local_host, local_port),
    ]
    write_json(
        command_plan(
            command,
            plan_kind="client",
            notes=[
                "Materialize only the public key, then compare its fingerprint again.",
                "The local listener forwards one TCP service; DNSTT is not a VPN or anonymity layer.",
                "Use only the operator-approved resolver and domain.",
            ],
            extra={
                "verified_card": verification,
                "public_key_file_to_create": {
                    "path": public_key_path,
                    "mode": "0644",
                    "content": card["server_public_key"],
                    "contains_sensitive_material": False,
                },
            },
        ),
        args.output,
        force=args.force_output,
    )


DIAGNOSTICS = {
    "dns-delegation": [
        "Confirm the tunnel subdomain has an NS delegation to a nameserver outside the delegated child zone.",
        "Confirm the nameserver hostname has correct A/AAAA records for the authorized server.",
        "Confirm UDP/53 reaches the reviewed DNSTT listener or an explicit high-port forwarding rule.",
    ],
    "key-mismatch": [
        "Recompute the server public-key SHA-256 fingerprint on both agents.",
        "Compare it through an independent authenticated channel.",
        "Regenerate the card after intentional key rotation; never copy the private key to clients.",
    ],
    "no-response": [
        "Confirm the server process and loopback upstream service are running.",
        "Check authoritative DNS reachability using one operator-approved resolver; never sweep resolver ranges.",
        "Check logs for response-size/MTU warnings and use the installed build's documented tuning.",
    ],
    "connects-no-service": [
        "Test the loopback upstream service directly and confirm the expected protocol.",
        "Confirm the card points to the intended upstream port and that application authentication is enabled.",
        "Do not expose a general unauthenticated proxy.",
    ],
    "intermittent": [
        "Check packet loss, approved-resolver latency, and server resource limits with bounded tests.",
        "Reduce concurrency/query rate before changing MTU; preserve logs without secrets.",
        "Exchange timestamped status reports to separate DNS-path failure from upstream failure.",
    ],
}


def cmd_diagnose(args: argparse.Namespace) -> None:
    card = load_card(Path(args.card))
    verification = verify_card(
        card,
        expected_fingerprint=args.expected_fingerprint,
        secret=hmac_secret(args.hmac_env),
        allow_expired=True,
        require_hmac=args.require_hmac,
    )
    warning = "Read-only guidance; do not scan third-party resolvers or alter DNS/firewalls without authorization."
    if verification["expired"]:
        warning += " This card is expired; use diagnostics only for historical analysis and issue a new card before reconnecting."
    write_json(
        {
            "symptom": args.symptom,
            "verified_card": verification,
            "card_expired": verification["expired"],
            "checks": DIAGNOSTICS[args.symptom],
            "automatic_actions": [],
            "warning": warning,
        },
        args.output,
        force=args.force_output,
    )


def verify_status(
    report: dict[str, Any],
    *,
    card_id: str,
    secret: bytes | None,
    require_hmac: bool,
) -> dict[str, Any]:
    unknown = sorted(set(report) - STATUS_FIELDS)
    required = STATUS_FIELDS - {"coordination_hmac_sha256", "previous_status_id"}
    missing = sorted(required - set(report))
    if missing or unknown:
        raise RendezvousError(
            "status fields are missing or unknown",
            code="invalid_status_schema",
            hint=f"missing={missing}, unknown={unknown}",
        )
    if report["schema"] != STATUS_SCHEMA or report["card_id"] != card_id:
        raise RendezvousError("status schema/card_id mismatch", code="status_card_mismatch")
    agent_id = validate_safe_text(report["agent_id"], label="status agent_id", maximum=64)
    if not AGENT_RE.fullmatch(agent_id):
        raise RendezvousError("status agent_id is invalid", code="invalid_agent_id")
    if report["role"] not in ROLES or report["state"] not in STATES:
        raise RendezvousError("status role/state is invalid", code="invalid_status_state")
    observed = parse_time(report["observed_at"])
    if observed > utcnow() + CLOCK_SKEW:
        raise RendezvousError("status timestamp is too far in the future", code="future_status")
    message = validate_status_message(report["message"])
    if report["safe_to_share"] is not True or report["contains_private_key"] is not False:
        raise RendezvousError("status safety flags are invalid", code="invalid_status_flags")
    previous = report.get("previous_status_id")
    if previous is not None and (not isinstance(previous, str) or not HEX64_RE.fullmatch(previous)):
        raise RendezvousError("previous_status_id is invalid", code="invalid_previous_status")
    if not isinstance(report["transition_verified"], bool):
        raise RendezvousError("transition_verified must be boolean", code="invalid_status_flags")
    if (previous is None and report["transition_verified"] is True) or (
        previous is not None and report["transition_verified"] is False
    ):
        raise RendezvousError("status transition fields are inconsistent", code="invalid_status_flags")
    status_id, authenticated = verify_object_signature(
        report,
        id_field="status_id",
        secret=secret,
        require_hmac=require_hmac,
    )
    return {
        "status_id": status_id,
        "agent_id": agent_id,
        "role": report["role"],
        "state": report["state"],
        "message": message,
        "observed_at": iso(observed),
        "hmac_authenticated": authenticated,
    }


def cmd_status(args: argparse.Namespace) -> None:
    card = load_card(Path(args.card))
    secret = hmac_secret(args.hmac_env)
    card_verification = verify_card(
        card,
        expected_fingerprint=args.expected_fingerprint,
        secret=secret,
        allow_expired=args.allow_expired,
        require_hmac=args.require_hmac,
    )
    agent_id = validate_safe_text(args.agent_id, label="agent-id", maximum=64)
    if not AGENT_RE.fullmatch(agent_id):
        raise RendezvousError("agent-id is invalid", code="invalid_agent_id")
    message = validate_status_message(args.message)
    previous_id = None
    transition_verified = False
    if args.previous_report:
        previous_report = load_json_object(Path(args.previous_report), maximum=MAX_STATUS_BYTES, label="previous status report")
        previous = verify_status(
            previous_report,
            card_id=card_verification["card_id"],
            secret=secret,
            require_hmac=args.require_hmac,
        )
        if previous["agent_id"] != agent_id or previous["role"] != args.role:
            raise RendezvousError("previous status belongs to another agent/role", code="status_identity_mismatch")
        if parse_time(previous["observed_at"]) > utcnow():
            raise RendezvousError("previous status is later than the new report", code="status_time_order")
        if args.state not in ALLOWED_TRANSITIONS[previous["state"]]:
            raise RendezvousError(
                f"invalid state transition: {previous['state']} -> {args.state}",
                code="invalid_state_transition",
            )
        previous_id = previous["status_id"]
        transition_verified = True
    elif args.state not in {"planned", "failed"}:
        raise RendezvousError(
            "non-initial state requires --previous-report",
            code="previous_status_required",
            hint="start with planned, then provide each prior report for the next transition",
        )
    report = {
        "schema": STATUS_SCHEMA,
        "card_id": card_verification["card_id"],
        "agent_id": agent_id,
        "role": args.role,
        "state": args.state,
        "observed_at": iso(utcnow()),
        "message": message,
        "previous_status_id": previous_id,
        "transition_verified": transition_verified,
        "safe_to_share": True,
        "contains_private_key": False,
    }
    signed = sign_object(report, id_field="status_id", secret=secret)
    write_json(signed, args.output, force=args.force_output)


def cmd_verify_status(args: argparse.Namespace) -> None:
    card = load_card(Path(args.card))
    secret = hmac_secret(args.hmac_env)
    card_verification = verify_card(
        card,
        expected_fingerprint=args.expected_fingerprint,
        secret=secret,
        allow_expired=True,
        require_hmac=args.require_hmac,
    )
    report = load_json_object(Path(args.status), maximum=MAX_STATUS_BYTES, label="status report")
    result = verify_status(
        report,
        card_id=card_verification["card_id"],
        secret=secret,
        require_hmac=args.require_hmac,
    )
    previous_id = report.get("previous_status_id")
    if previous_id is not None:
        if not args.previous_report:
            raise RendezvousError(
                "chained status requires --previous-report for transition verification",
                code="previous_status_required",
            )
        previous_report = load_json_object(
            Path(args.previous_report),
            maximum=MAX_STATUS_BYTES,
            label="previous status report",
        )
        previous = verify_status(
            previous_report,
            card_id=card_verification["card_id"],
            secret=secret,
            require_hmac=args.require_hmac,
        )
        if previous["status_id"] != previous_id:
            raise RendezvousError("previous status ID does not match chain", code="previous_status_mismatch")
        if previous["agent_id"] != result["agent_id"] or previous["role"] != result["role"]:
            raise RendezvousError("status chain changes agent or role", code="status_identity_mismatch")
        if result["state"] not in ALLOWED_TRANSITIONS[previous["state"]]:
            raise RendezvousError("status chain transition is invalid", code="invalid_state_transition")
        result["transition_from"] = previous["state"]
    elif args.previous_report:
        raise RendezvousError("initial status must not supply --previous-report", code="unexpected_previous_status")
    write_json({"valid": True, **result}, args.output, force=args.force_output)


def cmd_doctor(args: argparse.Namespace) -> None:
    source = Path(__file__).resolve()
    source_text = source.read_text(encoding="utf-8")
    forbidden_runtime_imports = [name for name in ("subprocess", "socket", "requests", "urllib.request") if re.search(rf"^\s*(?:import|from)\s+{re.escape(name)}\b", source_text, re.MULTILINE)]
    checks = {
        "python_3_10_or_newer": sys.version_info >= (3, 10),
        "no_network_or_subprocess_imports": not forbidden_runtime_imports,
        "source_is_regular_file": source.is_file() and not source.is_symlink(),
        "card_schema": SCHEMA,
        "status_schema": STATUS_SCHEMA,
        "version": VERSION,
    }
    ok = all(value is True or isinstance(value, str) for value in checks.values()) and not forbidden_runtime_imports
    result: dict[str, Any] = {"ok": ok, "checks": checks, "forbidden_imports": forbidden_runtime_imports}
    if args.card:
        result["card"] = verify_card(
            load_card(Path(args.card)),
            expected_fingerprint=args.expected_fingerprint,
            secret=hmac_secret(args.hmac_env),
            allow_expired=args.allow_expired,
            require_hmac=args.require_hmac,
        )
    write_json(result, args.output, force=args.force_output)
    if not ok:
        raise RendezvousError("doctor found a failed invariant", code="doctor_failed")


def add_common_output(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--output", help="write JSON to this path instead of stdout")
    parser.add_argument("--force-output", action="store_true", help="atomically replace an existing regular output file")


def add_ack(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--ack-authorized",
        action="store_true",
        help="confirm the domain, server, resolver, and service are owned or explicitly authorized",
    )


def add_card_auth(parser: argparse.ArgumentParser, *, operational: bool = False) -> None:
    parser.add_argument("--hmac-env", help="environment variable holding a 32+ byte coordination HMAC secret")
    if operational:
        parser.add_argument(
            "--allow-unsigned-card",
            action="store_true",
            help="explicitly allow an unsigned card for an authorized offline workflow",
        )
    else:
        parser.add_argument("--require-hmac", action="store_true", help="reject cards/status reports without HMAC authentication")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Plan and verify authorization-gated DNSTT rendezvous between cooperating agents")
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    parser.add_argument("--debug", action="store_true", help="emit bounded secret-free JSON debug events to stderr")
    parser.add_argument("--json-errors", action="store_true", help="emit machine-readable errors to stderr")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("server-card", help="create a short-lived public rendezvous card")
    p.add_argument("--agent-id", required=True)
    p.add_argument("--domain", required=True)
    p.add_argument("--pubkey-file", required=True)
    p.add_argument("--listen", default="0.0.0.0:5300")
    p.add_argument("--upstream", default="127.0.0.1:8000")
    p.add_argument("--expires-minutes", type=int, default=30, choices=range(5, 1441), metavar="5..1440")
    p.add_argument("--authorization-ref", required=True)
    p.add_argument("--purpose", default="authorized agent-to-agent TCP service")
    p.add_argument("--hmac-env")
    p.add_argument("--allow-nonloopback-upstream", action="store_true")
    p.add_argument("--allow-lan-client-listener", action="store_true")
    add_ack(p); add_common_output(p); p.set_defaults(func=cmd_server_card)

    p = sub.add_parser("verify-card", help="verify schema, integrity, expiry, fingerprint, and optional HMAC")
    p.add_argument("--card", required=True)
    p.add_argument("--expected-fingerprint")
    add_card_auth(p)
    p.add_argument("--allow-expired", action="store_true")
    add_common_output(p); p.set_defaults(func=cmd_verify)

    p = sub.add_parser("keygen-plan", help="print a reviewed key-generation command; never execute it")
    p.add_argument("--dnstt-server", default="dnstt-server")
    p.add_argument("--privkey-file", default="server.key")
    p.add_argument("--pubkey-file", default="server.pub")
    add_ack(p); add_common_output(p); p.set_defaults(func=cmd_keygen_plan)

    p = sub.add_parser("server-plan", help="print a server argv plan; never execute it")
    p.add_argument("--card", required=True)
    p.add_argument("--privkey-file", required=True)
    p.add_argument("--dnstt-server", default="dnstt-server")
    add_card_auth(p, operational=True)
    add_ack(p); add_common_output(p); p.set_defaults(func=cmd_server_plan)

    p = sub.add_parser("client-plan", help="print a client argv plan and public-key handoff; never execute it")
    p.add_argument("--card", required=True)
    p.add_argument("--expected-fingerprint", required=True)
    p.add_argument("--transport", choices=("udp", "doh", "dot"), default="udp")
    p.add_argument("--resolver", required=True)
    p.add_argument("--local-listen", default="127.0.0.1:7000")
    p.add_argument("--pubkey-file", default="server.pub")
    p.add_argument("--dnstt-client", default="dnstt-client")
    p.add_argument("--allow-lan-listener", action="store_true")
    add_card_auth(p, operational=True)
    add_ack(p); add_common_output(p); p.set_defaults(func=cmd_client_plan)

    p = sub.add_parser("diagnose", help="produce bounded read-only troubleshooting guidance")
    p.add_argument("--card", required=True)
    p.add_argument("--symptom", choices=tuple(DIAGNOSTICS), required=True)
    p.add_argument("--expected-fingerprint")
    add_card_auth(p)
    add_common_output(p); p.set_defaults(func=cmd_diagnose)

    p = sub.add_parser("status-report", help="create an authenticated secret-free state report")
    p.add_argument("--card", required=True)
    p.add_argument("--agent-id", required=True)
    p.add_argument("--role", choices=ROLES, required=True)
    p.add_argument("--state", choices=STATES, required=True)
    p.add_argument("--message", default="")
    p.add_argument("--previous-report")
    p.add_argument("--expected-fingerprint")
    p.add_argument("--allow-expired", action="store_true")
    add_card_auth(p)
    add_common_output(p); p.set_defaults(func=cmd_status)

    p = sub.add_parser("verify-status", help="verify a status report and its optional HMAC")
    p.add_argument("--card", required=True)
    p.add_argument("--status", required=True)
    p.add_argument("--previous-report", help="required when the status report links to a previous status ID")
    p.add_argument("--expected-fingerprint")
    add_card_auth(p)
    add_common_output(p); p.set_defaults(func=cmd_verify_status)

    p = sub.add_parser("doctor", help="run local, read-only implementation invariants")
    p.add_argument("--card")
    p.add_argument("--expected-fingerprint")
    p.add_argument("--allow-expired", action="store_true")
    add_card_auth(p)
    add_common_output(p); p.set_defaults(func=cmd_doctor)
    return parser


def main() -> int:
    global DEBUG_ENABLED
    parser = build_parser()
    args = parser.parse_args()
    DEBUG_ENABLED = bool(args.debug)
    debug_event("command_start", command=args.command, version=VERSION)
    try:
        args.func(args)
        debug_event("command_success", command=args.command)
        return 0
    except RendezvousError as exc:
        if args.json_errors:
            print(json.dumps(exc.as_dict(), ensure_ascii=False), file=sys.stderr)
        else:
            print(f"error[{exc.code}]: {exc}", file=sys.stderr)
            if exc.hint:
                print(f"hint: {exc.hint}", file=sys.stderr)
        debug_event("command_error", command=args.command, code=exc.code)
        return 2
    except BrokenPipeError:
        return 0
    except KeyboardInterrupt:
        print("interrupted", file=sys.stderr)
        return 130
    except OSError as exc:
        wrapped = RendezvousError(f"filesystem error: {exc}", code="filesystem_error")
        if args.json_errors:
            print(json.dumps(wrapped.as_dict(), ensure_ascii=False), file=sys.stderr)
        else:
            print(f"error[{wrapped.code}]: {wrapped}", file=sys.stderr)
        return 3
    except Exception as exc:  # fail closed at the CLI boundary; direct unit calls still expose bugs
        wrapped = RendezvousError(
            "unexpected internal error",
            code="internal_error",
            hint="rerun with --debug and report the command, version, and error type without secrets",
        )
        if args.json_errors:
            print(json.dumps(wrapped.as_dict(), ensure_ascii=False), file=sys.stderr)
        else:
            print(f"error[{wrapped.code}]: {wrapped} ({type(exc).__name__})", file=sys.stderr)
            if wrapped.hint:
                print(f"hint: {wrapped.hint}", file=sys.stderr)
        debug_event("internal_error", command=args.command, exception_type=type(exc).__name__)
        return 4


if __name__ == "__main__":
    sys.exit(main())
