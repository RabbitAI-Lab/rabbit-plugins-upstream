"""Structured field extraction from Iranian supplier Telegram posts — v2.12.

Why this module exists
----------------------
Until v2.11 a post became a listing only if the curated alias dictionary
matched a name inside it. Everything else was rejected as
``no_alias_or_cas_match`` — 3,256 posts in the live corpus. Sampling those
rejections showed the loss was not noise but the single most valuable post
shape on the whole network, the **structured catalogue line**:

    006123 Exir Melamine, 99% 500g
    🔜 موجود و آماده تحویل ✅ شیمیران صنعت فقط اصلی
    📱 سفارش کالا 👇 🆔 @ChemIranAdmin

That one post carries a supplier SKU, a brand, an IUPAC name, a purity and a
pack size — and the alias dictionary threw it away because "Melamine" was not
in the dictionary. Growing the dictionary is a treadmill; parsing the *shape*
is not.

This module extracts fields, and deliberately does NOT decide identity — that
stays in :mod:`src.parser.social_molecule_resolver`. It answers "what does this
post say?", so the resolver can answer "what molecule is that?".

Fields recovered
----------------
``sku``            supplier catalogue code (``006123``, ``M-2214``)
``brand``          Merck, Sigma-Aldrich, Exir, Daejung, TCI, …
``product_name``   the Latin chemical name, cleaned of brand/grade/pack noise
``purity``         99, 99.5, 98 (percent)
``grade_token``    USP, GR, AR, HPLC, ACS, EP, BP, extra pure, …
``pack_size``      value + unit, normalised to grams / millilitres
``cas_numbers``    checksum-validated CAS registry numbers
``price``          delegated to the hardened price parser
``availability``   in stock / to order / unavailable (Persian phrasing)

Everything is optional; extraction never raises and never invents a value.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from src.parser.persian_gate import fa_digits_to_en, normalize_persian

# ---------------------------------------------------------------------------
# Brands. Presence of a brand is a strong "this is a product post" signal; the
# brand itself is PRODUCT metadata and never implies a foreign supplier (see
# the country gate's supplier-vs-brand rule).
# ---------------------------------------------------------------------------
BRANDS: Dict[str, str] = {
    # foreign manufacturers commonly imported into Iran
    "merck": "Merck", "مرک": "Merck", "مرك": "Merck", "مركك": "Merck",
    "sigma": "Sigma-Aldrich", "sigma-aldrich": "Sigma-Aldrich",
    "سیگما": "Sigma-Aldrich", "سیگما آلدریچ": "Sigma-Aldrich",
    "aldrich": "Sigma-Aldrich", "آلدریچ": "Sigma-Aldrich",
    "fluka": "Fluka", "فلوکا": "Fluka",
    "tci": "TCI", "تی سی آی": "TCI",
    "acros": "Acros", "آکروس": "Acros",
    "alfa": "Alfa Aesar", "alfa aesar": "Alfa Aesar", "آلفا": "Alfa Aesar",
    "daejung": "Daejung", "دایجونگ": "Daejung", "دجونگ": "Daejung",
    "samchun": "Samchun", "سامچون": "Samchun",
    "duksan": "Duksan", "دوکسان": "Duksan",
    "carlo erba": "Carlo Erba", "carloerba": "Carlo Erba",
    "carl roth": "Carl Roth", "roth": "Carl Roth",
    "applichem": "AppliChem", "panreac": "Panreac",
    "honeywell": "Honeywell", "riedel": "Riedel-de Haen",
    "thermo": "Thermo Fisher", "fisher": "Thermo Fisher",
    "gibco": "Gibco", "گیبکو": "Gibco",
    "bdh": "BDH", "vwr": "VWR", "scharlau": "Scharlau", "شارلو": "Scharlau",
    "loba": "Loba Chemie", "لوبا": "Loba Chemie",
    "himedia": "HiMedia", "هایمدیا": "HiMedia",
    "qiagen": "Qiagen", "biobasic": "Bio Basic", "bio basic": "Bio Basic",
    "santa cruz": "Santa Cruz", "fluorochem": "Fluorochem",
    "chem-lab": "Chem-Lab", "chemlab": "Chem-Lab",
    "kanto": "Kanto", "wako": "Wako", "junsei": "Junsei",
    # Iranian producers/house brands
    "exir": "Exir", "اکسیر": "Exir",
    "mojallali": "Mojallali", "مجللی": "Mojallali",
    "dr mojallali": "Mojallali", "دکتر مجللی": "Mojallali",
    "temad": "Temad", "تماد": "Temad",
    "pars": "Pars", "شیمی پژوهش": "Shimi Pajouhesh",
    "زرین": "Zarrin", "کیمیا": "Kimia",
}
_BRAND_RE = re.compile(
    r"(?<![A-Za-z\u0600-\u06FF])(" +
    "|".join(sorted((re.escape(b) for b in BRANDS), key=len, reverse=True)) +
    r")(?![A-Za-z\u0600-\u06FF])", re.I)

# ---------------------------------------------------------------------------
# Grades / purity / pack sizes
# ---------------------------------------------------------------------------
GRADE_TOKENS = (
    "HPLC", "GC", "ACS", "USP", "BP", "EP", "JP", "GR", "AR", "LR", "CP",
    "puriss", "purum", "pract", "techn", "reagent grade", "analytical grade",
    "extra pure", "for analysis", "for synthesis", "molecular biology",
    "cell culture", "food grade", "pharma grade", "انالار", "گرید صنعتی",
    "گرید آزمایشگاهی", "خوراکی", "دارویی", "صنعتی", "آزمایشگاهی",
)
_GRADE_RE = re.compile(
    r"(?<![A-Za-z])(" + "|".join(re.escape(g) for g in
                                 sorted(GRADE_TOKENS, key=len, reverse=True)) +
    r")(?![A-Za-z])", re.I)

# Purity: "99%", ">=99.5 %", "99.9٪", "خلوص ۹۸ درصد"
_PURITY_RE = re.compile(
    r"(?:خلوص\s*)?(?:>=|>|≥|~|\+/-|min\.?|حداقل)?\s*"
    r"(\d{2}(?:\.\d{1,3})?)\s*(?:%|٪|درصد)")

#: unit -> (canonical unit, multiplier to base g / ml)
_PACK_UNITS = {
    "kg": ("g", 1000.0), "kilo": ("g", 1000.0), "kilogram": ("g", 1000.0),
    "کیلوگرم": ("g", 1000.0), "کیلو": ("g", 1000.0),
    "g": ("g", 1.0), "gr": ("g", 1.0), "gram": ("g", 1.0),
    "گرم": ("g", 1.0), "گرمی": ("g", 1.0),
    "mg": ("g", 0.001), "میلی گرم": ("g", 0.001),
    "l": ("ml", 1000.0), "lit": ("ml", 1000.0), "liter": ("ml", 1000.0),
    "litre": ("ml", 1000.0), "لیتر": ("ml", 1000.0), "لیتری": ("ml", 1000.0),
    "ml": ("ml", 1.0), "cc": ("ml", 1.0), "میلی لیتر": ("ml", 1.0),
    "میلیلیتر": ("ml", 1.0),
}
_PACK_RE = re.compile(
    r"(?<![\w.])(\d{1,4}(?:[.,]\d{1,3})?)\s*"
    r"(kg|kilogram|kilo|کیلوگرم|کیلو|mg|میلی\s?گرم|gram|gr|g|گرمی|گرم|"
    r"litre|liter|lit|l|لیتری|لیتر|ml|cc|میلی\s?لیتر|میلیلیتر)"
    r"(?![A-Za-z\u0600-\u06FF])", re.I)

# Supplier SKU: 5-7 digit code, or letter-digit catalogue code.
_SKU_RE = re.compile(r"(?<![\w.])(\d{6,7}|[A-Z]{1,3}[-–]?\d{3,6})(?![\w%.])")

_CAS_RE = re.compile(r"(?<!\d)(\d{2,7})-(\d{2})-(\d)(?!\d)")

AVAILABILITY = {
    "in_stock": ("موجود", "موجوده", "آماده تحویل", "موجودی", "in stock",
                 "available", "درانبار", "در انبار"),
    "to_order": ("سفارشی", "پیش سفارش", "قابل سفارش", "to order", "on order",
                 "وارداتی سفارش"),
    "unavailable": ("ناموجود", "اتمام موجودی", "تمام شد", "out of stock"),
}

# Words that look like chemical names but are not (channel/UI/marketing noise).
_NAME_STOPLIST = {
    "phone", "admin", "telegram", "instagram", "whatsapp", "channel", "group",
    "polyzone", "unitree", "ithenticate", "link", "click", "order", "price",
    "contact", "info", "email", "website", "www", "http", "https", "com",
    "ir", "co", "org", "net", "shop", "store", "company", "co ltd", "ltd",
    "iran", "tehran", "delivery", "free", "new", "offer", "sale", "stock",
    "available", "quality", "product", "products", "material", "materials",
    "chemical", "chemicals", "lab", "laboratory", "grade", "pure", "purity",
    "size", "pack", "packing", "bottle", "drum", "bag", "kg", "gr", "ml",
}

# Morphology that marks a token run as a plausible chemical name.
_CHEM_MORPHOLOGY = re.compile(
    r"(acid|ate\b|ide\b|ine\b|ol\b|one\b|ene\b|ane\b|yne\b|yl\b|amine|amide|"
    r"oxide|hydroxide|chlorid|chloro|sulfat|sulfate|sulphate|sulfon|nitrat|"
    r"nitro|phosph|carbonat|carbon|acetat|acetate|benz|phenyl|phenol|methyl|"
    r"ethyl|propyl|butyl|hexan|pentan|octan|toluen|xylen|ether|ester|alcohol|"
    r"aldehyd|keton|glyc|citrat|citric|borat|silan|silic|titan|zinc|copper|"
    r"sodium|potassium|calcium|magnesium|ammonium|lithium|barium|iron|nickel|"
    r"cobalt|mangan|chromi|alumin|ferric|ferrous|cupric|argent|plumb)", re.I)


_CAS_PLAIN_RE = re.compile(r"^(\d{2,7})-(\d{2})-(\d)$")


def _cas_checksum_ok(cas: str) -> bool:
    """Validate a CAS number's check digit — kills phone/date false positives."""
    m = _CAS_PLAIN_RE.match(cas.strip())
    if not m:
        return False
    body = (m.group(1) + m.group(2))[::-1]
    total = sum(int(d) * (i + 1) for i, d in enumerate(body))
    return total % 10 == int(m.group(3))


