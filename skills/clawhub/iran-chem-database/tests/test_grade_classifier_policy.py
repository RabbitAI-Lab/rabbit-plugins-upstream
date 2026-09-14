"""Tests for the configurable inclusion policy (guide §4)."""
from src.parser.grade_classifier import classify, GradeClassifier, normalize_text


def test_strict_mode_rejects_ambiguous():
    ok, reason, conf = classify({"title": "some chemical"}, "strict_research")
    assert not ok and reason == "ambiguous"


def test_all_catalogue_mode_accepts_ambiguous():
    ok, reason, conf = classify({"title": "some chemical"}, "all_catalogue")
    assert ok and reason == "all-identifiable-catalogue-mode"
    assert conf < 0.5


def test_old_mode_aliases_still_work():
    ok, reason, _ = classify({"title": "x"}, "all_catalogue")
    assert ok and reason == "all-identifiable-catalogue-mode"
    ok2, reason2, _ = classify({"title": "x"}, "strict_research")
    assert not ok2 and reason2 == "ambiguous"
    from src.parser.grade_classifier import canonical_mode
    assert canonical_mode("strict_research") == "research_only"
    assert canonical_mode("all_catalogue") == "all_identifiable_catalogue"
    assert canonical_mode("research_only") == "research_only"


def test_lab_or_research_accepts_ambiguity_only_for_lab_suppliers():
    rec = {"title": "some chemical"}
    ok, _, _ = classify(rec, "lab_or_research", supplier_is_lab=True)
    assert ok
    ok2, reason2, _ = classify(rec, "lab_or_research", supplier_is_lab=False)
    assert not ok2 and reason2 == "ambiguous"


def test_exclusion_wins_in_strict_and_lab_modes():
    for mode in ("strict_research", "lab_or_research"):
        ok, reason, _ = classify({"grade": "Industrial grade"}, mode, supplier_is_lab=True)
        assert not ok and reason == "excluded-grade-marker"


def test_all_catalogue_retains_industrial_grade_as_data():
    # remediation §5: identifiable records are retained (grade preserved), not deleted
    ok, reason, conf = classify({"grade": "Industrial grade"}, "all_catalogue")
    assert ok and reason == "excluded-grade-retained"
    assert conf < 0.5


def test_persian_variants_normalized():
    # Arabic yeh/kaf + ZWNJ variants all normalize to the Persian form
    n = normalize_text("گرید آزمایشگاهی\u200c\u064a\u0643")
    assert "\u200c" not in n
    assert "آزمایشگاهی" in n
    ok, reason, _ = classify({"grade": "گرید آزمايشگاهي"}, "strict_research")
    assert ok
    ok2, _, _ = classify({"grade": "درجه\u200cتحقیقاتی"}, "strict_research")
    assert ok2


def test_generic_pure_is_not_blanket_research_grade():
    ok, reason, _ = classify({"title": "خالص some solvent"}, "strict_research")
    assert not ok
    # but in all_catalogue it is accepted with low confidence
    ok2, reason2, conf2 = classify({"title": "خالص some solvent"}, "all_catalogue")
    assert ok2 and conf2 < 0.5


def test_purity_reason_names():
    ok, reason, _ = classify({"purity_numeric": 99.9}, "strict_research")
    assert ok and reason == "purity-threshold-99"
    ok, reason, _ = classify({"purity_numeric": 96.0}, "strict_research")
    assert ok and reason == "purity-threshold-95"


def test_classifier_instance_modes():
    gc = GradeClassifier(inclusion_mode="all_catalogue")
    ok, _, _ = gc.classify({"title": "x"})
    assert ok
    gc2 = GradeClassifier(inclusion_mode="strict_research")
    assert not gc2.classify({"title": "x"})[0]


def test_lab_supplier_heuristic():
    gc = GradeClassifier()
    assert gc.is_lab_supplier({"company_name_en": "Tehran Laboratory Chemicals Co."})
    assert not gc.is_lab_supplier({"company_name_en": "Bitumen Mining Corp."})
