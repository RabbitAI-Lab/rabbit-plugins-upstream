"""Telegram post parser — listing discriminator + price/contact extraction (v2.10).

Reads ONLY local mirror files written by
``src.crawler.telegram_engine.TelegramMirrorEngine`` (the skill's local-file-only
parser contract: no network access here).

Two precision bugs found by live debugging against the real Telegram DOM are
fixed and regression-tested:

1. **Price market-value false positive.** A coatings-news article containing
   "۱۰۰ میلیون دلار" (a market statistic) was extracted as a product price.
   A figure is now only a price when a *volume/pack unit* appears as a proper
   word token within a short window of the number. Requiring a real token —
   not a substring — also fixed a subtle leak where the unit ``gr`` matched
   inside the English word "group".

2. **Educational articles parsed as listings.** News/community channels publish
   explainers that mention chemicals for sale-sounding reasons. A bare Persian
   sales verb is no longer sufficient on ``news``-role channels: those require a
   STRONG listing marker (price, contact, brand, or product hashtag). Seller
   channels may still use verbs, since their posts are catalogue entries by
   construction.

Every rejected candidate carries a machine-readable reason so callers can write
it into ``rejected_catalogue_items`` instead of dropping it silently.
"""
from __future__ import annotations

import html as _html
import os
import re
from typing import Dict, Iterable, List, Optional

from src.discovery.social_seed_list import channel_role
from src.utils.persian_utils import fa_to_en_digits, normalize_fa

# --------------------------------------------------------------------------
# DOM extraction
# --------------------------------------------------------------------------
_MSG_RE = re.compile(
    r'<div class="tgme_widget_message_wrap.*?data-post="(?P<chan>[^"/]+)/(?P<id>\d+)"'
    r'(?P<body>.*?)(?=<div class="tgme_widget_message_wrap|\Z)',
    re.S,
)
_TEXT_RE = re.compile(
    r'<div class="tgme_widget_message_text[^"]*"[^>]*>(?P<t>.*?)</div>', re.S)
_TIME_RE = re.compile(r'<time[^>]+datetime="([^"]+)"')
_FORWARD_RE = re.compile(r'tgme_widget_message_forwarded_from_name"[^>]*href="https://t\.me/([^/"]+)')
_TAG_RE = re.compile(r"<[^>]+>")
_HASHTAG_RE = re.compile(r"#([\w\u0600-\u06FF_]+)")

# --------------------------------------------------------------------------
# Listing signals
# --------------------------------------------------------------------------
# Pack/volume units. Matched as WORD TOKENS (see _has_unit_near) — never as
# substrings, which is what caused the "gr" in "group" false positive.
_UNIT_TOKENS = {
    # Persian
    "گرم", "کیلو", "کیلوگرم", "کیلوگرمی", "لیتر", "لیتری", "میلی", "میلیگرم",
    "میلیلیتر", "بشکه", "بسته", "بستهای", "کارتن", "گالن", "تن", "عدد", "سیسی",
    # Latin
    "g", "gr", "kg", "kgs", "mg", "l", "lt", "ltr", "ml", "cc", "ton", "tonne",
    "drum", "pack", "packs", "bottle", "barrel", "gallon", "unit", "units",
}
_CURRENCY_TOKENS = {"تومان", "ریال", "toman", "rial", "irr", "usd", "دلار", "یورو", "eur"}
# Market-scale words: a figure qualified by these is a market statistic, not a
# unit price (e.g. "۱۰۰ میلیون دلار market size").
_MARKET_SCALE = {"میلیون", "میلیارد", "تریلیون", "million", "billion", "trillion"}

_QUOTE_ONLY = ("استعلام قیمت", "استعلام", "تماس بگیرید", "قیمت روز", "call for price")

# Recruitment adverts. `lead_source` marketplaces (e.g. LabTel) are dominated by
# job posts that carry price-like salary figures, phone numbers and hashtags —
# i.e. every "strong marker" a product listing has. Without this filter they
# flood the catalogue with thousands of phantom candidates.
_JOB_AD_MARKERS = (
    "استخدام", "جویای کار", "جویای_کار", "حقوق", "بیمه", "شیفت", "پورسانت",
    "سابقه کار", "رزومه", "مسئول فنی", "نیروی فنی", "کارشناس آزمایشگاه",
    "پذیرش آزمایشگاه", "حقوق توافقی", "ساعت کاری", "تمام وقت", "پاره وقت",
    "hiring", "vacancy", "recruit", "salary", "resume", "cv ",
)

