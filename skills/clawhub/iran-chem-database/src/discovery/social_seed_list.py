"""Social-channel seed list — content-verified public Telegram chemical channels.

v2.10. Iranian chemical suppliers publish live catalogue/price data on PUBLIC
Telegram channels. The web preview endpoint ``t.me/s/<channel>`` is
server-rendered, needs no login/API key, and — unlike most ``.ir`` hosts — is
NOT geo-blocked from foreign datacenter IPs. That makes it the one social
source that is genuinely automatable for free.

Every entry below was **content-verified** by a live probe (2026-08-22), not
guessed: a channel is only listed ``verified`` when its preview page contains
real posts. Many plausible-looking handles are empty "Channel created" stubs
(~9-11 KB) — those are recorded in :data:`REJECTED_CHANNELS` with the reason so
no crawl budget is ever wasted re-probing them.

Channel ``role`` drives the listing discriminator (see
``src/parser/telegram_parser.py``):

  * ``seller_research``   — research/analytical reagent sellers (importers of
                            Merck/Sigma/Gibco etc.). Highest-value source.
  * ``seller_industrial`` — bulk/industrial raw-material B2B traders.
  * ``news``              — industry news / community channels. These publish
                            educational articles that LOOK like listings; they
                            require a STRONG listing signal (price, contact,
                            brand or product hashtag) before a post is accepted.
  * ``lead_source``       — marketplaces/communities used to discover vendors,
                            not to harvest a product feed.

Honest scope: this covers Telegram only. Instagram, Facebook and X are
login-walled and WhatsApp is contact-only/E2E — none are automatable for free
from a foreign IP. Those platforms are represented as vendor contact leads
(:data:`CONTACT_LEADS`), never as a scraped feed.
"""
from __future__ import annotations

from typing import Dict, List, Optional

