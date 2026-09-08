"""v2.13 — agent-runnable verification of Iranian sellers.

These tests defend the property that matters: an agent must be able to reach
the Iranian-origin conclusion ITSELF from re-checkable evidence, and the
mechanism must fail CLOSED whenever the evidence is missing, foreign or forged.
"""
from __future__ import annotations

import pytest

from src.verification import (AgentVerdict, verify_channel, verify_dataset,
                              verify_listing_row)
from src.verification.agent_verify import (ATTESTATION_COLUMNS,
                                           attach_attestations, load_rows)
from src.verification.claims import (Claim, check_claim, check_national_id,
                                     check_phone_country_code,
                                     check_postal_code)


# --------------------------------------------------------------------------
# شناسه ملی (11-digit company ID) check-digit arithmetic
# --------------------------------------------------------------------------

def test_national_id_accepts_officially_documented_example():
    ok, detail = check_national_id("10380284790")
    assert ok, detail


@pytest.mark.parametrize("bad", [
    "10380284791",   # control digit tampered
    "1038028479",    # too short
    "103802847900",  # too long
    "11111111111",   # all identical digits
    "1038028479a",   # non-numeric
    "",
])
def test_national_id_rejects_invalid(bad):
    ok, _ = check_national_id(bad)
    assert not ok


# --------------------------------------------------------------------------
# Phone numbers: the strongest cheap signal, and the one that must not
# silently pass a foreign country.
# --------------------------------------------------------------------------

@pytest.mark.parametrize("num", [
    "+982188211234", "0098 21 8821 1234", "09121161187", "021-66565700",
])
def test_phone_accepts_iranian(num):
    ok, detail = check_phone_country_code(num)
    assert ok, detail


@pytest.mark.parametrize("num,cc", [
    ("+4961519720000", "DE"), ("+862112345678", "CN"),
    ("+971412345678", "AE"), ("+12125551234", "US"),
])
def test_phone_reports_foreign_country_code(num, cc):
    ok, detail = check_phone_country_code(num)
    assert not ok
    # The '-> XX' suffix is what the verdict parser reads to hard-disqualify.
    assert f"-> {cc}" in detail


def test_postal_code_rejects_leading_zero():
    assert check_postal_code("1968953591")[0]
    assert not check_postal_code("0968953591")[0]


def test_check_claim_never_raises_on_junk():
    for t in ("national_id", "phone_country_code", "postal_code", "cctld"):
        res = check_claim(Claim(t, "\x00 not a value \u200f"))
        assert res["supported"] is False


def test_unknown_claim_type_is_unsupported_not_an_error():
    res = check_claim(Claim("astrology_sign", "Leo"))
    assert res["supported"] is False


# --------------------------------------------------------------------------
# Fail-closed semantics
# --------------------------------------------------------------------------

def test_unknown_channel_defaults_to_deny():
    v = verify_channel("definitely_not_a_seeded_channel_xyz", level="offline")
    assert not v.verified
    assert v.score == 0
    assert "default deny" in v.reason


def test_known_multinational_is_disqualified():
    v = verify_channel("sigmaaldrich", level="offline")
    assert not v.verified


def test_row_without_channel_cannot_be_attributed():
    v = verify_listing_row({"canonical_name": "acetone"}, level="offline")
    assert not v.verified
    assert "no 'channel'" in v.reason


def test_dataset_with_unattributed_rows_is_not_safe():
    rep = verify_dataset([{"canonical_name": "acetone"}], level="offline")
    assert rep["safe_to_use"] is False


def test_empty_dataset_is_not_safe():
    assert verify_dataset([], level="offline")["safe_to_use"] is False


# --------------------------------------------------------------------------
# Real seeded suppliers
# --------------------------------------------------------------------------

def test_a_strong_supplier_verifies_offline():
    v = verify_channel("fanchem", level="offline")
    assert v.verified, v.reason
    assert v.country == "IR"
    assert len(set(v.families)) >= 2


def test_verdict_requires_two_independent_families():
    v = verify_channel("fanchem", level="offline")
    # A single family must never be enough, however heavy it is.
    assert len(set(v.families)) >= 2
    assert v.score >= 60


def test_explain_shows_its_working():
    text = verify_channel("fanchem", level="offline").explain()
    assert "PASS" in text
    assert "fanchem" in text


def test_verdict_serialises_to_json_safe_dict():
    import json
    d = verify_channel("fanchem", level="offline").as_dict()
    json.loads(json.dumps(d, ensure_ascii=False))
    assert {"subject", "verified", "score", "claims", "reason"} <= set(d)


# --------------------------------------------------------------------------
# Dataset + attestation round-trip
# --------------------------------------------------------------------------

def test_load_rows_strips_quoted_banner_comment(tmp_path):
    p = tmp_path / "x.csv"
    p.write_text('"# banner comment"\nchannel,name\nfanchem,acetone\n',
                 encoding="utf-8")
    rows = load_rows(str(p))
    assert len(rows) == 1
    assert rows[0]["channel"] == "fanchem"


def test_attestation_columns_are_attached(tmp_path):
    rows = [{"channel": "fanchem", "canonical_name": "acetone"}]
    out = attach_attestations(rows, level="offline")
    for col in ATTESTATION_COLUMNS:
        assert col in out[0]
    assert out[0]["supplier_verified"] == "true"
    assert out[0]["supplier_country"] == "IR"


def test_attested_rows_carry_recheckable_evidence():
    out = attach_attestations([{"channel": "fanchem"}], level="offline")
    ev = out[0]["supplier_verify_evidence"]
    assert "=" in ev  # claim_type=value pairs, not a badge


def test_unverified_supplier_is_marked_false_not_dropped():
    out = attach_attestations([{"channel": "labshop"}], level="offline")
    assert out[0]["supplier_verified"] == "false"


def test_dataset_report_counts_rows_per_supplier():
    rep = verify_dataset(
        [{"channel": "fanchem"}] * 3 + [{"channel": "labshop"}],
        level="offline")
    assert rep["row_counts"]["fanchem"] == 3
    assert rep["rows_total"] == 4
    assert rep["safe_to_use"] is False  # labshop is unproven -> fail closed


def test_verdict_dataclass_defaults_to_unverified():
    assert AgentVerdict(subject="x", level="offline", checked_at="t").verified is False
