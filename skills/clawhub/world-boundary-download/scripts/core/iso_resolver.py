"""Resolve country names to ISO 3166-1 alpha-3 codes.

The resolver first consults a small, hand-curated Chinese/English alias
table for the most common requests, then falls back to ``pycountry`` for
the long tail. It never makes a network call.

The resolver also provides the inverse: ISO 3 -> display name (English
and a Chinese alias if available), and a fuzzy search over country
names for the ``search`` CLI subcommand.
"""

from __future__ import annotations

from dataclasses import dataclass
from difflib import SequenceMatcher
from typing import Iterable, List, Optional

try:
    import pycountry  # type: ignore
except ImportError as e:  # pragma: no cover - pycountry is a hard dep
    raise ImportError(
        "pycountry is required: pip install pycountry"
    ) from e

from .exceptions import ResolutionError


# ---------------------------------------------------------------------------
# Aliases
# ---------------------------------------------------------------------------
# Chinese short names + a few non-standard English aliases that pycountry
# does not always expose (e.g. "UK" for the United Kingdom, "美国" for
# the United States). Keys are lower-cased; values are ISO 3166-1 alpha-3.

ALIASES: dict[str, str] = {
    # China + SARs
    "中国": "CHN",
    "中华人民共和国": "CHN",
    "大陆": "CHN",
    "内地": "CHN",
    "中国大陆": "CHN",
    "china": "CHN",
    "prc": "CHN",
    "中国香港": "HKG",
    "香港": "HKG",
    "港": "HKG",
    "hong kong": "HKG",
    "hk": "HKG",
    "中国澳门": "MAC",
    "澳门": "MAC",
    "澳": "MAC",
    "macao": "MAC",
    "macau": "MAC",
    "mo": "MAC",
    "中国台湾": "TWN",
    "台湾": "TWN",
    "台": "TWN",
    "taiwan": "TWN",
    "tw": "TWN",
    # United States
    "美国": "USA",
    "美利坚合众国": "USA",
    "usa": "USA",
    "us": "USA",
    "united states": "USA",
    "america": "USA",
    # United Kingdom
    "英国": "GBR",
    "大不列颠": "GBR",
    "uk": "GBR",
    "u.k.": "GBR",
    "united kingdom": "GBR",
    "great britain": "GBR",
    "britain": "GBR",
    "england": "GBR",
    # Russia
    "俄罗斯": "RUS",
    "俄国": "RUS",
    "russia": "RUS",
    # Korea
    "韩国": "KOR",
    "南韩": "KOR",
    "korea": "KOR",
    "south korea": "KOR",
    "朝鲜": "PRK",
    "北朝鲜": "PRK",
    "north korea": "PRK",
    # Misc common shortenings
    "阿联酋": "ARE",
    "酋长国": "ARE",
    "uae": "ARE",
    "emirates": "ARE",
    "新西兰": "NZL",
    "new zealand": "NZL",
    "捷克": "CZE",
    "czech": "CZE",
    "斯洛伐克": "SVK",
    "slovakia": "SVK",
    "荷兰": "NLD",
    "holland": "NLD",
    "netherlands": "NLD",
    "瑞士": "CHE",
    "switzerland": "CHE",
    "西班牙": "ESP",
    "spain": "ESP",
    "葡萄牙": "PRT",
    "portugal": "PRT",
    "意大利": "ITA",
    "italy": "ITA",
    "德国": "DEU",
    "germany": "DEU",
    "法国": "FRA",
    "france": "FRA",
    "巴西": "BRA",
    "brazil": "BRA",
    "阿根廷": "ARG",
    "argentina": "ARG",
    "墨西哥": "MEX",
    "mexico": "MEX",
    "加拿大": "CAN",
    "canada": "CAN",
    "澳大利亚": "AUS",
    "澳洲": "AUS",
    "australia": "AUS",
    "日本": "JPN",
    "japan": "JPN",
    "印度": "IND",
    "india": "IND",
    "印尼": "IDN",
    "印度尼西亚": "IDN",
    "indonesia": "IDN",
    "越南": "VNM",
    "vietnam": "VNM",
    "泰国": "THA",
    "thailand": "THA",
    "新加坡": "SGP",
    "singapore": "SGP",
    "马来西亚": "MYS",
    "malaysia": "MYS",
    "菲律宾": "PHL",
    "philippines": "PHL",
    "南非": "ZAF",
    "south africa": "ZAF",
    "埃及": "EGY",
    "egypt": "EGY",
    "尼日利亚": "NGA",
    "nigeria": "NGA",
    "肯尼亚": "KEN",
    "kenya": "KEN",
    "土耳其": "TUR",
    "turkey": "TUR",
    "沙特": "SAU",
    "沙特阿拉伯": "SAU",
    "saudi arabia": "SAU",
    "伊朗": "IRN",
    "iran": "IRN",
    "伊拉克": "IRQ",
    "iraq": "IRQ",
    "以色列": "ISR",
    "israel": "ISR",
    "巴勒斯坦": "PSE",
    "palestine": "PSE",
}


