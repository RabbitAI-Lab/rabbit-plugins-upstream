"""Social catalogue API routes (v2.10).

Exposes the Telegram-sourced catalogue with the same honesty guarantees as the
rest of the API: coverage is measured, rejections are queryable, and the
platform scope is stated on every response.
"""
from __future__ import annotations

import os
from typing import Optional

from fastapi import APIRouter, HTTPException, Query

from src.config import get_config
from src.discovery.social_seed_list import (CONTACT_LEADS, REJECTED_CHANNELS,
                                            SOCIAL_CHANNELS, active_channels,
                                            whatsapp_rfq_link)
from src.parser.social_catalog_pipeline import build_catalog

router = APIRouter(prefix="/api/v1/social", tags=["social"])

SCOPE_NOTE = (
    "Telegram public channels only. Instagram/Facebook/X are login-walled and "
    "WhatsApp is contact-only, so those platforms appear as vendor contact "
    "leads, never as scraped feeds. Never infer national availability."
)


def _mirror_dir() -> str:
    """Mirror root from config (get_config() returns a Config, not a dict)."""
    try:
        data = get_config().as_dict()
    except Exception:  # noqa: BLE001 - fall back to the documented default
        data = {}
    httrack = data.get("httrack")
    httrack = httrack if isinstance(httrack, dict) else {}
    return httrack.get("base_mirror_dir", "/var/lib/iran_chem_db/mirrors")


@router.get("/channels")
def list_channels():
    """Verified channels, their roles, and the content-checked rejects."""
    return {
        "verified": [
            {"handle": h, **meta} for h, meta in SOCIAL_CHANNELS.items()
        ],
        "rejected": [
            {"handle": h, "reason": r} for h, r in REJECTED_CHANNELS.items()
        ],
        "counts": {"verified": len(SOCIAL_CHANNELS),
                   "rejected": len(REJECTED_CHANNELS)},
        "scope": SCOPE_NOTE,
    }


@router.get("/coverage")
def social_coverage():
    """Per-channel mirror coverage — what HAS and has NOT been fetched."""
    from src.crawler.telegram_engine import TelegramMirrorEngine

    eng = TelegramMirrorEngine(_mirror_dir())
    out = []
    for ch in active_channels():
        cdir = eng.channel_dir(ch)
        state = eng.read_state(ch)
        pages = (len([f for f in os.listdir(cdir) if f.endswith(".html")])
                 if os.path.isdir(cdir) else 0)
        out.append({
            "channel": ch,
            "mirrored": pages > 0,
            "pages": pages,
            "newest_id": state.get("newest_id"),
            "oldest_id": state.get("oldest_id"),
            "last_run": state.get("last_run"),
            "crawl_state": ("never_crawled" if pages == 0 else "mirrored"),
        })
    mirrored = sum(1 for r in out if r["mirrored"])
    return {
        "channels": out,
        "summary": {"total": len(out), "mirrored": mirrored,
                    "never_crawled": len(out) - mirrored},
        "complete": mirrored == len(out) and len(out) > 0,
        "scope": SCOPE_NOTE,
    }


