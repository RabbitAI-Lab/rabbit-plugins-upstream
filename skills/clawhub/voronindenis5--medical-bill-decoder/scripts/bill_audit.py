#!/usr/bin/env python3
"""bill_audit.py — audit a US medical bill: classify CPT/HCPCS lines, detect error
patterns (duplicates, unbundling, E/M level jumps, chain violations), reconcile
against an EOB, and draft itemized-bill / dispute letters.

Stdlib only. Input: a text itemized bill (one service per line) and/or EOB numbers.

Examples:
  python3 bill_audit.py --line "99283 1850.00" --line "85025 95.00" --line "85025 95.00"
  python3 bill_audit.py bill.txt --allowed 1204.00 --paid 936.00 --patient 412.00
  python3 bill_audit.py --letter itemized --provider "City Hospital" --acct 8842
"""
import argparse
import re
import sys

# CPT/HCPCS -> (plain name, typical allowed lo, typical allowed hi, family)
CODES = {
    "99202": ("New patient visit, level 1", 90, 130, "E/M"),
    "99203": ("New patient visit, level 2", 130, 190, "E/M"),
    "99204": ("New patient visit, level 3", 220, 300, "E/M"),
    "99205": ("New patient visit, level 4", 320, 440, "E/M"),
    "99211": ("Established visit, level 0 (staff)", 35, 60, "E/M"),
    "99212": ("Established visit, level 1", 70, 105, "E/M"),
    "99213": ("Established visit, level 2", 90, 130, "E/M"),
    "99214": ("Established visit, level 3", 130, 190, "E/M"),
    "99215": ("Established visit, level 4", 180, 260, "E/M"),
    "99281": ("ER visit, level 1", 200, 350, "ER"),
    "99282": ("ER visit, level 2", 350, 550, "ER"),
    "99283": ("ER visit, level 3", 550, 850, "ER"),
    "99284": ("ER visit, level 4", 900, 1300, "ER"),
    "99285": ("ER visit, level 5", 1300, 1900, "ER"),
    "99291": ("Critical care, first hour", 700, 1000, "ER"),
    "71046": ("Chest X-ray, 2 views", 45, 80, "radiology"),
    "71045": ("Chest X-ray, 1 view", 35, 60, "radiology"),
    "73630": ("Wrist X-ray, 3+ views", 45, 90, "radiology"),
    "70551": ("MRI brain, without contrast", 400, 700, "radiology"),
    "70553": ("MRI brain, with and without contrast", 600, 900, "radiology"),
    "72148": ("MRI lumbar spine, without contrast", 400, 700, "radiology"),
    "73721": ("MRI lower extremity joint, w/o contrast", 450, 800, "radiology"),
    "70450": ("CT head/brain, without contrast", 300, 550, "radiology"),
    "80053": ("Comprehensive metabolic panel", 25, 45, "lab"),
    "80048": ("Basic metabolic panel", 18, 35, "lab"),
    "85025": ("CBC with differential", 15, 30, "lab"),
    "85027": ("CBC without differential", 12, 25, "lab"),
    "84443": ("TSH (thyroid stimulating hormone)", 30, 50, "lab"),
    "84410": ("T4 free", 20, 40, "lab"),
    "81001": ("Urinalysis, microscopic", 15, 30, "lab"),
    "81003": ("Urinalysis, dip stick only", 10, 20, "lab"),
    "83520": ("Immunoassay, infectious agent", 30, 70, "lab"),
    "87880": ("Rapid flu test", 25, 50, "lab"),
    "36415": ("Blood draw (venipuncture)", 10, 20, "lab"),
    "93000": ("ECG 12-lead with interpretation", 40, 70, "cardio"),
    "93010": ("ECG interpretation only", 20, 35, "cardio"),
    "94640": ("Nebulizer treatment", 40, 70, "resp"),
    "96372": ("Therapeutic injection, SC/IM", 30, 60, "inject"),
    "96365": ("IV infusion, initial hour", 100, 150, "inject"),
    "96375": ("IV push, add-on", 35, 55, "inject"),
    "96376": ("IV push, repeat", 25, 40, "inject"),
    "20552": ("Trigger point injection, 1-2 muscles", 80, 140, "inject"),
    "20610": ("Joint aspiration/injection, major", 90, 150, "inject"),
    "64483": ("Transforaminal epidural injection, lumbar", 400, 700, "inject"),
    "J1885": ("Ketorolac 15 mg", 2, 4, "drug"),
    "J3420": ("Vitamin B12 1000 mcg", 8, 15, "drug"),
    "J2250": ("Midazolam 1 mg", 2, 5, "drug"),
    "J2704": ("Ondansetron 2 mg", 1, 3, "drug"),
    "J1453": ("Iron sucrose 100 mg", 40, 80, "drug"),
    "43239": ("Upper endoscopy with biopsy", 900, 1400, "endoscopy"),
    "45378": ("Colonoscopy, diagnostic", 900, 1400, "endoscopy"),
    "45380": ("Colonoscopy with biopsy", 1100, 1700, "endoscopy"),
    "66984": ("Cataract surgery with lens implant", 1600, 2400, "surgery"),
    "27447": ("Total knee replacement", 18000, 28000, "surgery"),
    "29881": ("Knee arthroscopy w/ meniscectomy", 2500, 4000, "surgery"),
    "47562": ("Laparoscopic cholecystectomy", 5000, 8000, "surgery"),
    "49505": ("Inguinal hernia repair", 3500, 5500, "surgery"),
    "58150": ("Total abdominal hysterectomy", 8000, 13000, "surgery"),
}