def extract_cas_numbers(text: str) -> List[str]:
    """All checksum-valid CAS numbers in the post, order-preserved."""
    out, seen = [], set()
    for m in _CAS_RE.finditer(fa_digits_to_en(text or "")):
        cas = f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
        if cas in seen:
            continue
        seen.add(cas)
        if _cas_checksum_ok(cas):
            out.append(cas)
    return out


def extract_brand(text: str) -> Optional[str]:
    m = _BRAND_RE.search(normalize_persian(text or ""))
    return BRANDS.get(m.group(1).lower()) if m else None


def extract_purity(text: str) -> Optional[float]:
    best = None
    for m in _PURITY_RE.finditer(fa_digits_to_en(normalize_persian(text or ""))):
        try:
            val = float(m.group(1))
        except ValueError:
            continue
        # Purity below 50% is almost always a concentration or a discount.
        if 50.0 <= val <= 100.0 and (best is None or val > best):
            best = val
    return best


def extract_grade_token(text: str) -> Optional[str]:
    m = _GRADE_RE.search(normalize_persian(text or ""))
    return m.group(1) if m else None


def extract_pack_size(text: str) -> Optional[dict]:
    """First pack size in the post, normalised to grams or millilitres."""
    norm = fa_digits_to_en(normalize_persian(text or ""))
    for m in _PACK_RE.finditer(norm):
        raw_val, raw_unit = m.group(1), re.sub(r"\s+", " ", m.group(2).lower())
        try:
            val = float(raw_val.replace(",", "."))
        except ValueError:
            continue
        if val <= 0:
            continue
        unit_key = raw_unit if raw_unit in _PACK_UNITS else raw_unit.replace(" ", "")
        if unit_key not in _PACK_UNITS:
            continue
        canon, mult = _PACK_UNITS[unit_key]
        return {"value": val, "unit": raw_unit, "normalised_value": val * mult,
                "normalised_unit": canon, "raw": m.group(0).strip()}
    return None