# Common special entities that pycountry covers but the data sources do not
# always list. Map of alpha-3 -> list of (chinese, english) display variants.
SPECIAL_DISPLAY: dict[str, tuple[str, str]] = {
    "HKG": ("中国香港", "Hong Kong"),
    "MAC": ("中国澳门", "Macao"),
    "TWN": ("中国台湾", "Taiwan"),
    "PSE": ("巴勒斯坦", "Palestine"),
    "XKX": ("科索沃", "Kosovo"),
    "ALA": ("奥兰", "Åland Islands"),
}


# ---------------------------------------------------------------------------
# Data class
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class CountryMatch:
    """One result of a country resolution attempt."""

    iso3: str
    iso2: str
    name_en: str
    name_zh: str
    score: float = 1.0  # 1.0 for exact match; lower for fuzzy

    def to_dict(self) -> dict:
        return {
            "iso3": self.iso3,
            "iso2": self.iso2,
            "name_en": self.name_en,
            "name_zh": self.name_zh,
        }


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _norm(s: str) -> str:
    return (s or "").strip().lower()


def _pycountry_lookup(query: str) -> Optional[CountryMatch]:
    """Try to look up *query* in pycountry by alpha-3, alpha-2, or name."""

    q = _norm(query)
    if not q:
        return None

    # Exact alpha-3
    c = pycountry.countries.get(alpha_3=q.upper())
    if c:
        return _mk_match(c, score=1.0)

    # Exact alpha-2
    c = pycountry.countries.get(alpha_2=q.upper())
    if c:
        return _mk_match(c, score=1.0)

    # Exact name (case-insensitive)
    for cand in pycountry.countries:
        names = {_norm(cand.name), _norm(getattr(cand, "official_name", ""))}
        if q in names:
            return _mk_match(cand, score=1.0)

    # Common name (zh, fr, es, de, ja, etc.)
    for cand in pycountry.countries:
        for attr in ("common_name",):
            v = getattr(cand, attr, None)
            if v and _norm(v) == q:
                return _mk_match(cand, score=1.0)

    return None


def _mk_match(c, score: float) -> CountryMatch:
    """Build a CountryMatch from a pycountry Country object."""

    iso3 = c.alpha_3
    zh = SPECIAL_DISPLAY.get(iso3, (None, None))[0]
    if zh is None:
        # The pycountry 'name' field is always English; Chinese would
        # require an external table we deliberately do not bundle.
        zh = ""
    return CountryMatch(
        iso3=iso3,
        iso2=c.alpha_2,
        name_en=c.name,
        name_zh=zh,
        score=score,
    )