# --------------------------------------------------------------------------
# Verified public Telegram channels
# --------------------------------------------------------------------------
# handle -> {role, description, verified_on, id_span (observed at probe time)}
SOCIAL_CHANNELS: Dict[str, dict] = {
    # ---- research / analytical reagent sellers (the research supply line) ----
    "merckmillipore": {
        "role": "seller_research",
        "description": "Merck/Sigma-Aldrich/Gibco reagent importer; English IUPAC name + CAS + formula per post",
        "verified_on": "2026-08-22",
        "country": "IR",
        "country_confidence": "high",
        "country_verified_on": "2026-08-23",
        "country_signals": ['phone_09xx:09121161187', 'persian_content', 'iran_reference'],
        "country_evidence": (
            "Tehran importer brand-squatting the Merck name — NOT Merck KGaA. Bio: 'واردات مرك به صورت عمده و سفارشى' (bulk Merck importer), mobile 09121161187 (MCI Iran), admin @Peiman_golmohammadi"
        ),
        "language": "fa",
        "persian_ratio": 0.556,
        "persian_verified_on": "2026-08-23",
    },
    "labshop": {
        "role": "seller_research",
        "description": "Lab equipment + research reagents retailer",
        "verified_on": "2026-08-22",
        "country": "IR",
        "country_confidence": "medium",
        "country_verified_on": "2026-08-23",
        "country_signals": ['persian_content', 'importer_statement_fa'],
        "country_evidence": (
            "Persian bio: 'یکی از بزرگترین وارد کننده محصولات پزشکی و آزمایشگاهی' (major Iranian importer of medical/lab products); Persian-only feed, Iranian admin"
        ),
        "language": "fa",
        "persian_ratio": 0.603,
        "persian_verified_on": "2026-08-23",
    },
    "minatajhiz": {
        "role": "seller_research",
        "description": "Mina Tajhiz Aria — laboratory chemical importer (minatajhiz.co.ir)",
        "verified_on": "2026-08-22",
        "country": "IR",
        "country_confidence": "high",
        "country_verified_on": "2026-08-23",
        "country_signals": ['cctld:minatajhiz.co.ir', 'phone_09xx', 'persian_content'],
        "country_evidence": (
            'Mina Tajhiz Aria — site minatajhiz.co.ir (.ir ccTLD); Persian bio with Iran business hours; WhatsApp 09362048289/09927282910'
        ),
        "language": "fa",
        "persian_ratio": 0.644,
        "persian_verified_on": "2026-08-23",
    },
    "ChemIranSanat": {
        "role": "seller_research",
        "description": ("Shimiran Sanat — lab chemical importer "
                        "(Sigma-Aldrich, Alfa Aesar, Acros, Merck, Santa Cruz, TCI, "
                        "Fluorochem); found via forwarded-from harvest"),
        "verified_on": "2026-08-23",
        "country": "IR",
        "country_confidence": "high",
        "country_verified_on": "2026-08-23",
        "country_signals": ['phone_09xx:09388990438', 'persian_content'],
        "country_evidence": (
            "Shimiran Sanat — Persian bio 'تامین مواد آزمایشگاهی از برندهای معتبر دنیا (مرک، سیگما)', mobile 09388990438, admins @ChemIranAdmin/@ChemIranOwner. Iranian RESELLER of foreign brands: brands are product metadata, not supplier country"
        ),
        "language": "fa",
        "persian_ratio": 0.956,
        "persian_verified_on": "2026-08-23",
    },
    # ---- industrial / B2B raw-material traders ----
    "Maran_Tejarat_Eshen": {
        "role": "seller_industrial",
        "description": "Maran Tejarat (MTE) — monomers/acrylates/PVA/aerosil wholesale",
        "verified_on": "2026-08-22",
        "country": "IR",
        "country_confidence": "high",
        "country_verified_on": "2026-08-23",
        "country_signals": ['persian_content', 'irr_pricing', 'iran_city'],
        "country_evidence": (
            "Persian bio 'واردکننده مواد اولیه شیمیایی' (Iranian raw-material importer); IRR/تومان pricing; Iranian city references"
        ),
        "language": "fa",
        "persian_ratio": 0.97,
        "persian_verified_on": "2026-08-23",
    },
    "jahaneshimicom": {
        "role": "seller_industrial",
        "description": "Jahane Shimi — lab chemicals + equipment price channel",
        "verified_on": "2026-08-22",
        "country": "IR",
        "country_confidence": "medium",
        "country_verified_on": "2026-08-23",
        "country_signals": ['phone_09xx', 'persian_content'],
        "country_evidence": (
            'Jahane Shimi — Persian classifieds bio; Iranian mobile contact; WhatsApp 09336611982'
        ),
        "language": "fa",
        "persian_ratio": 0.993,
        "persian_verified_on": "2026-08-23",
    },
    "Ch_Chemical_leaders": {
        "role": "seller_industrial",
        "description": "Chemical & polymer market leaders — industrial + lab chem buy/sell",
        "verified_on": "2026-08-22",
        "country": "IR",
        "country_confidence": "high",
        "country_verified_on": "2026-08-23",
        "country_signals": ['persian_content', 'irr_pricing', 'iran_city'],
        "country_evidence": (
            'Persian bio for Iranian chemical/polymer industry actors; IRR/تومان pricing; Iranian city references'
        ),
        "language": "fa",
        "persian_ratio": 0.997,
        "persian_verified_on": "2026-08-23",
    },
    "Boof_company": {
        "role": "seller_industrial",
        "description": "Resins & solvents trader (discovered via forwarded-from harvest)",
        "verified_on": "2026-08-22",
        "country": "IR",
        "country_confidence": "high",
        "country_verified_on": "2026-08-23",
        "country_signals": ['phone_+98:+982188211234', 'iran_reference:established in Iran'],
        "country_evidence": (
            "Bio states 'established in 1975 in Iran'; landline (+98) 02188211234 (Tehran); site boof-co.com. 'International trading company' = Iranian firm trading internationally, NOT a foreign supplier"
        ),
        "language": "fa",
        "persian_ratio": 0.875,
        "persian_verified_on": "2026-08-23",
    },
    "fanchem": {
        "role": "seller_industrial",
        "description": "Metal-stearates producer & chemical trader (discovered via forwarded-from harvest)",
        "verified_on": "2026-08-22",
        "country": "IR",
        "country_confidence": "high",
        "country_verified_on": "2026-08-23",
        "country_signals": ['cctld:fanchem.ir', 'phone_landline:02166565700', 'persian_content'],
        "country_evidence": (
            "Persian bio 'تولید کننده افزودنی های پیشرفته پلیمری'; Tehran landline 021-66565700; site www.fanchem.ir (.ir ccTLD)"
        ),
        "language": "fa",
        "persian_ratio": 0.99,
        "persian_verified_on": "2026-08-23",
    },
    # ---- news / community / lead-only ----
    "IranChemicals": {
        "role": "news",
        "description": "Industry news; polymer/colour chemical group",
        "verified_on": "2026-08-22",
        "country": "IR",
        "country_confidence": "high",
        "country_verified_on": "2026-08-23",
        "country_signals": ['persian_content', 'iran_reference', 'iran_city'],
        "country_evidence": (
            "Persian bio 'صنایع شیمیایی ایران' with Iranian calendar date (خرداد ۱۳۹۵); Iranian city references"
        ),
        "language": "fa",
        "persian_ratio": 0.763,
        "persian_verified_on": "2026-08-23",
    },
    "chemgroup": {
        "role": "news",
        "description": "Multi-platform chemistry community",
        "verified_on": "2026-08-22",
        "country": "IR",
        "country_confidence": "medium",
        "country_verified_on": "2026-08-23",
        "country_signals": ['persian_content', 'irr_pricing'],
        "country_evidence": (
            'Persian bio; IRR/تومان pricing; Iranian community with Iranian contact handles'
        ),
        "language": "fa",
        "persian_ratio": 0.985,
        "persian_verified_on": "2026-08-23",
    },
    "LabTel": {
        "role": "lead_source",
        "description": "~28K-member lab marketplace — vendor lead source, not a product feed",
        "verified_on": "2026-08-22",
        "country": "IR",
        "country_confidence": "high",
        "country_verified_on": "2026-08-23",
        "country_signals": ['persian_content', 'iran_reference', 'iran_city'],
        "country_evidence": (
            "Persian bio 'بزرگترین و معتبرترین کانال نیازمندی آزمایشگاهی ایران'; Iranian mobile contacts; Iranian city references"
        ),
        "language": "fa",
        "persian_ratio": 0.999,
        "persian_verified_on": "2026-08-23",
    },
    # ---- v2.18 (2026-08-24): parallel-AI discovery wave ----
    # Admitted 2026-08-24 via the multi-model screening campaign (country-gate
    # signal families, 2-model quorum available) — see
    # output/iranian_chemical_suppliers_2026-08-24.csv.
    "ATRmedShop": {
        "role": "seller_research",
        "description": "ATR Med (Arka Teb Roham) — research chemicals + research/lab kit shop channel (Chemscene imports since 2017); www.atrmed.com",
        "verified_on": "2026-08-24",
        "country": "IR",
        "country_confidence": "high",
        "country_verified_on": "2026-08-24",
        "country_signals": ['phone_021:02166361543', 'phone_021:02166379026', 'persian_content'],
        "country_evidence": (
            "Pinned Persian bio: research/production co. 'آرکا طب روهام (ATR)' active since 1396 (2017) in (1) importing research chemicals & kits, (2) lab services, (3) the shop; Tehran landlines 021-66361543 / 021-66379026; website www.atrmed.com (Tehran address on site); posts in Persian with IRR prices + order links"
        ),
        "language": "fa",
        "persian_ratio": 0.9,
        "persian_verified_on": "2026-08-24",
    },
}

