from __future__ import annotations

import base64
import binascii
import hashlib
import hmac
import json
import re
from datetime import datetime, timedelta, timezone
from importlib.resources import files
from typing import Mapping

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
from packaging.version import InvalidVersion, Version
from pydantic import ValidationError

from sql_data_analyst_local.contracts import (
    KEY_ID_PATTERN,
    ExpectedTicket,
    TicketClaims,
    TicketEnvelope,
)
from sql_data_analyst_local.settings import TRUSTED_KEYS_SHA256


_SIGNATURE_BYTES = 64
_PUBLIC_KEY_BYTES = 32
_TICKET_TTL = timedelta(seconds=300)
_UTC_TIMESTAMP = re.compile(r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)$")
_RELEASE_VERSION = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
_AMOUNT = re.compile(r"^(?:0|[1-9]\d*)\.\d{6}$")
_KEY_ID = re.compile(KEY_ID_PATTERN)


class TicketError(RuntimeError):
    """A ticket failure that never carries remote or signed content."""

    def __init__(self, code: str = "authorization_invalid") -> None:
        if code not in {"authorization_invalid", "authorization_expired"}:
            code = "authorization_invalid"
        self.code = code
        super().__init__(code)


def _canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def trusted_key_bundle_sha256(public_keys: Mapping[str, str]) -> str:
    canonical = _canonical_json(dict(public_keys)).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def load_trusted_keys(expected_sha256: str | None = None) -> dict[str, str]:
    try:
        raw = files("sql_data_analyst_local").joinpath("trusted_keys.json").read_text(
            encoding="utf-8"
        )
        value = json.loads(raw)
    except (OSError, UnicodeError, json.JSONDecodeError):
        raise TicketError() from None
    if (
        not isinstance(value, dict)
        or not value
        or not all(isinstance(key, str) and isinstance(item, str) for key, item in value.items())
    ):
        raise TicketError()
    public_keys = dict(value)
    if expected_sha256 is not None:
        if not re.fullmatch(r"[a-f0-9]{64}", expected_sha256) or not hmac.compare_digest(
            trusted_key_bundle_sha256(public_keys), expected_sha256
        ):
            raise TicketError()
    return public_keys


class TicketVerifier:
    def __init__(self, public_keys: Mapping[str, str] | None = None) -> None:
        source = (
            load_trusted_keys(TRUSTED_KEYS_SHA256)
            if public_keys is None
            else dict(public_keys)
        )
        if not source:
            raise TicketError()
        decoded: dict[str, bytes] = {}
        for key_id, encoded_key in source.items():
            if not isinstance(key_id, str) or _KEY_ID.fullmatch(key_id) is None:
                raise TicketError()
            if not isinstance(encoded_key, str):
                raise TicketError()
            try:
                public_key = base64.b64decode(encoded_key, validate=True)
            except (binascii.Error, ValueError):
                raise TicketError() from None
            if len(public_key) != _PUBLIC_KEY_BYTES:
                raise TicketError()
            decoded[key_id] = public_key
        self._public_keys = decoded

    def verify(
        self,
        envelope: TicketEnvelope,
        expected: ExpectedTicket,
        now: datetime,
    ) -> TicketClaims:
        signature = self._decode_signature(envelope.signature)

        public_key_bytes = self._public_keys.get(envelope.key_id)
        if public_key_bytes is None:
            raise TicketError()

        try:
            Ed25519PublicKey.from_public_bytes(public_key_bytes).verify(
                signature, envelope.signed_payload.encode("utf-8")
            )
        except (InvalidSignature, ValueError, UnicodeError):
            raise TicketError() from None

        claims = self._parse_claims(envelope.signed_payload)
        issued_at = self._timestamp(claims.issued_at)
        expires_at = self._timestamp(claims.expires_at)
        current_time = self._current_time(now)
        if expires_at - issued_at != _TICKET_TTL or issued_at > current_time:
            raise TicketError()
        if current_time >= expires_at:
            raise TicketError("authorization_expired")

        if self._version(expected.runner_version) < self._version(
            claims.runner_min_version
        ):
            raise TicketError()
        if claims.operation != expected.operation:
            raise TicketError()
        if claims.installation_id != expected.installation_id:
            raise TicketError()
        if not hmac.compare_digest(
            claims.input_fingerprint, expected.input_fingerprint
        ):
            raise TicketError()
        if claims.currency != "CNY" or _AMOUNT.fullmatch(claims.charged_amount) is None:
            raise TicketError()
        return claims

    @staticmethod
    def _decode_signature(encoded: str) -> bytes:
        try:
            signature = base64.b64decode(encoded, validate=True)
        except (binascii.Error, ValueError):
            raise TicketError() from None
        if len(signature) != _SIGNATURE_BYTES:
            raise TicketError()
        return signature

    @staticmethod
    def _parse_claims(payload: str) -> TicketClaims:
        try:
            value = json.loads(payload)
            if not isinstance(value, dict) or _canonical_json(value) != payload:
                raise TicketError()
            return TicketClaims.model_validate(value)
        except (json.JSONDecodeError, ValidationError, TypeError, ValueError):
            raise TicketError() from None

    @staticmethod
    def _timestamp(value: str) -> datetime:
        if _UTC_TIMESTAMP.fullmatch(value) is None:
            raise TicketError()
        try:
            return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=timezone.utc
            )
        except ValueError:
            raise TicketError() from None

    @staticmethod
    def _current_time(value: datetime) -> datetime:
        if value.tzinfo is None or value.utcoffset() is None:
            raise TicketError()
        return value.astimezone(timezone.utc)

    @staticmethod
    def _version(value: str) -> Version:
        if _RELEASE_VERSION.fullmatch(value) is None:
            raise TicketError()
        try:
            return Version(value)
        except InvalidVersion:
            raise TicketError() from None