_SALES_VERBS = ("فروش", "عرضه", "تأمین", "تامین", "موجود", "پخش", "واردات",
                "صادرات", "قیمت", "خرید", "sale", "supply", "available", "in stock")
_STRONG_MARKERS = ("قیمت", "تومان", "ریال", "موجودی", "بسته بندی", "بسته‌بندی",
                   "خلوص", "گرید", "برند", "price", "purity", "grade", "brand")

_PHONE_RE = re.compile(r"(?:\+?98|0)9\d{9}\b")
_CAS_RE = re.compile(r"\b\d{2,7}-\d{2}-\d\b")
_PRICE_NUM_RE = re.compile(r"\b\d{1,3}(?:[,،]\d{3})+\b|\b\d{4,12}\b")
_TOKEN_SPLIT_RE = re.compile(r"[^\w\u0600-\u06FF]+")


def _strip_html(fragment: str) -> str:
    text = fragment.replace("<br/>", "\n").replace("<br>", "\n")
    text = _TAG_RE.sub(" ", text)
    return _html.unescape(text)


def _tokens(text: str) -> List[str]:
    return [t for t in _TOKEN_SPLIT_RE.split(text.lower()) if t]


def _has_unit_near(text: str, match_start: int, match_end: int,
                   window: int = 30) -> bool:
    """True when a pack/volume unit is a WORD TOKEN near the figure.

    Substring matching is deliberately avoided: it made "gr" match inside
    "group" and produced phantom prices.
    """
    left = text[max(0, match_start - window):match_start]
    right = text[match_end:match_end + window]
    for tok in _tokens(left) + _tokens(right):
        if tok in _UNIT_TOKENS:
            return True
    return False


def _has_market_scale_near(text: str, start: int, end: int, window: int = 20) -> bool:
    span = text[max(0, start - window):end + window]
    return any(w in _tokens(span) for w in _MARKET_SCALE)


def extract_price(text: str) -> Optional[dict]:
    """Extract a unit price, or None.

    Returns ``{"value", "currency", "raw"}``. Quote-only posts
    ("استعلام قیمت") correctly return None — that is a real absence of price,
    not a parse failure.
    """
    norm = fa_to_en_digits(text)
    lowered = norm.lower()
    if any(q in norm or q in lowered for q in _QUOTE_ONLY):
        return None
    if not any(c in _tokens(norm) for c in _CURRENCY_TOKENS):
        return None
    for m in _PRICE_NUM_RE.finditer(norm):
        # Reject market statistics ("100 million dollars") outright.
        if _has_market_scale_near(norm, m.start(), m.end()):
            continue
        if not _has_unit_near(norm, m.start(), m.end()):
            continue
        digits = m.group(0).replace(",", "").replace("،", "")
        try:
            value = float(digits)
        except ValueError:
            continue
        if value < 1000:  # below any realistic IRR/toman unit price
            continue
        currency = "IRR"
        toks = _tokens(norm)
        if "تومان" in toks or "toman" in toks:
            currency = "IRT"
        elif "دلار" in toks or "usd" in toks:
            currency = "USD"
        return {"value": value, "currency": currency, "raw": m.group(0)}
    return None


def is_job_advert(text: str) -> bool:
    """True for recruitment posts, which mimic every product-listing signal."""
    norm = normalize_fa(text)
    hits = sum(1 for m in _JOB_AD_MARKERS if m in norm)
    return hits >= 2