# Content-checked and found unusable. Do NOT retry these: re-probing costs
# budget and they will not become catalogues.
REJECTED_CHANNELS: Dict[str, str] = {
    "safirazma": "empty stub ('Channel created')",
    "arioexir": "empty stub ('Channel created')",
    "geniusshimi": "empty stub ('Channel created')",
    "sigmairan": "empty stub ('Channel created')",
    "azmalab": "empty stub ('Channel created')",
    "pakshoo": "empty stub ('Channel created')",
    "labmaterials": "empty stub ('Channel created')",
    "chemsupply": "empty stub ('Channel created')",
    "shimiyar": "educational chemistry notes, not a seller",
    "irancoatingmarket": "returns empty page (dead/stub)",
    "maplastco": "plastic goods, not chemical reagents",
    "iins_ir": "perfume-making school, not a reagent seller",
    "University_Workshops": "academic workshops, not a seller",
    "graduates_qut": "university alumni channel, not a seller",
    "amoozeshgah_dr_bolboli": "training institute, not a seller",
    # content-checked 2026-08-23 from the forwarded-from harvest
    "chemical_leaders": "empty stub ('Channel created')",
    "polyzone": "polymer industry news/QC articles, not a product catalogue",
    "Laboratory_Industrial_Medical": "used lab INSTRUMENTS (photometers), not chemicals",
    "labsnet": "national lab-network news/training announcements, not a seller",
    "sanatir": "general news channel, not chemical sales",
    "nanogram_ir": "nanotech news/training, not a reagent seller",
    "WKPlast": "WikiPlast plastics-industry news portal, not a reagent seller",
    "Biology_Network": "biology community, not a seller",
    "Iran_Biochemical_Society": "academic society, not a seller",
    "Iranchemicals": "duplicate casing of IranChemicals (already seeded)",
}

