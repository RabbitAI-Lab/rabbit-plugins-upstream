"""Tests for the research-grade classification filter (spec §4.4)."""
from src.parser.grade_classifier import classify_as_research_grade, GradeClassifier


def test_explicit_acs_grade():
    ok, reason = classify_as_research_grade({"grade": "ACS Reagent"})
    assert ok and reason == "explicit-grade-label"


def test_hplc_grade():
    ok, _ = classify_as_research_grade({"grade": "HPLC Grade"})
    assert ok


def test_persian_grade_label():
    ok, _ = classify_as_research_grade({"grade": "گرید آزمایشگاهی"})
    assert ok


def test_purity_threshold():
    ok, reason = classify_as_research_grade({"purity_numeric": 99.9})
    assert ok and reason == "purity-threshold-99"


def test_industrial_grade_excluded():
    ok, reason = classify_as_research_grade({"grade": "Industrial Grade"})
    assert not ok and reason == "excluded-grade-marker"


def test_industrial_beats_purity():
    ok, _ = classify_as_research_grade({"grade": "Technical grade", "purity_numeric": 99.9})
    assert not ok


def test_ambiguous_rejected():
    ok, reason = classify_as_research_grade({"title": "some chemical"})
    assert not ok and reason == "ambiguous"


def test_merck_brand():
    ok, reason = classify_as_research_grade({"brand": "Merck"})
    assert ok and reason == "research-brand"


def test_classifier_caches():
    gc = GradeClassifier()
    rec = {"grade": "ACS"}
    assert gc.is_research_grade(rec)
    assert gc.is_research_grade(rec)
    assert gc.classify(rec)[0]
