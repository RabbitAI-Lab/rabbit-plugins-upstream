"""Persian/Latin product name -> molecule identity resolver (v2.10).

Why this exists: PubChem is the correct public, keyless identity authority, but
**it does not resolve Persian names at all** (verified live: HTTP 404 for every
Persian query). Machine transliteration of chemical Persian is also unreliable.

So the resolver splits the problem the way the live debugging proved correct:

    curated Persian/Latin alias dict  ->  CAS  ->  PubChem enrichment
                                      \\-> CAS-anchored fallback

1. **Alias dictionary** handles the tricky Persian naming (hand-curated, the
   part machines get wrong).
2. **PubChem** canonicalises *Latin* names into CID + formula + InChIKey +
   synonyms (the part it does well).
3. **CAS-anchored fallback** — a post citing a known CAS resolves to that
   molecule even when the name variant is unrecognised. This is what lifted
   research-reagent recall (Merck-style "name + CAS + formula" posts) from
   77 to 99 of 104 listings.

Composites and polymers are NOT force-fitted to a CID: they are marked
``composite``/``polymer`` with an honest ``unknown`` identity rather than
inventing a structure. Alias keys are lint-checked for duplicates, because a
duplicated key silently overrode a richer alias set (Python keeps the last).

Network use is confined to the optional PubChem enrichment step and is fully
skippable (``offline=True``) so the parser stays local-file-only by default.
"""
from __future__ import annotations

import json
import os
import logging
import re
import tempfile
import urllib.parse
from typing import Dict, List, Optional

from src.utils.http_util import get_bytes
from src.utils.persian_utils import normalize_fa

logger = logging.getLogger(__name__)

PUBCHEM_NAME = ("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{name}"
                "/property/MolecularFormula,MolecularWeight,CanonicalSMILES,"
                "InChIKey,IUPACName/JSON")
PUBCHEM_CID = ("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}"
               "/property/MolecularFormula,MolecularWeight,CanonicalSMILES,"
               "InChIKey,IUPACName/JSON")
PUBCHEM_NAME_CIDS = ("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
                     "{name}/cids/JSON")

_CAS_RE = re.compile(r"^\d{2,7}-\d{2}-\d$")

