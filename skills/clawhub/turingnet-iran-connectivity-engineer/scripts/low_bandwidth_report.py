#!/usr/bin/env python3
"""low_bandwidth_report.py — offline-first report builder.

Text (already redacted) -> minimal self-contained HTML: embedded CSS, no JS,
no CDN, no trackers, no external requests, hard size cap (--maxsize, default
100KB) enforced with a visible truncation marker and a split suggestion.
Runs scripts/guard.py on the input first (BLOCK refuses to build the report).
Exit codes: 0 built · 1 input error · 2 guard blocked · 3 size would truncate? (no — truncation is allowed and reported).
"""
import argparse
import datetime
import html
import json
import os
import subprocess
import sys

SCHEMA = "turingnet.report.v1"
CSS = ("body{font-family:system-ui,sans-serif;max-width:46rem;margin:1rem auto;"
       "padding:0 .8rem;line-height:1.45;color:#111;background:#fff}"
       "h1{font-size:1.25rem}pre{background:#f5f5f5;padding:.6rem;overflow-x:auto;"
       "white-space:pre-wrap}footer{color:#555;font-size:.85rem;border-top:1px solid #ddd;padding-top:.4rem}")


def build(text, title, maxsize):
    body = html.escape(text)
    paras = "\n".join(
        f"<pre>{html.escape(line)}</pre>" if line.startswith((" ", "\t", "#"))
        else f"<p>{html.escape(line)}</p>"
        for line in text.splitlines() if line.strip())
    doc = ("<!doctype html><html lang=\"fa\" dir=\"auto\"><head><meta charset=\"utf-8\">"
           f"<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
           f"<title>{html.escape(title)}</title><style>{CSS}</style></head>"
           f"<body><h1>{html.escape(title)}</h1>{paras}"
           f"<footer>TuringNet low-bandwidth report · embedded CSS only · no JS/trackers · "
           f"generated {datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')}</footer></body></html>")
    truncated = False
    if len(doc.encode("utf-8")) > maxsize:
        truncated = True
        marker = ("\n<p><b>[TRUNCATED to fit the size cap — split the input into "
                  "multiple reports.]</b></p></body></html>")
        keep = maxsize - len(marker.encode()) - 200
        cut = doc.encode("utf-8")[:keep].decode("utf-8", errors="ignore")
        # close safely
        doc = cut.rsplit("<", 1)[0] + marker
    return doc, truncated


def main():
    ap = argparse.ArgumentParser(description="TuringNet low-bandwidth report builder")
    ap.add_argument("--input", required=True, help="redacted text file")
    ap.add_argument("--output", required=True, help="report.html path")
    ap.add_argument("--maxsize", default=100 * 1024, type=int, help="byte cap (default 100KB)")
    ap.add_argument("--title", default="Connectivity report")
    ap.add_argument("--skip-guard", action="store_true", help="skip the guard pre-check (not recommended)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    try:
        text = open(args.input, encoding="utf-8", errors="replace").read()
    except Exception as e:
        print(json.dumps({"schema": SCHEMA, "error": f"cannot read input: {e}"}))
        return 1
    if not args.skip_guard:
        here = os.path.dirname(os.path.abspath(__file__))
        r = subprocess.run([sys.executable, os.path.join(here, "guard.py"), "--input", args.input],
                           capture_output=True, text=True)
        if r.returncode == 2:
            print(json.dumps({"schema": SCHEMA, "built": False,
                              "reason": "guard blocked the draft",
                              "guard": r.stdout[-600:]}) if args.json
                  else f"[report] GUARD BLOCKED — fix the draft first:\n{r.stdout[-600:]}")
            return 2
    doc, truncated = build(text, args.title, args.maxsize)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(doc)
    size = os.path.getsize(args.output)
    out = {"schema": SCHEMA, "built": True, "file": args.output, "bytes": size,
           "cap": args.maxsize, "truncated": truncated,
           "self_contained": True, "js": False, "cdn": False, "trackers": False}
    print(json.dumps(out) if args.json else f"[report] wrote {args.output} ({size} bytes"
          f"{', truncated' if truncated else ''})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
