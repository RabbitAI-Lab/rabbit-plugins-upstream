#!/usr/bin/env python3
"""Query the MC translation dictionary (Dict-Sqlite.db) and zh.minecraft.wiki.

Data sources:
  1. Dict-Sqlite.db  — pre-built SQLite from i18n-Dict-Extender (900K+ mod entries)
  2. zh.minecraft.wiki — MediaWiki API for vanilla MC term lookups via redirect resolution

Usage:
    python query.py --modid <modid>              # Dump all entries for a mod
    python query.py --key <key>                   # Lookup by lang key
    python query.py --text <english>              # Lookup by English name (dict + wiki)
    python query.py --text <english> --no-wiki    # Dict only, skip wiki fallback
    python query.py --list-mods                   # List all modids with counts
    python query.py --list-mods --search <term>   # Filter mod list
    python query.py --modid <modid> --text <eng>   # Combined filter

Output: TSV (tab-separated) to stdout. Use --json for JSON output.
"""

import argparse
import json as json_mod
import os
import sqlite3
import sys
import urllib.parse
import urllib.request

# Fix Windows console encoding (GBK -> UTF-8)
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "Dict-Sqlite.db")
WIKI_API = "https://zh.minecraft.wiki/api.php"


def get_db():
    if os.path.exists(DB_PATH):
        return DB_PATH
    print("ERROR: Dict-Sqlite.db not found. Run fetch_dict.py first.", file=sys.stderr)
    sys.exit(1)


def wiki_lookup(english_name):
    """Look up a vanilla MC term via zh.minecraft.wiki redirect resolution.

    Returns the Chinese page title if the English name redirects to a Chinese page,
    otherwise returns None.
    """
    params = urllib.parse.urlencode({
        "action": "query",
        "titles": english_name,
        "redirects": "1",
        "format": "json",
    })
    url = f"{WIKI_API}?{params}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "mc-mod-translate-skill/1.0",
    })
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json_mod.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"  [wiki] Lookup failed: {e}", file=sys.stderr)
        return None

    query = data.get("query", {})
    # Check if there's a redirect chain
    redirects = query.get("redirects", [])
    pages = query.get("pages", {})

    for r in redirects:
        if r.get("from") == english_name:
            return r.get("to")

    # If no redirect but the page exists with a non-English title, use it
    for pid, page in pages.items():
        if pid != "-1" and page.get("title"):
            title = page["title"]
            # Only return if the title contains CJK characters
            if any("\u4e00" <= ch <= "\u9fff" for ch in title):
                return title

    return None


def main():
    p = argparse.ArgumentParser(description="Query MC translation dictionary")
    p.add_argument("--db", default=None, help="Path to Dict-Sqlite.db (auto-detected by default)")
    p.add_argument("--modid", default=None, help="Filter by mod ID (e.g. minecraft, tconstruct)")
    p.add_argument("--key", default=None, help="Lookup by lang key")
    p.add_argument("--text", default=None, help="Lookup by English name")
    p.add_argument("--list-mods", action="store_true", help="List all modids with counts")
    p.add_argument("--search", default=None, help="Filter mod list by keyword (use with --list-mods)")
    p.add_argument("--limit", type=int, default=500, help="Max rows to return (default 500)")
    p.add_argument("--no-wiki", action="store_true", help="Skip zh.minecraft.wiki fallback for text lookups")
    p.add_argument("--json", action="store_true", help="Output as JSON instead of TSV")
    args = p.parse_args()

    db_path = args.db or get_db()
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    if args.list_mods:
        if args.search:
            c.execute(
                "SELECT MODID, COUNT(*) as cnt FROM dict WHERE MODID LIKE ? GROUP BY MODID ORDER BY cnt DESC",
                (f"%{args.search}%",),
            )
        else:
            c.execute("SELECT MODID, COUNT(*) as cnt FROM dict GROUP BY MODID ORDER BY cnt DESC")
        rows = c.fetchall()
        print(f"{'modid':<40} {'count':>8}")
        print("-" * 50)
        for r in rows:
            print(f"{r['MODID']:<40} {r['cnt']:>8}")
        print(f"\nTotal: {len(rows)} mods")
        conn.close()
        return

    results = []

    if args.key:
        c.execute(
            "SELECT ORIGIN_NAME, TRANS_NAME, MODID, KEY, VERSION FROM dict WHERE KEY = ? LIMIT ?",
            (args.key, args.limit),
        )
        for r in c.fetchall():
            results.append({
                "origin": r["ORIGIN_NAME"], "trans": r["TRANS_NAME"],
                "modid": r["MODID"], "key": r["KEY"], "source": "dict",
            })

    if args.text:
        # Dict lookup by English name
        if args.modid:
            c.execute(
                "SELECT ORIGIN_NAME, TRANS_NAME, MODID, KEY FROM dict WHERE MODID = ? AND ORIGIN_NAME LIKE ? LIMIT ?",
                (args.modid, f"%{args.text}%", args.limit),
            )
        else:
            c.execute(
                "SELECT ORIGIN_NAME, TRANS_NAME, MODID, KEY FROM dict WHERE ORIGIN_NAME LIKE ? LIMIT ?",
                (f"%{args.text}%", args.limit),
            )
        for r in c.fetchall():
            results.append({
                "origin": r["ORIGIN_NAME"], "trans": r["TRANS_NAME"],
                "modid": r["MODID"], "key": r["KEY"], "source": "dict",
            })

        # Wiki fallback for vanilla MC terms
        if not args.no_wiki and not args.modid:
            print("  [wiki] Querying zh.minecraft.wiki...", file=sys.stderr)
            wiki_result = wiki_lookup(args.text)
            if wiki_result:
                results.append({
                    "origin": args.text, "trans": wiki_result,
                    "modid": "minecraft", "key": "", "source": "wiki",
                })

    if args.modid and not args.text and not args.key:
        c.execute(
            "SELECT ORIGIN_NAME, TRANS_NAME, KEY FROM dict WHERE MODID = ? ORDER BY ORIGIN_NAME LIMIT ?",
            (args.modid, args.limit),
        )
        for r in c.fetchall():
            results.append({
                "origin": r["ORIGIN_NAME"], "trans": r["TRANS_NAME"],
                "modid": args.modid, "key": r["KEY"], "source": "dict",
            })

    conn.close()

    if not results:
        print("No matches found.", file=sys.stderr)
        sys.exit(1)

    if args.json:
        print(json_mod.dumps(results, ensure_ascii=False, indent=2))
    else:
        print(f"{'origin_name'}\t{'trans_name'}\t{'modid'}\t{'key'}\t{'source'}")
        for r in results:
            print(f"{r['origin']}\t{r['trans']}\t{r['modid']}\t{r['key']}\t{r['source']}")

    print(f"\n[{len(results)} matches]", file=sys.stderr)


if __name__ == "__main__":
    main()
