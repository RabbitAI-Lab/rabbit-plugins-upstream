#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""registry_rules.py - Registration-record quality rule engine (P21-style).

Methodology transplant from Pinnacle 21 Validation Rules (see
ct-base/references/pinnacle21_validation_rules/): every check carries a stable
rule id (RG-xxx) and a severity tier (E=Error / W=Warning), and emits a
numbered issue list instead of silently passing bad records.

Input : normalized.json produced by ct-registry (list of unified records, or
        {"records": [...]}/{"normalized": [...]} wrappers).
Output: issue list (JSON + optional Markdown report). Advisory only -- this
        tool never mutates records.

Usage:
    python scripts/registry_rules.py --in normalized.json [--out-json issues.json] [--out-md issues.md]
    python scripts/registry_rules.py --in normalized.json --severity error   # report Errors only

Rule register (v1):
  RG-001 E  date-logic contradiction: start_date > primary_completion_date
  RG-002 E  primary_outcome empty while the source path provides it
  RG-003 W  CT.gov record missing ALL eligibility fields (sex + age bounds)
  RG-004 E  CT.gov Completed-like trial with no results posted and no update
            in the last 365 days (results-discipline gap)
  RG-005 W  enrollment empty while the source path provides it
  RG-006 E  registry_id does not match the source's id pattern
  RG-007 W  conditions empty while the source path provides them
  RG-008 E  registry_id AND url both missing (record unusable for bridging)
  RG-009 W  CT.gov record not updated for > 24 months (stale snapshot; the
            in-pipeline stale_check.py complements this at fetch time)

Known overlap note: RG-009 duplicates part of stale_check.py's concern, but
stale_check runs in-pipeline at retrieval time while this engine is an offline
audit over any normalized.json snapshot; both are kept intentionally.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import datetime as _dt

RULES_META = [
    ("RG-001", "E", "date logic: start_date > primary_completion_date"),
    ("RG-002", "E", "primary_outcome empty while source path provides it"),
    ("RG-003", "W", "CT.gov eligibility (sex + age bounds) entirely missing"),
    ("RG-004", "E", "CT.gov Completed-like, no results, no update > 365d"),
    ("RG-005", "W", "enrollment empty while source path provides it"),
    ("RG-006", "E", "registry_id pattern mismatch for its source"),
    ("RG-007", "W", "conditions empty while source path provides them"),
    ("RG-008", "E", "registry_id and url both missing"),
    ("RG-009", "W", "CT.gov last update > 24 months old"),
]

_ID_PATTERNS = {
    "CTGOV": re.compile(r"^NCT\d{8}$", re.I),
    "ISRCTN": re.compile(r"^ISRCTN\d+$", re.I),
    "DRKS": re.compile(r"^DRKS\d+$", re.I),
    "CHICTR": re.compile(r"^ChiCTR[0-9A-Za-z\-]+$"),
    "EUCTR": re.compile(r"^\d{4}-\d{6}-\d{2}$"),
    "CDE": re.compile(r"^CTR\d{6,}", re.I),
    "ICTRP": re.compile(r"^.+", re.S),  # WHO mirror: any non-empty id
}

_COMPLETED_RE = re.compile(r"completed|已完成", re.I)
_DATE_RE = re.compile(r"^(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?")


def _date(s):
    """Parse YYYY[-MM[-DD]] to date; return None on failure."""
    if not s:
        return None
    m = _DATE_RE.match(str(s).strip())
    if not m:
        return None
    y = int(m.group(1))
    mo = int(m.group(2) or 1)
    d = int(m.group(3) or 1)
    try:
        return _dt.date(y, mo, d)
    except ValueError:
        return None


def _limited(rec):
    return set(rec.get("source_limited_fields") or [])


def _txt(v):
    if v is None:
        return ""
    if isinstance(v, list):
        return "; ".join(str(x).strip() for x in v if str(x).strip())
    return str(v).strip()