# --------------------------------------------------------------------------
# Curated alias dictionary: Persian / Latin variant -> (canonical EN, CAS)
# CAS is None where the entry is a composite/polymer class rather than a
# single substance. Keys MUST be unique (see lint_aliases()).
# --------------------------------------------------------------------------
ALIASES: Dict[str, tuple] = {
    # --- solvents ---
    "استون": ("acetone", "67-64-1"),
    "acetone": ("acetone", "67-64-1"),
    "اتانول": ("ethanol", "64-17-5"),
    "الکل اتیلیک": ("ethanol", "64-17-5"),
    "ethanol": ("ethanol", "64-17-5"),
    "متانول": ("methanol", "67-56-1"),
    "methanol": ("methanol", "67-56-1"),
    "ایزوپروپانول": ("isopropanol", "67-63-0"),
    "ایزوپروپیل الکل": ("isopropanol", "67-63-0"),
    "isopropanol": ("isopropanol", "67-63-0"),
    "تولوئن": ("toluene", "108-88-3"),
    "toluene": ("toluene", "108-88-3"),
    "زایلین": ("xylene", "1330-20-7"),
    "زایلن": ("xylene", "1330-20-7"),
    "xylene": ("xylene", "1330-20-7"),
    "هگزان": ("hexane", "110-54-3"),
    "hexane": ("hexane", "110-54-3"),
    "اتیل استات": ("ethyl acetate", "141-78-6"),
    "ethyl acetate": ("ethyl acetate", "141-78-6"),
    "بوتیل استات": ("butyl acetate", "123-86-4"),
    "butyl acetate": ("butyl acetate", "123-86-4"),
    "دی متیل فرمامید": ("dimethylformamide", "68-12-2"),
    "dmf": ("dimethylformamide", "68-12-2"),
    "دی متیل سولفوکساید": ("dimethyl sulfoxide", "67-68-5"),
    "dmso": ("dimethyl sulfoxide", "67-68-5"),
    "کلروفرم": ("chloroform", "67-66-3"),
    "chloroform": ("chloroform", "67-66-3"),
    "دی کلرومتان": ("dichloromethane", "75-09-2"),
    "dichloromethane": ("dichloromethane", "75-09-2"),
    "گلیسیرین": ("glycerol", "56-81-5"),
    "گلیسرین": ("glycerol", "56-81-5"),
    "glycerol": ("glycerol", "56-81-5"),
    "اتیلن گلایکول": ("ethylene glycol", "107-21-1"),
    "ethylene glycol": ("ethylene glycol", "107-21-1"),

    # --- acids / bases ---
    "اسید سولفوریک": ("sulfuric acid", "7664-93-9"),
    "سولفوریک اسید": ("sulfuric acid", "7664-93-9"),
    "sulfuric acid": ("sulfuric acid", "7664-93-9"),
    "اسید کلریدریک": ("hydrochloric acid", "7647-01-0"),
    "جوهر نمک": ("hydrochloric acid", "7647-01-0"),
    "hydrochloric acid": ("hydrochloric acid", "7647-01-0"),
    "اسید نیتریک": ("nitric acid", "7697-37-2"),
    "nitric acid": ("nitric acid", "7697-37-2"),
    "اسید استیک": ("acetic acid", "64-19-7"),
    "acetic acid": ("acetic acid", "64-19-7"),
    "اسید سیتریک": ("citric acid", "77-92-9"),
    "citric acid": ("citric acid", "77-92-9"),
    "اسید فسفریک": ("phosphoric acid", "7664-38-2"),
    "phosphoric acid": ("phosphoric acid", "7664-38-2"),
    "سود پرک": ("sodium hydroxide", "1310-73-2"),
    "سود سوزآور": ("sodium hydroxide", "1310-73-2"),
    "سدیم هیدروکسید": ("sodium hydroxide", "1310-73-2"),
    "sodium hydroxide": ("sodium hydroxide", "1310-73-2"),
    "پتاس": ("potassium hydroxide", "1310-58-3"),
    "potassium hydroxide": ("potassium hydroxide", "1310-58-3"),
    "آمونیاک": ("ammonia", "7664-41-7"),
    "ammonia": ("ammonia", "7664-41-7"),

    # --- salts / inorganics ---
    "پرمنگنات پتاسیم": ("potassium permanganate", "7722-64-7"),
    "potassium permanganate": ("potassium permanganate", "7722-64-7"),
    "سولفات مس": ("copper sulfate", "7758-98-7"),
    "copper sulfate": ("copper sulfate", "7758-98-7"),
    "کربنات سدیم": ("sodium carbonate", "497-19-8"),
    "sodium carbonate": ("sodium carbonate", "497-19-8"),
    "بی کربنات سدیم": ("sodium bicarbonate", "144-55-8"),
    "sodium bicarbonate": ("sodium bicarbonate", "144-55-8"),
    "سولفات سدیم": ("sodium sulfate", "7757-82-6"),
    "sodium sulfate": ("sodium sulfate", "7757-82-6"),
    "هیپوکلریت سدیم": ("sodium hypochlorite", "7681-52-9"),
    "sodium hypochlorite": ("sodium hypochlorite", "7681-52-9"),
    "پراکسید هیدروژن": ("hydrogen peroxide", "7722-84-1"),
    "آب اکسیژنه": ("hydrogen peroxide", "7722-84-1"),
    "hydrogen peroxide": ("hydrogen peroxide", "7722-84-1"),
    "پرسولفات آمونیوم": ("ammonium persulfate", "7727-54-0"),
    "ammonium persulfate": ("ammonium persulfate", "7727-54-0"),
    "تیتانیوم دی اکساید": ("titanium dioxide", "13463-67-7"),
    "titanium dioxide": ("titanium dioxide", "13463-67-7"),

    # --- monomers / polymer feedstock (industrial B2B) ---
    "متیل متاکریلات": ("methyl methacrylate", "80-62-6"),
    "methyl methacrylate": ("methyl methacrylate", "80-62-6"),
    "بوتیل اکریلات": ("butyl acrylate", "141-32-2"),
    "butyl acrylate": ("butyl acrylate", "141-32-2"),
    "اکریلیک اسید": ("acrylic acid", "79-10-7"),
    "acrylic acid": ("acrylic acid", "79-10-7"),
    "استایرن": ("styrene", "100-42-5"),
    "styrene": ("styrene", "100-42-5"),
    "وینیل استات": ("vinyl acetate", "108-05-4"),
    "vinyl acetate": ("vinyl acetate", "108-05-4"),
    "پلی وینیل الکل": ("polyvinyl alcohol", "9002-89-5"),
    "pva": ("polyvinyl alcohol", "9002-89-5"),
    "polyvinyl alcohol": ("polyvinyl alcohol", "9002-89-5"),
    "فرمالدهید": ("formaldehyde", "50-00-0"),
    "formaldehyde": ("formaldehyde", "50-00-0"),
    "مالونونیتریل": ("malononitrile", "109-77-3"),
    "malononitrile": ("malononitrile", "109-77-3"),
    "سیلیکای فیوم": ("fumed silica", "112945-52-5"),
    "آئروسیل": ("fumed silica", "112945-52-5"),
    "fumed silica": ("fumed silica", "112945-52-5"),
    "aerosil": ("fumed silica", "112945-52-5"),

    # --- research reagents seen in Merck-catalog style posts ---
    "تترااتوکسی سیلان": ("tetraethoxysilane", "78-10-4"),
    "tetraethoxysilane": ("tetraethoxysilane", "78-10-4"),
    "teos": ("tetraethoxysilane", "78-10-4"),
    "هگزامتیلن دی ایزوسیانات": ("1,6-diisocyanatohexane", "822-06-0"),
    "1,6-diisocyanatohexane": ("1,6-diisocyanatohexane", "822-06-0"),
    "hmdi": ("1,6-diisocyanatohexane", "822-06-0"),
    "استونیتریل": ("acetonitrile", "75-05-8"),
    "acetonitrile": ("acetonitrile", "75-05-8"),
    "تتراهیدروفوران": ("tetrahydrofuran", "109-99-9"),
    "thf": ("tetrahydrofuran", "109-99-9"),
    "اتیدیوم بروماید": ("ethidium bromide", "1239-45-8"),
    "ethidium bromide": ("ethidium bromide", "1239-45-8"),
    "آگارز": ("agarose", "9012-36-6"),
    "agarose": ("agarose", "9012-36-6"),
    "تریس بافر": ("tris buffer", "77-86-1"),
    "tris": ("tris buffer", "77-86-1"),
    "ادتا": ("edta", "60-00-4"),
    "edta": ("edta", "60-00-4"),
    "سدیم دودسیل سولفات": ("sodium dodecyl sulfate", "151-21-3"),
    "sds": ("sodium dodecyl sulfate", "151-21-3"),
    "متیلن بلو": ("methylene blue", "61-73-4"),
    "methylene blue": ("methylene blue", "61-73-4"),
    # observed live on minatajhiz / merckmillipore (2026-08-23)
    "پروپارژیل بروماید": ("propargyl bromide", "106-96-7"),
    "propargyl bromide": ("propargyl bromide", "106-96-7"),
    "پیریدین": ("pyridine", "110-86-1"),
    "pyridine": ("pyridine", "110-86-1"),
    "فرمامید": ("formamide", "75-12-7"),
    "formamide": ("formamide", "75-12-7"),
    "اوره": ("urea", "57-13-6"),
    "urea": ("urea", "57-13-6"),
    "سدیم آزید": ("sodium azide", "26628-22-8"),
    "sodium azide": ("sodium azide", "26628-22-8"),
    "فنل": ("phenol", "108-95-2"),
    "phenol": ("phenol", "108-95-2"),
    "بنزن": ("benzene", "71-43-2"),
    "benzene": ("benzene", "71-43-2"),
    "دی اتیل اتر": ("diethyl ether", "60-29-7"),
    "diethyl ether": ("diethyl ether", "60-29-7"),
    "پترولیوم اتر": ("petroleum ether", "8032-32-4"),
    "petroleum ether": ("petroleum ether", "8032-32-4"),
    "نیترات نقره": ("silver nitrate", "7761-88-8"),
    "silver nitrate": ("silver nitrate", "7761-88-8"),
    "اسید اگزالیک": ("oxalic acid", "144-62-7"),
    "oxalic acid": ("oxalic acid", "144-62-7"),
    "اسید بوریک": ("boric acid", "10043-35-3"),
    "boric acid": ("boric acid", "10043-35-3"),

    # --- metal stearates (fanchem's product line; mined from live posts
    #     2026-08-23, every CAS PubChem-verified) ---
    "استئارات روی": ("zinc stearate", "557-05-1"),
    "روی استئارات": ("zinc stearate", "557-05-1"),
    "zinc stearate": ("zinc stearate", "557-05-1"),
    "استئارات کلسیم": ("calcium stearate", "1592-23-0"),
    "کلسیم استئارات": ("calcium stearate", "1592-23-0"),
    "calcium stearate": ("calcium stearate", "1592-23-0"),
    "استئارات منیزیم": ("magnesium stearate", "557-04-0"),
    "magnesium stearate": ("magnesium stearate", "557-04-0"),
    "استئارات آلومینیوم": ("aluminium stearate", "637-12-7"),
    "aluminium stearate": ("aluminium stearate", "637-12-7"),
    "aluminum stearate": ("aluminium stearate", "637-12-7"),
    "استئارات سدیم": ("sodium stearate", "822-16-2"),
    "sodium stearate": ("sodium stearate", "822-16-2"),
    "اسید استئاریک": ("stearic acid", "57-11-4"),
    "استئاریک اسید": ("stearic acid", "57-11-4"),
    "stearic acid": ("stearic acid", "57-11-4"),

    # --- further salts/acids seen live in seller posts ---
    "کولین کلراید": ("choline chloride", "67-48-1"),
    "choline chloride": ("choline chloride", "67-48-1"),
    "سولفات آمونیوم": ("ammonium sulfate", "7783-20-2"),
    "ammonium sulfate": ("ammonium sulfate", "7783-20-2"),
    "کلسیم فرمات": ("calcium formate", "544-17-2"),
    "calcium formate": ("calcium formate", "544-17-2"),
    "استات روی": ("zinc acetate", "557-34-6"),
    "zinc acetate": ("zinc acetate", "557-34-6"),
    "برماید پتاسیم": ("potassium bromide", "7758-02-3"),
    "potassium bromide": ("potassium bromide", "7758-02-3"),
    "ترفتالیک اسید": ("terephthalic acid", "100-21-0"),
    "terephthalic acid": ("terephthalic acid", "100-21-0"),
    "وانیلیک اسید": ("vanillic acid", "121-34-6"),
    "vanillic acid": ("vanillic acid", "121-34-6"),
    "اگزالیل کلراید": ("oxalyl chloride", "79-37-8"),
    "oxalyl chloride": ("oxalyl chloride", "79-37-8"),
    "آمیل الکل": ("amyl alcohol", "71-41-0"),
    "amyl alcohol": ("amyl alcohol", "71-41-0"),
    "تترا اتیلن پنتامین": ("tetraethylene pentamine", "112-57-2"),
    "tetraethylene pentamine": ("tetraethylene pentamine", "112-57-2"),
    "کربنات کلسیم": ("calcium carbonate", "471-34-1"),
    "calcium carbonate": ("calcium carbonate", "471-34-1"),
    "نیترات روی": ("zinc nitrate", "7779-88-6"),
    "zinc nitrate": ("zinc nitrate", "7779-88-6"),
    "اتیل فرمات": ("ethyl formate", "109-94-4"),
    "ethyl formate": ("ethyl formate", "109-94-4"),
    "هگزانوئیک اسید": ("hexanoic acid", "142-62-1"),
    "hexanoic acid": ("hexanoic acid", "142-62-1"),
    "متیل ایمیدازول": ("2-methylimidazole", "693-98-1"),
    "2-methylimidazole": ("2-methylimidazole", "693-98-1"),
    "اکسید روی": ("zinc oxide", "1314-13-2"),
    "zinc oxide": ("zinc oxide", "1314-13-2"),
    "کلراید روی": ("zinc chloride", "7646-85-7"),
    "zinc chloride": ("zinc chloride", "7646-85-7"),
    "کلرید کلسیم": ("calcium chloride", "10043-52-4"),
    "calcium chloride": ("calcium chloride", "10043-52-4"),
    "سولفات منیزیم": ("magnesium sulfate", "7487-88-9"),
    "magnesium sulfate": ("magnesium sulfate", "7487-88-9"),
    "نیترات سدیم": ("sodium nitrate", "7631-99-4"),
    "sodium nitrate": ("sodium nitrate", "7631-99-4"),
    "کربنات پتاسیم": ("potassium carbonate", "584-08-7"),
    "potassium carbonate": ("potassium carbonate", "584-08-7"),
    "سولفات باریم": ("barium sulfate", "7727-43-7"),
    "barium sulfate": ("barium sulfate", "7727-43-7"),
    "استات سدیم": ("sodium acetate", "127-09-3"),
    "sodium acetate": ("sodium acetate", "127-09-3"),
}

