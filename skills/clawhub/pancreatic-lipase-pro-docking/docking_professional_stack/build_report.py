#!/usr/bin/env python3
"""build_report.py — generate the final markdown report from docking results.

Usage:
  python3 build_report.py --results dock_results/results_all_sites.csv
      [--results-ex16 dock_results_ex16/results_ex16.csv]
      [--analysis-dir analysis]            # optional per-provider AI analyses
      [--sites-file sites.json] [--top 20] [-o REPORT.md]

Produces: header, site table, global top-N, per-site top-10, ex16 comparison
section (if provided), provider-picks table + full AI analyses (if analysis-dir).
"""
import argparse, csv, json, re, unicodedata
from collections import defaultdict
from pathlib import Path


def norm(x):
    return re.sub(r"[^a-z0-9 ]+", "", unicodedata.normalize("NFKC", x).lower()).strip()


def provider_picks(pf, known, n=3):
    """Extract top molecule picks from a provider analysis markdown."""
    picks = []
    for line in open(pf):
        if not re.search(r"-?\d+\.\d{2}", line):
            continue
        m = re.match(r"\s*\d+[\.\)]?\s*\*{0,2}([A-Za-z0-9][^|*\n]{2,50})\*{0,2}", line)
        name = m.group(1).strip() if m else None
        if not name:
            continue
        score = float(re.search(r"-?\d+\.\d{2}", line).group(0))
        key = norm(name)
        if key in known and score < -6 and known[key] not in [p[0] for p in picks]:
            picks.append((known[key], score))
        if len(picks) >= n:
            break
    return picks


def site_table(ok, site, n=10):
    hits = sorted([(r["name"], float(r["score"])) for r in ok if r["site"] == site],
                  key=lambda x: x[1])[:n]
    return "\n".join(f"| {i}. | {nm} | {v:.2f} |" for i, (nm, v) in enumerate(hits, 1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True)
    ap.add_argument("--results-ex16", default=None)
    ap.add_argument("--analysis-dir", default=None)
    ap.add_argument("--sites-file", default=None)
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("-o", "--output", default="REPORT.md")
    args = ap.parse_args()

    rows = list(csv.DictReader(open(args.results)))
    ok = [r for r in rows if r["status"] == "ok" and r["score"]]
    mol = defaultdict(dict)
    for r in ok:
        mol[r["name"]][r["site"]] = float(r["score"]) or 0.0
    if not mol:
        print("no scored results found")
        return 1

    sites = {}
    if args.sites_file and Path(args.sites_file).exists():
        sites = json.loads(Path(args.sites_file).read_text())

    lines = ["# hPL Pancreatic Lipase Virtual Screen (multi-site docking)",
             f"**Molecules docked:** {len(mol)} · **Jobs:** {len(rows)} ({sum(1 for r in ok if r['score'])} scored OK) · **Date:** 2026-08-03",
             ""]
    if sites:
        lines += ["## Sites (from structure / sites.json)", "| Site | Center | Box (Å) | Residues |", "|---|---|---|---|"]
        for k, v in sites.items():
            lines.append(f"| {k} | {v['center']} | {v['box']} | {v.get('note','')} |")
        lines.append("")

    lines += ["## Global top %d (best score across any site)" % args.top,
              "| # | Molecule | Best (kcal/mol) |", "|---|---|---|"]
    for i, (n, v) in enumerate(sorted(mol.items(), key=lambda kv: min(kv[1].values()))[: args.top], 1):
        lines.append(f"| {i}. | {n} | {min(v.values()):.2f} |")
    lines.append("")

    site_names = list({r["site"] for r in ok})
    for site in site_names:
        lines += [f"### {site}", "| # | Molecule | Score |", site_table(ok, site), ""]

    if args.results_ex16 and Path(args.results_ex16).exists():
        ex16 = {(r["name"], r["site"]): float(r["score"])
                for r in csv.DictReader(open(args.results_ex16)) if r["status"] == "ok" and r["score"]}
        ex2 = {(r["name"], r["site"]): float(r["score"]) for r in ok}
        lines += ["## High-exhaustiveness re-dock (ex16) — best per molecule",
                  "| Molecule | ex2 | ex16 | Δ |", "|---|---|---|---|"]
        best = defaultdict(dict)
        for (n, s), v in ex16.items():
            best[n][s] = v
        for n in sorted(best, key=lambda x: min(best[x].values())):
            s16 = min(best[n].values())
            site16 = min(best[n], key=best[n].get)
            v2 = min((ex2.get((n, s)) for s in best[n] if (n, s) in ex2), default=None)
            d = (s16 - v2) if v2 is not None else None
            lines.append(f"| {n} | {v2 if v2 is not None else '—':.2f} | **{s16:.2f}** ({site16}) | {d:+.2f} |" if v2 is not None and d is not None else f"| {n} | — | **{s16:.2f}** ({site16}) | — |")
        lines.append("")

    if args.analysis_dir and Path(args.analysis_dir).exists():
        known = {norm(nm): nm for nm in mol.keys()}
        files = sorted(Path(args.analysis_dir).glob("*.md"))
        if files:
            lines += ["## AI-model analyses (parallel, disjoint shards)", ""]
            for pf in files:
                picks = provider_picks(pf, known)
                lines.append(f"### {pf.stem}")
                if picks:
                    lines.append("Top picks: " + ", ".join(f"{nm} ({v:.2f})" for nm, v in picks))
                lines.append("")
                lines.append(open(pf).read())
                lines.append("")
        else:
            lines.append("(analysis-dir given but empty)")

    out = Path(args.output)
    out.write_text("\n".join(lines))
    print(f"report written -> {out} ({len(lines)} lines)")


if __name__ == "__main__":
    raise SystemExit(main())
