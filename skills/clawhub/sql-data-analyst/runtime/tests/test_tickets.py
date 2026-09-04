from __future__ import annotations

import base64
import json
from datetime import datetime, timedelta, timezone
from uuid import UUID

import pytest

from conftest import canonical_json, sign_payload, sign_raw_payload
from sql_data_analyst_local.contracts import ExpectedTicket, TicketEnvelope
from sql_data_analyst_local.tickets import (
    TicketError,
    TicketVerifier,
    load_trusted_keys,
)


NOW = datetime(2026, 8, 24, tzinfo=timezone.utc)
INSTALLATION_ID = UUID("018f47a2-7b2b-7e47-8794-c11316f5023c")


def expected_ticket(**changes: object) -> ExpectedTicket:
    values: dict[str, object] = {
        "operation": "query.execute",
        "installation_id": INSTALLATION_ID,
        "input_fingerprint": "a" * 64,
        "runner_version": "1.0.0",
    }
    values.update(changes)
    return ExpectedTicket(**values)


def test_verifier_binds_operation_installation_fingerprint_expiry(ticket_fixture):
    claims = TicketVerifier(ticket_fixture.public_keys).verify(
        ticket_fixture.envelope,
        expected_ticket(),
        now=NOW,
    )

    assert claims.execution_id == UUID("018f47a2-7b2b-7e47-8794-c11316f5023b")
    assert claims.charged_amount == "0.080000"
    assert claims.currency == "CNY"


@pytest.mark.parametrize(
    "field,replacement",
    [
        ("schema_version", 2),
        ("execution_id", "018f47a2-7b2b-7e47-8794-c11316f5023d"),
        ("operation", "analysis.run"),
        ("installation_id", "018f47a2-7b2b-7e47-8794-c11316f5023d"),
        ("input_fingerprint", "b" * 64),
        ("billing_units", 0),
        ("charged_amount", "0.090000"),
        ("currency", "USD"),
        ("runner_min_version", "1.1.0"),
        ("issued_at", "2026-08-24T00:00:01Z"),
        ("expires_at", "2026-08-24T00:05:01Z"),
    ],
)
def test_verifier_rejects_each_unsigned_payload_tamper_without_echoing_payload(
    ticket_fixture, field, replacement
):
    claims = dict(ticket_fixture.claims)
    claims[field] = replacement
    tampered_payload = canonical_json(claims)
    envelope = ticket_fixture.envelope.model_copy(
        update={"signed_payload": tampered_payload}
    )

    with pytest.raises(TicketError) as caught:
        TicketVerifier(ticket_fixture.public_keys).verify(
            envelope, expected_ticket(), now=NOW
        )

    assert str(caught.value) == "authorization_invalid"
    assert tampered_payload not in str(caught.value)


@pytest.mark.parametrize(
    "change",
    [
        {"operation": "analysis.run"},
        {"installation_id": UUID("018f47a2-7b2b-7e47-8794-c11316f5023d")},
        {"input_fingerprint": "b" * 64},
        {"runner_version": "0.9.9"},
    ],
)
def test_verifier_rejects_valid_ticket_when_expected_binding_differs(
    ticket_fixture, change
):
    with pytest.raises(TicketError, match="^authorization_invalid$"):
        TicketVerifier(ticket_fixture.public_keys).verify(
            ticket_fixture.envelope, expected_ticket(**change), now=NOW
        )


def test_verifier_maps_expired_ticket_to_stable_error_without_payload(ticket_fixture):
    with pytest.raises(TicketError) as caught:
        TicketVerifier(ticket_fixture.public_keys).verify(
            ticket_fixture.envelope,
            expected_ticket(),
            now=NOW + timedelta(minutes=5),
        )

    assert str(caught.value) == "authorization_expired"
    assert ticket_fixture.envelope.signed_payload not in str(caught.value)


@pytest.mark.parametrize(
    "envelope",
    [
        TicketEnvelope(key_id="unknown", signed_payload="{}", signature=base64.b64encode(b"x" * 64).decode()),
        TicketEnvelope(key_id="local-2026-01", signed_payload="{}", signature="not-base64"),
        TicketEnvelope(key_id="local-2026-01", signed_payload="{}", signature=base64.b64encode(b"short").decode()),
    ],
)
def test_verifier_rejects_unknown_key_and_bad_signature_encoding(ticket_fixture, envelope):
    with pytest.raises(TicketError, match="^authorization_invalid$"):
        TicketVerifier(ticket_fixture.public_keys).verify(
            envelope, expected_ticket(), now=NOW
        )


@pytest.mark.parametrize(
    "updates",
    [
        {"extra": "not allowed"},
        {"schema_version": 2},
        {"expires_at": "2026-08-24T00:06:00Z"},
        {"issued_at": "2026-08-24T00:00:01+00:00"},
        {"charged_amount": "0.08"},
        {"charged_amount": "-0.080000"},
        {"currency": "USD"},
    ],
)
def test_verifier_rejects_signed_noncanonical_claims(ticket_fixture, updates):
    claims = dict(ticket_fixture.claims)
    claims.update(updates)

    with pytest.raises(TicketError, match="^authorization_invalid$"):
        TicketVerifier(ticket_fixture.public_keys).verify(
            sign_payload(claims), expected_ticket(), now=NOW
        )


def test_ticket_schema_error_suppresses_signed_payload_validation_details(ticket_fixture):
    claims = dict(ticket_fixture.claims)
    claims["private_input"] = ticket_fixture.envelope.signed_payload

    with pytest.raises(TicketError) as caught:
        TicketVerifier(ticket_fixture.public_keys).verify(
            sign_payload(claims), expected_ticket(), now=NOW
        )

    assert caught.value.__cause__ is None
    assert caught.value.__suppress_context__ is True


def test_verifier_rejects_noncanonical_signed_json(ticket_fixture):
    payload = json.dumps(ticket_fixture.claims, sort_keys=False)

    with pytest.raises(TicketError, match="^authorization_invalid$"):
        TicketVerifier(ticket_fixture.public_keys).verify(
            sign_raw_payload(payload), expected_ticket(), now=NOW
        )


def test_default_verifier_fails_closed_without_release_trusted_keys():
    with pytest.raises(TicketError, match="^authorization_invalid$"):
        load_trusted_keys()

    with pytest.raises(TicketError, match="^authorization_invalid$"):
        TicketVerifier()