def _alias_lookup(query: str) -> Optional[CountryMatch]:
    q = _norm(query)
    iso3 = ALIASES.get(q)
    if not iso3:
        return None
    c = pycountry.countries.get(alpha_3=iso3)
    if not c:
        return None
    return _mk_match(c, score=1.0)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def resolve(query: str, *, fuzzy: bool = True, threshold: float = 0.78) -> CountryMatch:
    """Resolve *query* (name, alpha-2, or alpha-3) to a CountryMatch.

    Raises :class:`ResolutionError` if no match is found. When *fuzzy* is
    True, falls back to a sequence-matcher search over pycountry names
    if exact lookup fails.
    """

    if not query or not query.strip():
        raise ResolutionError("empty country query")

    q = query.strip()

    # 1. Try explicit alias table (catches Chinese short names).
    m = _alias_lookup(q)
    if m:
        return m

    # 2. Try pycountry.
    m = _pycountry_lookup(q)
    if m:
        return m

    # 3. Fuzzy search.
    if fuzzy:
        fuzzy_match = _fuzzy_search(q, limit=1, threshold=threshold)
        if fuzzy_match:
            return fuzzy_match[0]

    # Nothing matched.
    raise ResolutionError(
        f"could not resolve country: {query!r}. "
        "Try a 3-letter ISO code, e.g. --iso CHN, or use the 'search' subcommand."
    )


def search(keyword: str, limit: int = 10) -> List[CountryMatch]:
    """Return up to *limit* country matches ranked by name similarity.

    Always returns at least an empty list, never raises.
    """

    return _fuzzy_search(keyword, limit=limit, threshold=0.0) or _exact_filter(keyword, limit)


def _fuzzy_search(
    keyword: str, *, limit: int, threshold: float
) -> Optional[List[CountryMatch]]:
    """Sequence-matcher search over all pycountry names + alias table.

    The alias table is searched first so that Chinese / common short
    names always score 1.0. The pycountry search is then layered on top
    for any keyword that does not match an alias.
    """

    k = _norm(keyword)
    if not k:
        return None

    scored: list[tuple[float, CountryMatch]] = []

    # 1. Aliases — substring matches count as exact.
    for alias, iso3 in ALIASES.items():
        a = _norm(alias)
        if not a:
            continue
        if k == a or a.startswith(k) or k in a:
            c = pycountry.countries.get(alpha_3=iso3)
            if c:
                scored.append((1.0, _mk_match(c, score=1.0)))
                continue
        s = SequenceMatcher(None, k, a).ratio()
        if s >= threshold:
            c = pycountry.countries.get(alpha_3=iso3)
            if c:
                scored.append((s, _mk_match(c, score=s)))

    # 2. pycountry names — substring matches also count as exact.
    for c in pycountry.countries:
        names = [_norm(c.name), _norm(getattr(c, "official_name", ""))]
        for n in names:
            if not n:
                continue
            if k == n or n.startswith(k) or k in n:
                scored.append((1.0, _mk_match(c, score=1.0)))
                break
        else:
            best = max(
                (SequenceMatcher(None, k, n).ratio() for n in names if n),
                default=0.0,
            )
            if best >= threshold:
                scored.append((best, _mk_match(c, score=best)))

    if not scored:
        return None
    # Dedup keeping highest score per iso3.
    best_by_iso: dict[str, tuple[float, CountryMatch]] = {}
    for s, m in scored:
        prev = best_by_iso.get(m.iso3)
        if prev is None or s > prev[0]:
            best_by_iso[m.iso3] = (s, m)
    final = sorted(best_by_iso.values(), key=lambda x: -x[0])
    return [m for _, m in final[:limit]]


def _exact_filter(keyword: str, limit: int) -> List[CountryMatch]:
    """Last-ditch substring filter (case-insensitive)."""

    k = _norm(keyword)
    out: list[CountryMatch] = []
    for c in pycountry.countries:
        names = [_norm(c.name), _norm(getattr(c, "official_name", ""))]
        if any(k in n for n in names if n):
            out.append(_mk_match(c, score=0.5))
            if len(out) >= limit:
                break
    return out


def get_display(iso3: str) -> CountryMatch:
    """Return a CountryMatch for the given ISO 3-letter code.

    Raises :class:`ResolutionError` if the code is not a known country.
    """

    c = pycountry.countries.get(alpha_3=iso3.upper())
    if not c:
        raise ResolutionError(f"unknown ISO 3166-1 alpha-3 code: {iso3!r}")
    return _mk_match(c, score=1.0)


def all_iso3() -> Iterable[str]:
    """Yield every supported ISO 3-letter code."""

    for c in pycountry.countries:
        yield c.alpha_3