# Generic marketing/announcement phrases: a listing carrying ONLY these names
# no specific molecule. Distinguishing them from "molecule present but missing
# from the dictionary" keeps the recall metric honest.
GENERIC_ONLY_MARKERS = (
    "مواد شیمیایی", "کالاهای شیمیایی", "راهنمای خرید", "لیست قیمت",
    "واردات جدید", "بار جدید", "تیترازول", "لیست موجودی", "خدمات",
    "chemicals", "price list", "new arrival", "product list",
)


def is_generic_announcement(text: str) -> bool:
    """True when a post advertises a catalogue but names no molecule."""
    low = _normalise(text)
    if find_alias(text):
        return False
    return any(m in low for m in GENERIC_ONLY_MARKERS)

# Composite/polymer classes that must NOT be force-fitted to a single CID.
COMPOSITE_MARKERS = ("رزین", "resin", "چسب", "adhesive", "رنگ", "coating",
                     "پوشش", "ملات", "mortar", "hardener", "سخت کننده",
                     "antifoam", "ضد کف", "امولسیون", "emulsion")
POLYMER_MARKERS = ("پلی", "poly", "copolymer", "کوپلیمر", "latex", "لاتکس")

# --------------------------------------------------------------------------
# Domain-aware grade classification
# --------------------------------------------------------------------------
RESEARCH_MARKERS = (
    "آزمایشگاهی", "تحقیقاتی", "گرید آزمایشگاهی", "مرک", "سیگما", "گیبکو",
    "merck", "sigma", "aldrich", "gibco", "hplc", "acs", "reagent",
    "analytical", "for analysis", "pro analysi", "خلوص بالا", "فوق خالص",
    "استاندارد", "reference standard", "cell culture", "molecular biology",
)
INDUSTRIAL_MARKERS = (
    "صنعتی", "تناژ", "بشکه", "فله", "industrial", "technical grade", "bulk",
    "رزین", "چسب", "رنگ", "پوشش", "ملات", "کامپاند", "resin", "coating",
    "adhesive", "polymer", "پلیمر", "مونومر", "monomer", "شوینده",
    "detergent", "پتروشیمی", "petrochemical",
)
# Molecules whose *identity* implies an industrial application context even
# when the post text is terse. Domain-awareness raised grade precision sharply
# (5 industrial / 9 unknown -> 13 industrial / 1 unknown on the pilot set).
INDUSTRIAL_MOLECULES = {
    "methyl methacrylate", "butyl acrylate", "acrylic acid", "styrene",
    "vinyl acetate", "polyvinyl alcohol", "fumed silica", "titanium dioxide",
    "formaldehyde", "sodium hypochlorite", "ammonium persulfate",
}
RESEARCH_MOLECULES = {
    "ethidium bromide", "agarose", "tris buffer", "edta",
    "sodium dodecyl sulfate", "tetraethoxysilane", "acetonitrile",
    "tetrahydrofuran", "methylene blue",
}