def extract_sku(text: str) -> Optional[str]:
    """Supplier catalogue code, avoiding CAS fragments and phone numbers."""
    norm = fa_digits_to_en(text or "")
    cas_spans = [m.span() for m in _CAS_RE.finditer(norm)]
    for m in _SKU_RE.finditer(norm):
        s, e = m.span()
        if any(cs <= s and e <= ce for cs, ce in cas_spans):
            continue
        tok = m.group(1)
        # Iranian mobile / long phone digits are not SKUs.
        if tok.isdigit() and (tok.startswith("09") or len(tok) > 7):
            continue
        # A bare year is not a SKU.
        if tok.isdigit() and len(tok) == 4:
            continue
        return tok
    return None


def extract_availability(text: str) -> Optional[str]:
    norm = normalize_persian(text or "").lower()
    # Check "unavailable" first: "ناموجود" contains "موجود".
    for state in ("unavailable", "to_order", "in_stock"):
        if any(k.lower() in norm for k in AVAILABILITY[state]):
            return state
    return None


def _clean_name(candidate: str) -> str:
    """Strip brand, grade, purity, pack and punctuation noise from a name."""
    s = candidate.strip(" ,،.:;-–—\t")
    s = _BRAND_RE.sub(" ", s)
    s = _GRADE_RE.sub(" ", s)
    s = _PURITY_RE.sub(" ", s)
    s = _PACK_RE.sub(" ", s)
    s = re.sub(r"\b(?:min|max|approx|approximate|content|solution|extra|pure)\b",
               " ", s, flags=re.I)
    # Drop a trailing bare number left behind by a stripped "%"/purity token
    # ("Melamine, 99" -> "Melamine"), but keep leading locants ("2-Propanol")
    # and embedded numbers ("1,4-Butanediol").
    s = re.sub(r"[\s,،]+\d{1,3}(?:\.\d{1,3})?\s*$", "", s)
    s = re.sub(r"[\u2018\u2019\u201c\u201d]", "'", s)
    s = re.sub(r"\s{2,}", " ", s)
    return s.strip(" ,،.:;-–—()[]")


