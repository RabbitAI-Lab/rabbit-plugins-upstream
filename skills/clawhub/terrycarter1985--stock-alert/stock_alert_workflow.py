#!/usr/bin/env python3
"""Daily stock price alerts via WhatsApp using the finance + wacli skills.

Robust against common runtime issues:
- Portable imports/paths (no hardcoded /workspace).
- Live-quote failures fall back to a bundled local CSV snapshot.
- Missing `wu` CLI (wacli) degrades gracefully to dry-run instead of crashing.
- Defensive formatting so "N/A" values never raise.

Usage:
  python3 stock_alert_workflow.py                 # send if `wu` available, else dry-run
  python3 stock_alert_workflow.py --dry-run       # never send, just print
  STOCK_ALERT_RECIPIENT=123@g.us python3 ...      # override recipient
"""
import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

# --- Portable path setup -----------------------------------------------------
HERE = Path(__file__).resolve().parent
# finance_tools lives either alongside (skill bundle) or in ../skills/finance
for cand in (HERE, HERE / "lib", HERE.parent / "skills" / "finance"):
    if (cand / "finance_tools.py").exists():
        sys.path.insert(0, str(cand))
        break

from finance_tools import get_stock_price  # noqa: E402

try:
    import yaml
except Exception:
    yaml = None

DEFAULT_WATCHLIST = ["AAPL", "MSFT", "GOOGL", "TSLA"]
DEFAULT_RECIPIENT = "finance-alerts@g.us"


def load_wacli_config():
    """Load wacli config if present; tolerate absence."""
    if yaml is None:
        return {}
    for cand in (HERE / "wacli_config.yaml",
                 HERE.parent / "config" / "wacli_config.yaml"):
        if cand.exists():
            try:
                with open(cand) as f:
                    return yaml.safe_load(f) or {}
            except Exception:
                return {}
    return {}


def _fmt_price(v):
    try:
        return f"${float(v):.2f}"
    except (TypeError, ValueError):
        return f"{v}"


def _fmt_change(v):
    try:
        return f"{float(v):+.2f}%"
    except (TypeError, ValueError):
        return "n/a"


def _fmt_cap(v):
    try:
        return f"${float(v) / 1e9:.1f}B"
    except (TypeError, ValueError):
        return "n/a"


def build_alert(watchlist):
    lines = ["📈 Daily Stock Price Alert 📉", ""]
    for symbol in watchlist:
        data = get_stock_price(symbol)
        if "error" in data:
            lines.append(f"❌ {symbol}: {data['error']}")
            continue
        change = data.get("change_percent")
        try:
            cval = float(change)
            emoji = "🟢" if cval > 0 else "🔴" if cval < 0 else "⚪"
        except (TypeError, ValueError):
            emoji = "⚪"
        lines.append(
            f"{emoji} {data.get('name', symbol)} ({symbol}): "
            f"{_fmt_price(data.get('current_price'))} "
            f"({_fmt_change(change)}) | Cap: {_fmt_cap(data.get('market_cap'))}"
        )
    return "\n".join(lines)


def send_whatsapp_alert(recipient_jid: str, message: str):
    """Send via wacli `wu`. Returns (status, detail).

    status: "sent" | "skipped" | "error"
    """
    if shutil.which("wu") is None:
        return "skipped", "wacli `wu` not installed (npm i -g @ibrahimwithi/wu-cli)"
    try:
        result = subprocess.run(
            ["wu", "send", recipient_jid, message],
            capture_output=True, text=True, check=True,
        )
        return "sent", result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return "error", (e.stderr or e.stdout or str(e)).strip()
    except Exception as e:  # FileNotFoundError, OSError, etc.
        return "error", str(e)


def main():
    parser = argparse.ArgumentParser(description="WhatsApp stock price alert")
    parser.add_argument("--dry-run", action="store_true", help="print only, never send")
    parser.add_argument("--recipient", default=os.environ.get("STOCK_ALERT_RECIPIENT", DEFAULT_RECIPIENT))
    parser.add_argument("--symbols", nargs="*", default=None)
    args = parser.parse_args()

    load_wacli_config()  # validated/tolerated; reserved for future use
    watchlist = args.symbols or DEFAULT_WATCHLIST

    print(f"Generating stock price alert for {len(watchlist)} stocks...")
    alert_message = build_alert(watchlist)
    print("\nGenerated alert:\n" + alert_message)

    if args.dry_run:
        print("\n(dry-run) not sending.")
        return 0

    print(f"\nSending alert to {args.recipient}...")
    status, detail = send_whatsapp_alert(args.recipient, alert_message)
    if status == "sent":
        print("✅ Alert sent successfully!")
        return 0
    if status == "skipped":
        print(f"⚠️  Skipped sending: {detail}")
        return 0  # not a hard failure; alert was generated
    print(f"❌ Failed to send alert: {detail}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
