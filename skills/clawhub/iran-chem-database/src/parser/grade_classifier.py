"""Grade classification — selectable inclusion policy (fix guide §4).

Modes (config: parsing.inclusion_mode):
  * strict_research  — only explicit research/analytical-grade, high-purity,
                       or validated lab signals are accepted;
  * lab_or_research  — strict entries PLUS ambiguous items from suppliers
                       classified as laboratory-chemical suppliers (default);
  * all_catalogue    — all identifiable chemical catalogue entries; grade and
                       confidence are retained as data instead of discarding.

Every decision returns a (decision, reason, confidence) triple so callers can
record audit trails (RejectedCatalogueItem) instead of silently dropping rows.

Persian grade vocabulary is expanded and normalized (Arabic/Persian character
variants, ZWNJ/ZWSP removal) before matching. The generic Persian word for
"pure" is a confidence signal, not a blanket research-grade guarantee.
"""
from __future__ import annotations

import re
from typing import Optional, Tuple

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
        "Gradient HPLC", "isocratic hplc", "uv spectroscopy",
        "for microscopy", "standard material", "standard solution",
        "titrant", "indicator", "histology grade",
    ],
    "fa": [
        # research/lab grades
        "درجه تحقیقاتی", "گرید تحقیقاتی", "درجه آزمایشگاهی", "گرید آزمایشگاهی",
        "درجه تجزیه‌ای", "گرید تجزیه‌ای", "ویژه تحقیقات", "برای آنالیز",
        "برای آزمایشگاه", "گرید HPLC", "درجه واکنشگر", "گرید واکنشگر",
        "درجه مرجع", "استاندارد مرجع", "مواد استاندارد",
        "فوق خالص", "خالص آزمایشگاهی", "فوق العاده خالص",
        # common misspellings / spacing variants
        "درجه تحقيقاتي", "گرید تحقيقاتي", "درجه آزمايشگاهي", "گرید آزمايشگاهي",
        "درجه آزمایشگاهی", "گرید آزمایشگاهی", "درجه تجزیه ای", "گرید تجزیه ای",
        "درجه تحقیقاتی", "گریدتحقیقاتی", "گریدتحقیقاتى",
    ],
}

# Broad lab-context words (weaker signals, boost confidence only)
LAB_CONTEXT_FA = [
    "مواد شیمیایی آزمایشگاهی", "مواد آزمایشگاهی", "شیمیایی آزمایشگاهی",
    "آزمایشگاهی", "ویژه آزمایشگاه", "محیط آزمایشگاه",
]

# The generic word "pure" — signal, not a guarantee.
PURE_SIGNALS = ["خالص", "خالصسازی", "pur", "pure"]

EXCLUDE_GRADES = [
    "industrial grade", "technical grade", "commercial grade",
    "food grade", "feed grade", "construction grade",
    "agricultural grade", "practical grade",
    "درجه صنعتی", "گرید صنعتی", "درجه فنی", "گرید فنی", "درجه تجاری",
    "گرید تجاری", "صنعتی", "خوراکی", "غذایی", "درجه غذایی", "گرید غذایی",
    "درجه کشاورزی", "گرید کشاورزی",
]

RESEARCH_BRANDS = ["merck", "sigma-aldrich", "sigma aldrich", "fluka", "acros", "tci",
                   "supelco", "honeywell", "fisher scientific", "thermo scientific",
                   "carlo erba", "scharlau", "daejung", "samchun", "mojallali",
                   "دکتر مجللی", "مجللی", "مرک", "سیگما"]

LAB_SUPPLIER_MARKERS = ["laboratory", "lab", "reagent", "chemicals",
                        "آزمایشگاه", "مواد شیمیایی", "تجهیزات آزمایشگاهی"]

BARE_GRADE_TOKENS = ("acs", "hplc", "gc", "ar", "gr", "usp", "bp", "ep", "jp", "puriss")


def normalize_text(text: str) -> str:
    """Normalize Persian/Arabic character variants + zero-width chars."""
    if not text:
        return ""
    out = str(text)
    out = out.replace("\u064a", "\u06cc")   # Arabic yeh -> Persian yeh
    out = out.replace("\u0643", "\u06a9")   # Arabic kaf  -> Persian kaf
    out = out.replace("\u200c", " ")        # ZWNJ -> space
    out = out.replace("\u200d", " ")        # ZWJ  -> space
    out = out.replace("\u200f", "")         # RLM
    out = out.replace("\u200e", "")         # LRM
    out = out.replace("\ufeff", "")         # BOM
    out = out.replace("\u00a0", " ")        # NBSP
    out = re.sub(r"\s+", " ", out).strip()
    return out


def _has_any(text: str, terms) -> bool:
    low = text.lower()
    return any(normalize_text(t).lower() in low for t in terms)


def _bare_grade_token(grade_label: str) -> bool:
    label = normalize_text(grade_label).strip().lower()
    if not label:
        return False
    tokens = re.split(r"[^a-z.]+", label)
    return any(tok in BARE_GRADE_TOKENS for tok in tokens if tok)


def _purity_number(purity_numeric) -> Optional[float]:
    try:
        if purity_numeric is None:
            return None
        return float(purity_numeric)
    except (TypeError, ValueError):
        return None


# Mode aliases keep old configs working (remediation §5): the canonical names
# are research_only | lab_or_research | all_identifiable_catalogue.
_MODE_ALIASES = {
    "strict_research": "research_only",
    "research_only": "research_only",
    "lab_or_research": "lab_or_research",
    "all_catalogue": "all_identifiable_catalogue",
    "all_identifiable_catalogue": "all_identifiable_catalogue",
}


