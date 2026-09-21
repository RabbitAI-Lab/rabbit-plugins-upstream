"""Social catalogue pipeline — mirror -> parse -> resolve -> metrics (v2.10).

Ties the v2.10 pieces together and produces the same auditable outputs the rest
of the skill guarantees:

  * confirmed listings with molecule identity, grade, price and contact;
  * every rejected candidate with a stage + reason (never silently dropped);
  * measured metrics (coverage %, resolve rate, listing precision inputs).

Parsing is **local-file-only**: this module never fetches. Mirroring is a
separate, explicit step (``src.crawler.telegram_engine``). The only optional
network call is PubChem enrichment, disabled with ``offline=True``.
"""
from __future__ import annotations

import logging
from datetime import datetime
from typing import Dict, List, Optional

from src.parser.listing_extractor import extract_listing_fields
from src.parser.persian_gate import channel_persian_profile, post_language
from src.discovery.social_seed_list import (SOCIAL_CHANNELS, active_channels,
                                            channel_description, channel_role,
                                            country_provenance, foreign_reason,
                                            is_iranian_channel)
from src.parser.social_molecule_resolver import (classify_grade,
                                                 is_generic_announcement,
                                                 resolve)
from src.parser.telegram_parser import (harvest_forwarded_sources,
                                        parse_channel_dir)

logger = logging.getLogger(__name__)


def build_channel_catalog(channel_dir: str, channel: str, *,
                          offline: bool = True) -> dict:
    """Parse one mirrored channel into listings + rejections + metrics."""
    role = channel_role(channel)
    posts = parse_channel_dir(channel_dir, channel=channel)

    # v2.12 PERSIAN GATE — every channel must actually publish Persian/Farsi.
    # Measured over the whole mirror, so one English catalogue post cannot
    # disqualify a Persian channel and an English-only channel cannot pass.
    persian = channel_persian_profile(channel, [p["text"] for p in posts])

    listings: List[dict] = []
    rejections: List[dict] = []

    if not persian.is_persian:
        logger.warning("social: EXCLUDED non-Persian channel %s (%s)",
                       channel, persian.reason)
        return {
            "channel": channel, "role": role,
            "description": channel_description(channel),
            "listings": [], "rejections": [{
                "channel": channel, "post_id": None, "url": None,
                "rejection_stage": "persian_language_gate",
                "rejection_reason": persian.reason,
            }],
            "forwarded_sources": [],
            "persian_profile": persian.as_dict(),
            "excluded": True,
            "metrics": {"posts_parsed": len(posts), "listings": 0,
                        "rejected": len(posts), "listing_rate_pct": 0.0,
                        "with_price": 0},
        }

    for post in posts:
        if not post["is_listing"]:
            rejections.append({
                "channel": channel, "post_id": post["post_id"],
                "url": post["url"], "rejection_stage": "listing_discriminator",
                "rejection_reason": post["listing_reason"],
            })
            continue

        cas_hint = post["cas_numbers"][0] if post["cas_numbers"] else None
        ident = resolve(post["text"], cas_hint=cas_hint, offline=offline)
        if not ident["resolved"]:
            # Separate "advertises a catalogue but names no molecule" from
            # "names a molecule we can't resolve" — only the latter is a
            # dictionary gap worth remediating.
            generic = is_generic_announcement(post["text"])
            rejections.append({
                "channel": channel, "post_id": post["post_id"],
                "url": post["url"], "rejection_stage": "identity_resolution",
                "rejection_reason": ("generic_announcement_no_molecule_named"
                                     if generic else "no_alias_or_cas_match"),
            })
            continue

        fields = extract_listing_fields(post["text"]).as_dict()
        grade, grade_reason = classify_grade(
            post["text"], ident.get("canonical_name"), role)
        listings.append({
            "channel": channel, "role": role, "post_id": post["post_id"],
            "url": post["url"], "date": post["date"],
            "canonical_name": ident["canonical_name"],
            "display_name": (ident["canonical_name"]
                             or (f"CAS {ident['cas_number']}"
                                 if ident["cas_number"] else "unidentified")),
            "cas_number": ident["cas_number"],
            "kind": ident["kind"], "identity_method": ident["method"],
            "pubchem_cid": ident["pubchem_cid"],
            "inchi_key": ident["inchi_key"],
            "molecular_formula": ident["molecular_formula"],
            "grade": grade, "grade_reason": grade_reason,
            "price": post["price"], "contacts": post["contacts"],
            "hashtags": post["hashtags"],
            "source_file_dir": channel_dir,
            # v2.12 structured commercial fields — the practical payload for
            # anyone actually sourcing a chemical.
            "sku": fields.get("sku"),
            "brand": fields.get("brand"),
            "purity_percent": fields.get("purity_percent"),
            "grade_token": fields.get("grade_token"),
            "pack_size": fields.get("pack_size"),
            "availability": fields.get("availability"),
            "name_candidate": ident.get("name_candidate"),
            "post_language": post_language(post["text"]),
            # Persian users search in Persian, but resolved names are English.
            # Keep a trimmed snippet of the original post so `search --query`
            # matches the vendor's own wording (e.g. «سدیم هیدروکسید»).
            "text_snippet": " ".join((post["text"] or "").split())[:300],
            "structured_field_count": fields.get("structured_field_count", 0),
        })

    total = len(posts)
    resolved = len(listings)
    return {
        "channel": channel,
        "role": role,
        "description": channel_description(channel),
        "listings": listings,
        "rejections": rejections,
        "forwarded_sources": harvest_forwarded_sources(posts),
        "persian_profile": persian.as_dict(),
        "excluded": False,
        "metrics": {
            "posts_parsed": total,
            "listings": resolved,
            "rejected": len(rejections),
            "listing_rate_pct": round(100.0 * resolved / total, 1) if total else 0.0,
            "with_price": sum(1 for x in listings if x["price"]),
            "with_contact": sum(1 for x in listings if x["contacts"]),
            "grade_split": _count(listings, "grade"),
        },
    }