def _run_rules(recs, today=None):
    today = today or _dt.date.today()
    issues = []

    def add(rule, rec, field, msg):
        sev = dict((r[0], r[1]) for r in RULES_META)[rule]
        issues.append({"rule": rule, "severity": sev,
                       "record": _txt(rec.get("registry_id")) or "?",
                       "source": rec.get("source") or "?",
                       "field": field, "message": msg})

    for rec in recs:
        rid = _txt(rec.get("registry_id"))
        src = (rec.get("source") or "").upper()
        limited = _limited(rec)

        # RG-001 date-logic contradiction
        sd, pcd = _date(rec.get("start_date")), _date(rec.get("primary_completion_date"))
        if sd and pcd and sd > pcd:
            add("RG-001", rec, "start_date/primary_completion_date",
                f"start {sd} is after primary completion {pcd}")

        # RG-002 primary outcome missing although provided by this path
        if not _txt(rec.get("primary_outcome")) and "primary_outcome" not in limited:
            add("RG-002", rec, "primary_outcome", "primary outcome empty")

        # RG-003 CT.gov eligibility entirely absent
        if src == "CTGOV":
            if not any(_txt(rec.get(k)) for k in
                       ("eligibility_sex", "eligibility_min_age", "eligibility_max_age")):
                add("RG-003", rec, "eligibility_*", "no sex / age bounds extracted")

            # RG-004 completed but no results and stale
            if _COMPLETED_RE.search(_txt(rec.get("status"))):
                lu = _date(rec.get("last_update_posted"))
                if not _txt(rec.get("results_first_posted")) and (
                        lu is None or (today - lu).days > 365):
                    add("RG-004", rec, "results_first_posted",
                        "Completed-like trial without posted results and no update > 365d")

            # RG-009 stale snapshot
            lu = _date(rec.get("last_update_posted"))
            if lu and (today - lu).days > 730:
                add("RG-009", rec, "last_update_posted",
                    f"last update {lu} is > 24 months old")

        # RG-005 enrollment missing although provided
        if rec.get("enrollment") in (None, "") and "enrollment" not in limited:
            add("RG-005", rec, "enrollment", "enrollment empty")

        # RG-006 id pattern mismatch
        if rid:
            pat = _ID_PATTERNS.get(src)
            if pat and not pat.match(rid):
                add("RG-006", rec, "registry_id",
                    f"id '{rid}' does not match {src} pattern")

        # RG-007 conditions missing although provided
        if not rec.get("conditions") and "conditions" not in limited:
            add("RG-007", rec, "conditions", "conditions empty")

        # RG-008 unusable record (no id, no url)
        if not rid and not _txt(rec.get("url")):
            add("RG-008", rec, "registry_id/url", "no registry id and no url")

    return issues


def _summary(issues):
    by_rule, by_sev = {}, {"E": 0, "W": 0}
    for it in issues:
        by_rule[it["rule"]] = by_rule.get(it["rule"], 0) + 1
        by_sev[it["severity"]] = by_sev.get(it["severity"], 0) + 1
    return {"total": len(issues), "errors": by_sev["E"], "warnings": by_sev["W"],
            "by_rule": by_rule}


def _md_report(issues, summary, n_records, min_sev):
    L = ["# Registration Record Quality Report (registry_rules v1)", ""]
    L.append(f"- Records audited: **{n_records}**")
    L.append(f"- Issues: **{summary['total']}** (Error {summary['errors']} / "
             f"Warning {summary['warnings']}; min severity filter: {min_sev})")
    L.append("")
    L.append("| Rule | Sev | Count | Meaning |")
    L.append("|---|---|---|---|")
    for rid, sev, desc in RULES_META:
        c = summary["by_rule"].get(rid, 0)
        if c:
            L.append(f"| {rid} | {sev} | {c} | {desc} |")
    L.append("")
    cur = None
    for it in sorted(issues, key=lambda x: (x["rule"], x["record"])):
        if it["rule"] != cur:
            cur = it["rule"]
            desc = dict((r[0], r[2]) for r in RULES_META)[cur]
            L.append(f"## {cur} ({it['severity']}) — {desc}")
            L.append("")
        L.append(f"- `{it['record']}` [{it['source']}] {it['field']}: {it['message']}")
    L.append("")
    return "\n".join(L)


def load_records(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for k in ("records", "normalized", "trials"):
            if isinstance(data.get(k), list):
                return data[k]
    raise SystemExit(f"unrecognized normalized.json shape: {type(data)}")


def main(argv=None):
    ap = argparse.ArgumentParser(description="P21-style quality rules for "
                                             "ct-registry normalized records")
    ap.add_argument("--in", dest="inp", required=True, help="normalized.json path")
    ap.add_argument("--out-json", default=None, help="write issue list JSON")
    ap.add_argument("--out-md", default=None, help="write Markdown report")
    ap.add_argument("--severity", choices=["all", "error", "warning"], default="all",
                    help="minimum severity to report (default: all)")
    args = ap.parse_args(argv)

    recs = load_records(args.inp)
    issues = _run_rules(recs)
    if args.severity == "error":
        issues = [i for i in issues if i["severity"] == "E"]
    elif args.severity == "warning":
        issues = [i for i in issues if i["severity"] == "W"]
    summary = _summary(issues)

    payload = {"schema": "ct-registry/registry_rules/v1",
               "input": args.inp, "records": len(recs),
               "summary": summary, "issues": issues}
    if args.out_json:
        with open(args.out_json, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
    if args.out_md:
        with open(args.out_md, "w", encoding="utf-8") as f:
            f.write(_md_report(issues, summary, len(recs), args.severity))

    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