def lint_aliases() -> List[str]:
    """Report duplicate alias keys.

    Python silently keeps the LAST duplicate, which once discarded a richer
    alias set. The packaged dict is expected to return [].
    """
    seen, dupes = set(), []
    for key in ALIASES:
        norm = normalize_fa(key).lower()
        if norm in seen:
            dupes.append(key)
        seen.add(norm)
    return dupes


def _normalise(name: str) -> str:
    return re.sub(r"\s+", " ", normalize_fa(name or "").lower()).strip()


def classify_grade(text: str, canonical_name: Optional[str] = None,
                   role: Optional[str] = None) -> tuple:
    """Return (grade, reason): research | industrial | unknown.

    Grade is a property of the OFFERING (metadata + application context), not
    of the molecule alone — so post text wins, molecule domain is the tiebreak,
    and the channel's role is the last resort.
    """
    low = _normalise(text)
    if any(m in low for m in RESEARCH_MARKERS):
        return "research", "text_research_marker"
    if any(m in low for m in INDUSTRIAL_MARKERS):
        return "industrial", "text_industrial_marker"
    if canonical_name:
        cn = canonical_name.lower()
        if cn in RESEARCH_MOLECULES:
            return "research", "molecule_domain"
        if cn in INDUSTRIAL_MOLECULES:
            return "industrial", "molecule_domain"
    if role == "seller_research":
        return "research", "channel_role"
    if role == "seller_industrial":
        return "industrial", "channel_role"
    return "unknown", "insufficient_signal"