# Vendor contact leads on platforms that are NOT freely automatable.
# Captured as leads (with an RFQ bridge) — never scraped.
CONTACT_LEADS: List[dict] = [
    {"vendor": "Mina Tajhiz Aria", "platform": "whatsapp", "handle": "09362048289"},
    {"vendor": "Mina Tajhiz Aria", "platform": "whatsapp", "handle": "09927282910"},
    {"vendor": "Jahane Shimi", "platform": "whatsapp", "handle": "09336611982"},
    {"vendor": "Neda Shimi", "platform": "whatsapp", "handle": "09394453175"},
    {"vendor": "Maran Tejarat", "platform": "whatsapp", "handle": "09102296278"},
    {"vendor": "Sadra Shimi", "platform": "whatsapp", "handle": "09191448231"},
    {"vendor": "Iran Chemicals", "platform": "instagram", "handle": "iran.chemicals"},
    {"vendor": "Iran Elab", "platform": "instagram", "handle": "iranelab"},
    {"vendor": "Chem Group", "platform": "instagram", "handle": "chemgroup"},
    {"vendor": "Kimia Tehran Acid", "platform": "instagram", "handle": "kimia_acid"},
    {"vendor": "Sadra Shimi", "platform": "instagram", "handle": "sadrashimi"},
    {"vendor": "Chem Group", "platform": "twitter", "handle": "ChemGroupIr"},
    {"vendor": "Chem Group", "platform": "facebook", "handle": "ChemGroupIr"},
    # v2.18 (2026-08-24): directory-verified lab suppliers without websites —
    # phone leads from the parallel-AI discovery wave (2-model screening).
    {"vendor": "Bluemoonlight Co.", "platform": "phone", "handle": "0218822515"},
    {"vendor": "Kimyagaran Saadat", "platform": "phone", "handle": "021888395"},
    {"vendor": "Navid Kala Daran", "platform": "phone", "handle": "02177626511"},
    {"vendor": "Jonoub Laboratory Supplies", "platform": "phone", "handle": "0218820712"},
    # v2.20.0 (2026-08-25): contact leads from live-probed research-grade
    # website seeds. Telegram @HSDLifeScience is a bio-only page (no public
    # posts) so it is a lead, not a SOCIAL_CHANNELS catalogue.
    {"vendor": "Hamrahan Safineh Danesh (HSD LifeScience)", "platform": "telegram", "handle": "HSDLifeScience"},
    {"vendor": "Hamrahan Safineh Danesh (HSD LifeScience)", "platform": "instagram", "handle": "hsdint"},
    {"vendor": "Hamrahan Safineh Danesh (HSD LifeScience)", "platform": "phone", "handle": "02188444222"},
    {"vendor": "Imen Gostar Shimi", "platform": "whatsapp", "handle": "09359629191"},
    {"vendor": "Imen Gostar Shimi", "platform": "phone", "handle": "02166412612"},
    {"vendor": "Nirvana Exir Gostar Pars", "platform": "phone", "handle": "02165020336"},
    {"vendor": "Arzan Azma", "platform": "whatsapp", "handle": "09364702056"},
    {"vendor": "Arzan Azma", "platform": "phone", "handle": "02166381559"},
    {"vendor": "Nova Shimi", "platform": "instagram", "handle": "nova_shimi"},
    {"vendor": "Nova Shimi", "platform": "phone", "handle": "02192003669"},
    # v2.21.0 (2026-08-26): phones published on country-gated website seeds
    {"vendor": "Shimi Merck (شیمی مرک)", "platform": "whatsapp", "handle": "09377601793"},
    {"vendor": "Shimi Merck (شیمی مرک)", "platform": "phone", "handle": "02166368169"},
    {"vendor": "Neutron Pharmachemical (شیمی دارویی نوترون)", "platform": "whatsapp", "handle": "09370549881"},
    {"vendor": "Neutron Pharmachemical (شیمی دارویی نوترون)", "platform": "phone", "handle": "09370549881"},
]

