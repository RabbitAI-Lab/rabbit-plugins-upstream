#!/usr/bin/env python3
"""
Agent Master Monitor
========================
Runs the healthcheck and balance monitors and sends one consolidated
alert when anything is wrong. Designed to run as a cron job every 5 minutes.

Usage:
    python3 master_monitor.py
    python3 master_monitor.py --quiet

Requires env vars:
    ALCHEMY_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID (optional)

v1.0.1: the systemd service checks for mining/earning workers
(agent-miner, agent-0xwork, agent-arb) were removed with supervisor.sh —
this skill no longer starts, maintains, or monitors mining workers.
"""

import os
import sys
import json
import subprocess
import asyncio
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from alert_bot import AlertBot

# Scripts are resolved relative to this file, not the current working
# directory — running the monitor from another directory (or via cron
# with an unexpected cwd) must not pick up a different healthcheck.py /
# balance-monitor.py from the cwd.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

async def main():
    quiet = "--quiet" in sys.argv
    bot = AlertBot()
    issues = []

    if not quiet:
        print(f"🔍 Master Monitor | {datetime.utcnow().isoformat()}")

    # 1. Healthcheck
    if not quiet:
        print("\n--- Healthcheck ---")
    try:
        result = subprocess.run(
            [sys.executable, os.path.join(SCRIPT_DIR, "healthcheck.py"), "--quiet"],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode != 0:
            issues.append(("Healthcheck", "One or more checks failed"))
            if not quiet:
                print("  🔴 Healthcheck failed")
        else:
            if not quiet:
                print("  ✅ All healthy")
    except Exception as e:
        issues.append(("Healthcheck", str(e)[:50]))

    # 2. Balance monitor
    if not quiet:
        print("\n--- Balance Monitor ---")
    try:
        result = subprocess.run(
            [sys.executable, os.path.join(SCRIPT_DIR, "balance-monitor.py")],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0:
            # Parse which wallet is low
            found = False
            for line in result.stdout.split("\n"):
                if "LOW" in line or "error" in line.lower():
                    issues.append(("Gas", line.strip()[:80]))
                    found = True
            if not found:
                # The check crashed (e.g. `web3` not installed — it is
                # imported at the top of balance-monitor.py) and exited
                # nonzero with empty stdout. That is a failure, never a
                # pass: record it so it is alerted on (v1.0.3 fix — the
                # old code recorded nothing and reported "nominal").
                issues.append(("Gas", f"balance monitor failed to run (exit code {result.returncode})"))
            if not quiet:
                print("  🔴 One or more wallets low on gas")
        else:
            if not quiet:
                print("  ✅ All wallets OK")
    except Exception as e:
        issues.append(("Balance", str(e)[:50]))

    # Send consolidated alert if issues found
    if issues:
        body = "\n".join(f"• {name}: {detail}" for name, detail in issues)
        await bot.alert("Agent Alert", body, "high")
        if not quiet:
            print(f"\n🔴 {len(issues)} issue(s) found — alert sent")
        sys.exit(1)
    else:
        if not quiet:
            print("\n✅ All systems nominal. No alerts sent.")
        sys.exit(0)

if __name__ == "__main__":
    asyncio.run(main())
