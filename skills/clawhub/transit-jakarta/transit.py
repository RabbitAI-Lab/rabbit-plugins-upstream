#!/usr/bin/env python3
"""
Transit Jakarta CLI — Query real-time bus arrivals, halte info, route stats.
Usage: transit.py <command> [args]

Examples:
  python3 transit.py search "Cibubur Junction"
  python3 transit.py halte B00248P --rute P11 --arah "Blok M"
  python3 transit.py stats
  python3 transit.py route P11
  python3 transit.py nearest -6.36873 106.89366
  python3 transit.py bus MYS-21238
  python3 transit.py top-routes 10
  python3 transit.py refresh-cache
"""
import sys, argparse, textwrap, math, time
from api import (
    get_meta, get_stats, get_arrivals, get_bus,
    get_static_data, search_halte, search_route,
    get_halte_by_id, get_routes_for_halte, nearest_halte,
    format_eta, format_age, KIND_LABELS, CACHE_DIR, STATIC_DATA_FILE,
)

CSI = "\x1b["
RESET = f"{CSI}0m"
BOLD = f"{CSI}1m"
DIM = f"{CSI}2m"
CYAN = f"{CSI}36m"
YELLOW = f"{CSI}33m"
GREEN = f"{CSI}32m"
RED = f"{CSI}31m"
MAGENTA = f"{CSI}35m"
BLUE = f"{CSI}34m"
WHITE = f"{CSI}37m"

def c(text, color) -> str:
    return f"{color}{text}{RESET}"

def banner():
    return f"""
{c('🚌 Transit Jakarta Live', CYAN + BOLD)}
{c('   transit.oyenza.com  |  Data real-time TransJakarta', DIM)}
"""

def fmt_rute(route_id: str, kind: str = "") -> str:
    """Format route ID with kind color."""
    colors = {
        "brt": CYAN,
        "integrasi": GREEN,
        "mikrotrans": YELLOW,
        "jabodetabek": MAGENTA,
        "royal": RED,
        "rusun": BLUE,
        "wisata": WHITE,
    }
    col = colors.get(kind, WHITE)
    return c(f"[{route_id}]", col + BOLD)

def cmd_search(args):
    """Search halte by name."""
    verbose = getattr(args, 'verbose', False)
    if not args.query:
        print("Usage: transit.py search <nama halte>")
        return
    results = search_halte(args.query, limit=args.limit)
    if not results:
        print(f"❌ Tidak ketemu halte untuk: {args.query}")
        return
    print(f"\n{c('📍 Hasil pencarian:', BOLD)} \"{args.query}\"")
    print(c("─" * 50, DIM))
    for i, h in enumerate(results, 1):
        brt_flag = c(" 🏛️", CYAN) if h.get("brt") else ""
        routes = ", ".join(h.get("routes", [])[:6])
        if len(h.get("routes", [])) > 6:
            routes += f" +{len(h.get('routes', [])) - 6} lagi"
        print(f"  {i}. {c(h['name'], BOLD)}{brt_flag}")
        print(f"     ID: {h['id']}  │ Rute: {routes}")
        if args.verbose:
            print(f"     Koordinat: {h['lat']}, {h['lng']}")
        print()