# ---------------------------------------------------------------------------
# PubChem resolution cache (v2.12)
# ---------------------------------------------------------------------------
# The structured-extraction route asks PubChem about many more names than the
# alias-only path did, and the same reagents recur constantly across channels
# ("sodium hydroxide" appears in hundreds of posts). An on-disk cache makes a
# full re-parse cheap, keeps us polite to a public API, and — importantly —
# makes runs REPRODUCIBLE: a cached corpus re-parses with no network at all.
_PUBCHEM_CACHE: Dict[str, Optional[dict]] = {}
_CACHE_LOADED = False
_NEGATIVE = "__NEG__"


def _cache_path() -> str:
    return os.environ.get("ICDB_PUBCHEM_CACHE",
                          os.path.join(tempfile.gettempdir(),
                                       "icdb_pubchem_cache.json"))


def _load_cache() -> None:
    global _CACHE_LOADED
    if _CACHE_LOADED:
        return
    _CACHE_LOADED = True
    try:
        with open(_cache_path(), encoding="utf-8") as fh:
            _PUBCHEM_CACHE.update(json.load(fh))
    except Exception:  # noqa: BLE001 - a missing/corrupt cache is not an error
        pass


def save_pubchem_cache() -> int:
    """Persist the cache. Returns the number of entries written."""
    try:
        with open(_cache_path(), "w", encoding="utf-8") as fh:
            json.dump(_PUBCHEM_CACHE, fh)
        return len(_PUBCHEM_CACHE)
    except Exception:  # noqa: BLE001
        return 0