def has_sales_signal(text: str, role: str) -> tuple:
    """Decide whether a post is a product LISTING. Returns (bool, reason).

    Seller channels: a sales verb is enough (their posts are catalogue entries).
    News/community/lead channels: a STRONG marker is required, because these
    publish educational articles that mention chemicals in passing.
    Recruitment adverts are excluded everywhere.
    """
    if is_job_advert(text):
        return False, "job_advert_not_a_product_listing"
    norm = normalize_fa(text)
    strong = (
        bool(_PHONE_RE.search(fa_to_en_digits(text)))
        or extract_price(text) is not None
        or bool(_HASHTAG_RE.search(text))
        or any(mk in norm for mk in _STRONG_MARKERS)
    )
    # v2.12: a post with the SHAPE of a catalogue entry (SKU + Latin name +
    # purity/pack/CAS) is a product listing even without a sales verb or price.
    # This is how structured importer posts like
    # "006123 Exir Melamine, 99% 500g" are recovered instead of discarded.
    from src.parser.listing_extractor import is_structured_catalogue_post
    structured = is_structured_catalogue_post(text)

    if role in ("seller_research", "seller_industrial"):
        if strong:
            return True, "strong_marker"
        if structured:
            return True, "structured_catalogue_line"
        if any(v in norm for v in _SALES_VERBS):
            return True, "sales_verb_on_seller_channel"
        return False, "no_sales_signal"
    # news / lead_source / unknown -> strict. A structured catalogue line still
    # counts: it is unambiguous product data wherever it is posted.
    if strong:
        return True, "strong_marker_on_news_channel"
    if structured:
        return True, "structured_catalogue_line_on_news_channel"
    return False, "news_channel_requires_strong_marker"


def parse_page(html_text: str, *, channel: Optional[str] = None) -> List[dict]:
    """Parse one saved preview page into post dicts."""
    posts: List[dict] = []
    for m in _MSG_RE.finditer(html_text):
        chan = channel or m.group("chan")
        body = m.group("body")
        tm = _TEXT_RE.search(body)
        text = _strip_html(tm.group("t")).strip() if tm else ""
        text = re.sub(r"[ \t]+", " ", text)
        when = _TIME_RE.search(body)
        fwd = _FORWARD_RE.search(body)
        posts.append({
            "channel": chan,
            "post_id": int(m.group("id")),
            "url": f"https://t.me/{chan}/{m.group('id')}",
            "text": text,
            "date": when.group(1) if when else None,
            "forwarded_from": fwd.group(1) if fwd else None,
            "hashtags": _HASHTAG_RE.findall(text),
        })
    return posts


def parse_post(post: dict, *, role: Optional[str] = None) -> dict:
    """Enrich a post with listing decision, price, contact and CAS numbers."""
    role = role or channel_role(post.get("channel", ""))
    text = post.get("text", "") or ""
    is_listing, reason = has_sales_signal(text, role)
    phones = _PHONE_RE.findall(fa_to_en_digits(text))
    out = dict(post)
    out.update({
        "role": role,
        "is_listing": is_listing,
        "listing_reason": reason,
        "price": extract_price(text) if is_listing else None,
        "contacts": sorted(set(phones)),
        "cas_numbers": sorted(set(_CAS_RE.findall(text))),
    })
    return out


def parse_channel_dir(channel_dir: str, *, channel: Optional[str] = None) -> List[dict]:
    """Parse every saved page in a channel mirror dir, de-duplicated by post id."""
    if not os.path.isdir(channel_dir):
        return []
    chan = channel or os.path.basename(channel_dir.rstrip("/"))
    by_id: Dict[int, dict] = {}
    for name in sorted(os.listdir(channel_dir)):
        if not name.endswith(".html"):
            continue
        try:
            with open(os.path.join(channel_dir, name), "r", encoding="utf-8") as fh:
                page = fh.read()
        except OSError:
            continue
        for post in parse_page(page, channel=chan):
            by_id[post["post_id"]] = post  # dedup across pagination seams
    return [parse_post(p) for p in sorted(by_id.values(), key=lambda p: p["post_id"])]


def harvest_forwarded_sources(posts: Iterable[dict]) -> List[str]:
    """Channels these posts were forwarded FROM — the discovery mechanism that
    surfaced new real sellers (e.g. Boof_company, fanchem).

    Returns candidate handles only; each still needs content-verification
    before it may enter the seed list.
    """
    seen = {p.get("forwarded_from") for p in posts if p.get("forwarded_from")}
    return sorted(h for h in seen if h)