# Panels and their components (unbundling detection)
PANELS = {
    "80053": {"82040", "84155", "84520", "84855"},  # CMP: albumin, protein, etc.
    "80048": {"84132", "84295"},
    "85025": {"85007", "85008", "85009"},
    "93000": {"93010"},
}
# Family-specific level ladders for E/M jump detection
EM_LADDERS = {
    "new": ["99202", "99203", "99204", "99205"],
    "est": ["99211", "99212", "99213", "99214", "99215"],
    "er": ["99281", "99282", "99283", "99284", "99285"],
}

LINE_RE = re.compile(
    r"(?P<cpt>[A-Z]?\d{4,5}[A-Z]?)\s+(?:(?P<mods>[0-9A-Z]{2}\s+)?)"
    r"(?:x\s?(?P<units>\d+)\s+)?(?:[-—]?\s*\$?(?P<charge>[\d,]+(?:\.\d{2})?))")


def parse_lines(text):
    rows = []
    for raw in text.splitlines():
        s = raw.strip()
        if not s:
            continue
        m = LINE_RE.search(s)
        if not m:
            continue
        charge = m.group("charge")
        try:
            amt = float(charge.replace(",", "")) if charge else 0.0
        except ValueError:
            amt = 0.0
        rows.append({"code": m.group("cpt").upper(), "mods": (m.group("mods") or "").strip(),
                     "units": int(m.group("units") or 1), "charge": amt, "raw": s})
    return rows


def audit(rows):
    findings = []
    seen = {}
    for i, r in enumerate(rows, 1):
        code = r["code"]
        key = (code, r["mods"])
        if key in seen:
            findings.append(("DUPLICATE", i,
                             f"{code} already billed at line {seen[key]} (same date) — "
                             f"ask provider to remove one; duplicates are the #1 error."))
        else:
            seen[key] = i
        name, lo, hi, fam = CODES.get(code, (None, None, None, None))
        if name is None:
            findings.append(("UNKNOWN", i, f"{code} not in local table — demand the "
                             "CPT description and units from the provider."))
        else:
            if r["charge"] and hi is not None and r["charge"] > hi * 3:
                findings.append(("PRICE?", i, f"{code} ({name}) charged ${r['charge']:,.0f} — "
                                 f"3× above typical ${lo}-{hi}; ask for the fee basis."))
        for panel, comps in PANELS.items():
            if code in comps and any(x["code"] == panel for x in rows):
                findings.append(("UNBUNDLE", i, f"{code} is a component of {panel} "
                                 f"(billed elsewhere) — components of a panel can't be "
                                 "billed separately."))
    # E/M ladder jump within same visit cluster (all E/M same date)
    ems = [(i, r) for i, r in enumerate(rows, 1) if r["code"] in {c for lad in EM_LADDERS.values() for c in lad}]
    for lad_name, lad in EM_LADDERS.items():
        codes_present = [r["code"] for _, r in ems if r["code"] in lad]
        if len(codes_present) >= 2:
            findings.append(("EM-STACK", ems[0][0],
                             f"Multiple {lad_name} visit levels billed together "
                             f"({', '.join(codes_present)}) — same-day E/M usually needs "
                             "modifier 25 or is one visit."))
    return findings