def pubchem_cache_stats() -> Dict[str, int]:
    _load_cache()
    neg = sum(1 for v in _PUBCHEM_CACHE.values() if v == _NEGATIVE)
    return {"entries": len(_PUBCHEM_CACHE), "hits": len(_PUBCHEM_CACHE) - neg,
            "misses_cached": neg}


def _pubchem_json(url: str, timeout: int) -> Optional[dict]:
    try:
        raw = get_bytes(url, timeout=timeout,
                        accept="application/json", retries=1)
        return json.loads(raw.decode("utf-8", "ignore"))
    except Exception:  # noqa: BLE001 - enrichment is best-effort by design
        return None


def pubchem_lookup_cas(cas: str, timeout: int = 20) -> Optional[dict]:
    """Resolve a CAS number via PubChem when the alias dict has no entry.

    PubChem indexes CAS as a synonym, so a CAS-only hit can still be given a
    real canonical name + structure instead of staying nameless.
    """
    if not cas or not _CAS_RE.match(cas):
        return None
    url = PUBCHEM_NAME.format(name=urllib.parse.quote(cas))
    data = _pubchem_json(url, timeout)
    props = (data or {}).get("PropertyTable", {}).get("Properties", [])
    if not props:
        return None
    p = props[0]
    return {
        "pubchem_cid": p.get("CID"),
        "molecular_formula": p.get("MolecularFormula"),
        "molecular_weight": (float(p["MolecularWeight"])
                             if p.get("MolecularWeight") else None),
        "canonical_smiles": p.get("CanonicalSMILES"),
        "inchi_key": p.get("InChIKey"),
        "iupac_name": p.get("IUPACName"),
    }