def cmd_halte(args):
    """Show arrivals at a halte."""
    verbose = getattr(args, 'verbose', False)
    halte_id = args.halte_id or ""

    # If halte_id looks like a search query (not a TJ-style ID), search first
    if not halte_id.startswith("B") and not halte_id.startswith("TJ"):
        results = search_halte(halte_id, limit=1)
        if not results:
            print(f"❌ Tidak ketemu: {halte_id}")
            return
        halte_id = results[0]["id"]
        halte_name = results[0]["name"]
    else:
        halte = get_halte_by_id(halte_id)
        halte_name = halte["name"] if halte else halte_id

    try:
        data = get_arrivals(halte_id)
    except Exception as e:
        print(f"❌ Gagal ambil data arrivals: {e}")
        return

    arrivals = data.get("arrivals", [])
    if not arrivals:
        print(f"❌ Tidak ada data arrivals untuk: {halte_name}")
        return

    # Apply filters
    filtered = arrivals
    if args.rute:
        filtered = [a for a in filtered if args.rute.upper() in a.get("route", "").upper()]
    if args.arah:
        q = args.arah.lower()
        filtered = [a for a in filtered if q in a.get("head", "").lower()]

    if not filtered:
        if args.rute and args.arah:
            print(f"❌ Tidak ada bus {args.rute} arah {args.arah} di {halte_name}")
        elif args.rute:
            print(f"❌ Tidak ada bus {args.rute} di {halte_name}")
        elif args.arah:
            print(f"❌ Tidak ada bus arah {args.arah} di {halte_name}")
        else:
            print(f"❌ Tidak ada arrivals di {halte_name}")
        return

    # Deduplicate by route+head, keep nearest (lowest eta)
    seen = {}
    for a in filtered:
        key = (a.get("route"), a.get("head"))
        if key not in seen or a.get("etaMin", 999) < seen[key].get("etaMin", 999):
            seen[key] = a
    unique = list(seen.values())
    unique.sort(key=lambda a: a.get("etaMin", 999))

    now = data.get("now", 0)
    age_s = (int(time.time() * 1000) - now) // 1000

    kind_label = KIND_LABELS.get(arrivals[0].get("kind", ""), "")
    print(f"\n{c('🚌 Arrivals:', BOLD + CYAN)} {c(halte_name, BOLD)}")
    if args.rute:
        print(f"   Filter: {c(args.rute.upper(), YELLOW + BOLD)}", end="")
    if args.arah:
        print(f"  Arah: {c(args.arah, YELLOW + BOLD)}", end="")
    print()
    print(c("─" * 52, DIM))

    for a in unique[:args.limit]:
        route = a.get("route", "?")
        head = a.get("head", "?")
        eta = a.get("etaMin", 0)
        bus = a.get("bus", "?")
        kind = a.get("kind", "")
        age = a.get("ageS", 0)

        kind_tag = c(f"[{KIND_LABELS.get(kind, kind)}]", DIM)
        eta_str = c(format_eta(eta), GREEN + BOLD if eta <= 3 else WHITE + BOLD if eta <= 10 else YELLOW)
        bus_str = c(f"({bus})", DIM)

        print(f"  {fmt_rute(route, kind)} {c(head, WHITE)}")
        print(f"     ETA {eta_str}  {bus_str}  {c(format_age(age), DIM)}")
        print()

    # Summary
    total_filtered = len(unique)
    total_all = len(arrivals)
    print(c(f"📊 {total_filtered} keberangkatan shown / {total_all} total di halte ini", DIM))
    print(c(f"🕐 Updated: {format_age(age_s) if age_s < 5 else 'baru saja'} (live)", DIM))


def cmd_stats(args):
    """Show overall bus statistics."""
    try:
        data = get_stats()
    except Exception as e:
        print(f"❌ Gagal ambil stats: {e}")
        return

    now = data.get("now", 0)
    buses = data.get("buses", 0)
    by_kind = data.get("byKind", {})
    by_route = data.get("byRoute", {})

    print(f"\n{c('📊 Statistik Bus Aktif', BOLD + CYAN)}")
    print(c(f"   Total bus: {c(str(buses), BOLD + GREEN)}  •  Updated: {format_age((int(time.time()*1000)-now)//1000)}", DIM))
    print(c("─" * 40, DIM))

    # By kind
    print(f"\n{c('Per Jenis:', BOLD)}")
    total_kind = sum(by_kind.values())
    for kind, count in sorted(by_kind.items(), key=lambda x: -x[1]):
        bar = "█" * math.ceil(count / total_kind * 20) if total_kind else ""
        label = KIND_LABELS.get(kind, kind)
        pct = count / total_kind * 100 if total_kind else 0
        print(f"  {c(label.ljust(18), WHITE)}{c(bar, CYAN)} {c(str(count), BOLD)}  {c(f'({pct:.1f}%)', DIM)}")

    # Top routes
    top = sorted(by_route.items(), key=lambda x: -x[1])[:10]
    print(f"\n{c(f'Top 10 Rute Tersibuk:', BOLD)}")
    for route, count in top:
        bar = "█" * math.ceil(count / buses * 20) if buses else ""
        print(f"  {fmt_rute(route)} {c(bar, GREEN)} {c(str(count), BOLD)}")


def cmd_route(args):
    """Show route details and halte list."""
    if not args.route_id:
        print("Usage: transit.py route <rute_id>  e.g., P11, 1, JAK.73")
        return

    data, _ = get_static_data()
    route_map = {r.get("id"): r for r in data.get("routes", [])}

    # Try numeric ID first, then string
    route = route_map.get(args.route_id.upper())
    if not route:
        for rid, r in route_map.items():
            if r.get("short", "").upper() == args.route_id.upper():
                route = r
                break

    if not route:
        print(f"❌ Rute tidak ditemukan: {args.route_id}")
        return

    kind = route.get("kind", "")
    color = route.get("color", "#6B6B70")
    long = route.get("long", "")
    short = route.get("short", "")
    headway = route.get("headway", [])

    print(f"\n{c('🚌 Rute:', BOLD + CYAN)} {c(short, BOLD)} {c(long, DIM)}")
    print(f"   Jenis: {c(KIND_LABELS.get(kind, kind), WHITE + BOLD)}  │ Color: {c('●', color)} {color}")
    print(c("─" * 50, DIM))

    # Halte yang dilayani
    halte_data, _ = get_static_data()
    halte_by_route = {}
    for h in halte_data.get("halte", []):
        for rid in h.get("r", []):
            if rid not in halte_by_route:
                halte_by_route[rid] = []
            halte_by_route[rid].append(h.get("name"))

    halte_list = halte_by_route.get(route.get("id"), [])
    if halte_list:
        print(f"   {c(f'{len(halte_list)} halte dilayani:', DIM)}")
        for i, name in enumerate(halte_list[:20], 1):
            print(f"   {i:2}. {name}")
        if len(halte_list) > 20:
            print(f"   ... +{len(halte_list)-20} lagi")
    else:
        print("   (tidak ada data halte)")