def _count(rows: List[dict], key: str) -> Dict[str, int]:
    out: Dict[str, int] = {}
    for r in rows:
        out[str(r.get(key))] = out.get(str(r.get(key)), 0) + 1
    return dict(sorted(out.items()))


def build_catalog(base_mirror_dir: str, channels: Optional[List[str]] = None,
                  *, offline: bool = True) -> dict:
    """Build the full social catalogue from every mirrored channel."""
    import os

    channels = channels or active_channels()
    per_channel, all_listings, all_rejections = [], [], []
    forwarded: set = set()

    excluded_foreign = []
    for ch in channels:
        # v2.11 COUNTRY GATE — Iranian suppliers ONLY, enforced here as well as
        # in active_channels() so an explicit --channel argument can never
        # inject a foreign supplier into the catalogue. Default deny.
        if not is_iranian_channel(ch):
            reason = (foreign_reason(ch)
                      or ("not seeded with audited Iranian provenance"
                          if ch not in SOCIAL_CHANNELS
                          else "seeded country != IR"))
            logger.warning("social: EXCLUDED non-Iranian supplier %s (%s)", ch, reason)
            excluded_foreign.append({"channel": ch, "reason": reason,
                                     "policy": "iranian_suppliers_only"})
            continue
        cdir = os.path.join(base_mirror_dir, "social", "telegram", ch)
        if not os.path.isdir(cdir):
            logger.info("social: no mirror for %s (skipped)", ch)
            continue
        res = build_channel_catalog(cdir, ch, offline=offline)
        per_channel.append(res)
        all_listings.extend(res["listings"])
        all_rejections.extend(res["rejections"])
        forwarded.update(res["forwarded_sources"])

    molecules: Dict[str, dict] = {}
    for row in all_listings:
        key = (row["inchi_key"] or row["cas_number"]
               or f"name:{row['canonical_name']}")
        # A CAS-only hit may have no name yet (offline, or PubChem missed it).
        # Label it by its CAS instead of leaving None, which is unsortable and
        # renders as an empty cell downstream.
        display = (row["canonical_name"]
                   or (f"CAS {row['cas_number']}" if row["cas_number"] else "unidentified"))
        mol = molecules.setdefault(key, {
            "identity": key, "canonical_name": display,
            "cas_number": row["cas_number"], "kind": row["kind"],
            "pubchem_cid": row["pubchem_cid"], "inchi_key": row["inchi_key"],
            "molecular_formula": row["molecular_formula"],
            "vendors": set(), "offerings": 0,
        })
        mol["vendors"].add(row["channel"])
        mol["offerings"] += 1
    for mol in molecules.values():
        mol["vendors"] = sorted(mol["vendors"])

    # Only propose forwarded sources we haven't already judged, and RANK them:
    # forwarded-from harvesting is high-recall but noisy (news, podcasts, bots),
    # so ordering keeps human verification effort on plausible vendors.
    from src.discovery.social_seed_list import is_rejected, rank_leads
    from src.discovery.social_seed_list import is_foreign_channel
    raw_leads = sorted(h for h in forwarded
                       if h not in SOCIAL_CHANNELS and not is_rejected(h)
                       # Never propose a known foreign supplier as a lead.
                       and not is_foreign_channel(h))
    ranked = rank_leads(raw_leads)
    new_leads = [r["handle"] for r in ranked]

    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        # v2.11: auditable proof that every vendor in this catalogue is Iranian.
        # v2.12 — proof that every channel publishes Persian/Farsi.
        "persian_language_policy": {
            "policy": "iranian_persian_channels_only",
            "requirement": ("each channel must be Iranian (country gate) AND "
                            "publish Persian/Farsi text (>=30% of text posts)"),
            "channels": [c.get("persian_profile") for c in per_channel
                         if c.get("persian_profile")],
        },
        "supplier_country_policy": {
            "policy": "iranian_suppliers_only",
            "allowed_countries": ["IR"],
            "enforcement": ("active_channels() + build_catalog() country gate; "
                            "default deny, evidence-based"),
            "note": ("Supplier nationality only. Iranian importers legitimately "
                     "resell foreign BRANDS (Merck, Sigma-Aldrich, TCI); brand "
                     "is product metadata and never implies a foreign supplier."),
            "vendors": [country_provenance(c["channel"]) for c in per_channel],
            "excluded_foreign": excluded_foreign,
        },
        "channels": per_channel,
        "molecules": list(molecules.values()),
        "listings": all_listings,
        "rejections": all_rejections,
        "discovered_leads": new_leads,
        "discovered_leads_ranked": ranked,
        "discovered_leads_all": raw_leads,
        "metrics": {
            "channels_parsed": len(per_channel),
            "molecules": len(molecules),
            "listings": len(all_listings),
            "rejections": len(all_rejections),
            "vendors": len({r["channel"] for r in all_listings}),
            "grade_split": _count(all_listings, "grade"),
            "identity_methods": _count(all_listings, "identity_method"),
            "resolve_rate_pct": (
                round(100.0 * len(all_listings)
                      / (len(all_listings) + sum(
                          1 for r in all_rejections
                          if r["rejection_stage"] == "identity_resolution")), 1)
                if all_listings else 0.0),
            "discovered_leads": len(new_leads),
            "discovered_leads_unfiltered": len(raw_leads),
            "excluded_foreign_suppliers": len(excluded_foreign),
            "excluded_non_persian": len([c for c in per_channel
                                         if c.get("excluded")]),
            "listings_with_price": sum(1 for r in all_listings if r.get("price")),
            "listings_with_pack_size": sum(1 for r in all_listings
                                           if r.get("pack_size")),
            "listings_with_brand": sum(1 for r in all_listings if r.get("brand")),
            "listings_with_purity": sum(1 for r in all_listings
                                        if r.get("purity_percent")),
            "listings_with_sku": sum(1 for r in all_listings if r.get("sku")),
            "vendor_countries": sorted({country_provenance(c["channel"]).get("country")
                                        for c in per_channel} - {None}),
        },
        "disclaimer": (
            "BEST-EFFORT index of PUBLIC Telegram channel posts. Telegram only: "
            "Instagram/Facebook/X are login-walled and WhatsApp is contact-only, "
            "so they are captured as vendor leads, not scraped. Never infer "
            "national availability from this catalogue."
        ),
    }