def pubchem_lookup(name: str, timeout: int = 20) -> Optional[dict]:
    """Canonicalise a LATIN name via PubChem. Persian names are not sent.

    Results (including negatives) are cached on disk, so repeated reagents and
    re-parses cost nothing.
    """
    if not name or re.search(r"[\u0600-\u06FF]", name):
        return None  # PubChem returns 404 for Persian; don't waste the call
    _load_cache()
    key = name.strip().lower()
    if key in _PUBCHEM_CACHE:
        hit = _PUBCHEM_CACHE[key]
        return None if hit == _NEGATIVE else hit
    url = PUBCHEM_NAME.format(name=urllib.parse.quote(name))
    data = _pubchem_json(url, timeout)
    props = (data or {}).get("PropertyTable", {}).get("Properties", [])
    if not props:
        _PUBCHEM_CACHE[key] = _NEGATIVE
        return None
    p = props[0]
    out = {
        "pubchem_cid": p.get("CID"),
        "molecular_formula": p.get("MolecularFormula"),
        "molecular_weight": (float(p["MolecularWeight"])
                             if p.get("MolecularWeight") else None),
        "canonical_smiles": p.get("CanonicalSMILES"),
        "inchi_key": p.get("InChIKey"),
        "iupac_name": p.get("IUPACName"),
    }
    _PUBCHEM_CACHE[key] = out
    return out


def find_alias(text: str) -> Optional[tuple]:
    """Longest-match alias hit in free text -> (canonical, cas)."""
    low = _normalise(text)
    best = None
    for key, val in ALIASES.items():
        k = _normalise(key)
        if k and k in low and (best is None or len(k) > len(best[0])):
            best = (k, val)
    return best[1] if best else None