def chain_check(allowed, paid, patient):
    if None in (allowed, paid, patient):
        return None
    exp = allowed - paid
    if patient > exp + 0.01:
        return (f"CHAIN VIOLATION: patient ${patient:,.2f} > allowed−paid ${exp:,.2f}. "
                f"Overcharge ${patient - exp:,.2f}. Dispute in writing.")
    return f"Chain OK: allowed ${allowed:,.2f} = paid ${paid:,.2f} + patient ${patient:,.2f}"


LETTERS = {
    "itemized": """{provider} — Billing Department
RE: Account {acct}

I request a FULLY ITEMIZED bill for this account, including for each line: CPT/HCPCS
codes with descriptions, units, NDC numbers for any drugs, revenue codes, dates of
service, and the charge for each. I also request the insurer's Explanation of Benefits
alignment (billed, allowed, paid, patient responsibility per line).

Please hold this account from collections while the review is pending and provide a
reference number for this request. (30-day written response requested.)

Sincerely, ____________________""",
    "dispute": """{provider} — Billing Department
RE: Account {acct} — BILLING DISPUTE

I dispute the following charges in good faith:
{items}

Grounds: duplicate billing / unbundling / charge exceeding the contracted allowed
amount / patient responsibility exceeding allowed−paid (chain violation). Under the
Fair Credit Reporting Act and state billing-practices law I request:
1. Written, line-level explanation of each disputed line;
2. Correction or removal of the charges;
3. Written confirmation the account is held from collections during this dispute;
4. A reference number for this dispute.

If the balance remains unsupported after review, please issue a corrected bill at $0
for the disputed lines and confirm in writing.

Sincerely, ____________________""",
}


def main():
    p = argparse.ArgumentParser(description="Medical bill auditor + letter writer.")
    p.add_argument("billfile", nargs="?", help="text itemized bill")
    p.add_argument("--line", action="append", default=[], help="one bill line, e.g. '85025 95.00'")
    p.add_argument("--allowed", type=float, help="EOB allowed amount")
    p.add_argument("--paid", type=float, help="EOB insurance paid")
    p.add_argument("--patient", type=float, help="EOB patient responsibility")
    p.add_argument("--letter", choices=["itemized", "dispute"], help="print a letter")
    p.add_argument("--provider", default="[Provider name]")
    p.add_argument("--acct", default="[acct #]")
    a = p.parse_args()

    if a.letter:
        items = "\n".join(f"  - Line {i}: {r['raw']}" for i, r in
                          (parse_lines("\n".join(a.line)) if a.line else [])) or "  - [list disputed lines]"
        print(LETTERS[a.letter].format(provider=a.provider, acct=a.acct, items=items))
        return

    text = ""
    if a.billfile:
        with open(a.billfile, encoding="utf-8", errors="replace") as f:
            text = f.read()
    if a.line:
        text += "\n" + "\n".join(a.line)
    rows = parse_lines(text)
    if not rows:
        print("No bill lines detected. Use --line 'CODE AMOUNT' or pass a bill file.")
        sys.exit(1)

    total = sum(r["charge"] * (r["units"] if r["units"] else 1) for r in rows)
    print(f"Parsed {len(rows)} line(s); billed total ${total:,.2f}\n")
    print(f"{'#':>2}  {'CODE':<7} {'MOD':<4} {'UNITS':>4}  {'CHARGE':>10}  DESCRIPTION")
    for i, r in enumerate(rows, 1):
        name = CODES.get(r["code"], ("? unknown — request description",))[0]
        print(f"{i:>2}  {r['code']:<7} {r['mods'] or '-':<4} {r['units']:>4}  {r['charge']:>10,.2f}  {name}")

    findings = audit(rows)
    print()
    if findings:
        print(f"⚠ {len(findings)} finding(s):")
        for kind, line, msg in findings:
            print(f"  [{kind:<8}] line {line}: {msg}")
    else:
        print("✓ No structural errors found by local table checks.")

    if a.allowed is not None:
        c = chain_check(a.allowed, a.paid or 0.0, a.patient or 0.0)
        print("\nEOB chain: " + (c or "provide --allowed --paid --patient"))
    print("\nNext: demand itemized bill if not in hand; reconcile vs EOB; send dispute "
          "letter citing the lines above; request collections hold + reference number.")


if __name__ == "__main__":
    main()
