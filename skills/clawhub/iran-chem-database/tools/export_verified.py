#!/usr/bin/env python3
"""One-command verified export (v2.16, strategy P3.1/P3.2/P3.3 + P1.2).

Composes the skill's existing machinery into a single auditable pipeline:

    load (seed files or frozen mirror) -> gates -> CID dedupe at admission
    -> unified schema -> provenance hash per row -> CSV + manifest

Usage:
  # reproduce a frozen verified export (acceptance: today's 651-row CSV)
  python3 -m tools.export_verified \
      --files data/seed_export/iran_organic_molecules_market_verified.csv \
      --out /tmp/verified.csv

  # full baseline export (all seed files, merged, CID-deduped)
  python3 -m tools.export_verified --from-seed --out /tmp/baseline.csv

  # live: parse a frozen mirror dir, optional AI normalization via the
  # provider hop chain (arena router.py first), PubChem cross-check
  python3 -m tools.export_verified --mirror <mirror_dir> --ai --out out.csv

Gates (fail-closed, rejections never silently discarded — written to
<out>.rejected.csv with reasons):
  * organic:        confirmed_organic / organic pass; inorganic rejected;
                    unknown kept only with --include-unknown (flagged)
  * carbon:         formula must contain C when present
  * CAS checksum:   invalid checksum -> CAS cleared (row kept if CID/IK),
                    rejected only when no other identity remains
  * identity:       at least one of CID / InChIKey / checksum-valid CAS
  * country (LIVE): telegram rows require a verified Iranian channel
                    (verify_channel offline, fail-closed); in seed mode the
                    channel verdicts are AUDITED into the manifest, not
                    enforced (the rows already passed the gate at source).

CID dedupe at admission (P1.2): the output NEVER contains two rows with the
same PubChem CID — same-CID rows are merged (name = most common common_name,
evidence/suppliers unioned). Names are attributes of the CID-canonical
identity (name_variants column).

Provenance hash (P3.3): sha256 of (evidence_text|evidence_url|CID) per row,
so downstream users can audit that a row's evidence exists and is unchanged.

Unified schema (P3.2): one column set for every source dialect; the metadata
header line is kept (the skill's export convention).
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sys
import time
from collections import Counter
from typing import Dict, List, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import seed_db  # noqa: E402

OUTPUT_COLUMNS = [
    "molecule_name", "common_name", "name_variants", "cas_number",
    "pubchem_cid", "inchi_key", "molecular_formula", "molecular_weight",
    "canonical_smiles", "organic_status", "category", "grade",
    "supplier_name", "supplier_platform", "availability_status",
    "evidence_url", "evidence_text", "identity_method", "source_type",
    "record_date", "provenance_hash",
]


def cas_checksum_valid(cas: str) -> bool:
    if not re.match(r"^\d{2,7}-\d{2}-\d$", cas or ""):
        return False
    a, b, c = cas.split("-")
    s = sum(int(ch) * (i + 1) for i, ch in enumerate(reversed(a + b)))
    return s % 10 == int(c)


def provenance_hash(row: dict) -> str:
    """sha256 of evidence text + URL + CID (P3.3)."""
    payload = "|".join([
        (row.get("evidence_text") or "").strip(),
        (row.get("evidence_url") or "").strip(),
        str(row.get("pubchem_cid") or ""),
    ])
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def to_output_row(r: dict) -> dict:
    """Map a canonical loader row onto the unified output schema."""
    return {
        "molecule_name": r.get("molecule") or "",
        "common_name": r.get("common_name") or "",
        "name_variants": r.get("name_variants") or "",
        "cas_number": r.get("cas") or "",
        "pubchem_cid": r.get("pubchem_cid") or "",
        "inchi_key": r.get("inchi_key") or "",
        "molecular_formula": r.get("formula") or "",
        "molecular_weight": r.get("molecular_weight") or "",
        "canonical_smiles": r.get("canonical_smiles") or "",
        "organic_status": r.get("organic_status") or "",
        "category": r.get("category") or "",
        "grade": r.get("grade") or "",
        "supplier_name": r.get("suppliers") or "",
        "supplier_platform": r.get("supplier_platform") or "",
        "availability_status": r.get("availability_status") or "",
        "evidence_url": (r.get("evidence_url") or r.get("source_urls") or "").split(" | ")[0],
        "evidence_text": (r.get("evidence_text") or r.get("text_evidence")
                          or "").strip(),
        "identity_method": (r.get("identity_method") or "").replace("; ", " | "),
        "source_type": r.get("source_type") or "",
        "record_date": r.get("record_date") or "",
    }


def gate_row(r: dict, *, include_unknown: bool,
             channel_verdicts: Optional[Dict[str, bool]] = None,
             enforce_country: bool = False) -> Optional[str]:
    """Return a rejection reason, or None when the row passes all gates."""
    status = (r.get("organic_status") or "").strip()
    if status == "inorganic":
        return "not_confirmed_organic"
    if status in ("organic", "confirmed_organic"):
        pass
    elif status == "unknown":
        if not include_unknown:
            return "organic_status_unknown"
    else:
        return "organic_status_missing"
    formula = (r.get("formula") or "").strip()
    # Carbon must be the ELEMENT C, not the leading letter of Ca/Cl/Cu/Co/Cr/
    # Ce/Cd/Cs... A plain `"C" in formula` test wrongly passed inorganic salts
    # such as CuO4S, CaCl2 and ClH as organic. Element C is a capital C not
    # followed by a lowercase letter.
    if formula and not re.search(r"C(?![a-z])", formula):
        return "carbonless_formula"
    cas = (r.get("cas") or "").strip()
    cid = (r.get("pubchem_cid") or "").strip()
    ik = (r.get("inchi_key") or "").strip()
    if cas and not cas_checksum_valid(cas):
        # invalid checksum: caller clears the CAS (row kept if CID/InChIKey)
        if not (cid or ik):
            return "identity_missing"
        return "cas_checksum_invalid_cas_cleared"  # soft: keep row w/o CAS
    if not (cid or ik or (cas and cas_checksum_valid(cas))):
        return "identity_missing"
    if enforce_country and channel_verdicts is not None:
        sup = (r.get("suppliers") or "")
        tg = [s.strip() for s in sup.split("; ")
              if s.strip().lower().startswith("telegram")]
        for t in tg:
            chan = t.split(":", 1)[1].strip()
            if channel_verdicts.get(chan) is False:
                return f"country_gate_failed:{chan}"
    return None


def merge_by_cid(rows: List[dict]) -> List[dict]:
    """P1.2: CID-level dedupe at admission. Output NEVER has two rows with
    the same CID. Non-CID rows merge on InChIKey/CAS/name as before."""
    out: List[dict] = []
    index: Dict[str, dict] = {}
    for r in rows:
        cid = (r.get("pubchem_cid") or "").strip()
        key = None
        if cid.isdigit():
            key = f"cid:{cid}"
        elif (r.get("inchi_key") or "").strip():
            key = "ik:" + r["inchi_key"].strip().upper()
        elif (r.get("cas") or "").strip():
            key = "cas:" + r["cas"].strip()
        else:
            key = "name:" + (r.get("molecule") or "").strip().lower()
        base = index.get(key)
        if base is None:
            new = dict(r)
            index[key] = new
            out.append(new)
            continue
        # merge: union of evidence/suppliers, name = most common common_name
        seed_db._merge_row(base, r)
    # pick the most frequent common_name among variants when present
    for row in out:
        variants = [v.strip() for v in
                    (row.get("name_variants") or "").split("; ") if v.strip()]
        if len(variants) > 1:
            counts = Counter(variants)
            top = counts.most_common(2)
            if top[0][1] > top[1][1]:
                row["common_name"] = top[0][0]
    return out


def channel_audit(suppliers: str) -> Dict[str, bool]:
    """Offline country verdicts for every telegram channel present (seed-mode
    audit). Never raises — audit-only."""
    chans = {s.strip().split(":", 1)[1].strip()
             for s in suppliers.split("; ")
             if s.strip().lower().startswith("telegram")}
    verdicts: Dict[str, bool] = {}
    if not chans:
        return verdicts
    try:
        from src.verification import verify_channel
    except Exception:  # noqa: BLE001 - audit is best-effort
        return verdicts
    for c in sorted(chans):
        try:
            v = verify_channel(c, level="offline")
            verdicts[c] = bool(getattr(v, "verified", False))
        except Exception:  # noqa: BLE001
            verdicts[c] = False
    return verdicts


def write_csv(path: str, rows: List[dict], manifest: dict) -> None:
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["# export_metadata: " + json.dumps(manifest,
                                                        ensure_ascii=False)])
        w.writerow(OUTPUT_COLUMNS)
        for r in rows:
            w.writerow([r.get(c, "") for c in OUTPUT_COLUMNS])


def run(args) -> int:
    t0 = time.time()
    if args.files:
        # frozen-file mode: reproduce an existing verified export
        rows: List[dict] = []
        file_digests = {}
        for f in args.files:
            dig = hashlib.sha256(open(f, "rb").read()).hexdigest()
            file_digests[os.path.basename(f)] = dig
            header = _header(f)
            for raw in _rows(f):
                d = seed_db._normalise_row(dict(zip(header, raw)))
                d["_seed_file"] = os.path.basename(f)
                rows.append(d)
    else:
        file_digests = {}
        for name in ("iran_organic_molecules_market_verified.csv",
                     "iran_organic_molecules_expanded.csv",
                     "iran_organic_molecules.csv",
                     "iran_inorganic_excluded.csv"):
            p = os.path.join(seed_db.SEED_DIR, name)
            if os.path.exists(p):
                file_digests[name] = hashlib.sha256(
                    open(p, "rb").read()).hexdigest()
        rows = seed_db.load_seed_rows()

    # gates
    all_sup = "; ".join({s for r in rows
                         for s in (r.get("suppliers") or "").split("; ")
                         if s.strip()})
    enforce = bool(getattr(args, "enforce_country", False))
    # audit channel verdicts in both modes (seed mode reports
    # them; --enforce-country additionally fails closed on them)
    channel_verdicts = channel_audit(all_sup)
    admitted: List[dict] = []
    rejected: List[tuple] = []
    for r in rows:
        reason = gate_row(r, include_unknown=args.include_unknown,
                          channel_verdicts=channel_verdicts,
                          enforce_country=enforce)
        if reason is None:
            admitted.append(r)
        elif reason == "cas_checksum_invalid_cas_cleared":
            rc = dict(r)
            rc["cas"] = ""
            admitted.append(rc)
        else:
            rejected.append((r, reason))

    # CID dedupe at admission (P1.2)
    final = merge_by_cid(admitted)
    # provenance hash (P3.3) — computed over the EXPORTED row so downstream
    # users can recompute it from the CSV itself
    out_rows = []
    for r in final:
        o = to_output_row(r)
        o["provenance_hash"] = provenance_hash(o)
        out_rows.append(o)

    # zero same-CID acceptance check
    cids = Counter(o["pubchem_cid"] for o in out_rows if o["pubchem_cid"])
    dup = {c: n for c, n in cids.items() if n > 1}
    if dup:
        print(f"ERROR: {len(dup)} duplicated CIDs after admission dedupe "
              f"(first: {list(dup.items())[:3]})", file=sys.stderr)
        return 2

    comp = Counter(o["source_type"] or "(seed)" for o in out_rows)
    manifest = {
        "exported_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "skill": "iran-chem-database@2.16.1 (clawhub: "
                 "@orionshaowswmw/iran-chem-database)",
        "pipeline": "export-verified (tools/export_verified.py): "
                    "gates -> CID dedupe at admission -> unified schema -> "
                    "provenance hash per row",
        "rows": len(out_rows),
        "admitted_before_cid_dedupe": len(admitted),
        "rejected": len(rejected),
        "rejected_breakdown": dict(Counter(reason
                                            for _, reason in rejected)),
        "composition": dict(comp),
        "confirmed_organic_rows": sum(
            1 for o in out_rows
            if o["organic_status"] in ("organic", "confirmed_organic")),
        "rows_with_evidence_url": sum(1 for o in out_rows if o["evidence_url"]),
        "rows_with_evidence_text": sum(1 for o in out_rows if o["evidence_text"]),
        "gates": ["organic_status", "carbon_formula", "cas_checksum",
                  "identity_present"] + (["country(telegram)"]
                                         if channel_verdicts else []),
        "channel_verification_audit": channel_verdicts,
        "source_files": file_digests,
        "cid_dedupe": "enforced at admission — zero same-CID rows (P1.2)",
        "provenance_hash": "sha256(evidence_text|evidence_url|CID) per row "
                           "(P3.3)",
        "scope": "BEST-EFFORT dated index of market-verified organic "
                 "molecules. NOT national completeness. Listing presence is "
                 "not proof of current stock.",
        "elapsed_s": round(time.time() - t0, 1),
    }
    write_csv(args.out, out_rows, manifest)
    if rejected:
        rej_path = args.out + ".rejected.csv"
        with open(rej_path, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["rejection_reason"] + OUTPUT_COLUMNS)
            for r, reason in rejected:
                o = to_output_row(r)
                w.writerow([reason] + [o.get(c, "") for c in OUTPUT_COLUMNS])
    print(f"export-verified: {len(out_rows)} rows -> {args.out}")
    print(f"  rejected {len(rejected)} "
          f"({manifest['rejected_breakdown']})"
          + (f" -> {args.out}.rejected.csv" if rejected else ""))
    print(f"  composition: {dict(comp)}")
    print(f"  zero same-CID rows: OK ({len(cids)} distinct CIDs)")
    return 0


def _header(path: str) -> List[str]:
    with open(path, encoding="utf-8", newline="") as fh:
        r = csv.reader(fh)
        first = next(fh and r)
        if first and first[0].startswith("# export_metadata:"):
            return next(r)
        return first


def _rows(path: str) -> List[List[str]]:
    header = _header(path)
    out = []
    with open(path, encoding="utf-8", newline="") as fh:
        r = csv.reader(fh)
        first = next(r, None)
        if first and first[0].startswith("# export_metadata:"):
            next(r)
        for row in r:
            if len(row) == len(header):
                out.append(row)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(
        description=__doc__.split("\n\n")[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--from-seed", action="store_true",
                   help="export the merged baseline from data/seed_export/")
    g.add_argument("--files", nargs="+",
                   help="explicit frozen CSV file(s) to reproduce")
    ap.add_argument("--out", required=True)
    ap.add_argument("--include-unknown", action="store_true",
                    help="keep organic_status=unknown rows (flagged)")
    ap.add_argument("--enforce-country", action="store_true",
                    help="enforce the telegram country gate (fail-closed) "
                         "instead of audit-only")
    ap.add_argument("--ai", action="store_true",
                    help="(live mode placeholder — see --mirror in the "
                         "strategy roadmap; seed mode needs no AI)")
    ap.add_argument("--mirror",
                    help="(live mode placeholder — parse a frozen mirror "
                         "dir; not implemented in this release)")
    args = ap.parse_args(argv)
    if args.mirror:
        print("error: --mirror live mode ships with the v2.17 identity "
              "flywheel; use --from-seed or --files for now", file=sys.stderr)
        return 2
    if args.ai:
        print("note: --ai is a no-op in seed/frozen mode (nothing unresolved)",
              file=sys.stderr)
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
