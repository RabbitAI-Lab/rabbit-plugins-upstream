"""Research-grade classification filter (spec §4.4 — STRICT).

A molecule MUST be classified as research grade to enter the database.
Multi-signal approach: explicit grade label, purity threshold, brand
association, context clues — with an explicit EXCLUDE list. Ambiguous
entries are flagged for manual review but NOT included.
"""
from __future__ import annotations

import re
from typing import Optional

RESEARCH_GRADE_KEYWORDS = {
    "en": [
        "research grade", "reagent grade", "ACS grade", "ACS reagent",
        "analytical grade", "analytical reagent", "AR grade",
        "HPLC grade", "spectroscopic grade", "spectrophotometric grade",
        "GR grade", "guaranteed reagent", "for analysis",
        "for synthesis", "for research", "laboratory grade",
        "lab grade", "pro analysi", "p.a.", "puriss",
        "ultrapure", "semiconductor grade", "electronic grade",
        "molecular biology grade", "cell culture grade",
        "anhydrous", "dried", "extra pure", "high purity",
        "reference standard", "certified reference material",
        "pharmacopoeia grade", "USP", "BP", "EP", "JP",
    ],
    "fa": [
        "درجه تحقیقاتی", "درجه آزمایشگاهی", "درجه تجزیه‌ای",
        "خلوص بالا", "ویژه تحقیقات", "گرید آزمایشگاهی",
        "مرک", "سیگما", "گرید HPLC", "برای آنالیز",
        "درجه واکنشگر", "خالص", "فوق خالص",
    ],
}

EXCLUDE_GRADES = [
    "industrial grade", "technical grade", "commercial grade",
    "food grade", "feed grade", "construction grade",
    "درجه صنعتی", "درجه فنی", "درجه تجاری", "صنعتی",
]

RESEARCH_BRANDS = ["merck", "sigma-aldrich", "sigma aldrich", "fluka", "acros", "tci",
                   "supelco", "honeywell", "fisher scientific", "thermo scientific"]

# Bare grade tokens (matched against the grade label only, not free text)
BARE_GRADE_TOKENS = ("acs", "hplc", "gc", "ar", "gr", "usp", "bp", "ep", "jp", "puriss")


def _has_any(text: str, terms) -> bool:
    low = text.lower()
    return any(t.lower() in low for t in terms)


def _bare_grade_token(grade_label: str) -> bool:
    label = grade_label.strip().lower()
    if not label:
        return False
    # exact or word-boundary token match ("ACS", "ACS Reagent", "HPLC Grade", …)
    tokens = re.split(r"[^a-z.]+", label)
    return any(tok in BARE_GRADE_TOKENS for tok in tokens if tok)


def classify_as_research_grade(product_data: dict) -> tuple[bool, str]:
    """Return (is_research_grade, reason).

    Exclusion wins over everything; inclusion requires a positive signal.
    """
    text_fields = " ".join(str(v) for v in [
        product_data.get("grade", ""),
        product_data.get("purity", ""),
        product_data.get("description", ""),
        product_data.get("title", ""),
        product_data.get("name", ""),
        product_data.get("brand", ""),
        product_data.get("notes", ""),
    ]).strip()

    # 1) EXCLUDE if any industrial/technical/food grade marker found
    if _has_any(text_fields, EXCLUDE_GRADES):
        return False, "excluded-grade-marker"

    # 2) Positive signals
    grade_label = str(product_data.get("grade", "") or "")
    if _has_any(grade_label, RESEARCH_GRADE_KEYWORDS["en"] + RESEARCH_GRADE_KEYWORDS["fa"]):
        return True, "explicit-grade-label"
    if _bare_grade_token(grade_label):
        return True, "explicit-grade-token"

    if _has_any(text_fields, RESEARCH_GRADE_KEYWORDS["en"]):
        return True, "research-keyword"

    if _has_any(text_fields, RESEARCH_GRADE_KEYWORDS["fa"]):
        return True, "research-keyword-fa"

    # 3) Purity threshold: ≥95% numeric purity implies research grade
    purity_numeric = product_data.get("purity_numeric")
    try:
        if purity_numeric is not None and float(purity_numeric) >= 95.0:
            return True, "purity-threshold"
    except (TypeError, ValueError):
        pass

    # 4) Brand association (Merck/Sigma-distributed -> research grade)
    brand = str(product_data.get("brand", "") or "")
    if _has_any(brand, RESEARCH_BRANDS):
        return True, "research-brand"

    # 5) Context clues: sold for laboratory/research/analysis
    if re.search(r"\b(laboratory|research|analysis|analytical)\b", text_fields, re.I):
        return True, "context-clue"

    # Ambiguous → do NOT include
    return False, "ambiguous"


class GradeClassifier:
    def __init__(self) -> None:
        self._cache: dict[str, tuple[bool, str]] = {}

    def is_research_grade(self, product_data: dict) -> bool:
        key = str(sorted((k, str(v)) for k, v in product_data.items()))
        if key not in self._cache:
            self._cache[key] = classify_as_research_grade(product_data)
        return self._cache[key][0]

    def classify(self, product_data: dict) -> tuple[bool, str]:
        key = str(sorted((k, str(v)) for k, v in product_data.items()))
        if key not in self._cache:
            self._cache[key] = classify_as_research_grade(product_data)
        return self._cache[key]