# ---------------------------------------------------------------------------
# Country enforcement (v2.11) — Iranian suppliers ONLY
# ---------------------------------------------------------------------------
# Every entry in SOCIAL_CHANNELS carries audited country provenance
# (``country``, ``country_confidence``, ``country_signals``,
# ``country_evidence``, ``country_verified_on``) established by live probe of
# the channel's public t.me page. A channel without ``country == "IR"`` is
# NEVER crawled or parsed: see :func:`active_channels`, which filters on it.
#
# IMPORTANT — brand vs supplier: several Iranian channels resell foreign brands
# (Merck, Sigma-Aldrich, TCI) and one even brand-squats the name
# ``merckmillipore``. That channel is a Tehran importer, not Merck KGaA. The
# supplier is Iranian; the foreign brand is product metadata. Never infer a
# supplier's country from the brands it sells.

#: Handles that are (or front for) NON-Iranian suppliers. Hard deny — they can
#: never be seeded, crawled, parsed or promoted from a forwarded-from lead.
FOREIGN_CHANNELS: Dict[str, str] = {
    "sigmaaldrich": "US/DE — Merck KGaA global brand account",
    "merckgroup": "DE — Merck KGaA corporate",
    "thermofisher": "US — Thermo Fisher Scientific corporate",
    "tcichemicals": "JP — Tokyo Chemical Industry corporate",
    "carlroth": "DE — Carl Roth GmbH corporate",
    "vwrinternational": "US — VWR/Avantor corporate",
    "alfaaesar": "US — Alfa Aesar corporate",
    "chemicalbook": "CN — Chinese chemical portal",
    "lookchem": "CN — Chinese chemical marketplace",
    "echemi": "CN — Chinese chemical marketplace",
    "made_in_china": "CN — Chinese B2B marketplace",
    "alibaba": "CN — Chinese B2B marketplace",
    "chemtradeasia": "SG — Tradeasia International",
    "basf": "DE — BASF SE corporate",
    "dowchemical": "US — Dow Inc corporate",
    "sabic": "SA — SABIC corporate",
}


def is_foreign_channel(handle: str) -> bool:
    """True when a handle is a known NON-Iranian supplier (hard deny)."""
    return handle.lower() in {k.lower() for k in FOREIGN_CHANNELS}


def foreign_reason(handle: str) -> Optional[str]:
    for k, v in FOREIGN_CHANNELS.items():
        if k.lower() == handle.lower():
            return v
    return None


def channel_country(handle: str) -> Optional[str]:
    """ISO 3166-1 alpha-2 country for a seeded channel, else ``None``."""
    meta = SOCIAL_CHANNELS.get(handle)
    return meta.get("country") if meta else None


def country_provenance(handle: str) -> dict:
    """Auditable country record for a seeded channel (empty dict if unknown)."""
    meta = SOCIAL_CHANNELS.get(handle)
    if not meta:
        return {}
    return {
        "channel": handle,
        "country": meta.get("country"),
        "country_confidence": meta.get("country_confidence"),
        "country_verified_on": meta.get("country_verified_on"),
        "country_signals": list(meta.get("country_signals", [])),
        "country_evidence": meta.get("country_evidence", ""),
        "language": meta.get("language"),
        "persian_ratio": meta.get("persian_ratio"),
        "persian_verified_on": meta.get("persian_verified_on"),
    }


def channel_language(handle: str) -> Optional[str]:
    """Declared content language for a seeded channel (``fa`` expected)."""
    meta = SOCIAL_CHANNELS.get(handle)
    return meta.get("language") if meta else None


