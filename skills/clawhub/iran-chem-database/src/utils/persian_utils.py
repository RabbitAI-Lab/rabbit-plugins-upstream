"""Persian (Farsi) text utilities: normalization, numeral conversion, detection.

Uses hazm/parsivar when available; falls back to pure-stdlib implementations so
the rest of the pipeline never breaks.
"""
from __future__ import annotations

import re
import unicodedata

_FA_DIGITS = "۰۱۲۳۴۵۶۷۸۹"
_AR_DIGITS = "٠١٢٣٤٥٦٧٨٩"
_EN_DIGITS = "0123456789"


def fa_to_en_digits(text: str) -> str:
    """Convert Persian/Arabic digits to ASCII digits."""
    out = []
    for ch in text:
        if ch in _FA_DIGITS:
            out.append(_EN_DIGITS[_FA_DIGITS.index(ch)])
        elif ch in _AR_DIGITS:
            out.append(_EN_DIGITS[_AR_DIGITS.index(ch)])
        else:
            out.append(ch)
    return "".join(out)


def normalize_fa(text: str) -> str:
    """Normalize Persian text: NFC, ZWNJ handling, digit conversion, spacing."""
    if not text:
        return ""
    text = unicodedata.normalize("NFC", text)
    text = text.replace("\u200c", " ")          # ZWNJ -> space
    text = text.replace("\u200f", "").replace("\u200e", "")  # RTL/LTR marks
    text = fa_to_en_digits(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def detect_language(text: str) -> str:
    """Return 'fa' | 'en' | 'other' for a text snippet."""
    if not text:
        return "other"
    fa_hits = len(re.findall(r"[\u0600-\u06FF]", text))
    if fa_hits >= 1:
        return "fa"
    try:
        from langdetect import detect  # optional dependency
        return "en" if detect(text) == "en" else "other"
    except Exception:
        return "en"


def tokenize_fa(text: str) -> list[str]:
    """Tokenize Persian text (hazm if available, whitespace otherwise)."""
    try:
        from hazm import word_tokenize
        return word_tokenize(normalize_fa(text))
    except Exception:
        return normalize_fa(text).split()


def stem_fa(word: str) -> str:
    """Stem a Persian word (parsivar/hazm if available)."""
    try:
        from hazm import Stemmer
        return Stemmer().stem(word)
    except Exception:
        return word


def make_bilingual_search_terms(query: str) -> list[str]:
    """Build normalized search variants for bilingual (FA/EN) full-text search."""
    q = normalize_fa(query.strip())
    variants = [q]
    try:
        variants.append(" ".join(tokenize_fa(q)))
    except Exception:
        pass
    # remove exact duplicates, keep order
    seen, out = set(), []
    for v in variants:
        if v and v not in seen:
            seen.add(v)
            out.append(v)
    return out


def extract_persian_chemical_names(text: str) -> list[str]:
    """Heuristic: pull Persian phrases that look like chemical names.

    Matches a chemical signal word (اسید, هیدروکسید, سولفات, اتانول, …) with
    optional surrounding Persian words — e.g. 'اسید سولفوریک', 'هیدروکسید سدیم'.
    """
    signal = re.compile(
        r"(?:[\u0600-\u06FF]{0,12}\s*)?"
        r"(?:اسید|هیدروکسید|اکسید|کلرید|سولفات|نیترات|اتانول|متانول|استون|"
        r"بنزن|هگزان|سدیم|پتاسیم|کلسیم|آمونیوم|استات|کربنات|سیلیکات|سولفوریک)"
        r"(?:\s*[\u0600-\u06FF]{0,20})?"
    )
    matches = signal.findall(text)
    return [normalize_fa(m) for m in matches if len(normalize_fa(m)) > 1]
