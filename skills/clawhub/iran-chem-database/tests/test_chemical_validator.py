"""Tests for CAS checksum + RDKit validation."""
from src.parser.chemical_validator import ChemicalValidator
from src.utils.chemistry_utils import is_valid_cas, canonicalize_smiles, smiles_to_inchikey, smiles_to_formula


def test_cas_checksum_valid():
    assert is_valid_cas("64-17-5")      # ethanol
    assert is_valid_cas("7732-18-5")    # water


def test_cas_checksum_invalid():
    assert not is_valid_cas("64-17-6")
    assert not is_valid_cas("bad")


def test_smiles_canonicalization():
    canon = canonicalize_smiles("CCO")
    assert canon == "CCO"


def test_smiles_invalid():
    assert canonicalize_smiles("not-a-smiles") is None


def test_smiles_to_inchikey():
    key = smiles_to_inchikey("CCO")
    assert key == "LFQSCWFLJHTTHZ-UHFFFAOYSA-N"


def test_smiles_to_formula():
    assert smiles_to_formula("CCO") == "C2H6O"


def test_validator_enriches_smiles():
    v = ChemicalValidator()
    out = v.validate({"canonical_smiles": "CCO"})
    assert out is not None
    assert out["inchi_key"] == "LFQSCWFLJHTTHZ-UHFFFAOYSA-N"
    assert out["molecular_formula"] == "C2H6O"


def test_validator_rejects_garbage():
    v = ChemicalValidator()
    assert v.validate({"title": "no chemistry at all"}) is None


def test_validator_flags_invalid_cas():
    v = ChemicalValidator()
    out = v.validate({"title": "x", "cas_number": "64-17-6", "canonical_smiles": "CCO"})
    assert out is not None
    assert "invalid-cas" in out["_validation_problems"]