@router.get("/molecules")
def social_molecules(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    grade: str | None = Query(None, pattern="^(research|industrial|unknown)$"),
):
    """Paginated molecules from the social catalogue.

    Paginated by design — announce ``total_pages``/``has_more`` and use
    ``/api/v1/social/export`` for a full, unpaginated export.
    """
    cat = build_catalog(_mirror_dir(), offline=True)
    rows = cat["listings"]
    if grade:
        rows = [r for r in rows if r["grade"] == grade]
    total = len(rows)
    pages = max(1, (total + limit - 1) // limit)
    start = (page - 1) * limit
    return {
        "items": rows[start:start + limit],
        "page": page, "limit": limit, "total": total,
        "total_pages": pages, "has_more": page < pages,
        "scope": SCOPE_NOTE,
    }


@router.get("/rejections")
def social_rejections(limit: int = Query(100, ge=1, le=1000)):
    """Audit trail — candidates excluded, with stage + reason."""
    cat = build_catalog(_mirror_dir(), offline=True)
    return {"items": cat["rejections"][:limit],
            "total": len(cat["rejections"]), "scope": SCOPE_NOTE}


@router.get("/export")
def social_export(require_complete_coverage: bool = False):
    """Full, unpaginated social catalogue + metrics manifest."""
    if require_complete_coverage:
        cov = social_coverage()
        if not cov["complete"]:
            raise HTTPException(
                status_code=409,
                detail="social coverage incomplete; some channels never crawled")
    return build_catalog(_mirror_dir(), offline=True)


@router.get("/leads")
def social_leads():
    """Vendor contact leads on non-automatable platforms (+ wa.me RFQ links)."""
    items = []
    for lead in CONTACT_LEADS:
        row = dict(lead)
        if lead["platform"] == "whatsapp":
            row["rfq_link"] = whatsapp_rfq_link(
                lead["handle"], "Quotation request (academic procurement research)")
        items.append(row)
    return {"items": items, "total": len(items), "scope": SCOPE_NOTE}


@router.get("/country-policy")
def country_policy():
    """v2.11 — the Iranian-suppliers-ONLY policy and its audit trail.

    Returns the per-vendor country provenance behind every listing, so a
    consumer can verify (not merely trust) that no foreign supplier data is
    present. ``brand_note`` records the one nuance that matters chemically:
    Iranian importers legitimately resell foreign BRANDS.
    """
    from src.discovery.social_seed_list import (FOREIGN_CHANNELS,
                                                SOCIAL_CHANNELS,
                                                country_provenance)
    return {
        "policy": "iranian_suppliers_only",
        "allowed_countries": ["IR"],
        "enforcement": [
            "active_channels() returns only audited Iranian channels",
            "build_catalog() re-checks every channel (default deny)",
            "SupplierValidator.verify() gates the web-discovery path",
            "all Supplier inserts require country == IR",
        ],
        "brand_note": (
            "Supplier nationality only. Iranian importers legitimately resell "
            "foreign brands (Merck, Sigma-Aldrich, TCI); brand is product "
            "metadata and never implies a foreign supplier."
        ),
        "vendors": [country_provenance(h) for h in SOCIAL_CHANNELS],
        "foreign_denylist": FOREIGN_CHANNELS,
    }


@router.get("/search")
def social_search(
    q: str = Query(..., min_length=1,
                   description="name, CAS, brand, SKU or Persian text"),
    brand: str = Query(None), in_stock: bool = Query(False),
    with_price: bool = Query(False),
    limit: int = Query(100, ge=1, le=1000),
):
    """v2.12 — one-call retrieval of Iranian supplier listings.

    Searches resolved names, CAS, brand, SKU **and the original Persian post
    text**, so Persian queries («سدیم هیدروکسید») work even though canonical
    names are English.
    """
    from src.parser.persian_gate import normalize_persian
    cat = build_catalog(_mirror_dir(), offline=True)
    rows = cat.get("listings", [])
    ql = q.strip().lower()
    qn = normalize_persian(ql)

    def hit(r):
        hay = " ".join(str(r.get(k) or "") for k in
                       ("canonical_name", "display_name", "cas_number", "brand",
                        "sku", "name_candidate", "text_snippet")).lower()
        return ql in hay or qn in normalize_persian(hay)

    rows = [r for r in rows if hit(r)]
    if brand:
        rows = [r for r in rows if (r.get("brand") or "").lower() == brand.lower()]
    if in_stock:
        rows = [r for r in rows if r.get("availability") == "in_stock"]
    if with_price:
        rows = [r for r in rows if r.get("price")]
    return {"query": q, "count": len(rows), "listings": rows[:limit],
            "scope": "Iranian suppliers only; Persian-verified Telegram channels"}


@router.get("/persian-policy")
def persian_policy():
    """v2.12 — proof that every channel publishes Persian/Farsi."""
    cat = build_catalog(_mirror_dir(), offline=True)
    pol = cat.get("persian_language_policy", {})
    return {
        "policy": "iranian_persian_channels_only",
        "requirement": ("each channel must be Iranian (country gate) AND "
                        "publish Persian/Farsi text (>=30% of text posts)"),
        "note": ("Enforced at CHANNEL level. Individual Latin-only catalogue "
                 "lines inside a verified Persian channel are kept - they are "
                 "the highest-value structured product data on the network."),
        "channels": pol.get("channels", []),
    }


@router.get("/verify-suppliers")
def verify_suppliers(
    channel: Optional[str] = Query(None, description="verify a single channel"),
    level: str = Query("offline", pattern="^(offline|live|paranoid)$"),
    explain: bool = Query(True, description="include per-claim working"),
):
    """v2.13 — let the CALLING AGENT re-derive Iranian origin for itself.

    This endpoint deliberately returns the evidence, not just a boolean: every
    claim carries its value, its checker's verdict and a human-readable detail,
    so an agent can show its work (or disagree with ours).

    level=offline   arithmetic + local mirror only, no network
    level=live      additionally re-fetches t.me/s/<channel> right now
    level=paranoid  ignores stored claims entirely; live page must stand alone
    """
    from src.discovery.social_seed_list import SOCIAL_CHANNELS
    from src.verification import verify_channel
    from src.verification.agent_verify import MIN_FAMILIES, MIN_SCORE

    if channel:
        targets = [channel]
    else:
        targets = [c["handle"] if isinstance(c, dict) else c
                   for c in SOCIAL_CHANNELS]

    verdicts = [verify_channel(ch, level=level) for ch in targets]
    out = []
    for v in verdicts:
        d = v.as_dict()
        if not explain:
            d.pop("claims", None)
        out.append(d)
    return {
        "policy": "iranian_sellers_only",
        "level": level,
        "how_to_read": (
            "verified=true means this channel independently satisfied "
            f">= {MIN_FAMILIES} evidence families and score >= {MIN_SCORE} "
            "from re-checkable claims. Anything else is quarantined: do NOT "
            "present its listings as Iranian-sourced."
        ),
        "verified": sum(1 for v in verdicts if v.verified),
        "total": len(verdicts),
        "all_verified": all(v.verified for v in verdicts),
        "verdicts": out,
    }
