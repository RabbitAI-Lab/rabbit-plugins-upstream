"""CLI for the v2.10 social (Telegram) catalogue.

    python -m src.scripts.social_crawl verify            # content-verify channels
    python -m src.scripts.social_crawl mirror            # mirror to local store
    python -m src.scripts.social_crawl parse             # build catalogue (local only)
    python -m src.scripts.social_crawl parse --enrich    # + PubChem enrichment
    python -m src.scripts.social_crawl leads             # contact leads / RFQ links

Mirroring touches the network; parsing does not.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

from src.config import get_config
from src.crawler.telegram_engine import TelegramMirrorEngine
from src.discovery.social_seed_list import (CONTACT_LEADS, REJECTED_CHANNELS,
                                            active_channels, whatsapp_rfq_link)
from src.parser.social_catalog_pipeline import build_catalog


def _cfg_section(name: str, default: dict | None = None) -> dict:
    """Read a config section as a plain dict (get_config() returns a Config)."""
    try:
        data = get_config().as_dict()
    except Exception:  # noqa: BLE001 - config is optional for local parsing
        return dict(default or {})
    sec = data.get(name)
    return dict(sec) if isinstance(sec, dict) else dict(default or {})


def _engine() -> TelegramMirrorEngine:
    social = _cfg_section("social")
    httrack = _cfg_section("httrack")
    base = httrack.get("base_mirror_dir", "/var/lib/iran_chem_db/mirrors")
    return TelegramMirrorEngine(
        base,
        timeout=social.get("timeout_seconds", 40),
        max_pages=social.get("max_pages_per_channel", 200),
        concurrency=social.get("concurrency", 6),
        request_delay=social.get("request_delay_seconds", 0.2),
    )


def _print_table(rows) -> None:
    """Human-readable listing table — the default `search`/`fetch` output."""
    if not rows:
        print("no matching listings")
        return
    print(f"{'molecule':38} {'CAS':12} {'brand':13} {'pack':9} {'price':13} channel")
    print("-" * 104)
    for r in rows[:200]:
        pack = (r.get("pack_size") or {}).get("raw") or ""
        pr = r.get("price") or {}
        price = f"{pr.get('value'):,.0f} {pr.get('currency')}" if pr else ""
        print(f"{str(r.get('display_name') or '')[:38]:38} "
              f"{str(r.get('cas_number') or ''):12} "
              f"{str(r.get('brand') or '')[:13]:13} "
              f"{pack[:9]:9} {price[:13]:13} {r.get('channel','')}")
    if len(rows) > 200:
        print(f"... and {len(rows) - 200} more (use --out to write them all)")
    print(f"\n{len(rows)} listings")


def write_listings(rows, path: str, catalog=None) -> int:
    """Write listings to .csv / .json / .xlsx, chosen by file extension."""
    ext = os.path.splitext(path)[1].lower()
    cols = ["channel", "display_name", "canonical_name", "cas_number",
            "pubchem_cid", "molecular_formula", "brand", "sku",
            "purity_percent", "grade_token", "pack_raw", "pack_value",
            "pack_unit", "price_value", "price_currency", "availability",
            "grade", "identity_method", "post_language", "date", "url"]

    def flat(r):
        pack = r.get("pack_size") or {}
        pr = r.get("price") or {}
        return {
            "channel": r.get("channel"), "display_name": r.get("display_name"),
            "canonical_name": r.get("canonical_name"),
            "cas_number": r.get("cas_number"), "pubchem_cid": r.get("pubchem_cid"),
            "molecular_formula": r.get("molecular_formula"),
            "brand": r.get("brand"), "sku": r.get("sku"),
            "purity_percent": r.get("purity_percent"),
            "grade_token": r.get("grade_token"),
            "pack_raw": pack.get("raw"),
            "pack_value": pack.get("normalised_value"),
            "pack_unit": pack.get("normalised_unit"),
            "price_value": pr.get("value"), "price_currency": pr.get("currency"),
            "availability": r.get("availability"), "grade": r.get("grade"),
            "identity_method": r.get("identity_method"),
            "post_language": r.get("post_language"),
            "date": r.get("date"), "url": r.get("url"),
        }

    flat_rows = [flat(r) for r in rows]
    os.makedirs(os.path.dirname(os.path.abspath(path)) or ".", exist_ok=True)

    if ext == ".json":
        payload = {"listings": flat_rows, "count": len(flat_rows)}
        if catalog:
            payload["metrics"] = catalog.get("metrics")
            payload["supplier_country_policy"] = catalog.get("supplier_country_policy")
            payload["persian_language_policy"] = catalog.get("persian_language_policy")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=2, default=str)
        return len(flat_rows)

    if ext == ".xlsx":
        try:
            from openpyxl import Workbook
        except ImportError as exc:
            raise SystemExit("openpyxl is not installed; use .csv or .json") from exc
        wb = Workbook()
        ws = wb.active
        ws.title = "listings"
        ws.append(cols)
        for r in flat_rows:
            ws.append([r.get(c) for c in cols])
        wb.save(path)
        return len(flat_rows)

    import csv
    with open(path, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(["# Iran Chem DB — Iranian suppliers ONLY, Persian-verified "
                    "Telegram channels"])
        w.writerow(cols)
        for r in flat_rows:
            w.writerow([r.get(c) for c in cols])
    return len(flat_rows)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Iran Chem DB — social catalogue")
    ap.add_argument("command",
                    choices=["verify", "mirror", "parse", "leads", "channels",
                             "audit-country", "fetch", "search", "audit-persian",
                             "verify-suppliers"])
    ap.add_argument("--channel", action="append",
                    help="limit to this channel (repeatable)")
    ap.add_argument("--enrich", action="store_true",
                    help="allow PubChem enrichment during parse (network)")
    ap.add_argument("--no-full-history", action="store_true",
                    help="only fetch the newest page")
    ap.add_argument("--json", action="store_true", help="raw JSON output")
    ap.add_argument("--out", help="write results to this file (.csv/.json/.xlsx by extension)")
    ap.add_argument("--query", help="search term for `search` (name, CAS, brand or Persian)")
    ap.add_argument("--with-price", action="store_true",
                    help="only listings that carry a price")
    ap.add_argument("--in-stock", action="store_true",
                    help="only listings marked available")
    ap.add_argument("--brand", help="filter by brand, e.g. Merck")
    ap.add_argument("--level", choices=["offline", "live", "paranoid"],
                    default="offline",
                    help="verify-suppliers: how hard to re-check (default offline)")
    ap.add_argument("--dataset",
                    help="verify-suppliers: audit a listings .csv/.json instead "
                         "of the seed list")
    ap.add_argument("--explain", action="store_true",
                    help="verify-suppliers: print per-claim PASS/FAIL working")
    args = ap.parse_args(argv)

    channels = args.channel or active_channels()

    if args.command == "channels":
        for ch in channels:
            print(f"{ch:24s} {__import__('src.discovery.social_seed_list', fromlist=['x']).channel_role(ch)}")
        print(f"\nrejected (do not retry): {len(REJECTED_CHANNELS)}")
        return 0

    if args.command == "verify-suppliers":
        # v2.13 — the agent re-derives Iranian origin ITSELF instead of
        # trusting this package. Exits non-zero when anything fails to
        # verify, so it can be used as a gate in a pipeline.
        from src.verification import verify_channel, verify_dataset
        from src.verification.agent_verify import load_rows

        if args.dataset:
            report = verify_dataset(load_rows(args.dataset), level=args.level)
            if args.json:
                print(json.dumps(report, ensure_ascii=False, indent=2))
            else:
                print(f"dataset: {args.dataset}")
                print(f"policy : {report['policy']}  level={report['level']}")
                for name in sorted(report["verdicts"]):
                    v = report["verdicts"][name]
                    mark = "OK  " if v["verified"] else "FAIL"
                    print(f"  [{mark}] {name:24s} score={v['score']:>4} "
                          f"rows={report['row_counts'].get(name, 0):>4} "
                          f"{'' if v['verified'] else '- ' + v['reason']}")
                print(f"\n{report['suppliers_verified']}/{report['suppliers_total']} "
                      f"suppliers verified Iranian; "
                      f"{report['rows_from_unverified_suppliers']} of "
                      f"{report['rows_total']} rows quarantined")
                print(f"SAFE TO USE: {report['safe_to_use']}")
            return 0 if report["safe_to_use"] else 1

        verdicts = [verify_channel(ch, level=args.level) for ch in channels]
        if args.json:
            print(json.dumps({"policy": "iranian_sellers_only",
                              "level": args.level,
                              "verdicts": [v.as_dict() for v in verdicts]},
                             ensure_ascii=False, indent=2))
        else:
            for v in verdicts:
                if args.explain:
                    print(v.explain())
                    print()
                else:
                    mark = "OK  " if v.verified else "FAIL"
                    print(f"[{mark}] {v.subject:24s} score={v.score:>4} "
                          f"families={len(set(v.families))} "
                          f"{'' if v.verified else '- ' + v.reason}")
            ok = sum(1 for v in verdicts if v.verified)
            print(f"\n{ok}/{len(verdicts)} channels independently verified "
                  f"Iranian at level={args.level}")
        return 0 if all(v.verified for v in verdicts) else 1

    if args.command == "audit-country":
        # v2.11 — print the auditable Iranian-supplier provenance for every
        # vendor that can enter the catalogue.
        from src.discovery.social_seed_list import (FOREIGN_CHANNELS,
                                                    country_provenance,
                                                    is_iranian_channel)
        rows = [country_provenance(ch) for ch in channels]
        if args.json:
            print(json.dumps({"policy": "iranian_suppliers_only",
                              "allowed_countries": ["IR"],
                              "vendors": rows,
                              "foreign_denylist": FOREIGN_CHANNELS},
                             ensure_ascii=False, indent=2))
            return 0
        print("POLICY: Iranian suppliers ONLY (allowed countries: IR)\n")
        bad = 0
        for r in rows:
            ok = is_iranian_channel(r.get("channel", ""))
            bad += 0 if ok else 1
            print(f"[{'OK' if ok else 'DENY'}] {r.get('channel',''):22s} "
                  f"{r.get('country') or '??'} "
                  f"({r.get('country_confidence') or 'none'})  "
                  f"signals={','.join(r.get('country_signals') or []) or 'none'}")
            if r.get("country_evidence"):
                print(f"       evidence: {r['country_evidence']}")
        print(f"\n{len(rows) - bad}/{len(rows)} vendors verified Iranian; "
              f"{len(FOREIGN_CHANNELS)} handles on the foreign deny-list.")
        return 0 if bad == 0 else 1

    if args.command == "leads":
        for lead in CONTACT_LEADS:
            extra = (f"  rfq={whatsapp_rfq_link(lead['handle'])}"
                     if lead["platform"] == "whatsapp" else "")
            print(f"{lead['platform']:10s} {lead['handle']:20s} {lead['vendor']}{extra}")
        return 0

    if args.command == "audit-persian":
        # Prove every channel publishes Persian/Farsi.
        from src.parser.persian_gate import channel_persian_profile
        from src.parser.telegram_parser import parse_channel_dir
        eng0 = _engine()
        rows, bad = [], 0
        for ch in channels:
            cdir = os.path.join(eng0.base_mirror_dir, "social", "telegram", ch)
            if not os.path.isdir(cdir):
                print(f"[SKIP] {ch:22s} not mirrored yet")
                continue
            posts = parse_channel_dir(cdir, channel=ch)
            prof = channel_persian_profile(ch, [p["text"] for p in posts])
            rows.append(prof.as_dict())
            bad += 0 if prof.is_persian else 1
            if not args.json:
                print(f"[{'OK' if prof.is_persian else 'DENY'}] {ch:22s} "
                      f"fa={prof.persian_ratio:.0%} "
                      f"({prof.posts_persian}/{prof.posts_with_text} posts, "
                      f"ar={prof.posts_arabic})  {prof.reason}")
        if args.json:
            print(json.dumps({"policy": "iranian_persian_channels_only",
                              "channels": rows}, ensure_ascii=False, indent=2))
        elif rows:
            print(f"\n{len(rows) - bad}/{len(rows)} channels verified Persian.")
        return 0 if bad == 0 else 1

    if args.command in ("fetch", "search"):
        # ONE-COMMAND RETRIEVAL: mirror -> parse -> (filter) -> write.
        eng1 = _engine()
        if args.command == "fetch":
            eng1.mirror_channels(channels,
                                 full_history=not args.no_full_history)
        cat = build_catalog(eng1.base_mirror_dir, channels,
                            offline=not args.enrich)
        rows = cat["listings"]

        if args.query:
            q = args.query.strip().lower()
            from src.parser.persian_gate import normalize_persian
            qn = normalize_persian(q)
            def _hit(r):
                hay = " ".join(str(r.get(k) or "") for k in
                               ("canonical_name", "display_name", "cas_number",
                                "brand", "sku", "name_candidate",
                                "text_snippet")).lower()
                return q in hay or qn in normalize_persian(hay)
            rows = [r for r in rows if _hit(r)]
        if args.with_price:
            rows = [r for r in rows if r.get("price")]
        if args.in_stock:
            rows = [r for r in rows if r.get("availability") == "in_stock"]
        if args.brand:
            b = args.brand.lower()
            rows = [r for r in rows if (r.get("brand") or "").lower() == b]

        if args.out:
            n = write_listings(rows, args.out, catalog=cat)
            print(f"wrote {n} listings -> {args.out}")
            return 0
        if args.json:
            print(json.dumps(rows, ensure_ascii=False, indent=2, default=str))
            return 0
        _print_table(rows)
        return 0

    eng = _engine()

    if args.command == "verify":
        results = [eng.content_verify(ch) for ch in channels]
        if args.json:
            print(json.dumps(results, ensure_ascii=False, indent=2))
        else:
            for r in results:
                mark = "OK  " if r["populated"] else "FAIL"
                print(f"[{mark}] {r['channel']:24s} posts={r['posts']:3d} {r['reason']}")
        return 0

    if args.command == "mirror":
        stats = eng.mirror_channels(channels,
                                    full_history=not args.no_full_history)
        if args.json:
            print(json.dumps(stats, ensure_ascii=False, indent=2))
        else:
            for ch, s in stats.items():
                cov = s.get("coverage_pct")
                cov_txt = "up-to-date" if cov is None else f"coverage={cov}%"
                print(f"{ch:24s} pages={s.get('pages',0):3d} posts={s.get('posts',0):5d} "
                      f"span={s.get('oldest_id')}..{s.get('newest_id')} "
                      f"{cov_txt} beginning={s.get('reached_beginning')}")
        return 0

    # parse
    cat = build_catalog(eng.base_mirror_dir, channels, offline=not args.enrich)
    if args.out:
        n = write_listings(cat["listings"], args.out, catalog=cat)
        print(f"wrote {n} listings -> {args.out}")
        return 0
    if args.json:
        print(json.dumps(cat, ensure_ascii=False, indent=2, default=str))
        return 0
    m = cat["metrics"]
    print("── social catalogue ──")
    print(f"  channels : {m['channels_parsed']}")
    print(f"  molecules: {m['molecules']}")
    print(f"  listings : {m['listings']}  (vendors {m['vendors']})")
    print(f"  rejected : {m['rejections']}")
    print(f"  grades   : {m['grade_split']}")
    print(f"  methods  : {m['identity_methods']}")
    if cat["discovered_leads"]:
        print(f"  NEW leads (need verification): {', '.join(cat['discovered_leads'])}")
    print(f"\n  {cat['disclaimer']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
