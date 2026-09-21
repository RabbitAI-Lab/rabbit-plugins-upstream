"""Tests for the identity handling fix (guide §3)."""
import re

from src.database.identity import (build_source_identity, fallback_identity,
                                   is_valid_cas, is_valid_inchikey, normalize_cas)


def test_fallback_identity_is_exactly_27_chars():
    ident = fallback_identity("CAS-ONLY-RECORD|Ethanol|C2H6O")
    assert len(ident) == 27
    # deterministic
    assert ident == fallback_identity("CAS-ONLY-RECORD|Ethanol|C2H6O")
    # distinct from any real InChIKey pattern
    assert not is_valid_inchikey(ident)


def test_valid_cas_checksum():
    assert is_valid_cas("64-17-5")          # ethanol
    assert is_valid_cas("7732-18-5")        # water
    assert not is_valid_cas("64-17-6")      # bad checksum
    assert not is_valid_cas("200-075-1")    # an EC number, not a CAS
    assert not is_valid_cas("2-propanone")


def test_real_inchikey_wins():
    real = "LFQSCWFLJHTTHZ-UHFFFAOYSA-N"    # ethanol
    identity, inchi_key = build_source_identity({"inchi_key": real}, supplier_id=1)
    assert inchi_key == real
    assert identity == f"inchikey:{real}"


def test_cas_only_record_gets_cas_identity():
    identity, inchi_key = build_source_identity(
        {"cas_number": "64-17-5", "title": "Ethanol"}, supplier_id=1)
    assert identity == "cas:64-17-5"
    assert inchi_key is None  # never a fake InChIKey


def test_supplier_code_identity():
    identity, inchi_key = build_source_identity(
        {"title": "Ethanol", "supplier_product_code": "100983"}, supplier_id=7)
    assert identity == "sup:7:100983"
    assert inchi_key is None


def test_fallback_identity_never_claims_inchikey():
    identity, inchi_key = build_source_identity(
        {"title": "Sodium chloride", "molecular_formula": "NaCl"}, supplier_id=1)
    assert inchi_key is None
    assert identity.startswith("fallback-")
    assert len(identity) == 27
    # the legacy bug: 29 chars would have blown VARCHAR(27)
    assert len(identity) <= 27


def test_normalize_cas():
    assert normalize_cas(" 64-17-5 ") == "64-17-5"
    assert normalize_cas("invalid") == ""
