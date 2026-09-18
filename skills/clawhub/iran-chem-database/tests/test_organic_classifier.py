"""Tests for the explicit organic classification (guide §8)."""
from src.parser.organic_classifier import (OrganicClassifier,
                                           formula_has_carbon_atom)


def test_structure_first_true():
    c = OrganicClassifier(network=False)
    status, reason, conf = c.classify({"canonical_smiles": "CCO"})  # ethanol
    assert status == "true" and reason == "structure" and conf > 0.9


def test_structure_first_false():
    c = OrganicClassifier(network=False)
    status, reason, conf = c.classify({"canonical_smiles": "[Na+].[Cl-]"})
    assert status == "false" and reason == "structure"


def test_formula_carbon_atom_tokenization():
    assert formula_has_carbon_atom("C2H6O")
    assert formula_has_carbon_atom("C21H18O5S")
    # chlorine is NOT carbon
    assert not formula_has_carbon_atom("Cl2Ni")
    assert not formula_has_carbon_atom("CaCl2")


def test_formula_carbonate_and_cyanide_are_inorganic():
    c = OrganicClassifier(network=False)
    for formula in ("Na2CO3", "KCN", "CO2", "NaHCO3", "CS2", "HCN"):
        status, reason, _ = c.classify({"molecular_formula": formula})
        assert status == "false", formula
        assert reason == "structure"


def test_unknown_when_nothing_resolvable():
    c = OrganicClassifier(network=False)
    status, reason, conf = c.classify({"title": "Mysterious brand X solvent"})
    assert status == "unknown" and reason is None


def test_cas_and_name_lookup_offline_returns_unknown():
    # network disabled → CAS/name resolution is skipped, status stays unknown
    c = OrganicClassifier(network=False)
    status, _, _ = c.classify({"cas_number": "64-17-5"})
    assert status == "unknown"


def test_elemental_carbon_is_not_organic():
    c = OrganicClassifier(network=False)
    status, _, _ = c.classify({"canonical_smiles": "C"})
    assert status == "false"