def is_persian_channel(handle: str) -> bool:
    """v2.12: a seeded channel must be declared Persian/Farsi.

    Verified against the live mirror by ``social_crawl audit-persian`` and by
    :mod:`src.parser.persian_gate` at parse time; this is the static seed-list
    half of that contract.
    """
    return channel_language(handle) == "fa"


def is_iranian_channel(handle: str) -> bool:
    """The single admission predicate for the social path.

    Default deny: a handle must be explicitly seeded, not on the foreign deny
    list, and carry audited ``country == "IR"`` provenance.
    """
    if is_foreign_channel(handle):
        return False
    # v2.12: Iranian AND Persian-publishing are both required.
    return channel_country(handle) == "IR" and is_persian_channel(handle)


_ROLE_ORDER = {"seller_research": 0, "seller_industrial": 1, "news": 2, "lead_source": 3}


def active_channels(roles: Optional[List[str]] = None) -> List[str]:
    """Verified channel handles, research sellers first.

    ``roles`` optionally filters by role (e.g. ``["seller_research"]``).

    Only channels with audited Iranian provenance are ever returned (v2.11);
    non-Iranian suppliers cannot enter the crawl set.
    """
    items = [(h, m) for h, m in SOCIAL_CHANNELS.items()
             if (roles is None or m["role"] in roles)
             # v2.11 country gate: Iranian suppliers ONLY, default deny.
             and is_iranian_channel(h)]
    items.sort(key=lambda kv: (_ROLE_ORDER.get(kv[1]["role"], 9), kv[0].lower()))
    return [h for h, _ in items]


def channel_role(handle: str) -> str:
    """Role for a handle; unknown handles are treated as ``news`` (strictest)."""
    meta = SOCIAL_CHANNELS.get(handle)
    return meta["role"] if meta else "news"


def channel_description(handle: str) -> str:
    meta = SOCIAL_CHANNELS.get(handle)
    return meta["description"] if meta else ""


def is_rejected(handle: str) -> bool:
    return handle in REJECTED_CHANNELS


def rejection_reason(handle: str) -> Optional[str]:
    return REJECTED_CHANNELS.get(handle)


# Tokens that mark a forwarded-from handle as a plausible chemical/lab source.
# Forwarded-from harvesting is high-recall but noisy (news outlets, podcasts,
# bots), so candidates are ranked before a human spends a probe on them.
_RELEVANT_TOKENS = (
    "chem", "shimi", "kimia", "kimya", "lab", "azma", "polymer", "poly",
    "plast", "nano", "bio", "pharma", "daru", "sanat", "reagent", "solvent",
    "resin", "petro", "zone", "materials", "elab",
)
# Handles that are clearly not vendor catalogues.
_IRRELEVANT_TOKENS = (
    "bot", "news", "bbc", "dw_", "khabar", "podcast", "audiobook", "alumni",
    "society", "university", "unii", "student", "thought", "subtitle",
    "publish", "nobat", "energyir", "jomhor", "entekhab", "tabadl",
)


def score_lead(handle: str) -> int:
    """Heuristic relevance score for a forwarded-from candidate.

    Positive = worth content-verifying. This only ORDERS human effort; nothing
    enters the seed list without a real content check.
    """
    low = handle.lower()
    if low.endswith("bot"):
        return -10
    score = 0
    for tok in _RELEVANT_TOKENS:
        if tok in low:
            score += 2
    for tok in _IRRELEVANT_TOKENS:
        if tok in low:
            score -= 3
    return score


def rank_leads(handles: List[str], min_score: int = 1) -> List[dict]:
    """Rank + filter discovered handles, best candidates first."""
    scored = [{"handle": h, "score": score_lead(h)} for h in handles]
    keep = [s for s in scored if s["score"] >= min_score]
    keep.sort(key=lambda s: (-s["score"], s["handle"].lower()))
    return keep


def whatsapp_rfq_link(number: str, message: str = "") -> str:
    """Build a wa.me RFQ bridge for a vendor contact lead.

    This is a *link*, not an automated message: a human sends the quote request.
    """
    from urllib.parse import quote

    digits = "".join(c for c in number if c.isdigit())
    if digits.startswith("0"):
        digits = "98" + digits[1:]
    base = f"https://wa.me/{digits}"
    return f"{base}?text={quote(message)}" if message else base
