from __future__ import annotations

import base64
import json
from dataclasses import dataclass

import pytest
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

from sql_data_analyst_local.contracts import TicketEnvelope


TEST_KEY_ID = "local-2026-01"
TEST_SEED = b"\x01" * 32
TEST_PUBLIC_KEY = "iojj3XQJ8ZX9UtstPLpdcspnCb8dlBIb83SIAbQPb1w="
TEST_SIGNED_PAYLOAD = (
    '{"billing_units":1,"charged_amount":"0.080000","currency":"CNY",'
    '"execution_id":"018f47a2-7b2b-7e47-8794-c11316f5023b",'
    '"expires_at":"2026-08-24T00:05:00Z",'
    '"input_fingerprint":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",'
    '"installation_id":"018f47a2-7b2b-7e47-8794-c11316f5023c",'
    '"issued_at":"2026-08-24T00:00:00Z","operation":"query.execute",'
    '"runner_min_version":"1.0.0","schema_version":1}'
)
TEST_SIGNATURE = (
    "v00afhdUKW/C8vRNuX4PIKrJPfe3iaNyr+AzBGf+C/bVIJm3bRcyFaZGuREeiOt9"
    "YgqMy5MNRgEdOnelZ67tBw=="
)


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def sign_payload(claims: dict[str, object]) -> TicketEnvelope:
    payload = canonical_json(claims)
    return sign_raw_payload(payload)


def sign_raw_payload(payload: str) -> TicketEnvelope:
    signature = Ed25519PrivateKey.from_private_bytes(TEST_SEED).sign(payload.encode())
    return TicketEnvelope(
        key_id=TEST_KEY_ID,
        signed_payload=payload,
        signature=base64.b64encode(signature).decode("ascii"),
    )


@dataclass(frozen=True)
class TicketFixture:
    public_keys: dict[str, str]
    envelope: TicketEnvelope
    claims: dict[str, object]


@pytest.fixture
def ticket_fixture() -> TicketFixture:
    claims = json.loads(TEST_SIGNED_PAYLOAD)
    return TicketFixture(
        public_keys={TEST_KEY_ID: TEST_PUBLIC_KEY},
        envelope=TicketEnvelope(
            key_id=TEST_KEY_ID,
            signed_payload=TEST_SIGNED_PAYLOAD,
            signature=TEST_SIGNATURE,
        ),
        claims=claims,
    )