def cmd_nearest(args):
    """Find nearest halte to coordinates."""
    try:
        results = nearest_halte(args.lat, args.lng, limit=args.limit)
    except Exception as e:
        print(f"❌ Gagal cari nearest: {e}")
        return

    if not results:
        print("❌ Tidak ada halte ditemukan")
        return

    print(f"\n{c('📍 Halte Terdekat ke', BOLD + CYAN)} ({args.lat}, {args.lng})")
    print(c("─" * 50, DIM))
    for i, h in enumerate(results, 1):
        dist = h.get("dist_m", 0)
        if dist < 1000:
            dist_str = f"{dist}m"
        else:
            dist_str = f"{dist/1000:.1f}km"
        brt_flag = c(" 🏛️", CYAN) if False else ""
        routes = ", ".join(h.get("routes", [])[:8])
        if len(h.get("routes", [])) > 8:
            routes += f" +{len(h.get('routes', [])) - 8}"
        print(f"  {i}. {c(h['name'], BOLD)}{brt_flag}")
        print(f"     {c(dist_str, GREEN + BOLD)}  │  Rute: {routes}")
        print()


def cmd_bus(args):
    """Show bus detail (position, route, next halte)."""
    if not args.bus_id:
        print("Usage: transit.py bus <bus_id>  e.g., MYS-21238")
        return
    try:
        data = get_bus(args.bus_id)
    except Exception as e:
        print(f"❌ Gagal ambil data bus: {e}")
        return

    if "error" in data or not data.get("ok", True):
        msg = data.get("message", "Bus tidak ditemukan atau tidak ada data")
        print(f"❌ {msg}")
        return

    route = data.get("route", "?")
    lat = data.get("lat")
    lng = data.get("lng")
    heading = data.get("heading", 0)
    next_halte = data.get("nextHalte", {})
    eta = data.get("eta", 0)

    print(f"\n{c('🚌 Bus:', BOLD + CYAN)} {c(args.bus_id, BOLD)}")
    if route:
        print(f"   Rute: {fmt_rute(route)}")
    if lat and lng:
        print(f"   Posisi: {lat:.5f}, {lng:.5f}  (heading {heading}°)")
    if next_halte:
        nh_name = next_halte.get("name", "?")
        nh_eta = next_halte.get("etaMin", 0)
        print(f"   Next halte: {c(nh_name, WHITE)} — ETA {c(format_eta(nh_eta), GREEN)}")
    elif eta:
        print(f"   ETA: {format_eta(eta)}")
    else:
        print("   (sedang tidak beroperasi atau data tidak tersedia)")


def cmd_top_routes(args):
    """Show busiest routes."""
    try:
        data = get_stats()
    except Exception as e:
        print(f"❌ Gagal: {e}")
        return

    by_route = data.get("byRoute", {})
    top = sorted(by_route.items(), key=lambda x: -x[1])[:args.n]
    total = sum(by_route.values()) or 1

    print(f"\n{c(f'🔥 Top {args.n} Rute Tersibuk', BOLD + RED)}")
    print(c("─" * 40, DIM))
    for i, (route, count) in enumerate(top, 1):
        bar_len = math.ceil(count / total * 30)
        bar = "█" * bar_len
        pct = count / total * 100
        print(f"  {i:2}. {fmt_rute(route)} {c(bar, YELLOW)} {c(str(count), BOLD)}  {c(f'({pct:.1f}%)', DIM)}")


def cmd_refresh_cache(args):
    """Force refresh static data cache."""
    print("🔄 Mengambil data terbaru...")
    try:
        data, meta = get_static_data(force_refresh=True)
        routes = len(data.get("routes", []))
        halte = len(data.get("halte", []))
        version = meta.get("static", "?")
        print(f"✅ Cache refreshed! Version: {version}")
        print(f"   {routes} rute, {halte} halte")
    except Exception as e:
        print(f"❌ Gagal refresh: {e}")