def extract_product_names(text: str, *, limit: int = 3) -> List[str]:
    """Candidate Latin chemical names, best first.

    Conservative by design: a candidate must show chemical morphology and must
    not be channel/marketing vocabulary. Ranking prefers longer, more specific
    names ("N-Isopropylacrylamide" over "acid").
    """
    if not text:
        return []
    norm = normalize_persian(text)
    # Work line by line: catalogue posts put the product on its own line.
    candidates: List[str] = []
    for line in re.split(r"[\n\r•·|]+", norm):
        line = line.strip()
        if not line:
            continue
        # Start a run at an optional leading locant ("1,4-", "N,N-", "2-") so
        # chemically significant prefixes are not lost from the name.
        for run in re.findall(
                r"(?:(?<![\w.])[0-9NOSPnos](?:[,'\u2019][0-9NOSPnos])*-)*"
                r"[A-Za-z][A-Za-z0-9\-\(\)\[\],'\.\s]{2,70}", line):
            name = _clean_name(run)
            if not (4 <= len(name) <= 70):
                continue
            low = name.lower()
            if low in _NAME_STOPLIST:
                continue
            words = [w for w in re.split(r"[^A-Za-z0-9]+", low) if w]
            if not words or all(w in _NAME_STOPLIST for w in words):
                continue
            if not _CHEM_MORPHOLOGY.search(name):
                continue
            if re.fullmatch(r"[\d\W]+", name):
                continue
            candidates.append(name)

    seen, out = set(), []
    for c in sorted(candidates, key=lambda x: (-len(x.split()), -len(x))):
        k = c.lower()
        if k in seen:
            continue
        seen.add(k)
        out.append(c)
        if len(out) >= limit:
            break
    return out


@dataclass
class ExtractedListing:
    """Everything structured we could read out of one post."""
    sku: Optional[str] = None
    brand: Optional[str] = None
    product_names: List[str] = field(default_factory=list)
    purity: Optional[float] = None
    grade_token: Optional[str] = None
    pack_size: Optional[dict] = None
    cas_numbers: List[str] = field(default_factory=list)
    availability: Optional[str] = None

    @property
    def product_name(self) -> Optional[str]:
        return self.product_names[0] if self.product_names else None

    @property
    def field_count(self) -> int:
        """How many independent structured fields were recovered."""
        return sum(bool(x) for x in (
            self.sku, self.brand, self.product_names, self.purity,
            self.grade_token, self.pack_size, self.cas_numbers,
            self.availability))

    def as_dict(self) -> dict:
        return {
            "sku": self.sku, "brand": self.brand,
            "product_name": self.product_name,
            "product_name_candidates": self.product_names,
            "purity_percent": self.purity, "grade_token": self.grade_token,
            "pack_size": self.pack_size, "cas_numbers": self.cas_numbers,
            "availability": self.availability,
            "structured_field_count": self.field_count,
        }


def extract_listing_fields(text: str) -> ExtractedListing:
    """Extract every structured field from one post. Never raises."""
    if not text:
        return ExtractedListing()
    return ExtractedListing(
        sku=extract_sku(text),
        brand=extract_brand(text),
        product_names=extract_product_names(text),
        purity=extract_purity(text),
        grade_token=extract_grade_token(text),
        pack_size=extract_pack_size(text),
        cas_numbers=extract_cas_numbers(text),
        availability=extract_availability(text),
    )


def is_structured_catalogue_post(text: str, min_fields: int = 3) -> bool:
    """True when a post has the shape of a real catalogue entry.

    Used as an ADDITIONAL admission route in the listing discriminator: a post
    carrying a SKU + name + purity + pack is a product listing even if it has
    no explicit sales verb and no price.
    """
    ext = extract_listing_fields(text)
    if not (ext.product_names or ext.cas_numbers):
        return False
    return ext.field_count >= min_fields