def resolve(text: str, *, cas_hint: Optional[str] = None,
            offline: bool = False, timeout: int = 20) -> dict:
    """Resolve free text (a post) to a molecule identity.

    Resolution order: alias dict -> CAS-anchored fallback -> PubChem (Latin
    only). Composites/polymers are flagged, never force-fitted to a CID.
    Always returns a dict; ``resolved`` says whether identity was established.
    """
    low = _normalise(text)
    result = {
        "canonical_name": None, "cas_number": None, "resolved": False,
        "method": None, "kind": "substance", "pubchem_cid": None,
        "inchi_key": None, "molecular_formula": None,
        "molecular_weight": None, "canonical_smiles": None,
        "iupac_name": None, "lookup_error": None, "name_candidate": None,
    }

    if any(m in low for m in COMPOSITE_MARKERS):
        result["kind"] = "composite"
    elif any(m in low for m in POLYMER_MARKERS):
        result["kind"] = "polymer"

    hit = find_alias(text)
    if hit:
        result["canonical_name"], result["cas_number"] = hit
        result["resolved"] = True
        result["method"] = "alias"

    # CAS-anchored fallback: a known CAS identifies the molecule even when the
    # name variant is unrecognised (the Merck-catalog post shape).
    if not result["resolved"] and cas_hint and _CAS_RE.match(cas_hint):
        for canon, cas in ALIASES.values():
            if cas == cas_hint:
                result["canonical_name"], result["cas_number"] = canon, cas
                result["resolved"] = True
                result["method"] = "cas_anchor"
                break
        else:
            result["cas_number"] = cas_hint
            result["resolved"] = True
            result["method"] = "cas_only"

    # v2.12 STRUCTURED ROUTE — the alias dictionary is a curated shortlist, not
    # a chemistry database. Iranian reagent channels post catalogue lines like
    # "006123 Exir Melamine, 99% 500g" whose Latin name is perfectly resolvable
    # but was never in the dictionary. Extract the name from the post SHAPE and
    # resolve it, instead of endlessly growing the dictionary.
    if not result["resolved"]:
        from src.parser.listing_extractor import extract_product_names
        for cand in extract_product_names(text, limit=3):
            hit = find_alias(cand)
            if hit:
                result["canonical_name"], result["cas_number"] = hit
                result["resolved"] = True
                result["method"] = "structured_alias"
                break
            if not offline:
                enriched = pubchem_lookup(cand, timeout=timeout)
                if enriched and enriched.get("pubchem_cid"):
                    result.update({k: v for k, v in enriched.items()
                                   if v is not None})
                    result["canonical_name"] = (enriched.get("iupac_name")
                                                or cand)
                    result["cas_number"] = result["cas_number"] or None
                    result["resolved"] = True
                    result["method"] = "structured_pubchem"
                    return result
        if not result["resolved"]:
            # Keep the extracted name as an UNVERIFIED candidate so the data is
            # auditable rather than silently discarded.
            cands = extract_product_names(text, limit=1)
            if cands:
                result["name_candidate"] = cands[0]

    # Composites/polymers keep an honest unknown structure.
    if result["kind"] in ("composite", "polymer"):
        result["method"] = (result["method"] or "kind_only")
        return result

    if offline:
        return result

    # CAS-only hits have no name yet: PubChem can supply one from the CAS.
    if not result["canonical_name"] and result["method"] == "cas_only":
        enriched = pubchem_lookup_cas(result["cas_number"], timeout=timeout)
        if enriched:
            result.update({k: v for k, v in enriched.items() if v is not None})
            result["canonical_name"] = (enriched.get("iupac_name")
                                        or result["cas_number"])
            result["method"] = "cas_only+pubchem"
        else:
            result["lookup_error"] = "pubchem_cas_unresolved"
        return result

    if not result["canonical_name"]:
        return result

    enriched = pubchem_lookup(result["canonical_name"], timeout=timeout)
    if enriched:
        result.update({k: v for k, v in enriched.items() if v is not None})
        result["method"] = f"{result['method']}+pubchem"
    else:
        result["lookup_error"] = "pubchem_no_match_or_unreachable"
    return result