def cmd_help(args):
    print(banner())
    print(f"""
{c('📖 Perintah:', BOLD + CYAN)}

  {c('search <query>', CYAN)}          Cari halte berdasarkan nama
  {c('halte <id> [flags]', CYAN)}      Lihat arrivals di satu halte
  {c('route <rute_id>', CYAN)}         Detail satu rute + daftar halte
  {c('stats', CYAN)}                   Statistik semua bus aktif
  {c('top-routes [N]', CYAN)}          Top N rute tersibuk (default 10)
  {c('nearest <lat> <lng>', CYAN)}     Halte terdekat dari koordinat
  {c('bus <bus_id>', CYAN)}            Info satu bus (posisi, rute)
  {c('refresh-cache', CYAN)}           Refresh static data cache

{c('📌 Flags untuk command "halte":', BOLD + YELLOW)}
  --rute <kode>    Filter berdasarkan kode rute (e.g., P11, 7C)
  --arah <nama>    Filter berdasarkan arah tujuan (e.g., "Blok M")
  --limit <N>      Jumlah arrivals yang ditunjukkan (default 8)
  -v, --verbose    Tampilkan info tambahan

{c('💡 Contoh:', BOLD + GREEN)}
  python3 transit.py search "Cibubur Junction"
  python3 transit.py halte B00248P --rute P11 --arah "Blok M"
  python3 transit.py halte "Cibubur Junction" --rute P11
  python3 transit.py stats
  python3 transit.py top-routes 5
  python3 transit.py nearest -6.36873 106.89366

{c('⚙️  Setup Alias (opsional, tambahkan ke ~/.zshrc):', BOLD + DIM)}
  alias tj='python3 ~/.qclaw-oversea/skills/transit-jakarta/transit.py'
""")
    # Show cache status
    if STATIC_DATA_FILE.exists():
        import datetime
        mtime = datetime.datetime.fromtimestamp(STATIC_DATA_FILE.stat().st_mtime)
        print(f"{c('📦 Cache: ', DIM)}{c('OK', GREEN)} (last updated: {mtime.strftime('%Y-%m-%d %H:%M')})")
    else:
        print(f"{c('📦 Cache: ', DIM)}{c('belum ada / perlu refresh', YELLOW)}")


def main():
    parser = argparse.ArgumentParser(
        description="Transit Jakarta CLI — Query real-time bus arrivals",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Contoh:
              transit.py search "Cibubur Junction"
              transit.py halte B00248P --rute P11 --arah "Blok M"
              transit.py stats
        """)
    )
    parser.add_argument("command", nargs="?", default="help")
    parser.add_argument("args", nargs="*", default=[])
    # flags shared across commands
    parser.add_argument("--rute", dest="rute")
    parser.add_argument("--arah")
    parser.add_argument("-v", "--verbose", action="store_true")
    # top-routes
    parser.add_argument("-n", dest="n", type=int, default=10)

    args = parser.parse_args(sys.argv[1:] if len(sys.argv) > 1 else ["help"])
    cmd = args.command

    commands = {
        "search": cmd_search,
        "halte": cmd_halte,
        "stats": cmd_stats,
        "route": cmd_route,
        "nearest": cmd_nearest,
        "bus": cmd_bus,
        "top-routes": cmd_top_routes,
        "top_routes": cmd_top_routes,
        "refresh-cache": cmd_refresh_cache,
        "refresh_cache": cmd_refresh_cache,
        "help": cmd_help,
        "--help": cmd_help,
        "-h": cmd_help,
    }

    if cmd not in commands:
        print(f"❌ Perintah tidak dikenal: {cmd}")
        print("   Jalankan: transit.py help")
        sys.exit(1)

    # Build args namespace for each command
    if cmd == "search":
        ns = argparse.Namespace(
            query=" ".join(args.args),
            limit=8,
            verbose=args.verbose,
        )
        cmd_search(ns)
    elif cmd == "halte":
        ns = argparse.Namespace(
            halte_id=args.args[0] if args.args else "",
            rute=args.rute,
            arah=args.arah,
            limit=8,
            verbose=args.verbose,
        )
        cmd_halte(ns)
    elif cmd == "route":
        ns = argparse.Namespace(route_id=args.args[0] if args.args else "")
        cmd_route(ns)
    elif cmd == "nearest":
        ns = argparse.Namespace(
            lat=float(args.args[0]) if len(args.args) > 0 else 0,
            lng=float(args.args[1]) if len(args.args) > 1 else 0,
            limit=5,
        )
        cmd_nearest(ns)
    elif cmd == "bus":
        ns = argparse.Namespace(bus_id=args.args[0] if args.args else "")
        cmd_bus(ns)
    elif cmd in ("stats", "top-routes", "top_routes"):
        ns = argparse.Namespace(n=args.n if hasattr(args, 'n') else 10)
        if cmd in ("top-routes", "top_routes"):
            cmd_top_routes(ns)
        else:
            cmd_stats(ns)
    elif cmd in ("refresh-cache", "refresh_cache"):
        cmd_refresh_cache(args)
    else:
        cmd_help(args)


if __name__ == "__main__":
    main()