def canonical_mode(name: str | None) -> str:
    return _MODE_ALIASES.get((name or "").strip() or "research_only", "research_only")


def classify(product_data: dict, inclusion_mode: str = "research_only",
             supplier_is_lab: bool = False) -> Tuple[bool, str, float]:
    """Return (include, reason, confidence 0..1).

    `supplier_is_lab` activates the lab_or_research mode's ambiguity
    tolerance for entries from laboratory-chemical suppliers.
    """
    mode = canonical_mode(inclusion_mode)
    text_fields = " ".join(str(v) for v in [
        product_data.get("grade", ""),
        product_data.get("purity", ""),
        product_data.get("description", ""),
        product_data.get("title", ""),
        product_data.get("name", ""),
        product_data.get("brand", ""),
        product_data.get("notes", ""),
    ])
    text_fields = normalize_text(text_fields)

    # 1) Exclusion wins in strict/lab modes. In all_identifiable_catalogue the
    #    grade is RETAINED as data with low confidence (remediation §5: do not
    #    silently delete identifiable catalogue records).
    has_exclusion = _has_any(text_fields, EXCLUDE_GRADES)
    if has_exclusion and mode != "all_identifiable_catalogue":
        return False, "excluded-grade-marker", 0.0

    grade_label = normalize_text(str(product_data.get("grade", "") or ""))
    brand = normalize_text(str(product_data.get("brand", "") or ""))

    # 2) Strong positive signals (all modes)
    if _has_any(grade_label, RESEARCH_GRADE_KEYWORDS["en"] + RESEARCH_GRADE_KEYWORDS["fa"]):
        return True, "explicit-grade-label", 1.0
    if _bare_grade_token(grade_label):
        return True, "explicit-grade-token", 0.95
    if _has_any(brand, RESEARCH_BRANDS):
        return True, "research-brand", 0.9

    purity = _purity_number(product_data.get("purity_numeric"))
    if purity is not None and purity >= 99.0:
        return True, "purity-threshold-99", 0.95
    if purity is not None and purity >= 95.0:
        return True, "purity-threshold-95", 0.8

    if _has_any(text_fields, RESEARCH_GRADE_KEYWORDS["en"]):
        return True, "research-keyword", 0.7
    if _has_any(text_fields, RESEARCH_GRADE_KEYWORDS["fa"]):
        return True, "research-keyword-fa", 0.7

    lab_context = _has_any(text_fields, LAB_CONTEXT_FA)
    if re.search(r"\b(laboratory|research|analysis|analytical)\b", text_fields, re.I):
        return True, "context-clue", 0.6
    if lab_context:
        return True, "context-clue-fa", 0.6

    # 3) The generic "pure" word: confidence signal, not a guarantee
    has_pure_signal = _has_any(text_fields, PURE_SIGNALS)
    if has_pure_signal and purity is None:
        # only meaningful in permissive modes
        if mode == "all_identifiable_catalogue":
            return True, "pure-signal", 0.4
        if mode == "lab_or_research" and supplier_is_lab:
            return True, "pure-signal-lab-supplier", 0.4

    # 4) Mode-dependent handling of ambiguous entries
    if mode == "all_identifiable_catalogue":
        if has_exclusion:
            return True, "excluded-grade-retained", 0.2
        return True, "all-identifiable-catalogue-mode", 0.3
    if mode == "lab_or_research" and supplier_is_lab:
        return True, "lab-supplier-ambiguity", 0.3

    # Ambiguous → do NOT include
    return False, "ambiguous", 0.0


def classify_as_research_grade(product_data: dict) -> tuple[bool, str]:
    """Backwards-compatible strict wrapper (previous public API)."""
    ok, reason, _conf = classify(product_data, inclusion_mode="strict_research")
    return ok, reason


class GradeClassifier:
    """Caching classifier with configurable inclusion policy."""

    def __init__(self, inclusion_mode: str | None = None, supplier_is_lab: bool | None = None):
        try:
            from src.config import get_config
            cfg = get_config()
            parsing = cfg.as_dict().get("parsing", {}) or {}
            self.inclusion_mode = canonical_mode(inclusion_mode or parsing.get("inclusion_mode", "all_identifiable_catalogue"))
        except Exception:  # noqa: BLE001 (config unavailable in bare tests)
            self.inclusion_mode = canonical_mode(inclusion_mode or "all_identifiable_catalogue")
        self._supplier_is_lab = supplier_is_lab
        self._cache: dict[str, tuple[bool, str, float]] = {}

    def _cache_key(self, product_data: dict, supplier_is_lab: bool) -> str:
        return f"{self.inclusion_mode}|{supplier_is_lab}|" + str(
            sorted((k, str(v)) for k, v in product_data.items()))

    def classify(self, product_data: dict, supplier_is_lab: bool | None = None) -> tuple[bool, str, float]:
        lab = self._supplier_is_lab if supplier_is_lab is None else supplier_is_lab
        key = self._cache_key(product_data, bool(lab))
        if key not in self._cache:
            self._cache[key] = classify(product_data, self.inclusion_mode, bool(lab))
        return self._cache[key]

    def is_research_grade(self, product_data: dict) -> bool:
        return self.classify(product_data)[0]

    def is_lab_supplier(self, supplier: dict) -> bool:
        """Heuristic: is this supplier (row dict) a laboratory-chemical supplier?"""
        text = " ".join(str(supplier.get(k, "") or "") for k in
                         ("company_name_en", "company_name_fa", "supplier_type",
                          "specializations", "notes"))
        text = normalize_text(text)
        if isinstance(supplier.get("specializations"), list):
            text += " " + " ".join(str(x) for x in supplier["specializations"])
        return _has_any(text, LAB_SUPPLIER_MARKERS)
