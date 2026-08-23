#!/usr/bin/env python3
"""Cron wrapper: run scheduled XAU report, append to daily log, print only on setup."""
import os, sys, subprocess, datetime
SCRIPT_DIR = os.path.dirname(__file__)
LOG = os.path.join(os.path.expanduser("~"), ".openclaw", "workspace", "memory", "trading", "scheduled_log.md")

def main():
    out = subprocess.run([sys.executable, os.path.join(SCRIPT_DIR, "report_scheduled.py")],
                         capture_output=True, text=True, timeout=120).stdout
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M WIB")
    # only persist the report text (report_scheduled already wrote scheduled_report.md)
    try:
        with open(LOG, "a") as f:
            f.write(f"\n\n## {ts}\n\n{out}\n")
    except Exception:
        pass
    # print summary to cron log
    print(f"[{ts}] scheduled report ran; rec line below:")
    for line in out.splitlines():
        if "Rekomendasi" in line or "SETUP" in line:
            print("  ", line)

if __name__ == "__main__":
    main()
