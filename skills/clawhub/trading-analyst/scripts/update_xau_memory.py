#!/usr/bin/env python3
"""
update_xau_memory.py — AUTO-REFRESH memori XAU/USD biar TIDAK STALE.

Masalah lama: XAUUSD.md di-update manual (terakhir 19 Aug, level 4310-4500)
padahal harga udah 4528. Level nggak nyambung sama harga live -> bias rancu.

Pendekatan: PASS-THROUGH (aman, tidak menghapus data kurasi).
  - HANYA ganti 5 section: last_updated, bias, data_sources, indicators, macro_context.
  - Section LAIN (key_levels, context, scenarios, open_trades, notes, dst) DITULIS ULANG
    PERSIS seperti file lama. Tidak ada data bagus yang kebuang.

Alur:
  1. Baca XAUUSD.md lama.
  2. Tarik harga live (gold-api) + indikator REAL (Twelve Data, key di api_keys.md).
  3. Tarik korelasi makro (correlation_check.py, Yahoo gratis).
  4. Tulis ulang: section yang di-refresh diganti, sisanya di-copy mentah.

Usage:
  python3 update_xau_memory.py
  python3 update_xau_memory.py --price-bias bullish

No destructive ops: hanya file XAUUSD.md yang ditimpa (konten tergabung aman).
"""
import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
MEM = os.path.join(WORK, "memory", "trading")
XAU_MD = os.path.join(MEM, "XAUUSD.md")
API_KEYS = os.path.join(MEM, "api_keys.md")

WIB_TZ = timezone(timedelta(hours=7))

REFRESH_PREFIXES = ("last_updated:", "bias:", "data_sources:", "indicators", "macro_context")


def load_twelve_key():
    try:
        with open(API_KEYS, encoding="utf-8") as f:
            for line in f:
                m = re.search(r"Key:\s*([a-f0-9]{32})", line)
                if m:
                    return m.group(1)
    except FileNotFoundError:
        return None
    return None


def run(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=60, cwd=HERE)
    except Exception as e:  # noqa
        print(f"[warn] cmd failed: {e}", file=sys.stderr)
        return None


def is_top_header(ln):
    return re.match(r"^[a-z_]+:", ln) is not None


def is_refresh_start(ln):
    return ln.startswith(REFRESH_PREFIXES)


def main():
    p = argparse.ArgumentParser(description="Auto-refresh XAUUSD.md (safe pass-through).")
    p.add_argument("--price-bias", default="neutral-bullish",
                   help="bias label (freeform; 'bullish'/'bearish'/'neutral' used for macro filter)")
    args = p.parse_args()

    old = ""
    if os.path.exists(XAU_MD):
        with open(XAU_MD, encoding="utf-8") as f:
            old = f.read()

    # 1. live price + indicators
    r = run([sys.executable, "fetch_market.py", "--key"])
    market = {}
    if r and r.returncode == 0:
        try:
            market = json.loads(r.stdout)
        except json.JSONDecodeError:
            pass

    price = market.get("price")
    ind = market.get("indicators", {})
    rsi = ind.get("rsi14")
    ema20 = ind.get("ema20")
    sma50 = ind.get("sma50")
    sma200 = ind.get("sma200")
    high30 = ind.get("high30")
    low30 = ind.get("low30")

    # 2. correlation (normalize bias ke pilihan valid)
    macro_choice = "neutral"
    for k in ("bullish", "bearish", "neutral"):
        if k in args.price_bias:
            macro_choice = k
            break
    corr = {}
    rc = run([sys.executable, "correlation_check.py", "--price-bias", macro_choice])
    if rc and rc.returncode == 0:
        try:
            corr = json.loads(rc.stdout)
        except json.JSONDecodeError:
            pass

    macro_bias = corr.get("macro_bias", "unknown")
    macro_score = corr.get("macro_score", 0)
    filt = corr.get("filter_vs_price_bias", "unknown")

    now = datetime.now(timezone.utc).astimezone(WIB_TZ)
    wib_iso = now.strftime("%Y-%m-%dT%H:%M:%S+07:00")

    rsi_note = "(overbought >=70)" if (rsi and rsi >= 70) else \
               ("(oversold <=30)" if (rsi and rsi <= 30) else "(neutral)")

    refreshed = {
        "last_updated:": f'last_updated: "{wib_iso}"',
        "bias:": f'bias: "{args.price_bias} (macro {macro_bias}, score {macro_score:+d}, filter {filt})"',
        "data_sources:": (
            "data_sources:\n"
            "  - web: litefinance, fxstreet, investing.com, tradingview\n"
            "  - api: gold-api.com (price), Twelve Data (RSI/EMA/SMA), Yahoo (DXY/US10Y/SPX)\n"
            '  - chart_screenshot: false (data-driven, no screenshot needed)'
        ),
        "indicators": (
            f"indicators (REAL, Twelve Data, {wib_iso}):\n"
            f"  - RSI(14): {rsi:.1f} {rsi_note}\n"
            f"  - EMA20: {ema20:.2f}\n"
            f"  - SMA50: {sma50:.2f}\n"
            f"  - SMA200: {('%.2f' % sma200) if sma200 else 'n/a (need >200d)'}\n"
            f"  - 30d High: {high30:.2f}\n"
            f"  - 30d Low: {low30:.2f}"
        ),
        "macro_context": "macro_context (Yahoo, free):",
    }

    # build macro_context body
    macro_body = ""
    for k, v in corr.get("detail", {}).items():
        if v.get("available"):
            macro_body += f"  - {k}: {v['price']} ({v['chg_pct']:+.2f}%) -> emas {v['gold_bias']}\n"
        else:
            macro_body += f"  - {k}: n/a\n"

    lines = old.splitlines()
    out = []
    skip = False
    macro_seen = False
    i = 0
    while i < len(lines):
        ln = lines[i]
        if skip:
            # stop skipping at next genuine top-level header (or another refreshable)
            if is_refresh_start(ln) or (is_top_header(ln) and not ln.startswith(("indicators", "macro_context"))):
                skip = False
                # fall through to process ln
            else:
                i += 1
                continue

        if ln.startswith("last_updated:"):
            out.append(refreshed["last_updated:"]); skip = True; i += 1; continue
        if ln.startswith("bias:"):
            out.append(refreshed["bias:"]); skip = True; i += 1; continue
        if ln.startswith("data_sources:"):
            out.append(refreshed["data_sources:"]); skip = True; i += 1; continue
        if ln.startswith("indicators"):
            out.append(refreshed["indicators"]); skip = True; i += 1; continue
        if ln.startswith("macro_context"):
            macro_seen = True
            out.append(refreshed["macro_context"])
            if macro_body:
                out.append(macro_body.rstrip("\n"))
            skip = True; i += 1; continue
        # not refreshable: copy as-is
        out.append(ln)
        i += 1

    # Auto-append macro_context jika di file lama belum ada (jangan duplikat)
    if not macro_seen and macro_body:
        out.append("")
        out.append(refreshed["macro_context"])
        out.append(macro_body.rstrip("\n"))

    # trailing newline
    new_text = "\n".join(out).rstrip("\n") + "\n"
    os.makedirs(MEM, exist_ok=True)
    with open(XAU_MD, "w", encoding="utf-8") as f:
        f.write(new_text)
    print(f"[ok] safe-merge {XAU_MD}", file=sys.stderr)
    print(f"price={price} rsi={rsi:.1f} macro={macro_bias}({macro_score:+d}) filter={filt}",
          file=sys.stderr)


if __name__ == "__main__":
    main()
